# Chapter 16. Dynamic Programming

- DP: general technique for solving optimization, search, and counting problems that can be decomposed into subproblems
- Consider DP when have to make choices to solve, specifically, solution relates to subproblems
- DP efficient because caching results of intermeditate computation

- Break problem to subproblems:
  - Original problem solved easily if subproblems are solved
  - Subproblems are cached

## Tips

- DP when have to make choices to arrive at solution
- DP is applicable to counting and decision problems - solutions expressed recursively
- DP involves recrusion. For efficiency, cache is built "bottom up" -> iteratively
- Recursively, cache is hash table or BST; iteratively, cache is one or multi-dimensional array
- To save space, cache can be recycled
- DP is based on combining soltuons to subproblems to yield a solution to original problem.
