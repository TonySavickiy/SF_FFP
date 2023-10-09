class Tester:
    def __init__(self, testor) -> None:
        self.__testor = testor
        
    @property
    def tes(self):
        return self.__testor
    
    @tes.setter
    def tes(self, te):
        self.__testor = te
        
box = Tester('bur')
# print(box._testor)
print(box.tes)
box.tes = 'bur_now'
print(box.tes)