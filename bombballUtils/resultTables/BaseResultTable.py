# Table Base class
from dataclasses import dataclass
from typing import Optional

class TableValidationException(Exception):
  pass

class MultipleMinOptionsException(Exception):
  pass

class MultipleMaxOptionsException(Exception):
  pass

class OverlappingRowsException(Exception):
  pass

@dataclass
class ResultTableRow:
  min: Optional[int]
  max: Optional[int]
  result: str

class BaseResultTable:
  RESULT_ROWS = []
  def __init__(self):
    self.table = {}
    self.min_result = None
    self.min = None
    self.max_result = None
    self.max = None

    for result_row in self.RESULT_ROWS:
      if result_row.min in self.table or result_row.max in self.table:
        raise OverlappingRowsException(self)

      if result_row.min is None:
        if self.min_result is not None:
          raise MultipleMinOptionsException(self)
        self.min_result = result_row.result
        self.min = result_row.max
        self.table[result_row.max] = result_row.result
        continue

      if result_row.max is None:
        if self.max_result is not None:
          raise MultipleMaxOptionsException(self)
        self.max_result = result_row.result
        self.max = result_row.min
        self.table[result_row.min] = result_row.result
        continue

      for i in range(result_row.min, result_row.max + 1):
        self.table[i] = result_row.result
    self._validate()
    self.results = [row for row in self.table.values()]

  def _validate(self):
    try:
      assert self.min
      assert self.min_result
      assert self.max
      assert self.max_result
      assert self.table
      for i in range(self.min, self.max + 1):
        i in self.table
    except:
      raise TableValidationException(self)

  def determine_result(self, roll):
    if roll <= self.min:
      return self.min_result
    if roll >= self.max:
      return self.max_result
    return self.table[roll]