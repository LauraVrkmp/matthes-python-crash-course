class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, *raise_salary):
        if raise_salary:
            self.annual_salary += raise_salary[0]
        else:
            self.annual_salary += 5000