'''./model/Employee.py'''
class Employee:
    ''' this module use for employee in company'''
    # id_employee   : id number of employee
    # short_name    : short name in company
    # id_team       : id number of team belong to this employee
    # facerec_code  : vector 128 number get from face employee
    def __init__(self, id_employee, short_name, id_team, facerec_code):
        self.id_employee = id_employee
        self.short_name = short_name
        self.id_team = id_team
        self.facerec_code = facerec_code
