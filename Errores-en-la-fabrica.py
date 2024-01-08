# Errores en la Fabrica

import random

class Car:
    def __init__(self, color, model, id_number):
        self.color = color
        self.model = model
        self.id_number = id_number

class CarFactory:
    def __init__(self):
        self.colors = ["red", "yellow", "white"]
        self.models = ["Corolla", "Swift", "T-cross"]

    def create_random_car(self):
        color = random.choice(self.colors)
        model = random.choice(self.models)
        id_number = "ABC-123"  # Cambiar esto para que cada carro tenga un número de identificación único
        car = Car(color, model, id_number)
        return car  # Debes devolver el objeto "car", no la clase "Car"

class CloneFinder:
    def simulate_find(self):  # Cambiar "simulare_finde" a "simulate_find"
        car_list = self.generate_cars()
        self.show_cars(car_list)
        color = self.get_color_to_compare()
        self.find_clones(car_list, color)

    def show_cars(self, car_list):  # Indentar correctamente las funciones dentro de la clase
        print("The generated cars are:")
        for car in car_list:
            print("Color:", car.color, "| Model:", car.model, "| Id Number:", car.id_number)

    def generate_cars(self):  # Indentar correctamente las funciones dentro de la clase
        car_factory = CarFactory()
        car_list = []
        for number in range(0, 3):
            car = car_factory.create_random_car()
            car_list.append(car)
        return car_list  # Mover este retorno fuera del bucle for

    def get_color_to_compare(self):  # Indentar correctamente las funciones dentro de la clase
        value = input("Color of original car: ")
        return value

    def find_clones(self, car_list, color):  # Indentar correctamente las funciones dentro de la clase
        print("Clones found:")
        for car in car_list:
            if car.color == color:  # Cambiar el operador de comparación aquí
                print("Color:", car.color, "| Model:", car.model, "| Id Number:", car.id_number)

clone_finder = CloneFinder()
clone_finder.simulate_find()