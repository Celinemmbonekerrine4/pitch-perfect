class Pitch:

  def  __init__(self,id,title,pitch,vote_average,vote_count):
    self.id = id
    self.title = title
    self.pitch = pitch
    self.vote_average = vote_average
    self.vote_count = vote_count

  all_pitches = []

  def save_pitch(self):
      Pitch.all_pitches.append(self)

  @classmethod
  def clear_pitches(cls):
    Pitch.all_pitches.clear()

  @classmethod
  def get_pitches(cls):

    response = []

    for pitch in cls.all_pitches:
      if pitch.pitch_id == id:
        response.append(pitch)

      return response





  


    
    