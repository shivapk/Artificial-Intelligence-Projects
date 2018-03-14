row(1).
row(2).
row(3).
col(1).
col(2).
col(3).
symbol(x).
symbol(o).

twoInRow(S,R) :- symbol(S), row(R), col(C1), col(C2), C1 < C2, p(S,R,C1), p(S,R,C2).
twoInCol(S,C) :- symbol(S), col(C), row(R1), row(R2), R1 < R2, p(S,R1,C), p(S,R2,C).
twoInDiagLeft(S) :- symbol(S), row(R1), row(R2), R1 < R2, p(S,R1,R1), p(S,R2,R2).
twoInDiagRight(S) :- symbol(S), row(R1), row(R2), R1 < R2, p(S,R1,4-R1), p(S,R2,4-R2).

canWin(S,R,C) :- symbol(S), row(R), col(C), twoInRow(S,R), \+p(x,R,C), \+p(o,R,C).
canWin(S,R,C) :- symbol(S), row(R), col(C), twoInCol(S,C), \+p(x,R,C), \+p(o,R,C).
canWin(S,R,R) :- symbol(S), row(R), twoInDiagLeft(S), \+p(x,R,R), \+p(o,R,R).
canWin(S,R,C) :- symbol(S), row(R), col(C), twoInDiagRight(S), \+p(x,R,C), \+p(o,R,C), C is 4-R.

forcedMove(x,R,C) :- row(R), col(C), canWin(o,R,C), write('move to block opponent!').
forcedMove(o,R,C) :- row(R), col(C), canWin(x,R,C), write('move to block opponent!').

move(x,R,C) :- row(R), col(C), canWin(x,R,C), write('go for win!').
move(o,R,C) :- row(R), col(C), canWin(o,R,C), write('go for win!').

move(x,R,C) :- row(R), col(C), \+canWin(x,R,C), forcedMove(x,R,C).
move(o,R,C) :- row(R), col(C), \+canWin(o,R,C), forcedMove(o,R,C).

p(x,1,1).
p(x,2,3).
p(o,3,1).
p(o,3,3).