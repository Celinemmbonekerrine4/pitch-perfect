import unnitest
from app.models import Pitch

class PitchTest(unittest.TestCase):

    def setUp(self):
        self.new_pitch = Pitch(1234,'Pitch')

    def test_instance(self):
        self.asserttrue(isinstance(self.new_pitch.Pitch))

        