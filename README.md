# Coin Change Problem

This repository contains implementations of two algorithms for solving the coin change problem. Given a set of coin denominations and an amount, the objective is to determine the minimum number of coins needed to make up that amount. The repository includes:

- **Greedy Algorithm** implementation (`find_coins_greedy`)
- **Dynamic Programming Algorithm** implementation (`find_min_coins`)

The two approaches are compared in terms of efficiency and results based on different coin sets.

## Problem Statement

Imagine you are developing a system for a cash register that should determine the optimal way to provide change to a customer. The goal is to find the minimum number of coins needed to make up a given amount using available denominations.

### Requirements:

1. **Greedy Algorithm** (`find_coins_greedy`): The function should use a greedy approach, always selecting the largest possible denomination first.
2. **Dynamic Programming Algorithm** (`find_min_coins`): The function should use a dynamic programming approach to find the minimum combination of coins, regardless of order or size.

## Implementations

### Greedy Algorithm

The greedy algorithm is implemented in `find_coins_greedy`. This function:

- Iterates through each denomination in descending order.
- Selects the largest coin denomination possible for the remaining amount until it reaches zero.

This approach is fast but does not always guarantee an optimal solution.

### Dynamic Programming Algorithm

The dynamic programming algorithm, implemented in `find_min_coins`, uses:

- A table to keep track of the minimum number of coins required for each amount up to the target.
- It ensures that the solution is globally optimal by considering all possible combinations of coin denominations.

This method is slower for large inputs but provides an optimal solution for any set of coin denominations.

## Comparison Results

For testing, we ran both algorithms on two coin sets for an amount of **113**. Here are the results:

```plaintext
+-----------------------+-------------+----------------------------+---------------+
| Coin Set              | Algorithm   | Coins Used                 |   Total Coins |
+=======================+=============+============================+===============+
| [50, 25, 10, 5, 2, 1] | Greedy      | {50: 2, 10: 1, 2: 1, 1: 1} |             5 |
+-----------------------+-------------+----------------------------+---------------+
| [50, 25, 10, 5, 2, 1] | Dynamic     | {50: 2, 10: 1, 2: 1, 1: 1} |             5 |
+-----------------------+-------------+----------------------------+---------------+
| [10, 6, 1]            | Greedy      | {10: 11, 1: 3}             |            14 |
+-----------------------+-------------+----------------------------+---------------+
| [10, 6, 1]            | Dynamic     | {10: 10, 6: 2, 1: 1}       |            13 |
+-----------------------+-------------+----------------------------+---------------+
```

## Conclusions and Performance Analysis

### Algorithm Efficiency

Both algorithms have different time complexities:

- The **Greedy Algorithm** is generally faster with time complexity of **_O(n)_** where **_n_** is the number of denominations. However, it may not yield the optimal solution for arbitrary coin sets.
- **The Dynamic Programming Algorithm** has a higher time complexity, approximately **_O(m⋅n)_**, where **_m_** is the amount and **_n_** is the number of denominations. Despite this, it always finds the optimal solution.

### Handling Large Amounts

The greedy algorithm performs well with traditional coin denominations but can fail to produce optimal solutions with unconventional denominations. The dynamic programming approach, though computationally intensive, remains reliable even with larger sums and unusual coin sets, making it preferable for applications requiring consistent accuracy.

In summary, for general cases with typical coin sets, the greedy algorithm provides a quick solution. However, the dynamic programming algorithm ensures minimal coin usage and performs best when accuracy is essential, regardless of execution time.
