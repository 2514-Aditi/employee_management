from services.employee_service import get_employees

def show_employees():
    employees = get_employees()

    for employee in employees:
        print(employee)