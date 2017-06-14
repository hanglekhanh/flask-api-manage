from employee import employee


class student(employee):

    # following_class : list class of student following study
    def __init__(self, id_employee, short_name, id_team, facerec_code, following_class):
        self.following_class = following_class
        employee.__init__(self, id_employee=id_employee, short_name=short_name,
                          id_team=id_team, facerec_code=facerec_code)
