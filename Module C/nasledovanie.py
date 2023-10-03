import datetime


class Product:
    max_quantity = 100000

    def __init__(self, name='Fignya', category='HZ_chto_eto', quantity_in_stock=1):
        self.name = name
        self.category = category
        self.quantity_in_stock = quantity_in_stock

    def is_available(self):
        return True if self.quantity_in_stock > 0 else False
    
    def set_name(self, name):
        if name not in black_list:
            ex_name = self.name
            self.name = name
            print(f'Для объекта {ex_name} задано имя {name}')
        else:
            print('Имя недоступно для установки')
    
    def get_name(self):
        return self.name


class Food(Product):
    is_critical = True
    needs_to_be_refreshed = True
    refresh_frequency = datetime.timedelta(days=1)


eggs = Food(name="eggs", category="food", quantity_in_stock=5)
print(eggs.max_quantity)
print(eggs.is_available())