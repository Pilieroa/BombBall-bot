from .BaseResultTable import BaseResultTable, ResultTableRow
import constants

class CatchResultTable(BaseResultTable):
  RESULT_ROWS = [
      ResultTableRow(None, 6, constants.CAUGHT),
      ResultTableRow(7, None, constants.FAILED_CATCH),
  ]

CATCH_RESULT_TABLE = CatchResultTable()