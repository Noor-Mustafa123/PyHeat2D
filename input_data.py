from typing import Dict, List


class InitialConditions:
  def __init__(self, type: str, center: List[int], temperature: float):
    self.type = type
    self.center = center
    self.temperature = temperature


class InputData:
  def __init__(self, grid_map: Dict[str, int],
      physics_of_domain: Dict[str, int], initial_conditions,
      boundary_conditions: Dict[str, int]):

    self.initial_conditions = InitialConditions(
        type=initial_conditions["type"],
        center=initial_conditions["center"],
        temperature=initial_conditions["temperature"]
    )


    self.grid = grid_map
    self.physics_of_domain = physics_of_domain
    self.boundary_conditions = boundary_conditions





