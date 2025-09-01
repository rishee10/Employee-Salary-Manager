# employee_module.py

class Employee:
    def __init__(self, emp_id: int, name: str, salary: float):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.bonus = 20

    def apply_bonus(self, percentage: float) -> float:
        """
        Apply a percentage bonus to the employee's salary.
        Updates the bonus attribute and returns the final salary.
        """
        self.bonus = (self.salary * percentage) / 100
        return self.salary + self.bonus

    def __str__(self):
        return f"{self.name} | Final Salary: {self.salary + self.bonus}"
