import hashlib
import random
import json

class Order:

    _hash_obj: str = None

    def __init__(self, client_name: str, client_phone: str, price: float) -> None:
        self._client_name = client_name
        self._client_phone = client_phone
        self._price = price
        self._hash_obj = self._generate_hash()
    
    def _generate_hash(self) -> str:
        hash_string = self._client_name + str(self._price) + str(self._client_phone) + str(random.randint(-100, 10000))
        hash_object = hashlib.sha256(hash_string.encode())
        return hash_object.hexdigest()
    
    # def get_hash(self):
    #     return self._hash_obj
    
    def set_client_name(self, name):
        self._client_name = name
    
    def get_client_phone(self):
        return self._client_phone
    
    def set_client_phone(self, phone):
        self._client_phone = phone
    
    def set_price(self, price):
        self._price = price
    
    def get_client_name(self):
        return self._client_name

    def get_price(self):
        return self._price

class OrderesRepository:
    _orders = {}

    def get_hash(self,order: Order):
        return order._hash_obj
    
    def add_order(self, order: Order):
        self._orders[order._hash_obj] = order

    def remove_order(self, hash_key):
        self._orders.pop(hash_key)

    def display_orders(self):
        for key, value in self._orders.items():
            print(f"{key}: {value}")
    
    def save_orders(self, filename):
        orders_list = [{hash: order.__dict__} for hash, order in self._orders.items()]
        with open(filename, 'w') as wfile:
            json.dump(orders_list, wfile, indent=2)
        print("data saved")