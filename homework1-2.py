c = int (input("Введите количество секунд от 0 до 86400"))
d = c // 60
e = c - (d * 60)
f = d // 60
g = (c - (f * 3600)) // 60

if d < 0 or d > 1440:
   print ("Пожалуйста введите значение от 0 до 86400")

if d >= 0 and d < 1 and c >= 0 and c <= 9:
    print(f"00:00:0{c}")
if d >= 0 and d < 1 and c > 9 and c <= 59:
    print(f"00:0{d}:{c}")

if d >= 1 and d <= 9 and c >= 0 and c <= 9:
    print(f"00:0{d}:0{c}")
if d >= 1 and d <= 9 and c > 9 and c <= 59:
    print(f"00:0{d}:{c}")
if d >= 1 and d <= 9 and e >= 0 and e <= 9:
    print(f"00:0{d}:0{c - (d * 60)}")
if d >= 1 and d <= 9 and e > 9:
    print(f"00:0{d}:{c - (d * 60)}")

if d > 9 and d <= 59  and e >= 0 and e <= 9:
    print(f"00:{d}:0{c - (d * 60)}")
if d > 9 and d <= 59 and e > 9:
    print(f"00:{d}:{c - (d * 60)}")

if d > 59 and d <= 540 and e >= 0 and e <= 9 and g >= 0 and g <= 9:
    print(f"0{f}:0{g}:0{c - (d * 60)}")
if d > 59 and d <= 540 and e > 9 and g >= 0 and g <= 9:
    print(f"0{f}:0{g}:{c - (d * 60)}")
if d > 59 and d <= 540 and e >= 0 and e <= 9 and g >= 10 and g <= 59:
    print(f"0{f}:{g}:0{c - (d * 60)}")
if d > 59 and d <= 540 and e > 9 and g >= 10 and g <= 59:
    print(f"0{f}:{g}:{c - (d * 60)}")

if d > 540 and d <= 1440 and e >= 0 and e <= 9 and g >= 0 and g <= 9:
    print(f"{f}:0{g}:0{c - (d * 60)}")
if d > 540 and d <= 1440 and e > 9 and g >= 0 and g <= 9:
    print(f"{f}:0{g}:{c - (d * 60)}")
if d > 540 and d <= 1440 and e >= 0 and e <= 9 and g >= 10 and g <= 59:
    print(f"{f}:{g}:0{c - (d * 60)}")
if d > 540 and d <= 1440 and e > 9 and g >= 10 and g <= 59:
    print(f"{f}:{g}:{c - (d * 60)}")