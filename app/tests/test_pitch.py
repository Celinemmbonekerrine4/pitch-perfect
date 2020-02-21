import unittest
from app.models import Pitch,User
from app import db


class PitchTest(unittest.TestCase):

    def setUp(self):
        self.user_celine = Pitch(username = 'celine', password= 'celinemmbone3',email = 'celinekerrine@gmail.com')
        self.new_pitch = Pitch(pitch_id=12345)
        self.asserttrue(isinstance(self.new_pitch.Pitch))
def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

        