#класс шахматной фигуры
class ChessFigure:
  def __init__(self) -> None:
      pass


  # метод, который должен возвращать список доступных для фигуры ходов из указанной позиции
  def possibleMoves(self, pos, constrains = None):
     return []


#класс, который представляет фигуру коня
class ChessHorse(ChessFigure):
  def __init__(self) -> None:
      super().__init__()


#возможные ходы для коня из позиции pos
  def possibleMoves(self, pos, constrains = None):
      moves = []
      moves.append( (pos.x + 2, pos.y+1) )
      moves.append( (pos.x + 2, pos.y-1) )
      moves.append( (pos.x - 2, pos.y+1) )
      moves.append( (pos.x - 2, pos.y-1) )
      moves.append( (pos.x + 1, pos.y+2) )
      moves.append( (pos.x - 1, pos.y+2) )
      moves.append( (pos.x + 1, pos.y-2) )
      moves.append( (pos.x - 1, pos.y-2) )
      return moves