import requests


class Api(object):
    def __init__(self, size):
        self.size = size

    def request(self):
        try:
            self.resp = requests.get('http://www.cs.utep.edu/cheon/ws/sudoku/new/?level=1&size=' + str(self.size))
            if self.resp.status_code == 200:
                return self.stringBoard(self.size, self.resp)
        except Exception:
            return "Ups! Server not respond."

    def stringBoard(self, size, resp):
        jsonData = self.resp.json()['squares']
        self.respBoard = ""
        index = 0
        for i in range(int(self.size)**2):
            if i == (jsonData[index]['x']*int(self.size) + jsonData[index]['y']):
                self.respBoard += str(jsonData[index]['value'])
                if index < (len(jsonData)-1):
                    index += 1
            else:
                self.respBoard += "■"
        return self.respBoard
