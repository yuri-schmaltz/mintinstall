#!/usr/bin/python3

import os
import time

from gi.repository import Gio

def _debug_enabled() -> bool:
    value = os.getenv("DEBUG", "")
    return value.lower() in ("1", "true", "yes", "on")


DEBUG_MODE = _debug_enabled()

# Used as a decorator to time functions
def print_timing(func):
    if not DEBUG_MODE:
        return func
    else:
        def wrapper(*args, **kwargs):
            t1 = time.time()
            res = func(*args, **kwargs)
            t2 = time.time()
            print('%s took %0.3f ms' % (func.__qualname__, (t2 - t1) * 1000.0))
            return res
        return wrapper

def debug(message):
    if not DEBUG_MODE:
        return
    print("Mintinstall (DEBUG): %s" % message)

def networking_available():
    nm = Gio.NetworkMonitor.get_default()
    return nm.get_connectivity() == Gio.NetworkConnectivity.FULL
