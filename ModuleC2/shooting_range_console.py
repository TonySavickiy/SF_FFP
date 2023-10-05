import random as rnd
# Инициируем класс для создания объекта позиции(координат),
# который в дальнейшей логике будет передаваться в качестве аргумента pos
class Pos:
    def __init__(self, x: int,y: int) -> None:
        self.x = x
        self.y = y

#Родительский класс фигура
class Figure:
    def __init__(self, pos) -> None:#в момент создания объекта вызываем сетеры позиции и цвета
        self.setPos(pos)
        self.setColor(0)
    
    
    def setPos(self, pos):
        self.pos = pos
        
    def getPos(self):
        return self.pos
    


# проверка находится ли фигура по верх точки, т.к. род. класс не имеет формы, возвращает фолс, в дальнейшем
# будет переопределён в подклассах конкретных фигур
    def isIn(self, x, y) -> bool:
        return False

# Подкласс прямоугольник.
class Square(Figure):
# Переопределение родительского инита с добавлением атрибутов высоты и ширины(h, w)
    def __init__(self, pos,w: int,h: int) -> None:
        super().__init__(pos)
        self.w = w
        self.h = h


# Расширение функционала, как описано ранее. Если координаты фигуры "накладываются" на точку, возвращает тру    
    def isIn(self, x, y) -> bool:
        _pos = super().getPos()
        if (_pos.x < x) and ( (_pos.x + self.w) > x) and (_pos.y < y) and ( (_pos.y + self.y > y) ):
            return True
        return False
    

 # класс цели, включающий параметр стоимости
class HitMark:
    def __init__(self, cost) -> None:
        self.setCost(cost)
    
    def setCost(self, cost):
        self.cost = cost
        
        
    def getCost(self):
        return self.cost
    
class SquareHitMark(Square, HitMark):
    def __init__(self, pos, w: int, h: int, cost) -> None:
        super().__init__(pos, w, h)
        HitMark.setCost(self, cost)
        
        
class GameEvent:
    
    Event_Tick = 1
    
    def __init__(self, type, data) -> None:
        self.type = type
        self.data = data
    
    def getType(self):
        return self.type

    def getData(self):
        return self.data
    


class GameLogic:
    def __init__(self, w, h) -> None:
        self.gameboard_width = w
        self.gameboard_height = h
        
        self.marks = []
        
        self.hitMarks = []
        
        self.score = 0
#если сообщение “выстрел в цель”, то обрабатываем эту ситуацию
#используя позицию pos, переданную от интерфейса        
    def processEvent(self, event):
        if event.type == GameEvent.Event_Hit:
           self.hit(event.data)

# метод добавить цель на “логическую” доску    
    def addHitMark(self, mark):
        self.marks.append(mark)


# метод выстрела        
    def hit(self, pos):
        for markIndex in range(len(self.marks)):#проходим по списку сгенерированных целей
            mark  = self.marks[markIndex]
            if mark.isIn(pos.x, pos.y):#Если есть попадание, добавляем очки, убираем цель из списка целей
                self.score += mark.getCost()
                self.marks.pop(markIndex)
                self.hitMarks.append(mark)
                break
            
    def getBoard(self):
        return self.marks
    
    def getScore(self):
        return self.score
    
    
    
class Game:
    def run(self):
        running = True

        while running:
            print('------------------')
            print('0. exit')
            print('1. hit target')
            cmd = int(input())