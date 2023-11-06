from .BaseResultTable import BaseResultTable, ResultTableRow
from bombballUtils.resultTables import constants

class DodgeResultTable(BaseResultTable):
  RESULT_ROWS = [
      ResultTableRow(None, 4, constants.DODGER_STUMBLES),
      ResultTableRow(5, None, constants.DODGER_ESCAPES),
  ]

DODGE_RESULT_TABLE = DodgeResultTable()
