a = [ int(input(f"Напишите {i+1} значение: ")) for i in range(3) ]
print(f"Наши значения: {a}")

# №1  
print(a[0] and a[1] and a[2] and "Нет нулевых значений!!!")

# №2
print(a[0] or a[1] or a[2] or "Введены все нули!")

# №3
if a[0] >  a[1] + a[2]:
  print(f"({a[0]}) - ({a[1]}) - ({a[2]}) = \
        {a[0] - a[1] - a[2]}")
 
# №4
if a[0] <  a[1] + a[2]:
  print(f"({a[1]}) + ({a[2]}) - ({a[0]}) = \
        {-a[0] + a[1] + a[2]}")  

# №5
if a[0] > 50 and ((a[1] > a[0]) or (a[2] > a[0])):
  print('Вася')

# №6
if a[0] > 5 or ((a[1] == 7) and (a[2] == 7)):
  print('Петя')