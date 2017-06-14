from employee import employee


class teacher(employee):
    #teaching_course    : list course can be teach by teacher
    def __init__(self, teaching_course, id_employee, short_name, id_team, facerec_code, following_class):
        self.teaching_course = teaching_course
        employee.__init__(self, id_employee=id_employee, short_name=short_name,
                          id_team=id_team, facerec_code=facerec_code)
