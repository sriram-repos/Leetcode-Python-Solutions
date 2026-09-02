# LeetCode 1: Two Sum

## Leetcode Hint
A really brute force way would be to search for all possible pairs of numbers but that would be too slow. Again, it's best to try out brute force solutions just for completeness. It is from these brute force solutions that you can come up with optimizations.

## Python Dictionary
Using a brute-force approach requires a nested loop, leading to O(N²) time complexity. By utilizing a **Hash Map (Python Dictionary)**, we can look backward as we iterate forward, turning lookups into an instantaneous O(1) operation.

## Complexity Analysis
* **Time Complexity:** O(N) — We scan the array of `N` elements exactly once.
* **Space Complexity:** O(N) — In the worst-case scenario, the dictionary will store all elements.

