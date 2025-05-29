import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from employee import Employee
from assignment_engine import AssignmentEngine

class TestSecretSantaAssignment(unittest.TestCase):

    def setUp(self):
        self.employees = [
            Employee("Alice", "alice@example.com"),
            Employee("Bob", "bob@example.com"),
            Employee("Charlie", "charlie@example.com"),
            Employee("David", "david@example.com"),
        ]

    def test_no_self_assignment(self):
        engine = AssignmentEngine(self.employees)
        assignments = engine.assign_secret_santas()
        for giver in self.employees:
            self.assertNotEqual(giver.email, assignments[giver.email].email,
                                f"{giver.name} was assigned to themselves!")

    def test_unique_assignments(self):
        engine = AssignmentEngine(self.employees)
        assignments = engine.assign_secret_santas()

        assigned_emails = [receiver.email for receiver in assignments.values()]
        self.assertEqual(len(set(assigned_emails)), len(self.employees),
                         "Some employees were assigned to multiple people!")

    def test_no_repeat_from_last_year(self):
        last_year_map = {
            "alice@example.com": "bob@example.com",
            "bob@example.com": "charlie@example.com",
            "charlie@example.com": "david@example.com",
            "david@example.com": "alice@example.com",
        }

        engine = AssignmentEngine(self.employees, last_year_mapping=last_year_map)
        assignments = engine.assign_secret_santas()

        for giver in self.employees:
            current_child = assignments[giver.email].email
            last_child = last_year_map.get(giver.email)
            self.assertNotEqual(current_child, last_child,
                                f"{giver.name} was assigned the same child as last year!")

    def test_invalid_assignment_raises(self):
        emps = [
            Employee("Alice", "alice@example.com"),
            Employee("Bob", "bob@example.com"),
        ]
        last_year_map = {
            "alice@example.com": "bob@example.com",
            "bob@example.com": "alice@example.com",
        }
        engine = AssignmentEngine(emps, last_year_mapping=last_year_map)
        with self.assertRaises(ValueError):
            engine.assign_secret_santas()

if __name__ == "__main__":
    unittest.main()
