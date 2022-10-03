from point import CoolFunction, Point

start = Point(1,1)
end = Point(10,10)

print(f"Vi startar labyinten på {start.GetX()}, {start.GetY()}")
print(f"Vi slutar labyinten på {end.GetX()}, {end.GetY()}")

start.Add(end)
print(f"Efter plus är starten {start.GetX()}, {start.GetY()}")


print(CoolFunction(12))

