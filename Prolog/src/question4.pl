divisible(N,X) :- M is N mod X, M=0.

factor(N, M) :- numlist(2, N, L),sieve(L, N, M).
sieve([X|[]],X,[X]).
sieve([X|Y], N, [X|M]) :- divisible(N, X), Q is div(N,X), numlist(2, Q, L), sieve(L,Q,M). 
sieve([X|Y], N, M) :- \+divisible(N, X), sieve(Y,N,M). 