from .BaseResultTable import BaseResultTable, ResultTableRow
import constants

class PassBlockResultTable(BaseResultTable):
  RESULT_ROWS = [
      ResultTableRow(None, 7, constants.YA_MISSED),
      ResultTableRow(8, 9, constants.TIPPED),
      ResultTableRow(10, None, constants.INTERCEPTION),
  ]

PASS_BLOCK_RESULT_TABLE = PassBlockResultTable()