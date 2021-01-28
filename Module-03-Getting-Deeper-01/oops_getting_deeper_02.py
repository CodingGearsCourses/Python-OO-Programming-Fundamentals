# https://www.globaletraining.com/
# Public & Private Access Modifiers
# Public


class Employee:

    # Class Constructor (Method with a special name)
    def __init__(self, first_name, last_name, base_annual_salary, bonus_percentage):
        self.first_name = first_name
        self.last_name = last_name
        self.base_annual_salary = base_annual_salary
        self.bonus_percentage = bonus_percentage

    # Methods
    def get_monthly_gross(self):
        return self.base_annual_salary / 12

    def get_standard_annual_bonus_amount(self):
        return self.base_annual_salary * (self.bonus_percentage/100)


def main():
    print("Hello from main()!")

    employee1 = Employee("Kara", "Smith", 100000.00, 10)
    monthly_gross_pay = employee1.get_monthly_gross()
    standard_annual_bonus = employee1.get_standard_annual_bonus_amount()

    print("Annual salary : {:.2f}".format(employee1.base_annual_salary))
    print("Monthly gross salary : {:.2f}".format(monthly_gross_pay))
    print("Annual Standard Bonus : {:.2f}".format(standard_annual_bonus))


if __name__ == '__main__':
    main()
