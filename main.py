#Добавить gui
name = str(input("Введите свое имя: "))
age = int(input("Введите свой возраст: "))
while age < 10:
    age = int(input("Введите свой возраст еще раз: "))
    if age >= 10:
        break

wt = float(input("Введите свой вес: "))
while wt > 300:
    wt = float(input("Введите свой вес еще раз: "))
    if wt <= 300:
        break

height = float(input("Введите свой рост: "))
while height > 3:
    height = float(input("Введите свой рост еще раз: "))
    if height <= 3:
        break
 
#Вывод показателей и вашего ИМТ
print(f"Имя: {name} Возраст: {age} Вес: {wt} Рост: {height}")
bmi = wt / height ** 2
i = round(bmi)
if i >= 10 and i <= 25:
    print(f"Ваш ИМТ {i} в пределах нормы")
elif i >= 25 and i <= 35:
    print(f"Ваш ИМТ {i} это ожирение 1 степени")
elif i >= 35 and i <= 45:
    print(f"Ваш ИМТ {i} это ожирение 2 степени")
else:
    print(f"Ваш ИМТ {i} это ожирение 3 степени")