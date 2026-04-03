A collection of high-performance solvers exploring state-space search and heuristic optimization, inspired by techniques in "Artificial Intelligence: A Modern Approach" by Russell & Norvig.

🎯 Project Overview

The goal of this project is to implement and compare various search strategies for solving the 3x3 Rubik's Cube. 

🛠 Planned Search Strategies

I am implementing several foundational AI algorithms to benchmark their performance in terms of time complexity and solution optimality:

    Iterative Deepening Depth-First Search (IDDFS): Combines the memory efficiency of DFS with the optimality of BFS.

    Iterative Deepening A (IDA*):* Utilizing admissible heuristics (such as Manhattan distance for corners and edges) to prune the search tree.

    Bidirectional Search: Exploring the state space simultaneously from the scrambled state and the solved state to significantly reduce the effective search depth.

🚀 Key Technical Challenges

    Heuristic Generation: Developing pattern databases to provide the IDA* algorithm with strong lower bounds for the remaining distance to the goal.

    Move Pruning: Implementing symmetry reductions to avoid redundant search paths.

📚 References

    Russell, S. J., & Norvig, P. Artificial Intelligence: A Modern Approach.