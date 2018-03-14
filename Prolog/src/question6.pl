sin_zero(X,X) :- abs(sin(X)) < 0.0001.
sin_zero(X,Y) :- abs(sin(X)) >= 0.0001, Z is (X - sin(X)/cos(X)), sin_zero(Z,Y).