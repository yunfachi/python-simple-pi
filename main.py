from datetime import datetime
pi = 0
start1 = datetime.now()
for i in range(1, 10000):
    pi = pi+4*((-1)**(i+1))/(2*i-1)
result1=datetime.now() - start1
pi = 0
start2 = datetime.now()
for i in range(1, 10000):
    pi = pi+4*((-1)**(i+1))/(2*i-1)
    print("SYNC...     ", pi)
result2=datetime.now() - start2
result_procentage = result2/result1*100
pi = 0
correctness = int(input("correctness (the larger the number, the more correctness pi will be) $ "))
print_pi = input(f"to send presumptive pi in the course of calculation ({int(result_procentage)} percent slower) (y/n) $ ")
start = datetime.now()
if print_pi.lower() != "y":
    for i in range(1, correctness):
        pi = pi+4*((-1)**(i+1))/(2*i-1)
else:
    for i in range(1, correctness):
        pi = pi+4*((-1)**(i+1))/(2*i-1)
        print(pi)
result=datetime.now() - start
while True:
    try:
        digits = int(input("digits after decimal point $ "))
        if digits > 1000:
            agree = input("the script may crash. do you agree that you want more than 1000 digits after the dot? (y/n) $ ")
            if agree.lower() != "y":
                continue
        print("time:", result, "result:", f'{pi:.{digits}f}')
    except:
        pass