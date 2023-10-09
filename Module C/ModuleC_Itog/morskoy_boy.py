"""
    Игра "Морской бой".
    Играет пользователь против компьютера.
    Пользователь вводит координаты для осуществления выстрела, компьютер генерирует выстрелы случайным образом.
    Точками отображаются координаты, недоступные для выстрела(повторные выстрелы\зона вокруг подбитого корабля).
    Победитель - тот, кто подобьёт все корабли противника.
    На доске расположены: 1 корабль мощностью 3 клетки, 2 корабля мощностью 2 клетки и 4 корабля мощностью 1 клетка.
    
"""
from random import randint

#Класс для описания координат
class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x}, {self.y}'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

#Создаём свои подклассы для обработки ошибок, наследуя от встроенного класса Exception
class GameException(Exception):
    pass
  
class BoardUsedException(GameException):
    def __str__(self):
        return f'В данную точку уже был выстрел '
      
class OutBoardException(GameException):
    def __str__(self):
        return f'Координаты неверны'

class OutOfAreaException(GameException):
    pass

#Описание объекта "корабль", подразумевается передача объекта типа Dot
class Ship:
    def __init__(self, coords, power, orient):
        self.coords = coords
        self.power = power
        self.orient = orient
        self.health = power

    @property
    def _ship_dots(self):
        self.ship_array = []

        for i in range(self.power):
            _x = self.coords.x
            _y = self.coords.y

            if self.orient:
                _x += i
            else:
                _y += i

            self.ship_array.append(Dot(_x, _y))

        return self.ship_array

    def fired(self, fire):
        return fire in self._ship_dots

#Класс поле боя
class BattleZone:

    def __init__(self, hidden=False):
        self.zanyato = []
        self.coords = []
        self.hidden = hidden
        self.cnt = 0
        self.size = 6

        self.tild = []
        self.tild = [['~'] * 6 for i in range(self.size)]

#метод для добавления кораблей на поле боя.
    def add_ships(self, _ships):

#проверка на доступность(в зоне поля боя\занято или не занято)
        for i in _ships._ship_dots:
            if not (0 <= i.x < 6 > i.y >= 0) or i in self.zanyato:
                raise OutOfAreaException()
        for i in _ships._ship_dots:
            self.tild[i.x][i.y] = '◇'
            self.zanyato.append(i)

        self.coords.append(_ships)
        self.zone_around_ship(_ships)

    def __str__(self):
        lines = f'  1 2 3 4 5 6'
        for i, j in enumerate(self.tild):
            lines += f'\n{i + 1} ' + ' '.join(j)
        if self.hidden:
            lines = lines.replace('◇', '~')
        return lines

    def clear(self):
        self.zanyato = []

    def out(self, dots):
        return not (0 <= dots.x < 6 > dots.y >= 0)

    def shot(self, dots):
        if self.out(dots):
            raise OutBoardException()

        if dots in self.zanyato:
            raise BoardUsedException()

        self.zanyato.append(dots)

        for ship in self.coords:
            if dots in ship._ship_dots:
                ship.health -= 1
                self.tild[dots.x][dots.y] = "◈"
                if ship.health == 0:
                    self.cnt += 1
                    self.zone_around_ship(ship, verb=True)
                    print("Корабль уничтожен!")
                    return False
                else:
                    print("Попадание")
                    return True

        self.tild[dots.x][dots.y] = "◦"
        print("Мимо!")
        return False

# Добавление индикаторов вокруг уже подбитых кораблей
    def zone_around_ship(self, array, verb=False):
        around = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 0), (0, 1),
                  (1, -1), (1, 0), (1, 1)]
        for i in array._ship_dots:
            for i_x, i_y in around:
                current = Dot(i.x + i_x, i.y + i_y)
                if (0 <= current.x < 6 > current.y >= 0) and current not in self.zanyato:
                    if verb:
                        self.tild[current.x][current.y] = '◦'
                    self.zanyato.append(current)

# Родительский класс для описания логики ходов в игре
class Turn:
    def __init__(self, board, enem):
        self.b = board
        self.e = enem

    def ask(self):
        raise NotImplementedError()

    def turn(self):
        while True:
            try:
                target = self.ask()
                repeat = self.e.shot(target)
                return repeat
            except GameException as e:
                print(e)

# Описание процесса хода пользователя
class USER(Turn):
    def ask(self):
        while True:
            cords = input("Ваш ход, введите координаты: ").split()

            if len(cords) != 2:
                print(" Введите координаты(сначала Y, затем X через пробел) ")
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):
                print(" Введите число! ")
                continue

            x, y = int(x), int(y)

            return Dot(x - 1, y - 1)

# Ход компьютера
class AI(Turn):
    def ask(self):
        d = Dot(randint(0, 5), randint(0, 5))
        print(f"Ход компьютера: {d.x + 1} {d.y + 1}")
        return d

# Описание основной логики игры
class Game:
    def __init__(self):
        player = self.try_make_board()
        comp = self.try_make_board()
        comp.hidden = True
        self.AI = AI(comp, player)
        self.user = USER(player, comp)

# Создание игровой доски с кораблями
    def try_make_board(self):
        board = None
        while board is None:
            board = self.random_ships()
        return board
    
# Распределение кораблей
    def random_ships(self):
        battle_area = BattleZone()
        count_ships = [3, 2, 2, 1, 1, 1, 1]
        retry = 1
        for ship in count_ships:
            while True:
                retry += 1
                if retry > 2000:
                    return None
                _orient = randint(0, 1)
                _ship = Dot(randint(0, 6), randint(0, 6))
                power = ship
                x_y = Ship(_ship, power, _orient)
                try:
                    battle_area.add_ships(x_y)
                    break
                except OutOfAreaException:
                    pass
        battle_area.clear()
        return battle_area
    
#Приветственный блок
    def greet(self):
        print('-' * 20)
        print('Добро пожаловать!')
        print('Морской__Бой')
        print('-' * 20)
        print('   Для выстрела')
        print('   нужно вводить\n   координаты Y X')
        print('   X - Строка')
        print('   Y - Столбец')

#Блок хода игры
    def loop(self):
        num = 0
        while True:
            print("-" * 20)
            print("Карта пользователя:")
            print(self.user.b)
            print("-" * 20)
            print("Карта компьютера:")
            print(self.AI.b)
            if num % 2 == 0:
                print("-" * 20)
                print("Ходит пользователь!")
                repeat = self.user.turn()
            else:
                print("-" * 20)
                print("Ходит компьютер!")
                repeat = self.AI.turn()
            if repeat:
                num -= 1

            if self.AI.b.cnt == 7:
                print("-" * 20)
                print(self.AI.b)
                print("Пользователь выиграл!")
                break

            if self.user.b.cnt == 7:
                print("-" * 20)
                print(self.user.b)
                print("Компьютер выиграл!")
                break
            num += 1

    def start(self):
        self.greet()
        self.loop()


b = Game()
b.start()