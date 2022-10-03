from point import CoolFunction, Point
from rectangle import Rectangle
from circle import Circle

c = Circle(12)
d = Circle(2342)
omkrets = c.Circumference()
print(f"Omkrets {omkrets}")
print(f"Area {c.Area()}")
print(f"Omkrets {d.Circumference()}")
print(f"Area {d.Area()}")




width = 12
height = 13
print(f"Arean är {width*height}")

rect = Rectangle(width,height)
print(f"Arean är {rect.CalculateArea()}")

start = Point(1,1)
end = Point(10,10)

print(f"Vi startar labyinten på {start.GetX()}, {start.GetY()}")
print(f"Vi slutar labyinten på {end.GetX()}, {end.GetY()}")

start.Add(end)
print(f"Efter plus är starten {start.GetX()}, {start.GetY()}")


print(CoolFunction(12))

