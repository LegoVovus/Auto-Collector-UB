import keyboard
import time

i = int(input("Select the amount of cycles: "))
print("Open Discord chat and press Enter")
print("Running script...")
time.sleep(3)

for counter in range(1, i + 1):
    keyboard.write(";work", delay=0.1)
    keyboard.send("enter")
    print(f"Cycle {counter}: Work ✅Successful")
    keyboard.write(";collect", delay=0.1)
    keyboard.send("enter")
    print(f"Cycle {counter}: Collect ✅Successful")
    keyboard.write(";dep all", delay=0.1)
    keyboard.send("enter")
    print(f"Cycle {counter}: Deposit ✅Successful")

    time.sleep(1810)   # 30 min - 1800
    keyboard.write(";work", delay=0.1)
    keyboard.send("enter")
    print(f"Cycle {counter}: Work ✅Successful")
    keyboard.write(";dep all", delay=0.1)
    keyboard.send("enter")
    print(f"Cycle {counter}: Deposit ✅Successful")
    print(f"Cycle {counter} окончен.")

    time.sleep(1810)   # 30 min - 1800
