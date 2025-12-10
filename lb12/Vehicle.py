import random 
class Vehicle():
    def __init__(self, capacity):
        vehicle_id = f"{random.randint(0, 1000)}"
        capacity = 10.0
        current_load = 0.0
        clients_list = []

    def load_cargo(Client):
        if(Vehicle.current_load+Client.cargo_weight<=Vehicle.capacity):
            Vehicle.current_load+=Client.cargo_weight
        else:
            print("nth")

    def __str__():
        return f"id- {Vehicle.vehicle_id}, max mass- {Vehicle.capacity}, mass- {Vehicle.current_load}"
