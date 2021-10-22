import threading
import time
import queue
from threading import Thread, Lock
mutex = Lock()

class TenedorFilosofo(threading.Thread):
    def __init__(self, tenedores, filosofosNum):
        threading.Thread.__init__(self)
        self.tenedores = tenedores
        self.filosofosNum = filosofosNum
        #self.datoTemporal = self.filosofosNum + 1 % 5 --
   
    def iniciar(self):
        mutex.acquire()
        print("Filosofo iniciando", self.filosofosNum)
        time.sleep(2)
        print("Filosofo ", self.filosofosNum, "recoge tenedor del lado izquierdo")
        self.tenedores[self.filosofosNum]
        time.sleep(2)
        print("Filosofo ", self.filosofosNum, "recoge tenedor del lado derecho")
        #self.tenedores[self.datoTemporal]
        self.tenedores[self.filosofosNum]
        time.sleep(2)
    
    def terminar(self):
        #mutex.acquire()
        print("Filosofo ", self.filosofosNum, "libre izquierdo")
        self.tenedores[self.filosofosNum]
        time.sleep(2)
        print("Filosofo ", self.filosofosNum, "libre derecho")
        #self.tenedores[self.datoTemporal]
        self.tenedores[self.filosofosNum]
        time.sleep(2)
        mutex.release()

    def run(self):
        self.iniciar()
        self.terminar()


tenedorArray = [1,1,1,1,1]

for i in range(0,5):
    #print("for uno: ", i)
    tenedorArray[i] = threading.BoundedSemaphore(1)

for i in range(0,5):
    #print("for dos: ", i)
    total = TenedorFilosofo(tenedorArray, i)
    total.start()