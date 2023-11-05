from .BaseResultTable import BaseResultTable, ResultTableRow
import constants

class BallHoldResultTable(BaseResultTable):
  RESULT_ROWS = [
      ResultTableRow(None, 4, constants.BALL_DROPPED),
      ResultTableRow(5, None, constants.BALL_HELD),
  ]

BALL_HOLD_RESULT_TABLE = BallHoldResultTable()