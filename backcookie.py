#!/usr/bin/env/python
# -*- coding: utf-8 -*-

try:
    import requests
except:
    print "\t\nPlease install requests library, you can do it executing: \n" #
    print "\t\npip install requests" 
from core.backcookie import backcookie
from core.elemets import elements

appShell = Backcookie()
appShell.rootConnection()

if __name__ == "__main__":
    try:
        appShell.main()
    except Exception as error:
        elements.close(elements.color['red'] + "Error: " + elements.color['blue'] + "%s" % error + elements.color['white'])