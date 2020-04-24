#file that contains main function for the printing server
from PrintingService import PrintingService
from PrintOrder import PrintOrder
import time

def main():
    #start printing server
    #start gui
    #on separate threads
    #the 2 modules have to communicate
    print("main")
    global printingService
    printingService = PrintingService()
    #printingOrder = PrintOrder("bla bla", "bla bla")
    #printingService.addOrder(printingOrder)
    #time.sleep(3)
    #printingService.addOrder(printingOrder)

if __name__ == "__main__":
    main()