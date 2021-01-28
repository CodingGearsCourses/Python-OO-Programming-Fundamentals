# https://www.globaletraining.com/
# Payroll

from Module14_OOPs.ac_oops_getting_deeper_2.Example02.EmployeeTypes import *


class PayrollProcessor:
    def __init__(self, payroll_date):
        self.payroll_date = payroll_date

    def print_payroll_report(self, list_of_employees):
        print("Payroll Report : {} ".center(50, "-").format(self.payroll_date))

        for emp in list_of_employees:
            if isinstance(emp, Employee):
                print("{} {} : {:.2f}".format(emp.first_name, emp.last_name, emp.get_monthly_salary()))
            else:
                print("Found - The Hacker - {} {} - {:.2f}".format(emp.first_name, emp.last_name, emp.get_monthly_salary()))

    def print_annual_bonus_report(self, list_of_employees):
        print("Annual Bonus Report : {} ".center(50, "-").format(self.payroll_date))

        for emp in list_of_employees:
            if isinstance(emp, Employee):
                print("{} {} : {}".format(emp.first_name, emp.last_name, emp.get_annual_bonus()))
            else:
                print("Found - The Hacker - {} {} - {}".format(emp.first_name, emp.last_name, emp.get_annual_bonus()))