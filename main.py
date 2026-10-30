import keyboard
import config
import time

if config.LANG.upper() == "RU":
    input("Пожалуйста, настройте CONFIG перед использованием программы! (ENTER)")
    print(f"Signed in with {config.USERNAME}")
    i = int(input("Выберите количество циклов: "))
    print("Откройте чат в Дискорде и закройте программу")
    print("Запуск скрипта...")
    time.sleep(3)
    
    for counter in range(1, i + 1):
        keyboard.write(";work", delay=0.1)
        keyboard.send("enter")
        print(f"Цикл {counter}: Работа. Статус: Успешно")
        keyboard.write(";collect", delay=0.1)
        keyboard.send("enter")
        print(f"Цикл {counter}: Зарплата. Статус: Успешно")
        if config.TRANSFER == True:
            keyboard.write(";with all", delay=0.01)
            time.sleep(0.5)
            keyboard.send("enter")
            keyboard.write(f";give {config.TRANSFER_USERNAME} all", delay=0.01)
            time.sleep(0.5)
            keyboard.send("enter")
            print(f"Цикл {counter}: Перевод. Статус: Успешно")
        else:
            keyboard.write(";dep all", delay=0.1)
            keyboard.send("enter")
            print(f"Цикл {counter}: Депозит. Статус: Успешно")
    
    
        time.sleep(1810)   # 30 мин - 1800
        keyboard.write(";work", delay=0.1)
        keyboard.send("enter")
        print(f"Цикл {counter}: Работа. Статус: Успешно")
        keyboard.write(";dep all", delay=0.1)
        keyboard.send("enter")
        print(f"Цикл {counter}: Депозит. Статус: Успешно")
        print(f"Цикл {counter} окончен.")
    
        time.sleep(1810)   # 30 мин - 1800
elif config.LANG == "EN":
    input("Set up the CONFIG before starting the programm! (ENTER)")
        print(f"Signed in with {config.USERNAME}")
        i = int(input("Choose cycle count: "))
        print("Open the Discord chat and minimise the window (if you need)")
        print("Launching script...")
        time.sleep(3)
        
        for counter in range(1, i + 1):
            keyboard.write(";work", delay=0.1)
            keyboard.send("enter")
            print(f"Cycle {counter}: Work. Status: Success")
            keyboard.write(";collect", delay=0.1)
            keyboard.send("enter")
            print(f"Cycle {counter}: Collect. Status: Success")
            if config.TRANSFER == True:
                keyboard.write(";with all", delay=0.01)
                time.sleep(0.5)
                keyboard.send("enter")
                keyboard.write(f";give {config.TRANSFER_USERNAME} all", delay=0.01)
                time.sleep(0.5)
                keyboard.send("enter")
                print(f"Cycle {counter}: Transfer. Status: Success")
            else:
                keyboard.write(";dep all", delay=0.1)
                keyboard.send("enter")
                print(f"Cycle {counter}: Deposit. Status: Success")
        
        
            time.sleep(1810)   # 30 мин - 1800
            keyboard.write(";work", delay=0.1)
            keyboard.send("enter")
            print(f"Cycle {counter}: Work. Status: Success")
            keyboard.write(";dep all", delay=0.1)
            keyboard.send("enter")
            print(f"Cycle {counter}: Deposit. Status: Success")
            print(f"Cycle {counter} Ended.")
        
            time.sleep(1810)   # 30 мин - 1800
else:
    print("Something went wrong...")
