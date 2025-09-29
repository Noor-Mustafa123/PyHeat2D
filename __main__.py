import argparse
import json
import logging

import input_data
import parser
import heat_solver
from heat_solver import HeatSolver2D


def main():
  argumentParser = argparse.ArgumentParser()
  argumentParser.add_argument("-i", "--input", required=True, help="Path to the input JSON file")
  args = argumentParser.parse_args()
  with open(args.input,"r") as file:
    data = json.load(file)
    valid = parser.validate_input_json(data)
    if valid :
      input_object = input_data.InputData(data["grid"],data["physics"],data["initial_conditions"],data["boundary_temperatures"])
      print(" input json successfully parsed into object")
    else :
      logging.error("parsing failed incorrect json provided")
    heat_solver_obj: HeatSolver2D = heat_solver.HeatSolver2D(input_object)

    #################### simulation started ####################
    heat_solver_obj.run_simulation()
    ############################################################


# the python interpreter executes this block first when inside a package of scripts
if __name__ == '__main__':
  main()
