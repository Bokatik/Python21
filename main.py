# Задание 1
class Car:
    def __init__(self, model, year, producer, engine_volume, color, price):
        self.__model = model
        self.__year = year
        self.__producer = producer
        self.__engine_volume = engine_volume
        self.color = color
        self.price = price


    def set_model(self, model):
        self.__model = model


    def set_year(self, year):
        if str(year).isdigit():
            if year > 0:
                self.__year = year


    def set_producer(self, producer):
        self.__producer = producer


    def set_engine_volume(self, engine_volume):
        self.__engine_volume = engine_volume


    def set_color(self, color):
        color_list = ['black', 'white', 'red', 'blue', 'silver']
        for i in color_list:
            if i == color:
                self.color = color
            else:
                print('Input color')

    def set_price(self, price):
        if str(price).isdigit():
            if price > 0:
                self.price = price


    def get_model(self):
        return f'Car model - {self.__model}'

    def get_year(self):
        return f'Year - {self.__year}'

    def get_producer(self):
        return f'Producer - {self.__producer}'

    def get_engine_volume(self):
        return f'Engine_volume - {self.__engine_volume}'


    def get_color(self):
        return f'Color - {self.color}'


    def get_price(self):
        return f'Price - {self.price}'


    def __str__(self):
        return f'Car model - {self.__model}\nYear - {self.__year}\n' \
               f'Producer - {self.__producer}\nEngine_volume - {self.__engine_volume}\n' \
               f'Color - {self.color}\nPrice - {self.price}'

obj = Car('Accord', 2016, 'Honda', 2.0, 'blue', 25000)

print(obj.__str__())
print(obj.price)

