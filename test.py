from plog import *

def testfunction():
    plog("Starting timer.")
    time.sleep(0.2)
    plog("Heres a warning. Handing over to another function.", type=PLOG.warn)
    otherfunction()

def otherfunction():
    plog("I AM ANOTHER FUNCTION!!")
    time.sleep(0.2)
    plog("Stepped on LEGO. Exiting.", type=PLOG.err)




if __name__ == "__main__":
    plog_color()
    testfunction()
