import plog.plog as plg
PLOG = plg.PLOG
plog_color = plg.plog_color
plog = plg.plog

def perr(*msg, delim=" "):
    plog(*msg, type=PLOG.err, delim=delim)

def pwrn(*msg, delim=" "):
    plog(*msg, type=PLOG.warn, delim=delim)

__all__ = ["PLOG", "plog_color", "plog", "perr", "pwrn"]
