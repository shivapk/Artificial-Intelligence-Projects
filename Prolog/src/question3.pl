remdups([],[]).
remdups([H | T], List) :- member(H, T), remdups( T, List).
remdups([H | T], [H|T1]) :- \+member(H, T), remdups( T, T1).