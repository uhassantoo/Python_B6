from car import Car ,ElectricCar

new_car = Car('audi','a5','2024')
print(new_car.get_detail())
new_car.odometer = 2000
new_car.read_odo()

new_car1 = Car('ford','mustang',2024)
print(new_car1.get_detail())
car1 = ElectricCar('nissan','GT',2023)
print(car1.get_detail())