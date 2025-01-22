for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
    else:
        print(f"{n} is a prime number")


for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")


import matplotlib.pyplot as plt
li=[]
for n in range(2, 10000):
    for x in range(2, int((n+1)/2)+1):
        if n % x == 0:
            #print(f"{n} equals {x} * {n//x}")
            break
    else:
        li.append(n)
bins = range(0, 10010, 100)

# Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(li, bins=bins, edgecolor='black', color='skyblue')

# Add labels and title
plt.title("Distribution of Data in Bins of 100", fontsize=14)
plt.xlabel("Range (bins of 100)", fontsize=12)
plt.ylabel("Frequency", fontsize=12)

# Display the plot
plt.show()