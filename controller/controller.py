if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from model.meeting import Meeting


def controller():
    i = -1
    while i != 0:

        print('1.  Add training meeting to list')
        print('2.  Update trainning meeting in list')
        print('3.  Show training meeting list')
        print('4.  Delete training meeting in list')
        print('5.  Create student')
        print('6.  Update information student')
        print('7.  Show information student')
        print('8.  Show list student ')
        print('9.  Delete student')
        print('10. Add stundent to training meeting')

        options = {1: add_training_meeting,
                   2: update_training_meeting,
                   3: show_training_meeting,
                   4: delete_training_meeting,
                   5: create_student,
                   6: update_information_student,
                   7: show_info_student,
                   8: show_list_student,
                   9: delete_student,
                   10: add_student_training_meeting,
                   }
        i = int(input('Select option: '))
        if(i != 0):
            options[i]()


def add_training_meeting():
    print('Add trainning meeting completed' + '\n')


def update_training_meeting():
    print('Update completed' + '\n')


def show_training_meeting():
    print('Showw trainning meeting completed' + '\n')


def delete_training_meeting():
    print('delete training meeting completed' + '\n')


def create_student():
    print('create student completed' + '\n')


def update_information_student():
    print('update information completed' + '\n')


def show_info_student():
    print('show information completed' + '\n')


def show_list_student():
    print('showl ist student completed' + '\n')


def delete_student():
    print('delete student completed/n' + '\n')


def add_student_training_meeting():
    print('add student to trainning meeting completed' + '\n')
