from item import Item
from order import Order


class Restaurant:

    def __init__(self, restaurant_name, menu_list):
        self.__restaurant_name = restaurant_name
        self.__menu_list = menu_list
        self.__order_list = []
        self.__bill = 0

    def get_restaurant_name(self):
        return self.__restaurant_name

    def get_menu_list(self):
        return self.__menu_list

    def get_order_list(self):
        print(self.__order_list)
        if len(self.__order_list) == 0:
            return "No order yet"
        return self.__order_list

    def set_order(self, item_list):
        valid_items = []
        if len(item_list) != 0:
            for item in item_list:
                if item in self.__menu_list:
                    valid_items.append(item)
            self.__order_list.append(Order(valid_items))

    def get_revenue(self):
        for order in self.__order_list:
            self.__bill += Order.get_bill_amount(order)
        return self.__bill


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    # Create Item Objects with Name and Price
    steak = Item("Steak", 25)
    salad = Item("Salad", 10)
    fish = Item("Fish", 30)
    pizza = Item("Pizza", 40)
    hamburger = Item("Hamburger", 20)

    # Create menu list
    menu_list = [hamburger, pizza]
    # Create order list
    order_list = []
    # Create restaurant object with name and menu list
    restaurant = Restaurant("Zurich_1", menu_list)
    # Create an order with the order list
    restaurant.set_order(order_list)
    print(restaurant.get_order_list())
    # Get the revenue of the restaurant object
    #print(restaurant.get_revenue())
