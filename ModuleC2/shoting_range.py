import random as rnd
import pygame

#класс позиции элемента, хранящий значения х и у
class Pos:
  def __init__(self, x, y) -> None:
      self.x = x
      self.y = y


#абстракция — класс произвольной фигуры с полями позиция и цвет
class Figure:
  def __init__(self, pos) -> None:
      self.setPos(pos)
      self.setColor(0)

  def setPos(self, pos):
     self.pos = pos

  def getPos(self):
     return self.pos

  def setColor(self,color):
     self.color = color

  def getColor(self):
     return self.color

   #метод, который намекает на “форму” — при выполнении метода класс возвращает True, если 
   #точка, переданная х и у, лежит внутри фигуры и False в противном случае
   #поскольку класс Figure “не имеет” формы, то всегда возвращает False
  def isIn(self, x, y)->bool:
     return False


#класс прямоугольника с шириной и высотой 
class Square(Figure):
  def __init__(self, pos , w, h) -> None:
     super().__init__(pos)
     self.w =  w
     self.h =  h


#isIn в этом случае возвращает True, если точка лежит между границами прямоугольника
  def isIn(self, x, y) -> bool:
     _pos = super().getPos()
     if (_pos.x < x) and ( (_pos.x + self.w) > x) and (_pos.y < y) and  ( (_pos.y + self.h) > y):
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


#класс “прямоугольной” цели, наследуемый от класса прямоугольника и класса цели,
#который включает как форму, так и стоимость 
class SquareHitMark(Square, HitMark):
  def __init__(self, pos, w, h, cost) -> None:
      super().__init__(pos, w, h)
      HitMark.setCost(self, cost)
      
      
class GameEvent:

#пустое событие
  Event_None  = 0
#событие таймера
  Event_Tick  = 1
#событие “выстрела” по цели
  Event_Hit = 2

  def __init__(self, type, data) -> None:
      self.type = type
      self.data = data

  def getType(self):
     return self.type

  def getData(self):
     return self.data
  
  
#класс игровой логики
class GameLogic:
  def __init__(self, w, h) -> None:
 #ширина игрового поля     
      self.gameboard_width  = w
 #высота игрового поля
      self.gameboard_height = h
 #активные цели на доске
      self.marks = []
 #пораженные цели
      self.hitMarks = []
 #полученные очки
      self.score = 0


 #метод обработки сообщений, которые приходят к игровой логике
  def processEvent(self,event):
  #если событие таймер, то добавляем ещё одну цель к списку активных целей
     if event.type == GameEvent.Event_Tick:
        # на случайной позиции в пределах игровой доски
        markRandPos = Pos(rnd.randint(20,self.gameboard_width-20)
                         ,rnd.randint(20,self.gameboard_height-20))
        # случайного размера от 10 до 20
        markSize = rnd.randint(10,20)
        # стоимость цели обратно пропорциональна размеру
        markCost = 30 - markSize
        # случайный цвет цели в формате RGB
        markColor = (rnd.randint(0,255),rnd.randint(0,255),rnd.randint(0,255))
        mark = SquareHitMark(markRandPos,markSize,markSize,markCost)
        mark.setColor(markColor)
  #добавляем цель на доску
        self.addHitMark(mark)
  #если сообщение “выстрел в цель”, то обрабатываем эту ситуацию
  #используя позицию pos, переданную от интерфейса  
     if event.type == GameEvent.Event_Hit:
           self.hit(event.data)


# метод добавить цель на “логическую” доску
  def addHitMark(self, mark):
     self.marks.append(mark)


#метод поразить цель на “логической” доске
  def hit(self,pos):
#перебираем все цели, и если метод isIn возвращает True
# добавляем стоимость цели к счету и перемещаем ее из списка активных целей в пораженные
     for markIndex in range(len(self.marks)):
        mark = self.marks[markIndex]
        if mark.isIn(pos.x, pos.y):
           self.score += mark.getCost()
           self.marks.pop(markIndex)
           self.hitMarks.append(mark)
           break
 #метод возвращает все активные цели на доске
  def getBoard(self):
     return self.marks
 #метод возвращает текущий счёт
  def getScore(self):
     return self.score



      
#класс, реализующий графическую подсистему игры
class PyGameGui:
  def __init__(self, w, h, logic) -> None:
#ширина окна
      self.main_w = w
#высота окна
      self.main_h = h
#окно pygame
      self.screen = pygame.display.set_mode([self.main_w,self.main_h])
#логика игры в виде внутреннего объекта
      self.logic = logic
#шрифт для отображения счёта на экране
      self.font  = pygame.font.SysFont('Consolas', 30)
     
#метод, который запускает игру
  def run(self):
     running = True
#устанавливаем таймер pygame на 1 сек
     pygame.time.set_timer(pygame.USEREVENT + GameEvent.Event_Tick, 1000)
#создаем бесконечный цикл обработки сообщений от пользователя
     while running:
        #если пользователь закрыл окно, то завершаем обработку событий и заканчиваем игру
        #иначе обрабатываем сообщение
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 running = False
             else:
                 self.processEvent(event)
        #выполняем отрисовку
        self.draw()


#метод обработки сообщений от интерфейса
  def processEvent(self, event):
# если событие таймера, то переделываем событие pygame в события нашей игры GameEvent
     if (event.type >= pygame.USEREVENT) and (event.type < pygame.NUMEVENTS):
        myevent = GameEvent()
        myevent.type = event.type - pygame.USEREVENT
        self.logic.processEvent(myevent)


# если событие клик мышкой, то передаём позицию клика в сообщении Hit
     if event.type == pygame.MOUSEBUTTONDOWN:
        pypos= event.pos
        myevent = GameEvent(GameEvent.Event_Hit, Pos(pypos[0], pypos[1]))
        self.logic.processEvent(myevent)

#метод отрисовки доски
  def draw(self):
     # заполняем фон
     self.screen.fill((255, 255, 255))

#получаем все активные цели на доске и отрисовываем их в виде прямоугольников соответствующего цвета
     marks = self.logic.getBoard()
     for mark in marks:
        pygame.draw.rect(self.screen,mark.getColor(), pygame.Rect(mark.getPos().x, mark.getPos().y, mark.getWidth(), mark.getHeight()))


#получаем текущие очки 
     score = self.logic.getScore()
#отображаем счёт на окне
     self.screen.blit(self.font.render(f'score:{score}', True, (0, 0, 0)), (32, 48))

     pygame.display.flip()
     


if __name__ == "__main__":
  pygame.init()
  width = 800
  height  = 600
  gui = PyGameGui(width, height, GameLogic(width, height))
  gui.run()
  pygame.quit()