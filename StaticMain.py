import os

class StaticMain:
    def getLatestFile(dir):
        return sorted(os.listdir(dir)).pop()