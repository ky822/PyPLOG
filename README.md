# Pretty LOG - plog!

Nice little tool for printing pretty log messages!

Example:

```python
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
```

Result:

![screenie](http://i.imgur.com/AEBGglV.png)


Everything is printed to stdout.


### Usage:

------

`plog(message, type=PLOG.plog_info)`

Print a pretty log message. Default type is INFO.

Available types:

* PLOG.plog_info
* PLOG.plog_warn
* PLOG.plog_err


------

`plog_color(use=True)`

Change color setting. 

* True:  Print with colors.
* False: Boring white text.


