import json
from order import Order
from order import OrderesRepository
# Створіть два окремих "мікросервіси" (дві окремі
# програми). Одна програма створює та експортує дані у
# форматі JSON, а інша програма завантажує та обробляє ці
# дані. Це може бути, наприклад, система, яка створює та
# обробляє замовлення.

FILENAME = "orders.json"




ordersRepository = OrderesRepository()

order1 = Order("somename", "388465", 1234)
order2 = Order("leh", "335", 31)
order3 = Order("sonyashik", '124', "12")

ordersRepository.add_order(order1)
ordersRepository.add_order(order2)
ordersRepository.add_order(order3)

ordersRepository.save_orders(FILENAME)
