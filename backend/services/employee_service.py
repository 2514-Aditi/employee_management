def get_employees():
    return [
        {"id": 1, "name": "Aditi", "role": "SDE1"},
        {"id": 2, "name": "Rahul", "role": "SDE1"}
    ]

def find_employee(name):
    employees = get_employees()

    for employee in employees:
        if employee["name"].lower() == name.lower():
            return employee

    return None