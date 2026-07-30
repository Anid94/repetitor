class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        return f'name: {self.name}, price: {self.price}'

class Cart:
    def __init__(self):
        self.my_list = []

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

    def show(self):
        for obj in self.my_list:
            print(obj.display())

    def remove_product(self, product):
        if product in self.my_list:
            self.my_list.remove(product)
            print(f'Товар "{product.name}" удален из корзины')
        else:
            print(f'Товар "{product.name}" не найден')

    def clear(self):
        self.my_list.clear()
        print('Корзина очищена')

    def find_obj(self, product_name):
        for obj in self.my_list:
            if obj.name == product_name:
                return obj.display()
        return None

class DiscountProduct(Product):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def display(self):
        return f'name: {self.name}, price: {self.price * (1 - self.discount / 100)} руб. (original: {self.price} руб., discount: {self.discount}%)'

    def price_with_discount(self):
        print(self.display())

class WeightProduct(Product):
    def __init__(self, name, price_per_kg):
        super().__init__(name, price_per_kg)

    def get_cost(self, weight):
        return f'name: {self.name}, price: {self.price * weight} руб/кг'

banana = Product('banana', 59)
apple = Product('apple', 100)
tea = Product('tea', 130)
chocolate = Product('chocolate', 67)
milk = DiscountProduct('milk', 128, 15)

new_cart = Cart()
new_cart.add_product(apple)
new_cart.add_product(banana)
new_cart.add_product(milk)
new_cart.show()


new_cart.remove_product(apple)
new_cart.show()
new_cart.remove_product(chocolate)
#new_cart.clear()
#new_cart.show()
print(new_cart.find_obj('banana'))

milk.price_with_discount()
cheese = WeightProduct('cheese', 800)
print(cheese.display())
print(cheese.get_cost(0.5))
