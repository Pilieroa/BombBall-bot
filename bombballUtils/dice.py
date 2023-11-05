import random

def _roll_a_die(sides):
  return random.randint(1, sides)

roll_a_d8 = lambda: _roll_a_die(8)
roll_a_d10 = lambda: _roll_a_die(10)
roll_a_d100 = lambda: _roll_a_die(100)

def get_roll_func(die_roll, modifier):
  return lambda: die_roll() + modifier