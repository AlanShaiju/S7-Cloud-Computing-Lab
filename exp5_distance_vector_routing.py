class Router:
    def __init__(self, name, neighbors):
        self.name = name
        self.neighbors = neighbors  
        self.distance_vector = {name: 0}  
        self.next_hop = {name: name}  
        for neighbor, cost in neighbors.items():
            self.distance_vector[neighbor] = cost
            self.next_hop[neighbor] = neighbor
    def update_distance_vector(self, routers):
        updated = False
        for neighbor, cost in self.neighbors.items():
            neighbor_vector = routers[neighbor].distance_vector
            for dest, neighbor_dist in neighbor_vector.items():
                if dest not in self.distance_vector or self.distance_vector[dest] > cost + neighbor_dist:
                    self.distance_vector[dest] = cost + neighbor_dist
                    self.next_hop[dest] = neighbor
                    updated = True
        return updated
def print_distance_vectors(routers):
    for router in routers.values():
        print(f"Router {router.name}:")
        print("Distance Vector:", router.distance_vector)
        print("Next Hop:", router.next_hop)
        print()
def simulate_distance_vector_routing(routers):
    converged = False
    iteration = 0
    while not converged:
        print(f"Iteration {iteration}")
        print_distance_vectors(routers)
        converged = True
        for router in routers.values():
            if router.update_distance_vector(routers):
                converged = False
        iteration += 1
def get_user_input():
    routers = {}
    num_routers = int(input("Enter the number of routers: "))
    for _ in range(num_routers):
        name = input("Enter router name: ")
        neighbors = {}
        num_neighbors = int(input(f"Enter number of neighbors for router {name}: "))

        for _ in range(num_neighbors):
            neighbor_name = input("Enter neighbor router name: ")
            cost = int(input(f"Enter cost to reach router {neighbor_name}: "))
            neighbors[neighbor_name] = cost

        routers[name] = Router(name, neighbors)
    
    return routers
routers = get_user_input()
simulate_distance_vector_routing(routers)
