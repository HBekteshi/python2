import pickle

from employee_company.employee import Employee
from employee_company.company import Company

semos = Company("Semos Edukacija", "Kuzman Josifovski Pitu br. 1000", "1234")
seavus = Company("Seavus AD", "Boris Trajkovski br. 60", "9876")

marija = Employee("Marija", "Krstevska", "marija@gmail.com")
kristijan = Employee("Kristijan", "Gjorgiev", "kristijan@gmail.com")
jovan = Employee("Jovan", "Jankov", "jovan@yahoo.com")

# semos.make_offer(kristijan, 50000, "Python Developer")

# Serialize with pickle

#jovan.serialize("emp.pickle")
# print(jovan.deserialize("emp.pickle"))

# Serialize with json
#marija.serialize_json("emp.json")

# with open("emp.pickle", "rb") as f:
#     r = pickle.load(f)
#
# print(r)

# kristijan.accept_offer(semos)
# kristijan.quit()
# kristijan.quit()

# print(kristijan.company)


# semos.hire(jovan, "Developer", 14999)
# print(semos.employee_list)

# print(isinstance(jovan, Company))
#
# class A:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __eq__(self, other):
#         if self.a == other.a and self.b == other.b:
#             return True
#
#         return False
#
# obj1 = A("Hello", 100)
# obj2 = A("Hello", 100)
#
# print(obj1 == obj2)
