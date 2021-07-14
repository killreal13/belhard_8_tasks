class House:
    address: str
    area: int
    cost: float

    def __init__(self, address, area, cost):
        self.address = address
        self.area = area
        self.cost = cost

    def increase_cost(self, increase_value):
        self.cost += increase_value

    def decrease_cost(self, decrease_value):
        self.cost -= decrease_value
