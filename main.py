#Добавить gui
print("Введите свое имя.")
name = str(input())

print("Введите свой возраст.")
age = int(input())
while age < 10:
    print("Введите свой возраст еще раз.")
    age = int(input())
    if age >= 10:
        break

print("Введите свой вес.")
wt = float(input())
while wt > 300:
    print("Введите свой вес еще раз.")
    wt = float(input())
    if wt <= 300:
        break

print("Введите свой рост.")
height = float(input())
while height > 3:
    print("Введите свой рост еще раз.")
    height = float(input())
    if height <= 3:
        break

#Вывод показателей и вашего ИМТ
print(f"Имя: {name} Возраст: {age} Вес: {wt} Рост: {height}")
bmi = wt / height ** 2
i = round(bmi)
if i >= 10 and i <= 20:
    print(f"Ваш ИМТ {i} в пределах нормы")
elif i >= 20 and i <= 40:
    print(f"Ваш ИМТ {i} это ожирение 1 степени")
elif i >= 40 and i <= 60:
    print(f"Ваш ИМТ {i} это ожирение 2 степени")
else:
    print(f"Ваш ИМТ {i} это ожирение 3 степени")