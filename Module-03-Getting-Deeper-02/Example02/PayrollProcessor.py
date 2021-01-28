# https://www.globaletraining.com/
# Payroll


class PayrollProcessor:
    def __init__(self, payroll_date):
        self.payroll_date = payroll_date

    def print_payroll_report(self, list_of_employees):
        print("Payroll Report : {} ".center(50, "-").format(self.payroll_date))

        for emp in list_of_employees:
            print("{} {} : {:.2f}".format(emp.first_name, emp.last_name, emp.get_monthly_salary()))

    def print_annual_bonus_report(self, list_of_employees):
        print("Annual Bonus Report : {} ".center(50, "-").format(self.payroll_date))

        for emp in list_of_employees:
            print("{} {} : {}".format(emp.first_name, emp.last_name, emp.get_annual_bonus()))