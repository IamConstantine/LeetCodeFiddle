from unittest import TestCase

from MeetingRoomsII import minMeetingRooms


class Test(TestCase):
    def test_min_meeting_rooms(self):
        self.assertEqual(2, minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
        self.assertEqual(1, minMeetingRooms([[7,10],[2,4]]))
        self.assertEqual(1, minMeetingRooms([[13,15],[1,13]]))
