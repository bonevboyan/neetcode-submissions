import math

class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        try:
            resultingArr = self.map[key]
        except:
            resultingArr = []
            self.map[key] = resultingArr

        self.map[key].append({ 'value': value, 'timestamp': timestamp })
        

    def get(self, key: str, timestamp: int) -> str:
        try:
            resultingArr = self.map[key]
        except:
            return ''

        length = len(resultingArr)

        if length == 0:
            return ''

        lo = 0
        hi = length - 1
        currentValue = ''


        while lo <= hi:
            assumedIndex = math.floor((lo + hi) / 2)
            currTimestamp = resultingArr[assumedIndex]['timestamp']

            if currTimestamp > timestamp:
                hi = assumedIndex - 1
            else:
                currentValue = resultingArr[assumedIndex]['value']
                lo = assumedIndex + 1

            

        return currentValue

        
