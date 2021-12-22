import json

from .company import Company
import pickle


class Employee:

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.salary = None
        self.position = None
        self.company = None
        self.offers = dict()

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

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{'first_name': {self.first_name}, 'last_name': {self.first_name} }"

    def __repr__(self):
        return self.full_name()

    def receive_offer(self, offer):
        if not isinstance(offer.company, Company):
            raise Exception(f"{offer.company} is not instance of class Company.")

        if not isinstance(offer.employee, Employee):
            raise Exception(f"{offer.employee} must be instance of class Employee.")

        self.offers[offer.company.company_id] = offer

    def accept_offer(self, company):
        if self.company:
            raise Exception(f"{self} is already employeed in {self.company}")

        offer = self.offers.pop(company.company_id, None)
        if not offer:
            raise Exception(f"No offer was found from company {company}")

        self.company = offer.company
        self.salary = offer.salary
        self.position = offer.position
        self.company.employee_list.append(self)

        print(f"{self} accepted the offer from company {self.company}")

    def quit(self):
        if not self.company:
            raise Exception(f"{self} is not employeed. Can't quit.")

        print(f"{self} is quitting the job from {self.company}")

        self.company.employee_list.remove(self)
        self.company = None
        self.salary = None
        self.position = None
