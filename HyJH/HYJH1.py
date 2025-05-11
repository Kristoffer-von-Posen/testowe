class but:

  def __init__(self, lewy, rozmiar, kolor):
    self.rozmiar = rozmiar
    self.kolorek = kolor
    self.prawy = lewy + 1

  def zmien(self, y):
    self.rozmiar = y


x = but(2, 2, "niebieski")
x.zmien(4)

print(x.rozmiar)
