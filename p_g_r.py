#!/usr/bin/env python

"""
This file serves to return a DaVinci Resolve object
"""

import sys
def GetResolve():
        import dvR as bmd
        return bmd.scriptapp("Resolve")
