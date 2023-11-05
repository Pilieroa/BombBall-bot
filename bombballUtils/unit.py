from dataclasses import dataclass
from typing import Optional
import constants

@dataclass
class UnitType:
  movement: int
  strength: int
  dexterity: int
  ability: Optional[str]

ELF_FODDER = UnitType(4, -1, 1, None)
ELF_BLITZER = UnitType(5, 0, 1, constants.BLITZ)
ELF_THROWER = UnitType(3, -1, 2, constants.LONG_PASS)
ELF_CATCHER = UnitType(6, -2, 2, constants.CATCH)

ORC_FODDER = UnitType(3, 1, -1, None)
ORC_BLITZER = UnitType(4, 1, 0, constants.BLITZ)
ORC_BIGMAN = UnitType(2, 2, -2, constants.REALLY_BIG)
ORC_GOBLIN = UnitType(6, -3, 2, None)

@dataclass
class Unit:
  _type: UnitType
  condition: Optional[str] # think stunned, knocked out, down, etc.
  has_ball: bool
  team: str
  name: str

  @property
  def movement(self):
    return self._type.movement

  @property
  def strength(self):
    return self._type.strength

  @property
  def dexterity(self):
    return self._type.dexterity

  @property
  def ability(self):
    return self._type.ability

  @property
  def has_tackle_zone(self):
    return self.condition is None

  def is_ally(self, unit):
    return self.team == unit.team

  def __str__(self):
     return self.name