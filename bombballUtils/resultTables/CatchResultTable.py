from .BaseResultTable import BaseResultTable, ResultTableRow
from bombballUtils.resultTables import constants

class CatchResultTable(BaseResultTable):
  RESULT_ROWS = [
      ResultTableRow(None, 6, constants.FAILED_CATCH),
      ResultTableRow(7, None, constants.CAUGHT),
  ]

CATCH_RESULT_TABLE = CatchResultTable()
