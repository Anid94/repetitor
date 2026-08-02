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

    def total_without_discount(self):
        summ = 0
        for obj in self.my_list:
            summ += obj.price

        return summ

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

    def find_obj(self, product_name):
        for obj in self.my_list:
            if obj.name == product_name:
                return obj
        return None

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


banana1 = Product('banana', 59)
banana2 = Product('banana', 89)
apple1 = Product('apple', 90)
apple2 = Product('apple', 95)
apple3 = Product('apple', 100)

cart1 = Cart()
cart1.add_product(apple1)
cart1.add_product(apple2)
cart1.add_product(apple3)
cart1.add_product(banana1)
cart1.add_product(banana2)

print(cart1)
print(cart1.total_without_discount())
print('---------------------')
cart1.remove_product('apple')
print('---------------------')
print(cart1)
print('---------------------')

for product in cart1:
    print(product)

print(cart1.total_without_discount())
