from plog import *

def testfunction():
    plog_color()
    plog("Starting timer.")
    time.sleep(0.2)
    plog("Heres a warning. Handing over to another function.", type=PLOG.plog_warn)
    otherfunction()

def otherfunction():
    plog("I AM ANOTHER FUNCTION!!")
    time.sleep(0.2)
    plog("Stepped on LEGO. Exiting.", type=PLOG.plog_err)




if __name__ == "__main__":
    testfunction()
