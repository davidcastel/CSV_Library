# Imports
import csv
import os
import sys
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt


class CSVLibrary():
    # *** Constructor ***
    def __init__(self, file, seperator):
        self.__file = file
        self.__seperator = seperator
        self.__dic = {}
        self.__table = None
        # Register custom dialect
        csv.register_dialect('customDialect', delimiter=seperator)

    # *** Getters ***
    def getFileName(self):
        return self.__file

    def getSeperator(self):
        return self.__seperator

    def getDict(self):
        return self.__dic

    def getTable(self):
        return self.__table

    # *** Setters ***
    def setFileName(self, newFileName):
        self.__file = newFileName

    def setSeperator(self, newSeperator):
        self.__seperator = newSeperator

    def setTable(self, newTable):
        self.__table = newTable

    def setDict(self, newDict):
        self.__dic = newDict

    # *** Actions ***
    # Method : readFile
    # PURPOSE: Read the CSVfile using csv.reader and calling method '__populateHash'
    # AUHTOR: David
    def readFile(self):
        # Open file and read the file
        input_file = open(self.getFileName(), 'r')
        with input_file:
            csvReader = csv.reader(input_file, dialect='customDialect')
            self.__populateHash(csvReader)
            input_file.close()

    # METHOD : command
    # PARAMETERS: {string:command, int:x, int: y, string:newElement, int:row, int:column}
    # PURPOSE: Determine what the program should according to the command by the user
    # -> At the end, create and show a table according to the inputed CSV file
    # AUTHOR: David
    def command(self, command, x=0, y=0, newElement="", row=0, column=0):
        self.readFile()

        if self.__is_command_edit(command):
            self.__editTable(x, y, newElement)
        elif self.__is_command_see(command):
            self.__seePartOfTable(row, column)

        self.__createTable()

    # *** 'Private' methods ***
    # METHOD : __createTable
    # PURPOSE: Calls the class 'CreateTable'
    # AUTHOR: David
    def __createTable(self):
        table = self.getTable()
        table = CreateTable(self.__file, self.__seperator, self.__dic)
        table.create()
        self.setTable(table)

    # METHOD : __editTable
    # PARAMETERS: {int: x, int:y, string:element}
    # PURPOSE: Calls the class 'EditDictionary'
    # AUTHOR: David
    def __editTable(self, x, y, element):
        dic = self.getDict()
        newDict = EditDictionary(self.__file, self.__seperator, self.__dic, x, y, element)
        newDict.editAElement()
        dic = newDict.getLocalDic()
        self.setDict(dic)

    # METHOD : __seePartOfTable
    # PARAMETERS: {int: row, int: column}
    # PURPOSE: Calls the class 'SeeSpecificElements'
    # AUTHOR: David
    def __seePartOfTable(self, row, column):
        dic = self.getDict()
        newDict = SeeSpecificElements(self.__file, self.__seperator, self.__dic, row, column)
        newDict.see()

    # METHOD : __populateHash
    # PARAMETERS: {string: csvFile}
    # PURPOSE: Read through the CSVfile to save the element into a list within a dictionary according to the registered dialect
    # AUTHOR: David
    def __populateHash(self, csvFile):
        i = 1
        # Iterate through rows
        for row in csvFile:
            self.getDict()[i] = row
            i += 1

    # *** Boolean functions ***
    def __is_command_edit(self, command):
        return command == 'edit'

    def __is_command_see(self, command):
        return command == 'see'


class CreateTable(CSVLibrary):
    # *** Constructor ***
    def __init__(self, file, seperator, dic):
        super().__init__(file, seperator)
        self.__fig = None
        self.__dic = dic

    # *** Getter ***
    def getLocalDict(self):
        return self.__dic

    # *** Action ***
    # METHOD: create
    # PURPOSE: Create table by implementing Matplotlib table by using the information from dictionary
    # AUTHOR: David
    def create(self):
        np.random.seed(0)

        fig, ax = plt.subplots()
        table_data = list(self.getLocalDict().values())

        table = ax.table(cellText=table_data, loc='center')
        table.set_fontsize(14)
        table.scale(1, 4)
        ax.axis('off')

        plt.show()


class EditDictionary(CSVLibrary):
    # *** Constructor ***
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

    # *** Modifier ***
    def setDict(self, newDict):
        self.__dict = newDict

    # *** Action ***
    # METHOD: editAElement
    # PURPOSE: Figure out the position of the element that the user wants to change and change that specific element
    # AUTHOR: David
    def editAElement(self):
        temp = self.getLocalDic()
        get_list = temp.get(self.getY())
        get_list[self.getX() - 1] = self.getNewElement()
        temp[self.getY()] = get_list
        self.setDict(temp)


class SeeSpecificElements(CSVLibrary):
    # *** Constructor
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

    # *** Setters ***
    def setDict(self, newDict):
        self.__dic = newDict

    # *** Action ***
    # METHOD : see
    # PURPOSE: Use conditions to determine what method to call to show the table according to how the user wants to see
    # AUTHOR: David
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

    # *** Private Methods ***
    # METHOD: __iterateOnlyRow
    # PARAMETERS: {dict: temp_dict}
    # PURPOSE: If the row is not the row set by the user, clear the row
    # AUHTOR: David
    def __iterateOnlyRow(self, temp_dict):
        temp_row = self.getRow()

        for key in temp_dict:
            if self.__key_does_not_equal_row(key, temp_row):
                temp_dict[key] = ""

    # METHOD: __iterateOnlyCol
    # PARAMETERS: {dict: temp_dict}
    # PURPOSE: If the column is not the column set by the user, clear the column
    # AUTHOR: David
    def __iterateOnlyCol(self, temp_dict):
        temp_col = self.getCol() - 1

        for key in temp_dict:
            temp_list = temp_dict[key]
            for i in range(0, len(temp_list)):
                if self.__i_is_not_equal_col(i, temp_col):
                    temp_list[i] = ""

    # METHOD: __iterateRowAndCol
    # PARAMETERS: {dict: temp_dict}
    # PURPOSE: If the Row or the Column is not set by the user, clear the elements
    # AUTHOR: David
    def __iterateRowAndCol(self, temp_dict):
        temp_row = self.getRow()
        temp_col = self.getCol() - 1

        for key in temp_dict:
            temp_list = temp_dict[key]
            for i in range(0, len(temp_list)):
                if i != temp_col and self.__key_does_not_equal_row(key, temp_row):
                    temp_list[i] = ""

    # *** Boolean Methods ***
    def __is_row_and_col_0(self):
        return self.getRow() == 0 and self.getCol() == 0

    def __is_column_only_0(self):
        return self.getRow() != 0 and self.getCol() == 0

    def __is_row_only_0(self):
        return self.getRow() == 0 and self.getCol() != 0

    def __key_does_not_equal_row(self, key, row):
        return key != row

    def __i_is_not_equal_col(self, i, col):
        return i != col


if __name__ == '__main__':
    file = CSVLibrary('test.csv', '|')
    file.command('create', 0, 0, None, 0, 0)
