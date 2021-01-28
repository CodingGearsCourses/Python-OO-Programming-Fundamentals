# https://www.globaletraining.com/
# Public & Private Access Modifiers
# Public

from Module14_OOPs.ab_oops_getting_deeper_1.oops_getting_deeper_02 import Employee

employee2 = Employee("Papa", "Jones", 50000.00, 10)
monthly_gross_pay = employee2.get_monthly_gross()
standard_annual_bonus = employee2.get_standard_annual_bonus_amount()

print("Annual salary : {:.2f}".format(employee2.base_annual_salary))
print("Monthly gross salary : {:.2f}".format(monthly_gross_pay))
print("Annual Standard Bonus : {:.2f}".format(standard_annual_bonus))