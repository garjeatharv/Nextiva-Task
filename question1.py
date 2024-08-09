'''We have a large and complex workflow, made of tasks. And
have to decide who does what, when, so it all gets done on time.
All tasks have dependency on other tasks to complete
Each task(t) has a
D[t] = duration of task
EFT[t] = the earliest finish time for a task
LFT[t] = the latest finish time for a task
EST[t] = the earliest start time for a task
LST[t] = the last start time for a task
Assume
that “clock” starts at 0 (project starting time).
We are given the starting task T_START where the EST[t] = 0 and LST[t] = 0
You have to write an Java/Python/JS/Typescript console application to answer the following questions
Earliest time all the tasks will be completed?
Latest time all tasks will be completed?'''
from collections import defaultdict

class Task:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.predecessors = []
        self.successors = []
        self.est = 0  # Earliest Start Time
        self.eft = 0  # Earliest Finish Time
        self.lst = float('inf')  # Latest Start Time
        self.lft = float('inf')  # Latest Finish Time

    def add_predecessor(self, predecessor):
        self.predecessors.append(predecessor)
        predecessor.successors.append(self)

def calculate_est_eft(tasks):
    """
    Calculate Earliest Start Time (EST) and Earliest Finish Time (EFT) for each task.

    Time Complexity: O(n + m)
    - n: Number of tasks
    - m: Number of dependencies (predecessors)
    """
    for task in tasks:
        if not task.predecessors:
            task.eft = task.est + task.duration
        else:
            task.est = max(pred.eft for pred in task.predecessors)
            task.eft = task.est + task.duration

def calculate_lst_lft(tasks):
    """
    Calculate Latest Start Time (LST) and Latest Finish Time (LFT) for each task.

    Time Complexity: O(n + m)
    - n: Number of tasks
    - m: Number of dependencies (successors)
    """
    max_eft = max(task.eft for task in tasks)
    for task in reversed(tasks):
        if not task.successors:
            task.lft = max_eft
            task.lst = task.lft - task.duration
        else:
            task.lft = min(succ.lst for succ in task.successors)
            task.lst = task.lft - task.duration

def find_critical_paths(tasks, task, path, paths):
    """
    Recursively find all critical paths starting from a given task.

    Time Complexity: O(p * n)
    - p: Number of critical paths
    - n: Number of tasks in the longest path
    """
    path.append(task.name)

    if not task.successors:
        if task.est == task.lst:
            paths.append(path[:])
    else:
        for succ in task.successors:
            if succ.est == succ.lst:
                find_critical_paths(tasks, succ, path, paths)

    path.pop()

def find_all_critical_paths(tasks):
    """
    Find all critical paths in the task network.

    Time Complexity: O(p * n)
    - p: Number of critical paths
    - n: Number of tasks in the longest path
    """
    paths = []
    find_critical_paths(tasks, tasks[0], [], paths)
    return paths

def run_test_case(test_name, tasks, dependencies, expected_earliest, expected_latest, expected_critical_paths):
    """
    Run a test case to validate task scheduling and critical path calculations.

    Time Complexity: O(n + m + p * n) per test case
    - n: Number of tasks
    - m: Number of dependencies
    - p: Number of critical paths
    """
    # Create Task objects
    task_objects = {name: Task(name, duration) for name, duration in tasks.items()}
    
    # Set up dependencies
    for task, preds in dependencies.items():
        for pred in preds:
            task_objects[task].add_predecessor(task_objects[pred])

    # List of tasks in topological order
    task_order = list(tasks.keys())
    task_objects_list = [task_objects[name] for name in task_order]

    # Calculate EST and EFT
    calculate_est_eft(task_objects_list)

    # Calculate LST and LFT
    calculate_lst_lft(task_objects_list)

    # Determine all critical paths
    critical_paths = find_all_critical_paths(task_objects_list)

    # Output results and compare with expected
    earliest_completion = max(task.eft for task in task_objects_list)
    latest_completion = max(task.lft for task in task_objects_list)

    test_result = (earliest_completion == expected_earliest and
                   latest_completion == expected_latest and
                   any(path in expected_critical_paths for path in critical_paths))

    print(f"Test: {test_name}")
    print(f"  Expected Earliest Completion: {expected_earliest}, Got: {earliest_completion}")
    print(f"  Expected Latest Completion: {expected_latest}, Got: {latest_completion}")
    print(f"  Expected Critical Paths: {expected_critical_paths}, Got: {critical_paths}")
    print(f"  Test {'Passed' if test_result else 'Failed'}\n")

    return test_result

def main():
    test_cases = [
        {
            "name": "Test Case 1 - Simple Workflow",
            "tasks": {'T_START': 0, 'A': 4, 'B': 2, 'C': 3, 'D': 5, 'E': 2, 'T_END': 0},
            "dependencies": {
                'A': ['T_START'],
                'B': ['A'],
                'C': ['A'],
                'D': ['B', 'C'],
                'E': ['C'],
                'T_END': ['D', 'E'],
            },
            "expected_earliest": 12,
            "expected_latest": 12,
            "expected_critical_paths": [['T_START', 'A', 'C', 'D', 'T_END']]
        },
        {
            "name": "Test Case 2 - Parallel Tasks",
            "tasks": {'T_START': 0, 'A': 3, 'B': 3, 'C': 4, 'T_END': 0},
            "dependencies": {
                'A': ['T_START'],
                'B': ['T_START'],
                'C': ['A', 'B'],
                'T_END': ['C'],
            },
            "expected_earliest": 7,
            "expected_latest": 7,
            "expected_critical_paths": [['T_START', 'A', 'C', 'T_END'], ['T_START', 'B', 'C', 'T_END']]
        },
        {
            "name": "Test Case 3 - Independent Chains",
            "tasks": {'T_START': 0, 'A': 3, 'B': 2, 'C': 3, 'D': 2, 'T_END': 0},
            "dependencies": {
                'A': ['T_START'],
                'B': ['T_START'],
                'C': ['A'],
                'D': ['B'],
                'T_END': ['C', 'D'],
            },
            "expected_earliest": 6,
            "expected_latest": 6,
            "expected_critical_paths": [['T_START', 'A', 'C', 'T_END'], ['T_START', 'B', 'D', 'T_END']]
        },
        {
            "name": "Test Case 4 - Multiple Critical Paths",
            "tasks": {'T_START': 0, 'A': 4, 'B': 4, 'C': 2, 'D': 3, 'T_END': 0},
            "dependencies": {
                'A': ['T_START'],
                'B': ['T_START'],
                'C': ['A', 'B'],
                'D': ['C'],
                'T_END': ['D'],
            },
            "expected_earliest": 9,
            "expected_latest": 9,
            "expected_critical_paths": [['T_START', 'A', 'C', 'D', 'T_END'], ['T_START', 'B', 'C', 'D', 'T_END']]
        }
    ]

    all_tests_passed = True
    for test in test_cases:
        result = run_test_case(
            test["name"],
            test["tasks"],
            test["dependencies"],
            test["expected_earliest"],
            test["expected_latest"],
            test["expected_critical_paths"]
        )
        all_tests_passed = all_tests_passed and result

    if all_tests_passed:
        print("All tests passed!")
    else:
        print("Some tests failed.")

if __name__ == '__main__':
    main()
