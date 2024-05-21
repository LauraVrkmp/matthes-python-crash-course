import pytest
from employee import Employee

@pytest.fixture
def employee_instance():
    first_name = "Laura"
    last_name = "Veerkamp"
    annual_salary = 30000
    employee = Employee(first_name, last_name, annual_salary)
    return employee

def test_give_default_raise(employee_instance):
    employee_instance.give_raise()
    assert employee_instance.annual_salary == 35000

def test_give_custom_raise(employee_instance):
    employee_instance.give_raise(10000)
    assert employee_instance.annual_salary == 40000