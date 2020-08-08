import threading
import time

waiting = 0
chairs  = 10
customer = threading.Semaphore(0)
barber = threading.Semaphore(0)
mutex = threading.Semaphore(1)

def customer_thread():
    global waiting
    global chairs
    while True:
        mutex.acquire()
        if(waiting < chairs):
            waiting += 1
            customer.release()
            mutex.release()
            barber.acquire()
        else:
            mutex.release()
    time.sleep(1000)
   

def barber_thread():
    
    global waiting
    global chairs
    while True:
        customer.acquire()
        mutex.acquire()
        waiting -= 1
        
        barber.release()
        mutex.release()
        print("barber cutting hair\n")
    time.sleep(1000)
    
def cutomerEntry():

    while True:

        time.sleep(15)

        incomingCustomer = threading.Thread(target=customer_thread)

        incomingCustomer.start()

        print("no of customers waiting: ", waiting)

def barberWork():


    while True:

        time.sleep(15)

        gettingHairCut = threading.Thread(target=barber_thread)

        gettingHairCut.start()
        print("no of customers waiting: ", waiting)
 


cutomerEntryThread = threading.Thread(target=cutomerEntry)

barberWorkThread = threading.Thread(target=barberWork)


cutomerEntryThread.start()
barberWorkThread.start()

