% Vertices and edges
vertex(0..8).
edge(0, 1). edge(0, 8).
edge(1, 2). edge(1, 7).
edge(2, 3).
edge(3, 4). edge(3, 6).
edge(4, 5).

% Agent definition
agent(a).
agent(b).
#const n=10.

% Initial positions and goal
start(a, 7).   % Agent starts at vertex 7
start(b, 6).   % Agent starts at vertex 7
goal(a, 5).    % Agent's target is vertex 5
goal(b, 0).    % Agent's target is vertex 5

edge(U, V):- edge(V, U).

{move(A,U,V,T): edge(U,V)} <= 1 :- agent(A), T=1..n.
at(A,U,0) :- start(A,U).
at(A,V,T) :- move(A,_,V,T), T=1..n.
at(A,U,T) :- at(A,U,T-1), not move(A,U,_,T), T=1..n.
:- move(A,U,_,T), not at(A,U,T-1).
:- goal(A,U), not at(A,U,n).
:- {at(A,U,T)} > 1, vertex(U), T=0..n.
:- move(_,U,V,T), move(_,V,U,T).
:- at(A,U,T), at(B,U,T+1), A!=B, m=fc.
:- {at(A,U,T)} != 1, agent(A), T=1..n.

:-at(A,U,_),goal(A,U), move(A,U,_,_).

path_length(A, L) :- 
    agent(A), 
    #count { U, V: move(A, U, V, T) } = L.

#minimize { 1,U,V: move(A, U, V, _)}.

#show move/4.
#show at/3.
#show path_length/2.

%reach fact

#heuristic move( A,U,V,T) : agent(A), edge( U,V) ,V != V ’.
[1 ,sign ]
