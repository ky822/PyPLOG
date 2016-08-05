import time, inspect

class PLOG:
    #message types
    plog_info   = "[INFO] "
    plog_warn   = "[WARN] "
    plog_err    = "[ERROR]"

    #10 digits, 3 decimals
    TIME_FORMAT = "%13.3f"

    #use color?
    PLOG_USE_COLOR_PRINT = False

    TIME_COLOR  = u'\033[0;34m'
    INFO_COLOR  = u'\033[0;32m'
    WARN_COLOR  = u'\033[0;33m'
    ERROR_COLOR = u'\033[0;31m'
    COLOR_RESET = u'\033[0m'


#timestamp since start of program
def timestampinit():
    t_start = time.time()
    while True:
        t = time.time() - t_start
        yield "[{fmt}]".format(
                fmt = PLOG.TIME_FORMAT,
            ) % t

PLOG.timestamp_generator = timestampinit()


#get current timestamp
def timestamp():
    return next(PLOG.timestamp_generator)

#set plog coloring
def plog_color(use=True):
    PLOG.PLOG_USE_COLOR_PRINT = use




# Pretty LOG messages
def plog(message, type=PLOG.plog_info):
    #name of caller function
    caller = " [%s]" % inspect.stack()[1][3]

    if PLOG.PLOG_USE_COLOR_PRINT:
        snippet = "{TiCo}{time} {TyCo}{type}{TiCo}{caller}{CoRe} - %s"
        if type is PLOG.plog_err:
            #color message if it's an error.
            snippet = snippet % ("%s{msg}%s" % (PLOG.ERROR_COLOR, PLOG.COLOR_RESET))
            type_color = PLOG.ERROR_COLOR
        else:
            if type is PLOG.plog_warn:
                #color warnings too
                type_color = PLOG.WARN_COLOR
                snippet = snippet % ("%s{msg}%s" % (PLOG.WARN_COLOR, PLOG.COLOR_RESET))
            else:
                type_color = PLOG.INFO_COLOR
                snippet = snippet % "{msg}"

        snippet = snippet.format(
                TiCo = PLOG.TIME_COLOR,
                time = timestamp(),
                CoRe = PLOG.COLOR_RESET,
                TyCo = type_color,
                type = type,
                caller = caller,
                msg = message
            )
    else:
        snippet = "{time} {type}{caller} - {msg}".format(
                time = timestamp(),
                type = type,
                caller = caller,
                msg = message
            )
    print(snippet)




if __name__ == "__main__":
    #start timer. The program /was/ started, after all...
    next(PLOG.timestamp_generator)
