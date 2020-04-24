import threading

class PrintingService:
    _printQueue = []

    def worker(self):
        waiting = False
        while(1):
            if(len(self._printQueue)>0):
                self._printQueue.pop(0).Execute()
                waiting = False
            else:
                if(waiting == False):
                    print("Waiting jobs")
                    waiting = True

    def __init__(self):
        t = threading.Thread(target=self.worker)
        t.start()
        print("PrintingService Constructor")

    def addOrder(self, order):
        self._printQueue.append(order)

    
