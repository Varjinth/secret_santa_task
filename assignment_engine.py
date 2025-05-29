import random

class AssignmentEngine:
    def __init__(self, employees, last_year_mapping=None):
        self.employees = employees
        self.last_year_mapping = last_year_mapping or {}

    def assign_secret_santas(self):
        available = self.employees.copy()
        random.shuffle(available)
        assignments = {}

        for giver in self.employees:
            options = [
                receiver for receiver in available
                if receiver.email != giver.email
                and self.last_year_mapping.get(giver.email) != receiver.email
            ]
            if not options:
                raise ValueError("Valid assignment not possible. Try again or check constraints.")
            chosen = random.choice(options)
            assignments[giver.email] = chosen
            available.remove(chosen)

        return assignments
