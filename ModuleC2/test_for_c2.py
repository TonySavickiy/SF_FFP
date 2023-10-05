class Figure:
  def __init__(self, pos) -> None:
      self.setPos(pos)
      
  def setPos(self,pos):
    print(pos)
    
book = Figure('kwadrat')
    