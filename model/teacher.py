''' ./Model/teacher.py'''
from model.employee import Employee


class Teacher(Employee):
    ''' this class has been extended from Employee class and this is Teacher'''

    # teaching_course   : list course can be teach by teacher
    # following_class   : current list class have been taught by Teacher

    def __init__(self, teaching_course, id_employee,
                 short_name, id_team, facerec_code, following_class):
        self.teaching_course = list(teaching_course)
        self.following_class = list(following_class)
        Employee.__init__(self, id_employee=id_employee, short_name=short_name,
                          id_team=id_team, facerec_code=facerec_code)
