# salary_utils.py

import json
from employee_module import Employee

EMPLOYEE_FILE = "employees.json"

def fetch_employees():
    """
    Simulates a GET request to fetch all employees from employees.json.
    Returns a list of Employee objects.
    """
    with open(EMPLOYEE_FILE, "r") as file:
        data = json.load(file)

    employees = [
        Employee(emp["id"], emp["name"], emp["salary"])
        for emp in data["employees"]
    ]
    return employees


def post_salary_update(employee: Employee):
    """
    Simulates a POST request to update an employee's salary in employees.json.
    """
    with open(EMPLOYEE_FILE, "r") as file:
        data = json.load(file)

    for emp in data["employees"]:
        if emp["id"] == employee.emp_id:
            emp["salary"] = employee.salary + employee.bonus

    with open(EMPLOYEE_FILE, "w") as file:
        json.dump(data, file, indent=4)
