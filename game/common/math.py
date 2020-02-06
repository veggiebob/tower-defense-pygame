#Returns a point
class Point():
    def __init__(self, _posX, _posY):
        self.posX, self.posY = _posX, _posY

    def getX(self):
        return self.posX

    def getY(self):
        return self.posY