import threading, time

print("start program")

def take_a_nap():
    time.sleep(5)
    print("wake up")

threadObj = threading.Thread(target=take_a_nap)
threadObj.start()

print("end program")
# multi threading:
# start program
# end program
# wake up

