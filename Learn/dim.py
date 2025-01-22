import torch as torch 
import matplotlib.pyplot as plt
from tqdm import tqdm #progress bar for loop

vector_dim=100
no_vector=10000
matrix=torch.randn(no_vector,vector_dim)
#print(matrix)
#print(matrix.norm(p=2,dim=1,keepdim=True))
matrix/=matrix.norm(p=2,dim=1,keepdim=True) #Normalise
#print(matrix)
matrix.requires_grad_(True)

optimiser=torch.optim.Adam([matrix],lr=0.01) 
steps_num=20

losses=[]

dot_diff_cutoff = 0.01
big_id = torch.eye(no_vector, no_vector)

for step_num in tqdm(range(steps_num)):
    optimiser.zero_grad()

    dot_products = matrix @ matrix.T
    # Punish deviation from orthogonal
    diff = dot_products - big_id
    loss = (diff.abs() - dot_diff_cutoff).relu().sum()

    # Extra incentive to keep rows normalized
    loss += no_vector * diff.diag().pow(2).sum()

    loss.backward()
    optimiser.step()
    losses.append(loss.item())
    print(step_num)

# Loss curve
plt.plot(losses)
plt.grid(1)
plt.show()

# Angle distribution
dot_products = matrix @ matrix.T
norms = torch.sqrt(torch.diag(dot_products))
normed_dot_products = dot_products / torch.outer(norms, norms)
angles_degrees = torch.rad2deg(torch.acos(normed_dot_products.detach()))
# Use this to ignore self-orthogonality.
self_orthogonality_mask = ~(torch.eye(no_vector, no_vector).bool())
plt.hist(angles_degrees[self_orthogonality_mask].numpy().ravel(), bins=1000, range=(80, 100))
plt.grid(1)
plt.show()