from bombballUtils.dice import roll_a_d8, roll_a_d10, roll_a_d100
from bombballUtils import resultTables

def hit_roll(hitter_str, target_str, num_adj_attackers, num_adj_defenders):
  modifier = hitter_str - target_str + num_adj_attackers - num_adj_defenders
  roll = roll_a_d10()
  return [roll, modifier, resultTables.HIT_RESULT_TABLE.determine_result(roll + modifier)]

def dodge_roll(adj_ops_with_higher_dex, adj_ops_with_equal_dex):
  modifier = -2 * adj_ops_with_higher_dex - adj_ops_with_equal_dex
  roll = roll_a_d10()
  return [roll, modifier, resultTables.DODGE_RESULT_TABLE.determine_result(roll + modifier)]
  
def stumble_roll():
  roll = roll_a_d10()
  return [roll, 0, resultTables.INJURY_RESULT_TABLE.determine_result(roll)]

def fall_roll():
  # going to eventually log all these rolls
  roll = roll_a_d100()
  return [roll, 0, resultTables.INJURY_RESULT_TABLE.determine_result(roll)]

def throw_roll(thrower_dex):
  roll = roll_a_d10()
  return [roll, thrower_dex, resultTables.THROW_RESULT_TABLE.determine_result(roll + thrower_dex)]

def pass_block_roll(blocker_dex, num_additional_blockers):
  modifier = blocker_dex + num_additional_blockers
  roll = roll_a_d10()
  return [roll, modifier, resultTables.PASS_BLOCK_RESULT_TABLE.determine_result(roll + modifier)]

def catch_roll(catchers_dex, num_opposing_players, catch_bonus=0):
  modifier = catchers_dex - num_opposing_players + catch_bonus
  roll = roll_a_d10()
  return [roll, modifier, resultTables.CATCH_RESULT_TABLE.determine_result(roll + modifier)]

def ball_hold_roll(holders_dex):
  roll = roll_a_d10()
  return [roll, 0, resultTables.BALL_HOLD_RESULT_TABLE.determine_result(roll + holders_dex)]

def ball_scatter_roll():
  roll = roll_a_d8()
  results = [
    "top", 
    "top right", 
    "right", 
    "bottom right", 
    "bottom",
    "bottom left",
    "left",
    "top left",
  ]
  return [roll, 0, results[roll - 1]]
 
