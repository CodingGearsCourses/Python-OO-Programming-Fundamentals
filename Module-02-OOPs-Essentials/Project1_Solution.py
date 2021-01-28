# Project Solution


class EmployeeManagement:
    employer_retirement_contribution_percentage = 0.5
    vacation_hours_per_week = 2
    vacation_bonus_1 = 0.1
    vacation_bonus_2 = 0.2
    vacation_bonus_3 = 0.3
    vacation_bonus_4 = 0.4
    vacation_bonus_5 = 0.5

    # Class Constructor/Initializer (Method with a special name)
    def __init__(self, first_name, last_name, base_annual_salary, annual_bonus_percentage,
                 years_of_employment, employee_retirement_contribution_percentage):
        # Object Attributes/Variables
        self.first_name = first_name
        self.last_name = last_name
        self.base_annual_salary = base_annual_salary
        self.annual_bonus_percentage = annual_bonus_percentage
        self.years_of_employment = years_of_employment
        self.employee_retirement_contribution_percentage = employee_retirement_contribution_percentage

    #  Methods
    def calculate_bonus(self):
        return self.base_annual_salary * self.annual_bonus_percentage

    def calculate_vacation_hours(self):
        base_vacation_hours = self.vacation_hours_per_week * 52

        if self.years_of_employment == 1:
            bonus_vacation_hours = base_vacation_hours * self.vacation_bonus_1
        if self.years_of_employment == 2:
            bonus_vacation_hours = base_vacation_hours * self.vacation_bonus_2
        if self.years_of_employment == 3:
            bonus_vacation_hours = base_vacation_hours * self.vacation_bonus_3
        if self.years_of_employment == 4:
            bonus_vacation_hours = base_vacation_hours * self.vacation_bonus_4
        if self.years_of_employment == 5 or self.years_of_employment > 5:
            bonus_vacation_hours = base_vacation_hours * self.vacation_bonus_5

        return round(base_vacation_hours + bonus_vacation_hours, 2)

    def calculate_total_contribution_to_retirement_fund(self):
        employee_contribution_rf = self.base_annual_salary * self.employee_retirement_contribution_percentage

        if self.employee_retirement_contribution_percentage <= .05:
            employer_contribution_rf = employee_contribution_rf * self.employer_retirement_contribution_percentage
            return employee_contribution_rf + employer_contribution_rf

        if self.employee_retirement_contribution_percentage > .05:
            employee_contribution_rf_five_percent = self.base_annual_salary * 0.05
            employer_contribution_rf = employee_contribution_rf_five_percent * \
                                       self.employer_retirement_contribution_percentage
            return employee_contribution_rf + employer_contribution_rf


def main():
    first_name = str(input("Enter the employee's first name : "))
    last_name = str(input("Enter the employee's last name : "))
    while True:
        base_annual_salary = float(input("Enter the base annual salary : "))
        if 45000.00 <= base_annual_salary <= 125000.00:
            break
        else:
            print("Base annual salary must be between 45000.00 and 125000.00")

    while True:
        annual_bonus_percentage = float(float(input("Enter the bonus percentage: ")) / 100)
        if 0.1 <= annual_bonus_percentage <= 0.2:
            break
        else:
            print("Annual bonus must be between 10% and 20%")

    years_of_employment = int(input("Enter number of years of employment : "))

    while True:
        retirement_contribution_percentage = float(float(input("Enter the retirement contribution percentage: ")) / 100)
        if 0 <= retirement_contribution_percentage <= 0.1:
            break
        else:
            print("Retirement contributions must be between 0% and 10%")

    employee1 = EmployeeManagement(first_name, last_name, base_annual_salary, annual_bonus_percentage,
                                   years_of_employment, retirement_contribution_percentage)

    bonus = employee1.calculate_bonus()
    vacation = employee1.calculate_vacation_hours()
    retirement_fund_contribution = employee1.calculate_total_contribution_to_retirement_fund()
    print("Report: {} {}".format(first_name, last_name).center(50, "-"))

    # print("Bonus : ".ljust(35), str(bonus).rjust(10))
    # print("Vacation Hours : ".ljust(35), str(vacation).rjust(10))
    # print("Retirement Fund Contribution : ".ljust(35), str(retirement_fund_contribution).rjust(10))

    print("{:30} {:12,.2f}".format("Bonus :", bonus))
    print("{:30} {:12,.2f}".format("Vacation Hours :", vacation))
    print("{:30} {:12,.2f}".format("Retirement Fund Contribution :", retirement_fund_contribution))
    print("-".center(50, "-"))


if __name__ == '__main__':
    main()
