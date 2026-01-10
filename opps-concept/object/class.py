# Class: Class is blueprint or a template.Eg form for an exam that contains name age electives
# father name ects.

# Object: Specific instance created from the template (class ).Eg from which contains the data for duffy
class Employee:
    company="HCL"
    position="Data Analyst"

    def get_salary(self):
         #Self is a way to reference the object the class.
        return 30000

e=Employee()
# An Object of class employee is created here
print(e.get_salary())
print(e.position)

e2=Employee()
print(e2.company)