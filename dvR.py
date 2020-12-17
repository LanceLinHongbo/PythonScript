import sys
import imp
import os
script_module = None
script_module = imp.load_dynamic("fusionscript",  "C:\\Program Files\\Blackmagic Design\\DaVinci Resolve\\fusionscript.dll" )
sys.modules[__name__] = script_module

