file=open("my_app-test.log",'r').readlines()
flag=True

for line_number, line in enumerate(file):
    if "User-Service" in line and not("Start logging" in line or "id generated" in line):
        print("Логи User-Service запоминаются неверно")
        flag=False
        break
    elif "subscriber" in line and not("id:" in line or "Connecting to broker" in line or "received message" in line):
        print("Логи subscriber запоминаются неверно")
        flag=False
        break
    elif "subscriber" in line and "received message" in line:
        if line_number-1>0 and "publisher" in file[line_number-1] and "State is" in file[line_number-1]:
            continue
        else:
            print("Логи subscriber запоминаются неверно2")
            flag=False
            break
    elif "publisher" in line and not("id:" in line or "Connecting to broker" in line or "State is" in line):
        print("Логи publisher запоминаются неверно")
        flag=False
        break
if flag:
    print("Все логи запоминаются правильно")
