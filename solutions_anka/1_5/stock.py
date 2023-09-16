class Stock:
    def __init__(self, name, share, prices):
        self.name = name
        self.share = share
        self.prices = prices
        
    def cost(self):
        return self.share * self.prices