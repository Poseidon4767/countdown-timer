from time import sleep

timer = int(input("Set timer: "))

for i in range(timer, -1, -1):
    print(i)
    sleep(1)
    if i == 0:
        print("Buzzz!!! Your time's up!")