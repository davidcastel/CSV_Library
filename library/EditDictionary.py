from CSVLibrary import *


class EditDictionary(CSVLibrary):
    def __init__(self, file, seperator, dic, x, y, newElement):
        super().__init__(file, seperator)
        self.__dict = dic
        self.__x = x
        self.__y = y
        self.__newElement = newElement

    # *** Getters ***
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getNewElement(self):
        return self.__newElement

    def getLocalDic(self):
        return self.__dict

    # *** Setter ***
    def setDict(self, newDict):
        self.__dict = newDict

    # *** Modifier ***
    def editAElement(self):
        temp = self.getLocalDic()
        get_list = temp.get(self.getY())
        get_list[self.getX() - 1] = self.getNewElement()
        temp[self.getY()] = get_list
        self.setDict(temp)
