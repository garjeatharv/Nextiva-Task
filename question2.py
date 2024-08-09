'''Question: Both Alice & Bob have friends. Create a Java/Python/JS/Typescript console application to find all the friends of Alice and all the friends of Bob & common friends of Alice and Bob.
Your algorithm should be able to do the following:
Take any 2 friends and find the common friends between the 2 friends
Take any 2 friends find the nth connection - for example: connection(Alice, Janice) => 2
Alice has friend Bob and Bob has friend Janice, if the input given is Alice and Janice the output should be 2, meaning 2nd connection, that means Janice is the second connection of Alice and Bob being the 1st connection of Alice.
Likewise if input given is Alice and Bob, the output should be 1, for 1st connection
If there is no connection at all, it should return -1'''

from collections import defaultdict, deque

class SocialNetwork:
    def __init__(self):
        self.network = defaultdict(set)

    def add_friendship(self, person1, person2):
        """Adds a bidirectional friendship between two people."""
        self.network[person1].add(person2)
        self.network[person2].add(person1)
        # Time Complexity: O(1) - Adding an element to a set is O(1) on average.

    def find_friends(self, person):
        """Returns a list of friends for the given person."""
        return self.network[person]
        # Time Complexity: O(1) - Accessing the friends of a person is O(1).

    def find_common_friends(self, person1, person2):
        """Returns a list of common friends between two people."""
        return self.network[person1].intersection(self.network[person2])
        # Time Complexity: O(min(F1, F2)) - where F1 and F2 are the number of friends of person1 and person2.
        # The intersection operation takes O(min(F1, F2)).

    def find_nth_connection(self, person1, person2):
        """Finds the nth connection (degrees of separation) between two people."""
        if person1 == person2:
            return 0
            # Time Complexity: O(1) - Direct check if both persons are the same.

        visited = set()
        queue = deque([(person1, 0)])  # (current_person, level)

        while queue:
            current_person, level = queue.popleft()

            if current_person == person2:
                return level
                # Time Complexity: O(1) - Once the target person2 is found.

            visited.add(current_person)

            for friend in self.network[current_person]:
                if friend not in visited:
                    queue.append((friend, level + 1))
                    # Time Complexity: O(F) - where F is the number of friends for the current_person.

        return -1  # No connection found
        # Time Complexity: O(V + E) - where V is the number of people and E is the number of friendships.
        # The algorithm explores all vertices and edges in the worst case.

def run_tests():
    sn = SocialNetwork()

    # Adding friendships for testing
    sn.add_friendship("Alice", "Bob")
    sn.add_friendship("Bob", "Janice")
    sn.add_friendship("Alice", "Charlie")
    sn.add_friendship("Charlie", "David")
    sn.add_friendship("Janice", "David")
    sn.add_friendship("Bob", "Charlie")
    
    # Define test cases
    test_cases = [
        # Test case 1: Find all friends of Alice and Bob
        {
            "description": "Find all friends of Alice and Bob",
            "action": lambda: (
                sorted(sn.find_friends("Alice")),
                sorted(sn.find_friends("Bob"))
            ),
            "expected": (
                sorted(["Bob", "Charlie"]),
                sorted(["Alice", "Charlie", "Janice"])
            )
        },
        # Test case 2: Find common friends between Alice and Bob
        {
            "description": "Find common friends between Alice and Bob",
            "action": lambda: sorted(sn.find_common_friends("Alice", "Bob")),
            "expected": sorted(["Charlie"])
        },
        # Test case 3: Find nth connection between Alice and Janice
        {
            "description": "Find nth connection between Alice and Janice",
            "action": lambda: sn.find_nth_connection("Alice", "Janice"),
            "expected": 2
        },
        # Test case 4: Find nth connection between Alice and Bob
        {
            "description": "Find nth connection between Alice and Bob",
            "action": lambda: sn.find_nth_connection("Alice", "Bob"),
            "expected": 1
        },
        # Test case 5: Find nth connection between Alice and David
        {
            "description": "Find nth connection between Alice and David",
            "action": lambda: sn.find_nth_connection("Alice", "David"),
            "expected": 2
        },
        # Test case 6: Find nth connection between Alice and Eve (no connection)
        {
            "description": "Find nth connection between Alice and Eve (no connection)",
            "action": lambda: sn.find_nth_connection("Alice", "Eve"),
            "expected": -1
        }
    ]

    # Run test cases
    all_tests_passed = True
    for case in test_cases:
        result = case["action"]()
        if result == case["expected"]:
            print(f"Test Passed: {case['description']}, Got: {result}")
        else:
            print(f"Test Failed: {case['description']}")
            print(f"  Expected: {case['expected']}, Got: {result}")
            all_tests_passed = False

    if all_tests_passed:
        print("All tests passed!")
    else:
        print("Some tests failed.")

# Run the test cases
if __name__ == "__main__":
    run_tests()
