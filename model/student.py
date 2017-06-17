'''./model/student.py'''
from model.employee import Employee


class Student(Employee):
    ''' this class has been extended from Employee class and this is Student'''
    # following_class : list class of student following study
    def __init__(self, id_employee, short_name, id_team, facerec_code, following_class):
        self.following_class = following_class
        Employee.__init__(self, id_employee=id_employee, short_name=short_name,
                          id_team=id_team, facerec_code=facerec_code)
