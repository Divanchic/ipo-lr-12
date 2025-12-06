import random 

class Client():
    name = ""
    cargo_weight = 1.0
    is_vip = False
class Vehicle():
    vehicle_id = f"{random.randint(0, 1000)}"
    capacity = 10.0
    current_load = 1.0
    clients_list = []

    def load_cargo(Client):
        if(Vehicle.current_load+Client.cargo_weight<=Vehicle.capacity):
            Vehicle.current_load+=Client.cargo_weight
        else:
            print("nth")

    def __str__():
        return f"id- {Vehicle.vehicle_id}, max mass- {Vehicle.capacity}, mass- {Vehicle.current_load}"

class Van(Vehicle):
    is_refrigerated = False

class Ship(Vehicle):
    name = "Gordinya"

class TransportCompany():
    name = "OOOOO"
    vehicles = []
    clients = []

    def add_vehicle(vehicle):
        if(vehicle is str):
            TransportCompany.vehicles.append(vehicle)
    def list_vehicles():
        print(TransportCompany.vehicles)
    def add_client(client):
        TransportCompany.clients.append(client)
print(Vehicle.__str__())