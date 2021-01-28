# https://www.globaletraining.com/
# Understanding Inheritance
# Inherit: receive something from a predecessor or former owner


class Employee():
    def __init__(self, first_name, last_name, emp_id, years_of_experience):
        self.first_name = first_name
        self.last_name = last_name
        self.emp_id = emp_id
        self.years_of_experience = years_of_experience

    def get_monthly_salary(self):
        pass

    def get_annual_bonus(self):
        pass


class FullTimeManagementEmployee(Employee):
    __management_bonus_percentage = 20

    def __init__(self, first_name, last_name, emp_id, years_of_experience, annual_salary):
        super().__init__(first_name, last_name, emp_id, years_of_experience)
        self.annual_salary = annual_salary

    def get_monthly_salary(self):
        return round(self.annual_salary / 12, 2)

    def get_annual_bonus(self):
        std_bonus = self.annual_salary * (self.__management_bonus_percentage / 100)
        experience_bonus = std_bonus * (self.years_of_experience / 100)
        return std_bonus + experience_bonus


class FullTimeSalariedEmployee(Employee):
    __employee_bonus_percentage = 5

    def __init__(self, first_name, last_name, emp_id, years_of_experience, annual_salary):
        super().__init__(first_name, last_name, emp_id, years_of_experience)
        self.annual_salary = annual_salary

    def get_monthly_salary(self):
        return self.annual_salary / 12

    def get_annual_bonus(self):
        std_bonus = self.annual_salary * (self.__employee_bonus_percentage / 100)
        experience_bonus = std_bonus * (self.years_of_experience / 100)
        return std_bonus + experience_bonus


class HourlyContractor(Employee):
    __contractor_bonus_percentage = 0.00
    __weekly_work_hours = 40

    def __init__(self, first_name, last_name, emp_id, years_of_experience, hourly_rate):
        super().__init__(first_name, last_name, emp_id, years_of_experience)
        self.hourly_rate = hourly_rate

    def get_monthly_salary(self):
        return round((self.__weekly_work_hours * 4) * self.hourly_rate, )

    def get_annual_bonus(self):
        return self.__contractor_bonus_percentage


class HourlyEmployee(Employee):
    __employee_bonus_percentage = 2
    __weekly_work_hours = 40

    def __init__(self, first_name, last_name, emp_id, years_of_experience, hourly_rate):
        super().__init__(first_name, last_name, emp_id, years_of_experience)
        self.hourly_rate = hourly_rate

    def get_monthly_salary(self):
        return (self.__weekly_work_hours * 4) * self.hourly_rate

    def get_annual_bonus(self):
        std_bonus = ((self.__weekly_work_hours * 4) * self.hourly_rate * 12) * (self.__employee_bonus_percentage / 100)
        experience_bonus = std_bonus * (self.years_of_experience / 100)
        return round(std_bonus + experience_bonus, 2)


class FullTimeSalariedSalesEmployee(FullTimeSalariedEmployee):
    __employee_bonus_percentage = 3
    __weekly_work_hours = 40

    def __init__(self, first_name, last_name, emp_id, years_of_experience, annual_salary, commission_percentage):
        super().__init__(first_name, last_name, emp_id, years_of_experience, annual_salary)
        self.annual_salary = annual_salary
        self.commission_percentage = commission_percentage

    def get_monthly_salary(self):
        monthly_salary = (super().get_monthly_salary())
        monthly_commission = monthly_salary * (self.commission_percentage / 100)
        return monthly_salary + monthly_commission

    def get_annual_bonus(self):
        std_bonus = self.annual_salary * (self.__employee_bonus_percentage / 100)
        experience_bonus = std_bonus * (self.years_of_experience / 100)
        return round(std_bonus + experience_bonus, 2)
