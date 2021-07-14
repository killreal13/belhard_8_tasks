from house import House


class Townhouse(House):
    def __init__(self, address, cost, area=60):
        super().__init__(address, area, cost)
        self.area = 60

house = Townhouse('asd', 123123)