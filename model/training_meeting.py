''' ./Model/training_meeting.py'''
from model.meeting import Meeting


class TrainingMeeting(Meeting):
    ''' this class has been extended from Meeting class and this is training class'''

    # course       : course of this class (course.py)
    # teacher      : who teach this class (teacher.py)
    # list_student : list student join this class (student.py)
    # start_time   : start time of this class
    # end_time     : end time of this class
    # id_meeting   : id of meeting or class
    meetingList = []  # store currentlist training metting
    count_listmeeting = 0

    def __init__(self, course, teacher, list_student,
                 start_time, end_time, id_meeting):
        self.course = course
        self.teacher = teacher
        self.list_student = list_student
        Meeting.__init__(self, start_time=start_time,
                         end_time=end_time, id_meeting=id_meeting)

    @classmethod
    def add_meeting_list(cls, meeting_object):
        '''this function use for add object in the list'''
        if isinstance(TrainingMeeting, meeting_object):
            TrainingMeeting.meetingList.append(meeting_object)
        else:
            print('wrong type of objert')

    @classmethod
    def del_meeting_list(cls, meeting_object):
        '''this function use for del object in the list'''
        if isinstance(TrainingMeeting, meeting_object):
            name = Meeting.get_id_meeting(meeting_object)
            for i in TrainingMeeting.meetingList:
                if i.id_meeting == name:
                    TrainingMeeting.meetingList.remove(i)
                    break
        else:
            print('wrong type of objert')

    @classmethod
    def get_meeting_list(cls):
        '''this function use for get list meeting'''
        print(TrainingMeeting.meetingList)
