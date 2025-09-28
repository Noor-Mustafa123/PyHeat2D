from typing import List

from pydantic import BaseModel, ValidationError

# Pydantic models matching JSON structure
class Grid(BaseModel):
    nx: int
    ny: int
    dx: float
    dy: float


class PhysicsOfDomain(BaseModel):
    alpha: float
    total_time: float
    dt: float


class InitialConditions(BaseModel):
    type: str
    center: List[int]
    temperature: float


class BoundaryTemperatures(BaseModel):
    north: int
    south: int
    east: int
    west: int

def validate_input_json(data: dict) -> bool:
    try:
      Grid(**data["grid"])
      PhysicsOfDomain(**data["physics"])
      InitialConditions(**data["initial_conditions"])
      BoundaryTemperatures(**data["boundary_temperatures"])
      return True
    except ValidationError as e:
      print("Validation error:", e)
      return False

