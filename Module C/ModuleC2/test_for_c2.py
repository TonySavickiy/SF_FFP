# size = int(input('Введите колл-во полей'))
# board = [[] for i in range(size)]
# for i in range(len(board)):
#   if i == 0:
#     for _ in range(size):
#       if _ == str(0):
#         board[i].append('')
#       else:
#         board[i].append(str(_))
#   else:
#     for _ in range(size):
#       if _ == 0:
#         board[i].append(str(i))
#       else:
#         board[i].append(str(0))

# print(board)

# def display_field():
#   for i in board:
#     print('|'.join(i),end='|\n')
# display_field()
class Pos:
  def __init__(self, x, y) -> None:
      self.x = x
      self.y = y

class Board:
  def __init__(self, size) -> None:
    self.__size = size
    self.board = self.create_board()
    self.count1 = 0
    self.count2 = 0
    self.count3 = 0
  
  @property
  def size_board(self):
    return self.__size
    
  @size_board.setter
  def size_board(self):
    self.__size = size
      
  def create_board(self):
    board = [[] for i in range(self.__size + 1)]
    for i in range(len(board)):
      if i == 0:
        for _ in range(self.__size + 1):
          if _ == str(0):
            board[i].append('')
          else:
            board[i].append(str(_))
      else:
        for _ in range(self.__size + 1):
          if _ == 0:
            board[i].append(str(i))
          else:
            board[i].append(str(0))
    return board
  
  def add_sheep(self, sheep):
    if sheep.power in [0,1,2] and sheep.direction == 'g' or sheep.direction == 'v':
      if sheep.power == 0:
        if self.count1  < 4:
          self.board[sheep.y][sheep.x] == 'T'
          self.count1 += 1
          print('На доску добавлен одинарный кораблик')
          self.display_field()
      elif sheep.power == 1:
        if self.count2 < 2:
          if sheep.direction == "g":
            self.board[sheep.y][sheep.x1:sheep.x + 1] = 'T'
            print('сработало тут')
          else:
            for i in range(sheep.y,sheep.y1+1):
              self.board[i][sheep.x] = 'T'
            print('сработало здесь')
          self.count2 += 1
          print('На доску добавлен двойной корабль')
          print(self.board)
          self.display_field()
      # else: 
    else:
      print('Неверная мощность корабля')

  def display_field_player(self):
    for i in self.board:
      print('|'.join(i),end='|\n')
  def display_field_ai(self)
    for i in self.board:
      print('|'.join(i),end='|\n')

class Sheep:
  def __init__(self, pos,direction:str = 'g', power:int = 0 ) -> None:
    self.power = power
    self.direction = direction
    self.x = pos.x
    self.y = pos.y
    if direction == 'g':
      self.x1 = pos.x - power
      self.y1 = pos.y
    elif direction == 'v':
      self.x1 = pos.x
      self.y1 = pos.y + power


        
    
    
    
    
box = Board(6)
bo = Sheep(Pos(2,2),'v',1)

box.add_sheep(bo)

print('end')