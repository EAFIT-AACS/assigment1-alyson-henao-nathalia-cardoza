def minimize_dfa(q, alphabet, final_states, transitions):
    """
    Implements the DFA minimization algorithm to find equivalent states.

    Parameters:
    - q: Number of states in the DFA.
    - alphabet: List of alphabet symbols.
    - final_states: Set of final states.
    - transitions: Transition matrix where transitions[i][k] is the state reached 
                   from i with the kth symbol of the alphabet.

    Returns:
    - List of pairs of equivalent states that can be collapsed in the DFA minimization.
    """
    # Initialize an equivalence matrix of size q x q, initially False
    equivalence = [[False] * q for _ in range(q)]
    
    # Mark final and non-final states
    for i in range(q):
        for j in range(i + 1, q):
            if (i in final_states) != (j in final_states):  # If one is final and the other is not
                equivalence[i][j] = True
                equivalence[j][i] = True
    
    # Refine the equivalence matrix using the state minimization algorithm
    changed = True  # Detect changes in the table
    while changed:
        changed = False  # Assume no changes
        for i in range(q):
            for j in range(i + 1, q):
                if not equivalence[i][j]:  # If they are still indistinguishable
                    for k, symbol in enumerate(alphabet):  # Iterate through each alphabet symbol
                        p_next, q_next = transitions[i][k], transitions[j][k]  # Reached states
                        
                        # If the reached states are marked as different, also mark (i, j)
                        if equivalence[min(p_next, q_next)][max(p_next, q_next)]:
                            equivalence[i][j] = True
                            equivalence[j][i] = True
                            changed = True  # Changes detected, continue iterating
                            break  # (i, j) is distinguished, no need to check more symbols
    
    # Build list of equivalent state pairs
    equivalent_pairs = []
    for i in range(q):
        for j in range(i + 1, q):
            if not equivalence[i][j]:  # If they remain equivalent
                equivalent_pairs.append((i, j))
    
    return equivalent_pairs

def main():
    """
    Main function that reads data from a file, executes minimization, and displays equivalent states.
    """
    try:
        # Open the file "prueba.txt" in read mode with UTF-8 encoding
        with open("prueba.txt", "r", encoding="utf-8") as file:
            cases = int(file.readline().strip())  # Number of test cases
            test_cases = []  # List to store each case

            for _ in range(cases):
                states = int(file.readline().strip())  # Number of states
                alphabet = file.readline().strip().split()  # List of alphabet symbols
                final_states = set(map(int, file.readline().strip().split()))  # Set of final states
                
                # Read the transition table, omitting the first number of each line (state number)
                transitions = [list(map(int, file.readline().strip().split()[1:])) for _ in range(states)]

                # Store the test case in the list
                test_cases.append((states, alphabet, final_states, transitions))

    except FileNotFoundError:
        print("Error: The file does not exist.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    # Process each test case
    for case in test_cases:
        q, alphabet, final_states, transitions = case
        equivalent_pairs = minimize_dfa(q, alphabet, final_states, transitions)  # Execute minimization
        
        # Print equivalent state pairs on the same line
        for p, r in sorted(equivalent_pairs):
            print(f"({p}, {r})", end=" ")
        print()  # New line after printing all pairs of a case

# Execute the main function
main()
