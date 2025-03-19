import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged_data = employee.merge(department, how='left', left_on='departmentId', right_on='id')

    max_salaries = merged_data.groupby('departmentId')['salary'].transform(max)

    highest_salary_employees = merged_data[merged_data['salary'] == max_salaries]

    result = highest_salary_employees[['name_y', 'name_x', 'salary']].rename(
        columns={'name_y': 'Department', 'name_x': 'Employee', 'salary': 'Salary'})
    
    return result