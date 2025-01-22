% Vertices and edges
vertex(0..8).
edge(0, 1). edge(0, 8).
edge(1, 2). edge(1, 7).
edge(2, 3).
edge(3, 4). edge(3, 6).
edge(4, 5).

% Agent definition
%agent(a).
agent(b).
#const n=10.

% Initial positions and goal
%start(a, 7).   % Agent starts at vertex 7
start(b, 6).   % Agent starts at vertex 7
%goal(a, 5).    % Agent's target is vertex 5
goal(b, 0).    % Agent's target is vertex 5

#include <incmode>.

#program base.
% Define
edge(U, V):- edge(V, U).
at(A,U,0) :- start(A,U).


#program step(t).
% Generate valid moves

%path_length(A, L) :- 
%   agent(A), 
%    #count { U, V: move(A, U, V, T) } = L.

%#minimize { 1,U,V: move(A, U, V, _)}.

%:-at(A,U,_),goal(A,U), move(A,U,_,_).

{ move(A, U, V, t) : agent(A),edge(U, V) } 1 .

% Define agent positions at each time step
at(A, V, t) :- move(A, _, V, t).
at(A, U, t) :- at(A, U, t-1), not move(A, U, _, t).

% Constraints
:- move(A, U, _, t), not at(A, U, t-1).       % Agent must only move from its current position
:- { at(_, U, t) } > 1, vertex(U).            % Only one agent can occupy a vertex
%:- move(_, U, V, t), move(_, V, U, t).        % No back-and-forth moves
:- at(A, U, t), at(B, U, t), A != B , m=fc.          % Agents cannot share the same vertex
                    
#program check(t).
% Test
:- query(t), goal(A, U), not at(A, U, t).

% Display
#show at/3.

%reach fact
