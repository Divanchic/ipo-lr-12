import random
from Client import Client


class Vehicle():
    def __init__(self, capacity):
        vehicle_id = f"{random.randint(0, 1000)}"
        self.capacity = capacity
        self.current_load = 0.0
        self.clients_list = []

    def load_cargo(self, weight):
        if(self.current_loаd + weight<=self.capacity):
            self.current_load+=weight
        else:
            print("вес слишком велик")

    def __str__(self):
        return f"id- {self.vehicle_id}, max mass- {self.capacity}, mass- {self.current_load}"
