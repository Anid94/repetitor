from decorators import logging, timer, validate_positive, log_calls

class Product:
    @validate_positive
    @log_calls
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def is_expensive(self):
        return self.price > 100

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError('Цена не может быть отрицательной или равной нулю')
        self._price = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError('Пустое имя запрещено')
        self._name = value

    @log_calls
    def __str__(self):
        return f'name: {self.name}, price: {self.price}'

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.name == other.name

class Cart:
    def __init__(self):
        self.my_list = []

    def __add__(self, other):
        if not isinstance(other, Cart):
            raise TypeError('не является объектом класса')
        cart = Cart()
        cart.my_list = self.my_list + other.my_list
        return cart


    def add_product(self, product):
        '''Добавляет продукт в корзину, если он не пустой.'''
        if product:
            self.my_list.append(product)

    def count_product(self):
        return len(self.my_list)

    def total_without_discount(self):
        return sum(obj.price for obj in self.my_list)

    def __str__(self):
        if not self.my_list:
            return 'Корзина пуста'
        all_products = ', '.join(str(obj.name) for obj in self.my_list)
        return f'{all_products} | Итого: {self.total_without_discount()} руб.'

    def remove_product(self, product):
        '''
        Решил сделать через list comprehensions
        1. Сохраняю изначальную длину списка
        2. Через list comprehensions отсеиваю ненужное и результат пересохраняю в self.my_list
        3. сравниваю длины старого и нового списков. Если длина такая же, значит ничего не удалено и товар не был найден
        иначе, товар найден и удален.
        '''
        my_list_len = len(self.my_list)
        self.my_list = [obj for obj in self.my_list if obj.name != product]
        if len(self.my_list) != my_list_len:
            print(f'Товар {product} удален')
        else:
            print(f'Товар {product} в корзине не найден')
        return self.my_list

    def clear(self):
        self.my_list.clear()
        print('Корзина очищена')

    def __contains__(self, item):
        for obj in self.my_list:
            if obj.name == item:
                return True
        return False

    def __len__(self):
        return len(self.my_list)

    def __getitem__(self, index):
        return self.my_list[index]

    def __iter__(self):
        return iter(self.my_list)

class DiscountProduct(Product):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount
    @classmethod
    def from_product(cls, product, discount):
        return cls(product.name, product.price, discount)

    @logging
    def price_with_discount(self):
        return round(self.price * (1 - self.discount / 100), 2)

    @property
    def saved_amount(self):
        return f'{self.price - self.price_with_discount():.2f}'

    def display(self):
        return f'name: {self.name}, price: {self.price_with_discount()} руб. (original: {self.price} руб., discount: {self.discount}%)'

class WeightProduct(Product):
    def __init__(self, name, price_per_kg):
        super().__init__(name, price_per_kg)
        self.price_per_kg = price_per_kg

    def get_cost(self, weight):
        return self.price_per_kg * weight

    def display(self):
        return f'name: {self.name}, price per kg: {self.price_per_kg} руб./кг'

class Store():
    def __init__(self):
        self.catalog = []

    @log_calls
    def add_product(self, product):
        self.catalog.append(product)
        return f' Товар "{product.name}" добавлен в корзину'

    def show_catalog(self):
        if not self.catalog:
            print('Каталог пуст')
            return
        for item in self.catalog:
            if hasattr(item, 'display'):
                print(item.display())
            else:
                print(item)

    def find_product(self, name):
        for obj in self.catalog:
            if obj.name == name:
                return obj
        return None

    @validate_positive
    def get_product_by_price(self, min_price, max_price):
        for obj in self.catalog:
            if min_price <= obj.price <= max_price:
                print(obj)

milk = Product('milk', 89)
milk_discount = DiscountProduct.from_product(milk, 15)
bread1 = Product('bread', 67)
bread2 = Product('bread', 57)
cookie = Product('cookie', 200)

kiwi = WeightProduct('kiwi', 150)
beef = WeightProduct('beef', 600)

#print(milk_discount.saved_amount)
cart1 = Cart()
cart1.add_product(milk_discount)

store1 = Store()
store1.add_product(bread1)
store1.add_product(cookie)

store1.get_product_by_price(100, 500)

#print(Cart().add_product.__name__)
#print(Cart().add_product.__doc__)
#print(Cart().add_product.__wrapped__)