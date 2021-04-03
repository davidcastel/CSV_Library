from CSVLibrary import *


class SeeSpecificElements(CSVLibrary):
    def __init__(self, file, seperator, dic, row=0, column=0):
        super().__init__(file, seperator)
        self.__dic = dic
        self.__row = row
        self.__col = column

    # *** Getters ***
    def getRow(self):
        return self.__row

    def getCol(self):
        return self.__col

    def getLocalDict(self):
        return self.__dic

    def setDict(self, newDict):
        self.__dic = newDict

    # *** Actions ***
    def see(self):
        temp_dict = self.getLocalDict()

        if self.__is_row_and_col_0():
            self.getLocalDict()
        elif self.__is_column_only_0():
            self.__iterateOnlyRow(temp_dict)
        elif self.__is_row_only_0():
            self.__iterateOnlyCol(temp_dict)
        else:
            self.__iterateRowAndCol(temp_dict)

    # Private Methods
    def __iterateOnlyRow(self, temp_dict):
        temp_row = self.getRow()

        for key in temp_dict:
            if key != temp_row:
                temp_dict[key] = ""

    def __iterateOnlyCol(self, temp_dict):
        temp_col = self.getCol() - 1

        for key in temp_dict:
            temp_list = temp_dict[key]
            for i in range(0, len(temp_list)):
                if i != temp_col:
                    temp_list[i] = ""

    def __iterateRowAndCol(self, temp_dict):
        temp_row = self.getRow()
        temp_col = self.getCol() - 1

        for key in temp_dict:
            temp_list = temp_dict[key]
            for i in range(0, len(temp_list)):
                if i != temp_col and key != temp_row:
                    temp_list[i] = ""

    def __is_row_and_col_0(self):
        return self.getRow() == 0 and self.getCol() == 0

    def __is_column_only_0(self):
        return self.getRow() != 0 and self.getCol() == 0

    def __is_row_only_0(self):
        return self.getRow() == 0 and self.getCol() != 0
