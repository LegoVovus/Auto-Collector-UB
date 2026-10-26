import keyboard
import time

i = int(input("Выберите количество циклов: "))
print("Откройте чат в Дискорде и закройте программу")
print("Запуск скрипта...")
time.sleep(3)

for counter in range(1, i + 1):
    keyboard.write(";work", delay=0.1)
    keyboard.send("enter")
    print(f"Цикл {counter}: Работа ✅Успешно")
    keyboard.write(";collect", delay=0.1)
    keyboard.send("enter")
    print(f"Цикл {counter}: Зарплата ✅Успешно")
    keyboard.write(";dep all", delay=0.1)
    keyboard.send("enter")
    print(f"Цикл {counter}: Депозит ✅Успешно")

    time.sleep(1810)   # 30 мин - 1800
    keyboard.write(";work", delay=0.1)
    keyboard.send("enter")
    print(f"Цикл {counter}: Работа ✅Успешно")
    keyboard.write(";dep all", delay=0.1)
    keyboard.send("enter")
    print(f"Цикл {counter}: Депозит ✅Успешно")
    print(f"Цикл {counter} окончен.")

    time.sleep(1810)   # 30 мин - 1800