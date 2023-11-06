from bombballUtils import rolls

class BaseBomballRoll:
  ROLL = None
  NAME = None
  NUM_SAMPLES = 1000

  @classmethod
  def roll(cls, *args):
    roll, modifier, result = cls.ROLL(*args)
    formatted_result = cls._format(roll, modifier, result)
    return formatted_result

  @classmethod
  def sample_roll(cls, *args):
    results = {}
    for _ in range(cls.NUM_SAMPLES):
      _, _, result = cls.ROLL(*args)
      if result in results:
        results[result] += 1
      else:
        results[result] = 1
    probabilities = [
      f"{result}: {round(value / cls.NUM_SAMPLES, 2)} \n" 
      for result, value in results.items()
    ]
    return f"{cls.NAME}: \n" + " ".join(probabilities)
      
  @classmethod
  def _format(cls, roll, modifier, result):
    return f"{cls.NAME}: {roll} + {modifier} ({roll + modifier}) -> {result}"


class Hit(BaseBomballRoll):
  ROLL = rolls.hit_roll
  NAME = "Hit"

class Dodge(BaseBomballRoll):
  ROLL = rolls.dodge_roll
  NAME = "Dodge"

class Stumble(BaseBomballRoll):
  ROLL = rolls.stumble_roll
  NAME = "Stumble"

class Fall(BaseBomballRoll):
  ROLL = rolls.fall_roll
  NAME = "Fall"

class Throw(BaseBomballRoll):
  ROLL = rolls.throw_roll
  NAME = "Throw"

class PassBlock(BaseBomballRoll):
  ROLL = rolls.pass_block_roll
  NAME = "Pass Block"

class Catch(BaseBomballRoll):
  ROLL = rolls.catch_roll
  NAME = "Catch"

class HoldBall(BaseBomballRoll):
  ROLL = rolls.ball_hold_roll
  NAME = "Hold ball"

class BallScatter(BaseBomballRoll):
  ROLL = rolls.ball_scatter_roll
  NAME = "Ball Scatter"
