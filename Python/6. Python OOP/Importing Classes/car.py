class Car:
    def __init__(self , make ,model , year):
        #intial attributes
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0 
        
    def get_detail(self):
        name = f"{self.year} {self.make} {self.model}"
        return name.title()
    def read_odo(self):
        print(f"This car has {self.odometer} miles on it")
class Battery:
          def __init__(self,battery_size = 40):
               self.battery_size = battery_size
               
          def battery_health(self):
              print(f" this car has : {self.battery_size} aph battery")
    
    
           
class ElectricCar(Car):
      def __init__(self , make ,model , year):
            
          super().__init__(make,model,year)
          
          self.battery = Battery()
          
        