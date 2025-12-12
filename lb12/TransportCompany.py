import Client
import Vehicle
class TransportCompany():
    def __init__(self, name):
        self.name = name
        self.vehicles = []
        self.clients = []

    def add_vehicle(self, vehicle):
        if not isinstance(vehicle, Vehicle):
            raise TypeError("Нет Vehicle/наследуемый класс")
        self.vehicles.append(vehicle)

    def list_vehicles(self):
        return self.vehicles
        
    def add_client(self, client):
        if not isinstance(client, Client):
            raise TypeError("классом должен быть Client")
        self.clients.append(client)

    def optimize_cargo_distribution(self):
        sorted_clients = sorted(self.clients, key=lambda c: not c.is_vip)
        for client in sorted_clients:
            for vehicle in sorted(self.vehicles, key=lambda v: v.current_load):
                try:
                    vehicle.load_cargo(client)
                    break
                except ValueError:
                    continue