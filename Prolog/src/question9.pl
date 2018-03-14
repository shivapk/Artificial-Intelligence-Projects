row(1).
row(2).
row(3).
row(4).
col(1).
col(2).
col(3).
col(4).

candidate(X,Y) :- col(X), row(Y), not(visited(X,Y)), Z is X-1, visited(Z,Y), col(Z).
candidate(X,Y) :- col(X), row(Y), not(visited(X,Y)), Z is X+1, visited(Z,Y), col(Z).
candidate(X,Y) :- col(X), row(Y), not(visited(X,Y)), Z is Y-1, visited(X,Z), row(Z).
candidate(X,Y) :- col(X), row(Y), not(visited(X,Y)), Z is Y+1, visited(X,Z), row(Z).

adjacent(X,Y,P,Y) :- col(X), row(Y), P is X-1, col(P).
adjacent(X,Y,P,Y) :- col(X), row(Y), P is X+1, col(P).
adjacent(X,Y,X,Q) :- col(X), row(Y), Q is Y-1, row(Q).
adjacent(X,Y,X,Q) :- col(X), row(Y), Q is Y+1, row(Q).

not_wompus(X,Y) :- adjacent(X,Y,P,Q), visited(P,Q), not(stench(P,Q)).
not_pit(X,Y) :- adjacent(X,Y,P,Q), visited(P,Q), not(breeze(P,Q)).

move(X,Y) :- candidate(X,Y), not_wompus(X,Y), not_pit(X,Y).

visited(4,1).
visited(4,2).
visited(4,3).
visited(4,4).
stench(4,2).
breeze(4,3).
breeze(4,4).