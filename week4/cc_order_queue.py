class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)
    
    def show_queue(self):
        print(self.items)

# Define class name IceCreamShop
class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

# Method for take_order
    def take_order(self, customer, flavor, scoops):
        if flavor not in self.flavors:
            print("Sorry, we don't have that flavor")
        elif scoops < 1 or scoops > 3:               
            print("Choose between 1-3 scoops")
        else:
            print("Order created!")
            order = {"customer": customer, "flavor": flavor, "scoops": scoops}
            self.orders.enqueue(order)

# Method for show_all_orders
    def show_all_orders(self):
        print("\nAll Pending Ice Cream Orders: ")
        for order in self.orders.items:
            print(f"Customer: {order['customer']} -- Flavor: {order['flavor']} -- Scoops: {int(order['scoops'])}")

# Method for next_order
    def next_order(self):
        print("\nNext Order Up!")
        next_order = self.orders.dequeue()
        print(f"Customer: {next_order['customer']} -- Flavor: {next_order['flavor']} -- Scoops: {int(next_order['scoops'])}")

# Testing
shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()