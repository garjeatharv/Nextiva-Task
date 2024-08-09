# Task Scheduling & Social Network Console Applications

This repository contains two console applications implemented in Python: 

1. **Task Scheduling Application**: Designed to compute the earliest and latest completion times for a workflow of tasks, given their dependencies, and identify critical paths.
2. **Social Network Application**: Allows users to manage friendships, find common friends, and determine the degree of connection between people in a social network.

## Table of Contents

- [Task Scheduling Application](#task-scheduling-application)
  - [Overview](#overview)
  - [Features](#features)
  - [Code Structure](#code-structure)
  - [Time Complexity](#time-complexity)
- [Social Network Application](#social-network-application)
  - [Overview](#overview-1)
  - [Features](#features-1)
  - [Code Structure](#code-structure-1)
  - [Time Complexity](#time-complexity-1)

---

## Task Scheduling Application

### Overview

The Task Scheduling Application is designed to help project managers and developers determine the optimal schedule for completing tasks within a project. Each task has a specified duration and may depend on other tasks to be completed before it starts.

### Features

- **Earliest Start Time (EST)** and **Earliest Finish Time (EFT)** calculation for each task.
- **Latest Start Time (LST)** and **Latest Finish Time (LFT)** calculation for each task.
- Identification of **Critical Paths** that indicate the longest path(s) through the task network, determining the project's duration.

### Code Structure

- **`Task` Class**: Represents a task with attributes like duration, predecessors, successors, EST, EFT, LST, and LFT.
- **`calculate_est_eft(tasks)` Function**: Calculates the EST and EFT for all tasks based on their dependencies.
- **`calculate_lst_lft(tasks)` Function**: Calculates the LST and LFT for all tasks based on their dependencies.
- **`find_critical_paths(tasks)` Function**: Identifies all critical paths in the task network.
- **`run_test_case(test_name, tasks, dependencies, expected_earliest, expected_latest, expected_critical_paths)` Function**: Runs test cases to validate the correctness of the task scheduling algorithm.

### Time Complexity

- **`calculate_est_eft(tasks)`**: O(n + m)
- **`calculate_lst_lft(tasks)`**: O(n + m)
- **`find_critical_paths(tasks)`**: O(p * n)
- **Overall**: The overall time complexity per test case is O(n + m + p * n).

Where:
- **n** is the number of tasks.
- **m** is the number of dependencies.
- **p** is the number of critical paths.

---

## Social Network Application

### Overview

The Social Network Application allows users to manage and explore friendships within a network. The application provides functionalities to find all friends of a person, identify common friends between two individuals, and determine the degree of connection between them.

### Features

- Add friendships between users.
- Find all friends of a specific person.
- Find common friends between two users.
- Determine the degree of connection (nth connection) between two users.

### Code Structure

- **`SocialNetwork` Class**: Manages the network of users and their friendships.
  - **`add_friendship(person1, person2)`**: Adds a bidirectional friendship between two people.
  - **`find_friends(person)`**: Returns a list of friends for a specific person.
  - **`find_common_friends(person1, person2)`**: Returns a list of common friends between two people.
  - **`find_nth_connection(person1, person2)`**: Finds the nth connection (degrees of separation) between two people.

### Time Complexity

- **`add_friendship(person1, person2)`**: O(1) - Adding a friendship is O(1) on average.
- **`find_friends(person)`**: O(1) - Accessing the friends of a person is O(1).
- **`find_common_friends(person1, person2)`**: O(min(F1, F2)) - where F1 and F2 are the number of friends of person1 and person2.
- **`find_nth_connection(person1, person2)`**: O(V + E) - where V is the number of people and E is the number of friendships.

---
