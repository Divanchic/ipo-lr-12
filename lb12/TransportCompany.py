class TransportCompany():
    name = "OOOOO"
    vehicles = [Ship, Van]
    clients = []

    def add_vehicle(vehicle):
        if(vehicle is str):
            TransportCompany.vehicles.append(vehicle)
    def list_vehicles():
        print(TransportCompany.vehicles)
    def add_client(client):
        TransportCompany.clients.append(client)
    def optimize_cargo_distribution()