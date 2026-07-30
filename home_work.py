class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

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
        if product:
            self.my_list.append(product)

    def count_product(self):
        return len(self.my_list)

    def sum_price(self):
        summ = 0
        for obj in self.my_list:
            summ += obj.price

        return summ

    def __str__(self):
        return f'name: {self.name}, price: {self.price}'

    def remove_product(self, product):
        for obj in self.my_list:
            if product == obj.name:
                self.my_list.remove(obj)
                print(f'Товар {obj.name} удален из корзины')
            else:
                print(f'Товар {obj.name} не найден')

    def clear(self):
        self.my_list.clear()
        print('Корзина очищена')

    def find_obj(self, product_name):
        for obj in self.my_list:
            if obj.name == product_name:
                return obj
        return None

    def __len__(self):
        return len(self.my_list)

    def __getitem__(self, index):
        return self.my_list[index]

class DiscountProduct(Product):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def price_with_discount(self):
        return self.price * (1 - self.discount / 100)

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

banana = Product('banana', 59)
apple = Product('apple', 100)
apple1 = Product('apple', 90)

new_cart = Cart()
new_cart.add_product(apple)
new_cart.add_product(banana)
#new_cart.__add__(apple1)

cart1 = Cart()
cart1.add_product(apple1)
cart1.add_product(apple)

cart2 = Cart()
cart2.add_product(banana)

cart3 = cart1 + cart2

print(cart3)
