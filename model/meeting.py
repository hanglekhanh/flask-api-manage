'''./model/Meeting.py'''


class Meeting:
    ''' this module use for managing meeting in company'''
    count_meeting = 0

    def __init__(self, start_time, end_time, id_meeting, name_meeting):
        # id_meeting    : id number of meeting
        # start_time    : start time of this meeting
        # end_time      : end time of this
        # name_meeting  : name of meeting

        self.start_time = start_time
        self.end_time = end_time
        self.id_meeting = id_meeting
        self.name_meeting = name_meeting
        Meeting.count_meeting += 1

    def print_info_meeting(self):
        '''this function use for return infomation of meeting'''
        infomation = (self.id_meeting + ', ' + self.name_meeting +
                      ', ' + self.start_time + ', ' + self.end_time)
        return infomation

    def get_count_meeting(self):
        '''this function use for count how many meeting created'''
        return Meeting.count_meeting

    def get_id_meeting(self):
        '''' this function use for get id meeting '''
        return self.id_meeting
