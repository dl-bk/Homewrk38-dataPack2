import json

FILENAME = "orders.json"

def load_data(filepath):
    try:
        with open(filepath, 'r') as rfile:
            loaded_data = json.load(rfile)
            return loaded_data
    except FileNotFoundError:
        return None

def find_order(phone:str, orders):
    for order in orders:
        if phone in order.values():
            return order
    

loaded_orders = load_data(FILENAME)

order1 = find_order('335',loaded_orders)
order2 = find_order('388465',loaded_orders)
order3 = find_order('124',loaded_orders)

order1['status'] = 'done'
order2['status'] = 'waiting'
order3['status'] = 'payed'

print(order1)
print(order2)
print(order3)


