import math
from flask import Flask, redirect, request as req, jsonify
import ujson as json
import time
from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2

def distance(x1, y1, x2, y2):
    # Manhattan distance
    dist = abs(x1 - x2) + abs(y1 - y2)

    return dist

# Distance callback

class CreateDistanceCallback(object):
  """Create callback to calculate distances and travel times between points."""

  def __init__(self, locations):
    """Initialize distance array."""
    num_locations = len(locations)
    self.matrix = {}

    for from_node in xrange(num_locations):
      self.matrix[from_node] = {}
      for to_node in xrange(num_locations):
        if from_node == to_node:
          self.matrix[from_node][to_node] = 0
        else:
          x1 = locations[from_node][0]
          y1 = locations[from_node][1]
          x2 = locations[to_node][0]
          y2 = locations[to_node][1]
          self.matrix[from_node][to_node] = distance(x1, y1, x2, y2)

  def Distance(self, from_node, to_node):
    return self.matrix[from_node][to_node]


# Demand callback
class CreateDemandCallback(object):
  """Create callback to get demands at location node."""

  def __init__(self, demands):
    self.matrix = demands

  def Demand(self, from_node, to_node):
    return self.matrix[from_node]

app = Flask(__name__)

@app.route('/cvrp', methods=['POST'])
def cvrp():
    body = json.loads(req.data)
    data = create_data_array_from_request(body)
    locations = data[0]
    demands = data[1]
    customer_locations = data[2]
    customer_demands = data[3]
    depot = 0
    num_vehicles = 500
    print data, len(locations), len(demands)
    num_locations = len(locations)
    if num_locations > 0:
      print "enter"
      routing = pywrapcp.RoutingModel(num_locations, num_vehicles, depot)
      search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()
      search_parameters.first_solution_strategy = (
          routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

      dist_between_locations = CreateDistanceCallback(locations)
      dist_callback = dist_between_locations.Distance

      routing.SetArcCostEvaluatorOfAllVehicles(dist_callback)
      demands_at_locations = CreateDemandCallback(demands)
      demands_callback = demands_at_locations.Demand

      VehicleCapacity = data[5]
      NullCapacitySlack = 0
      fix_start_cumul_to_zero = True
      capacity = "Capacity"

      routing.AddDimension(demands_callback, NullCapacitySlack, VehicleCapacity,
                         fix_start_cumul_to_zero, capacity)


      assignment = routing.SolveWithParameters(search_parameters)

      if assignment:
        data = create_data_array_from_request(body)
        locations = data[0]
        demands = data[1]
        size = len(locations)
        # Solution cost.
        print ("Total distance of all routes: " , str(assignment.ObjectiveValue()))
        # Inspect solution.
        capacity_dimension = routing.GetDimensionOrDie(capacity);

        routes = []
        for vehicle_nbr in xrange(num_vehicles):
          index = routing.Start(vehicle_nbr)
          route = []
          while not routing.IsEnd(index):
            node_index = routing.IndexToNode(index)
            route.append(node_index-1)
            index = assignment.Value(routing.NextVar(index))

          node_index = routing.IndexToNode(index)
          route.append(node_index-1)

          if not (route[0] == -1 and route[1] == -1):
            routes.append(route[1:len(route)-1])

        return jsonify(dict(routes=routes))
      else:
        return ('No solution found.')
    else:
      return ('Specify an instance greater than 0.')
    return jsonify(body)

def create_data_array_from_request(data):
  customer_locations = data["problem_data"]["customer_locations"]
  customer_demands = data["problem_data"]["customer_demands"]
  depot = data["problem_data"]["depot"]
  vehicle_capacity = data["problem_data"]["vehicle_capacity"]


  locations = customer_locations
  locations.insert(0, depot)
  print locations
  demands = customer_demands
  demands.insert(0, 0)

  data = [locations, demands, customer_locations, customer_demands, depot, vehicle_capacity]
  return data

if __name__ == "__main__":
    app.run()

