class CarShop:
    
    def __init__(self,company):
        
        self.carcompany = company
        self.garage = {}
        self.rate = 1.5
        self.sale_profit = 0
        self.carprice = None
        self.store_profit = 0
        self.sellingprice = 0
        
    def initial_garage (self, car, quantity):
        
        self.garage[car] = quantity
        self.sellprice = self.originalprice * self.rate
        
    def showGarage (self):
        
        available = []
        for car in self.garage:
            if self.garage[car] > 0:
                available.append(car)
        return available
    
    def indiv_sale_profit(self, car_cost):
        
        self.carprice = car_cost
        self.sale_profit += (self.carprice * self.rate) - self.carprice
        
    def total_profit(self):
        
        self.store_profit +=self.sale_profit
        return self.store_profit
    
    def sell_car(self,car_name):
        self.garage[car_name] -=1
    


class Chevrolet(CarShop):
    pass


class Ford(CarShop):
    
    def total_profit(self):
        self.store_profit += self.sale_profit - tax
        return super().total_profit()
    
    def clear_garage(self):
        self.garage.clear()
        
        
        