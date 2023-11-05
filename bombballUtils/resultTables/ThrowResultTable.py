from .BaseResultTable import BaseResultTable, ResultTableRow
import constants

class ThrowResultTable(BaseResultTable):
  RESULT_ROWS = [
      ResultTableRow(None, 1, constants.THREE_SQUARE_SCATTER),
      ResultTableRow(2, 3, constants.TWO_SQUARE_SCATTER),
      ResultTableRow(4, 5, constants.ONE_SQUARE_SCATTER),
      ResultTableRow(6, 8, constants.ZERO_SQUARE_SCATTER),
      ResultTableRow(9, None, constants.ACCURATE_PASS),
  ]

THROW_RESULT_TABLE = ThrowResultTable()