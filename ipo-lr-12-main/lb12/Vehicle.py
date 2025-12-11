import random
import Client


class Vehicle():
    def __init__(self, capacity):
        vehicle_id = f"{random.randint(0, 1000)}"
        capacity = 10.0
        current_load = 0.0
        clients_list = []

    def load_cargo(self):
        if(self.current_load + Client.cargo_weight<=self.capacity):
            self.current_load+=Client.cargo_weight
        else:
            print("вес слишком велик")

    def __str__(self):
        return f"id- {self.vehicle_id}, max mass- {self.capacity}, mass- {self.current_load}"
