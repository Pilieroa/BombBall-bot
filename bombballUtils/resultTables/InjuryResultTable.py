from .BaseResultTable import BaseResultTable, ResultTableRow
from bombballUtils.resultTables import constants

class InjuryResultTable(BaseResultTable):
  RESULT_ROWS = [
      ResultTableRow(None, 6, constants.DOWNED),
      ResultTableRow(7, 44, constants.STUNNED),
      ResultTableRow(45, 79, constants.KNOCKED_OUT),
      ResultTableRow(80, 94, constants.CONCUSSION),
      ResultTableRow(95, None, constants.OUT_OF_GAME),
  ]

INJURY_RESULT_TABLE = InjuryResultTable()
