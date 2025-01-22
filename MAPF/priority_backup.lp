
% Define
time(1..lasttime).
delta(d).


#program makespan(horizon).

horizon(A,horizon) :- agent(A).
horizon(horizon).

%% setup the sum of costs based encoding
#program sum_of_costs(delta).

horizon(A,N+delta) :- sp_length(A,N).
horizon(M) :- M = #max { N: horizon(A,N) }.

%%% the basic mapf encoding

#program mapf.

time(A,1..N) :- horizon(A,N).
time(1..N) :- horizon(N)




at(A,U,0) :- start(A,U).


% Generate valid moves
{move(A,U,V,T): edge(U,V)} 1 :-  agent(A),time(T).


%Define 
at(A,V,T) :- move(A,_,V,T), time(T).

at(A,U,T) :- at(A,U,T-1), not move(A,U,_,T), time(T).



%test
:- move(A,U,_,T), not at(A,U,T-1). %can only move from current position
:- {at(A,U,T)} > 1, vertex(U), time(T). %only one agent can occupy vertex U at time T - no 2 agent start at the same vertex
:- move(_,U,V,T), move(_,V,U,T). %swap constraints
:- at(A,U,T), at(B,U,T+1), A!=B, m=fc. %follow constraints
:- {at(A,U,T)} != 1, agent(A), time(T). % given a time agent A can be at only one vertex


%check


:- goal(A,U), not at(A,U,lasttime).


penalty(A,N) :- sp_length(A,N+1), N >= 0.
penalty(A,T) :- sp_length(A,N), at(A,U,T), not goal(A,U), T >= N.
penalty(A,T) :- penalty(A,T+1), T >= 0.

bound(H+d) :- H = #sum{T,A : sp_length(A,T)}, delta(d).

:- #sum{ 1,A,T : penalty(A,T) } > B, bound(B).

#minimize{1,A,T : penalty(A,T)}.

% Display
#show at/3.
#show penalty/2.
#show bound/1.

#heuristic move( A,U,V,T) : agent(A), edge( U,V), time(T), priority(A,B). [B,level]

%priority(1,2).
priority(2,1).
priority(3,3).