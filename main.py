from csv_handler import CSVHandler
from assignment_engine import AssignmentEngine
from employee import Employee

def build_employee_objects(data):
    return [Employee(row['Employee_Name'], row['Employee_EmailID']) for row in data]

if __name__ == "__main__":
    employee_data = CSVHandler.read_employees("data/Employee-List.csv")
    employees = build_employee_objects(employee_data)

    try:
        previous = CSVHandler.read_employees("data/Secret-Santa-Game-Result-2023.csv")
        last_year_map = {row['Employee_EmailID']: row['Secret_Child_EmailID'] for row in previous}
    except FileNotFoundError:
        last_year_map = {}

    engine = AssignmentEngine(employees, last_year_map)
    assignments = engine.assign_secret_santas()

    output_data = []
    for giver in employees:
        child = assignments[giver.email]
        output_data.append({
            'Employee_Name': giver.name,
            'Employee_EmailID': giver.email,
            'Secret_Child_Name': child.name,
            'Secret_Child_EmailID': child.email
        })

    CSVHandler.write_assignments("output/Secret_Santa_assignments_2025.csv", output_data)
    print("Secret Santa assignments completed.")
