import os 
import sys
import socket 
import time

class elements:
    def __init__(self):
        # data general of author
        self.name = "Backcookie"
        self.description = "Small backdoor using cookie."
        self.authorName = "krishpranav"
        self.authorNick = "hacker"
        self.authorTwitter = "@krishpranav5"
        self.version = "1.0.2"
        # data of tool
        self.userAgentName = "User-Agent"
        self.userAgentValue = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"
        self.encode = "base64"
        self.cookie = "Cookie"


    # All color for design terminal UI
    color = {
      "purple": "\033[95m",
      "purpleBold": "\033[01;95m",
      "cyan": "\033[36m",
      "cyanBold": "\033[01;36m",
      "blue": "\033[94m",
      "blueBold": "\033[01;34m",
      "red": "\033[91m", 
      "redBold": "\033[01;31m",
      "green": "\033[92m", 
      "greenBold": "\033[01;32m",
      "white": "\033[0m", 
      "whiteBold": "\033[01;37m",
      "yellow": "\033[93m",
      "yellowBold": "\033[01;33m"
    }

    @staticmethod
    def go(value):
        print value
    
    @staticmethod
    def close(value):
        sys.exit(value)
    
    @staticmethod
    def goip(valueIP):
        try:
            Iphost = socket.gethostbyname(valueIP)
        except socket.gaierror:
            Iphost = "None"
        
        return Iphost

    
    @staticmethod
    def niceShell(text, state):
        matches = [i for i in commands if i.startswith(text)]
        if state < len(matches):
            return matches[state]
        else:
            return None

    @staticmethod
    def checkOS():
        if "linux" in sys.platform:
            os.system("clear")
            elements.go("Loading" + " " + elements.color["red"] + "backcookie" + elements.color["white"] + "...")
            time.sleep(0.2)
            pass
        elif "win" in sys.platform:
            os.system("cls")
            elements.go("Currently there is no support for windows")
        else:
            pass
        
        