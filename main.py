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
            self.__year = year


    def set_producer(self, producer):
        self.__producer = producer


    def set_engine_volume(self, engine_volume):
        self.__engine_volume = engine_volume


    def set_color(self, color):
        color_list = ['black', 'white', 'red', 'blue', 'silver']
        if color in color_list:
            self.color = color
        else:
            print('Error, no such color! Enter color again')

    def set_price(self, price):
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
        return self.color


    def get_price(self):
        return f'Price - {self.price}'


    def __str__(self):
        return f'Car model - {self.__model}\nYear - {self.__year}\n' \
               f'Producer - {self.__producer}\nEngine_volume - {self.__engine_volume}\n' \
               f'Color - {self.color}\nPrice - {self.price}'

obj = Car('Accord', 2016, 'Honda', 2.0, 'blue', 25000)

print(obj)
print(obj.price)

obj.set_color('black')
print(obj)
print(obj.get_model())

# Задание 2
print()
class Book:
    def __init__(self, name_book, year, publisher, genre, author, price):
        self.__name_book = name_book
        self.__year = year
        self.__publisher = publisher
        self.__genre = genre
        self.__author = author
        self.price = price


    def set_name(self, name_book):
        self.__name_book = name_book


    def set_year(self, year):
        if str(year).isdigit() and year > 0:
            self.__year = year


    def set_publisher(self,publisher):
        self.__publisher = publisher


    def set_genre(self, genre):
        self.__genre = genre


    def set_autor(self, autor):
        self.__author = autor


    def set_price(self, price):
        if str(price).isdigit():
            self.price = price


    def get_name(self):
        return f'Title - {self.__name_book}'


    def get_year(self):
        return f'Year - {self.__year}'


    def get_publisher(self):
        return f'Publisher - {self.__publisher}'


    def get_genre(self):
        return f'Genre - {self.__genre}'


    def get_author(self):
        return f'Author - {self.__author}'


    def get_price(self):
        return f'Price - {self.price}'


    def __str__(self):
        return f'Title - {self.__name_book}\nYear - {self.__year}\n' \
               f'Publisher - {self.__publisher}\nGenre - {self.__genre}\n' \
               f'Author - {self.__author}\nPrice - {self.price}'

obj = Book('I Owe You One', 2020, 'Black Swan', 'novel', 'Kinsella, S.', 150)

print(obj)
obj.set_price = 'five'
print(obj)
obj.set_autor = 'сто'
print(obj)
print(obj.get_name())


# Задание 3
print()
class Stadium:

    def __init__(self, name, date_open, country, city, capacity):
        self.__name = name
        self.__date_open = date_open
        self.__country = country
        self.__city = city
        self.__capacity = capacity


    def set_name(self, name:str):
        self.__name = name.capitalize()


    def set_date_open(self, date_open):
        self.__date_open = date_open


    def set_country(self, country: str):
        self.__country = country.capitalize()


    def set_city(self, city: str):
        self.__city = city.capitalize()


    def set_capacity(self, capacity):
        if str(capacity).isdigit():
            self.__capacity = capacity


    def get_name(self):
        return f'Name - {self.__name}'


    def get_date_open(self):
        return f'Date open - {self.__date_open}'


    def get_country(self):
        return f'Country - {self.__country}'


    def get_city(self):
        return f'City - {self.__city}'


    def get_capacity(self):
        return f'Capacity - {self.__capacity}'


    def __str__(self):
        return f'Name - {self.__name}\nDate open - {self.__date_open}\n' \
               f'Country - {self.__country}\nCity - {self.__city}\n' \
               f'Capacity - {self.__capacity}'

obj = Stadium('Spotify Camp Nou', '24.10.1957', 'Spain', 'Barcelona', 99354)

print(obj)
obj.set_name('kdjsg;l')
print(obj)
