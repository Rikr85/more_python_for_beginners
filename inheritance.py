# Inheriting from a class

class Person:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print('Hello, ' + self.name)

class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school
    def sing_school_song(self):
        print('Ode to ' + self.school)
    def say_hello(self):
        # Let the parent do some work
        super().say_hello()
        # Add on custom code
        print('I am rather tired')
    def __str__(self) -> str:
        return f'{self.name} attends {self.school}'
    
student = Student('Christopher', 'UVM')
student.say_hello()
# student.sing_school_song()

# What are you?
# print(isinstance(student, Student))
# print(isinstance(student, Person))
# print(issubclass(Student, Person))

print(f'Is this a student? {isinstance(student, Student)}')
print(f'Is this a person? {isinstance(student, Person)}')
print(f'Is Student a Person? {issubclass(Student, Person)}')
