numbers = []
while True:
    num = input()
    if num == "":
        break
    if num.count('1') > 1:
        print("один")
    if num.count('2') > 1:
        print("два")
    if num.count('3') > 1:
        print("три")
    if num.count('4') > 1:
        print("четыре")
    if num.count('5') > 1:
        print("пять")
    if num.count('6') > 1:
        print("шесть")
    if num.count('7') > 1:
        print("семь")
    if num.count('8') > 1:
        print("восемь")
    if num.count('9') > 1:
        print("девять")
    if num.count('0') > 1:
        print("ноль")
