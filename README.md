-Student’s full name: Nathalia Valentina Cardoza Azuaje, Alyson Dahiana Henao Fernandez

-Student’s class number: 7309

-Versions of the operating system: Python 3.12 (64-bit)

-Programming language: Python

-Tools used in the implementation: Visual Studio Code (Version 1.97.2)

-Detailed instructions for running your implementation: 
Download and install Visual Studio Code on your computer. Once installed, add the Python extension to Visual Studio Code. Next, download the provided files and open them within the Visual Studio Code environment. Finally, run the uploaded code to complete the process.

-Explanation of the algorithm: 
The algorithm identifies and show which states can be collapsed to produce a smaller DFA with the same language. It first initializes a q × q equivalence matrix assuming all states are equivalent. Then, it marks final and non-final states as distinguishable since they cannot be equivalent. The algorithm iteratively refines this distinction by checking transitions: if two states `(i, j)` transition to states that are already marked as distinguishable, then `(i, j)` must also be distinguishable. This refinement continues until no more changes occur. Finally, the algorithm collects all remaining unmarked pairs as they represent equivalent states that can be collapsed. Given a DFA with states, an alphabet, final states, and a transition table, this method finds and outputs pairs of equivalent states, helping to construct a minimized DFA.