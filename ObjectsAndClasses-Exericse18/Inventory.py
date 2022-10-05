class Inventory:

    def __init__(self, capacity: int):
        self.capacity = capacity  # not private attribute who we change in the code dinamic
        self.__capacity = capacity  # The private attribute who save only the first count of places for the inventory

        self.items = []

    def add_item(self, item: str):

        if self.capacity > 0:
            self.items.append(item)
            self.capacity -= 1
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        items = ", ".join(self.items)
        return f"Items: {items}.\nCapacity left: {self.capacity}"