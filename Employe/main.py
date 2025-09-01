# main.py

from salary_utils import fetch_employees, post_salary_update

BONUS_PERCENTAGE = 10  # Example bonus percentage

def main():
    employees = fetch_employees()

    print("\n--- Employee Salary Report ---")
    for emp in employees:
        final_salary = emp.apply_bonus(BONUS_PERCENTAGE)
        print(f"{emp.name} | Final Salary: {final_salary}")
        post_salary_update(emp)


if __name__ == "__main__":
    main()
