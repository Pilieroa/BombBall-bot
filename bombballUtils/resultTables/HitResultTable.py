from bombballUtils.resultTables.BaseResultTable import BaseResultTable, ResultTableRow
from bombballUtils.resultTables import constants

class HitResultTable(BaseResultTable):
  RESULT_ROWS = [
      ResultTableRow(None, 1, constants.HITTER_FALLS),
      ResultTableRow(2, 3, constants.HITTER_STUMBLES),
      ResultTableRow(4, 7, constants.PUSH_OR_LOCK_UP),
      ResultTableRow(8, 9, constants.TARGET_STUMBLES),
      ResultTableRow(10, None, constants.TARGET_FALLS),
  ]

HIT_RESULT_TABLE = HitResultTable()
