from typing import List, Dict, Tuple

import input_data
from input_data import InputData, InitialConditions
import numpy as np
import matplotlib.pyplot as plt


class HeatSolver2D:

  def __init__(self, input_data_object: InputData):
    self.input_data_object = input_data_object
    # other variables are set to none as they will be updated by internal methods
    self.temperature_grid = None
    self.current_time = 0.0
    self.step_count = 0
    self.fig = None
    self.initialized_plot = False

    # initalizing Phase I
    self.initialize_grid()
    self.apply_boundary_conditions()
    self.apply_initial_conditions()
    self.initialized_plot

  ###################################### Phase I ######################################
  # Creates empty "cold plate"
  def initialize_grid(self):
    # gets the number of grid points on the plate along x and y directions
    nx: int = self.input_data_object.grid["nx"]
    ny: int = self.input_data_object.grid["ny"]
    # creating a zeros temprature matrix
    self.temperature_grid = np.zeros(shape=(nx, ny), dtype=float)

  # Adds the hotspot "hot spot" to the plate
  def apply_initial_conditions(self):
    ic: InitialConditions = self.input_data_object.initial_conditions
    if ic.type == "hot_spot":
      center: List[int] = ic.center
      self.temperature_grid[center[0], center[1]] = ic.temperature

  # Sets edge temperatures of the plate
  def apply_boundary_conditions(self):
    bc: Dict[str, int] = self.input_data_object.boundary_conditions
    # top row (north)
    self.temperature_grid[0, :] = bc["north"]
    # bottom row (south)
    self.temperature_grid[-1, :] = bc["south"]
    # left column (west)
    self.temperature_grid[:, 0] = bc["west"]
    # right column (east)
    self.temperature_grid[:, -1] = bc["east"]

  def initialize_visualization(self):
    self.fig, ax = plt.subplots(figsize=(10, 8))
    plt.ion()
    self.initialized_plot = True

  ######################################### Phase II #########################################

  def solve_for_temps_and_update_grid(self):
    old_grid: np.ndarray = self.temperature_grid.copy()
    future_grid: np.ndarray = self.temperature_grid.copy()
    n_rows, n_columns = future_grid.shape

    # nested loop to operate on each grid point except the boundries
    for i in range(1, n_rows - 1):
      for j in range(1, n_columns - 1):
        lambda_ = self.calculate_lambda()
        future_grid[i, j] = old_grid[i, j] + lambda_ * (
            old_grid[i + 1, j] + old_grid[i - 1, j] + old_grid[i, j + 1] +
            old_grid[i, j - 1] - 4 * old_grid[i, j])

    # updating time and step count each time method is triggered
    self.current_time += self.input_data_object.physics_of_domain["dt"]
    self.step_count += 1

    # update older grid at each timestep
    self.temperature_grid = future_grid

  def calculate_lambda(self) -> float:
    global dx
    physics = self.input_data_object.physics_of_domain
    alpha = physics["alpha"]
    delta_t = physics["dt"]
    # Considering The spatial grid is uniform (equal spacing between nodes)
    # The spacing in the x and y directions is the same: dx == dy
    if self.input_data_object.grid["dx"] == self.input_data_object.grid["dy"]:
      dx = self.input_data_object.grid["dx"]
    result = alpha * delta_t / dx ** 2
    return result

  ######################################### Phase III #########################################

  def visualize_current_state(self):
    plt.clf()  # Clear current figure

    # Create heatmap
    plt.imshow(self.temperature_grid, cmap='hot', interpolation='bilinear')
    plt.colorbar(label='Temperature (°C)')
    plt.title(
        f'2D Heat Diffusion - Time: {self.current_time:.3f}s | Step: {self.step_count}')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')

    plt.draw()
    plt.pause(0.01)  # Brief pause to update

    ######################################### Main #########################################
  def run_simulation(self):
    print("simulation started")
    total_time = self.input_data_object.physics_of_domain["total_time"]
    # Updates the grid as long as time limit is not exceeded
    while self.current_time < total_time:
      self.solve_for_temps_and_update_grid()
      # Visualizes every 10 steps
      if self.step_count % 10 == 0:
        self.visualize_current_state()

    print("simulation finished")
    # Keep final plot open
    plt.ioff()
    plt.show()