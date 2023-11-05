from bombballUtils import rolls

class BaseBomballRoll:
  ROLL = None
  NAME = None
  NUM_SAMPLES = 1000

  @classmethod
  def roll(cls, *args):
    roll, modifier, result = cls.ROLL(*args)
    formatted_result = cls._format(roll, modifier, result)
    cls._log(formatted_result)
    return formatted_result

  @classmethod
  def sample_roll(cls, args):
    results = {}
    for _ in range(cls.NUM_SAMPLES):
      _, _, result = cls.ROLL(*args)
      if result in results:
        results[result] += 1
      else:
        results[result] = 1
    probabilities = [
      f"{result}: {round(value / cls.NUM_SAMPLES), 2} \n" 
      for result, value in results.items()
    ]
    return f"{cls.NAME}: \n" + sum(probabilities)
      
  @classmethod
  def _format(cls, roll, modifier, result):
    return f"{cls.NAME}: {roll} + {modifier} ({roll + modifier}) -> {result}"


class Hit:
  ROLL = rolls.hit_roll
  NAME = "Hit"

class Dodge:
  ROLL = rolls.dodge_roll
  NAME = "Dodge"

class Stumble:
  ROLL = rolls.stumble_roll
  NAME = "Stumble"

class Fall:
  ROLL = rolls.fall_roll
  NAME = "Fall"

class Throw:
  ROLL = rolls.throw_roll
  NAME = "Throw"

class PassBlock:
  ROLL = rolls.pass_block_roll
  NAME = "Pass Block"

class Catch:
  ROLL = rolls.catch_roll
  NAME = "Catch"

class HoldBall:
  ROLL = rolls.ball_hold_roll
  NAME = "Hold ball"

class BallScatter:
  ROLL = rolls.ball_scatter_roll
  NAME = "Ball Scatter"