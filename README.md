# Pretty LOG - plog!

Nice little tool for printing pretty log messages!

Example:

```python
from plog import *

def testfunction():
    plog_color()
    plog("Starting timer.")
    time.sleep(0.2)
    plog("Heres a warning. Handing over to another function.", type=PLOG.warn)
    otherfunction()

def otherfunction():
    plog("I AM ANOTHER FUNCTION!!")
    time.sleep(0.2)
    plog("Stepped on LEGO. Exiting.", type=PLOG.err)




if __name__ == "__main__":
    testfunction()
```

Result:

![screenie](http://i.imgur.com/AEBGglV.png)


Everything is printed to stdout.


### Usage:

------

`plog(message, type=PLOG.info)`


Print a pretty log message. Default type is INFO.

Available types:

* PLOG.info
* PLOG.warn
* PLOG.err


------

`plog_color(use=True)`

Change color setting. 

* True:  Print with colors.
* False: Boring white text.


