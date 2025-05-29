import csv

class CSVHandler:
    @staticmethod
    def read_employees(filepath):
        with open(filepath, newline='') as f:
            reader = csv.DictReader(f)
            return [row for row in reader]

    @staticmethod
    def write_assignments(filepath, assignments):
        with open(filepath, mode='w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'Employee_Name', 'Employee_EmailID', 'Secret_Child_Name', 'Secret_Child_EmailID'
            ])
            writer.writeheader()
            writer.writerows(assignments)
