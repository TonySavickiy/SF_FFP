class Angle:
    def __init__(self, angle = 0) -> None:
        self.__angle = angle

    def __str__(self):
        return f"""Angle: value = {self.__angle}"""

    def __repr__(self) -> str:
        return f"""Angle(angle={self.__angle})"""

    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, angle):
        self.__angle = angle

if __name__ == "__main__":
  a = Angle(30)
  print(a) # выведет Angle: value = 30
  print(repr(a)) #выведет Angle(angle=30)