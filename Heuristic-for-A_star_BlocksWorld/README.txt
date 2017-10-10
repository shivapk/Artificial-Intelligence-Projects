The overall goal of this project is to implement A* search and use it to solve a classic AI search
problem: the "Blocksworld". This problem involves stacking blocks into a target configuration. You are to write a program to solve random instances of this problem using your own implementation of A* search. The focus of the project, however, is to use our intuition to develop a heuristic that will make solving various instances of this problem more effectively and solve them in fewer iterations.

This task involves stacking blocks. The blocks are labeled by integers. Both the Number of Blocks and Stacks are parameters.

Detailed explanination:
Node class - representing states in the Blockworld, 
successor() function for generating all legal moves from a given state.
problem generator() that generates random initial states for testing. This is done by starting from the goal state and performing a sequence of random moves to "scramble" it.

There is a method for keeping track of visited states. As part of applying search algorithms to real-world problems, you have to check for when multiple paths lead to the same state. This frequently happens in many domains, including navigation (where a high degree of connectivity and bidirectional movement along edges creates the possibility for many alternative paths between vertices). If we allow multiple paths to the same state to be generated and placed into the frontier, the queue will quickly expand, and the search will explode exponentially. Thus I used an array for storing previously visited states.  Also, if I came across a state that has been previously visited,I didn't just discarded it - I kept track of the shortest path, whichever has least depth between the new node and the node from when it was previously visited. This is important for maintaining the optimality of algorithms like A*. Finally, there will be a traceback() method to generate and/or print out the solution path, once a goal node has been found. 

The solution path is the sequence of moves and intermediate states that transforms the initial state to the goal state. This can be achieved by calling the parent of the node, the parent's parent, and so on back up to the root (start state), recursively. This is why it is necessary to keep track of the parent state from which a node was generated.


Instructions for compiling and running the A_star.cpp file :

The code is in C++ under the file name A_star.cpp

Build and run the cpp file and then follow the instructions on the command line. 
In MAC/Linux Machines:

# g++ -std=c++11 -c A_star.cpp -o A_star
# ./A_star

Command prompt will ask to enter number of blocks and number of stacks. Enter with a space. 
e.g.
	
	Enter number of Blocks and Stacks respectively
	12 8

After this, the program will print the statistics related to that particular goal search. 

P.S. In case you want to run the program for specific initial states that definitely lead to goal states, inside the main function several examples have been created and commented out. You can 
comment the "problemGenerator" function and remove comments from one of the examples and run the program. Don't forget to mention 
the number of blocks and number of stacks here, that data is being used further in the code. Thanks!
