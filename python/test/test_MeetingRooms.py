from unittest import TestCase

from MeetingRooms import canAttendMeetings


class Test(TestCase):
    def test_can_attend_meetings(self):
        self.assertEqual(False, canAttendMeetings([[0, 30], [5, 10], [15, 20]]))
        self.assertEqual(True, canAttendMeetings([[7, 10], [2, 4]]))
