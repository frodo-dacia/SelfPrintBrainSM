import random

class Order:
    def __init__(self):
        self.ID = random.randrange(999999,9999999)

class ScanOrder(Order):
    def __init__(self, scanner, destination):
        Order.__init__(self)
        self._scanner = scanner
        self._destination = destination

    def Execute(self):
        #to be implemented
        print("execute ",self.ID)
        pass
    

class PrintOrder(Order):
    def __init__(self, filesToPrint, selectedPrinter):
        Order.__init__(self)
        self._files = filesToPrint
        self._printer = selectedPrinter

    def Execute(self):
        #to be implemented
        print("execute ",self.ID)
        pass
