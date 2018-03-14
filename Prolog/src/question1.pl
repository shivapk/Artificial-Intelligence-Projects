brother(X,Y) :- male(Y),parent(X,Z),parent(Y,Z),\+(X = Y).
sister(X,Y) :- female(Y),parent(X,Z),parent(Y,Z),\+(X = Y).
aunt(X,Y) :- parent(X,Z),sister(Z,Y).
uncle(X,Y) :- parent(X,Z),brother(Z,Y).
grandfather(X,Y) :- male(Y),parent(X,Z),parent(Z,Y).
granddaughter(X,Y) :- female(Y),parent(Y,Z),parent(Z,X).

ancestor(X,Y) :- parent(X,Y).
ancestor(X,Y) :- parent(X,Z),ancestor(Z,Y).

descendant(X,Y) :- ancestor(Y,X).

related(X,Y) :- brother(X,Y).
related(X,Y) :- sister(X,Y).
related(X,Y) :- ancestor(X,Z),related(Z,Y).
%related(X,Y) :- descendant(X,Z),related(Z,Y).
unrelated(X,Y) :- \+related(X,Y).

parent(bart,homer).
parent(bart,marge).
parent(lisa,homer).
parent(lisa,marge).
parent(maggie,homer).
parent(maggie,marge).
parent(homer,abraham).
parent(herb,abraham).
parent(tod,ned).
parent(rod,ned).
parent(marge,jackie).
parent(patty,jackie).
parent(selma,jackie).
female(maggie).
female(lisa).
female(marge).
female(patty).
female(selma).
female(jackie).
male(bart).
male(homer).
male(herb).
male(burns).
male(smithers).
male(tod).
male(rod).
male(ned).
male(abraham).
