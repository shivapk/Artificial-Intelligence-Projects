bit(0).
bit(1).
bitvec(1,[X]) :- bit(X).
bitvec(N, [X|Y]) :- N>1,M is N-1,bitvec(M, Y), bit(X).

count([1], 1).
count([0], 0).
count([X|Y], D) :- X=:=1, count(Y, C), D is C+1.
count([X|Y], C) :- X=:=0, count(Y, C).
code(N, M, X) :- bitvec(N, X), count(X, C), C =:= M.
