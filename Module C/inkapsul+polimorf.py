# class Product:
#     def __init__(self, name, category, quantity_in_stock):
#         self.name = name
#         self.category = category
#         self.quantity_in_stock = quantity_in_stock

#     def is_available(self):
#         return True if self.quantity_in_stock > 0 else False
    
    


# class Event:
#     def __init__(self, timestamp=0, event_type="", session_id=""):
#         self.timestamp = timestamp
#         self.type = event_type
#         self.session_id = session_id
        
#     def init_from_dict(self, event_dict):
#         self.timestamp = event_dict.get("timestamp")
#         self.type = event_dict.get("type")
#         self.session_id = event_dict.get("session_id")
        
        
# events = [
#     {
#      "timestamp": 1554583508000,
#      "type": "itemViewEvent",
#      "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
#     {
#      "timestamp": 1555296337000,
#      "type": "itemViewEvent",
#      "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
#     {
#      "timestamp": 1549461608000,
#      "type": "itemBuyEvent",
#      "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
# ]


# #Здесь мы создаём экземпляры класса Event по данным из словаря events.
# # for event in events:
# #     event_obj = Event(timestamp=event.get("timestamp"),
# #                       event_type=event.get("type"),
# #                       session_id=event.get("session_id"))
# #     print(event_obj.timestamp)
    
# #Здесь мы сделаем тоже самое, но через ранее определенный специальный метод

# for i in events:
#     event_obj = Event()
#     event_obj.init_from_dict(i)
#     print(event_obj)
    


# # Создаём неправильный класс.
# class Human:
#     # класс человек с полем возраста
#     age = None
 
#     def __init__(self, age=4):
#         self.age = age
        
# h = Human()
# h.age = 15 # (Так делать лучше не стоит, если вы хотите когда-нибудь найти работу)
# print(h.age) # и так тоже


# Более правильный пример
 
# Исправим наш предыдущий код.
class Human:
    age = None
 
    def __init__(self, age=4):
        self.age = age
 
    # добавляем геттер - специальный метод для получения поля
    def get_age(self):
        return self.age
 
    # добавляем сеттер - специальный метод для установки нового значения 
    def set_age(self, age):
        if age > 0 and isinstance(age, int): # проверяем условия, что человеку должно быть больше 0 лет и его возраст - целое число
            self.age = age
 
 
h = Human()
h.set_age(15)
print(h.get_age())