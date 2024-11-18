# STATIC METHOD - A method that belong to a class rather than any object from that class (instance)
#                 Usually used for general utility functions

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data



class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Web Developer", "Data Analyst", "Front End Dev", "Back End Dev", "Full Stacks Dev"]
        return position in valid_positions

# 1.) INSTANCE METHODS
employee1 = Employee("Rency","Software Developer")
employee2 = Employee("Gon","Hunter")
employee3 = Employee("Killua","Assasin & Hunter")

print(employee1.name)
print(employee1.position)
print(employee1.get_info())

print(employee2.name)
print(employee2.position)
print(employee2.get_info())

print(employee3.name)
print(employee3.position)
print(employee3.get_info())

# 2.) STATIC METHODS
print(Employee.is_valid_position("Data Analyst"))


# class ToyBox:
#     # This is a static method
#     @staticmethod
#     def count_toys():
#         # It doesn't need to look inside a specific toy box to work
#         return "There are 5 toys in the box!"
#
# # You can call the static method without creating a toy box
# print(ToyBox.count_toys())

# In Python, a static method is like that magic button.
# It belongs to the class (like a toy box), but it doesn’t need to open or look inside the class (or the toy box) to do its job.
# It just does something related to the class without needing to see the details inside.