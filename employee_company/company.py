from .offer import Offer
import pickle
import json


class Company:

    def __init__(self, name, address, company_id):
        # Initialization of attribute values
        self.name = name
        self.address = address
        self.company_id = company_id
        self.employee_list = []

    def make_offer(self, employee, salary, position):
        offer = Offer(self, employee, salary, position)
        offer.send_offer()
        print(offer)

    def fire(self, employee):
        if (not employee.company) or (employee.company.company_id != self.company_id):
            raise Exception(f"{employee} can't be fired, not working in {self.name}")

        employee.position = None
        employee.salary = None
        employee.company = None

        self.employee_list.remove(employee)

    def get_salary_costs(self):
        total_salary_costs = 0

        for employee in self.employee_list:
            total_salary_costs += employee.salary

        return total_salary_costs

    def serialize(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self.__dict__, f)

    def deserialize(self, filename):
        with open(filename, "rb") as f:
            r = pickle.load(f)
        return r

    def serialize_json(self, filename):
        with open(filename, "w") as f:
            f = json.dumps(self.__dict__, indent=4)
            print(f)

    def __str__(self):
        return self.name
