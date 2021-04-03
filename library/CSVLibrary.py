# Imports
import csv
import os
import sys
import pathlib
import plotly.graph_objects as go
import PySimpleGUI as sg


import CreateTable
import SeeSpecificElements
import EditDictionary


class CSVLibrary:
    # Constructor
    def __init__(self, file, seperator):
        self.__file = file
        self.__seperator = seperator
        self.__dic = {}
        self.__table = None
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
    # Method to read the file
    def readFile(self):
        # Open file
        input_file = open(self.getFileName())
        # Register custom dialect according to how user wants
        with input_file:
            csvReader = csv.reader(input_file, dialect='customDialect')
            self.__populateHash(csvReader)
            input_file.close()

    # Method that reads the Command input by the user (Edit/ get specific elements)
    def command(self, command, x=0, y=0, newElement="", row=0, column=0):
        self.readFile()

        if self.__is_command_edit(command):
            self.__editTable(x, y, newElement)
        elif self.__is_command_see(command):
            self.__seePartOfTable(row, column)

        print(self.getDict())

        self.__createTable()

    # *** Private methods ***
    # Private method to create table

    def __createTable(self):
        table = self.getTable()
        table = CreateTable(self.__file, self.__seperator, self.__dic)
        table.createTable()
        table.getFigure()
        self.setTable(table)

    # Private method to edit the dictionary
    def __editTable(self, x, y, element):
        dic = self.getDict()
        newDict = EditDictionary(
            self.__file, self.__seperator, self.__dic, x, y, element)
        newDict.editAElement()
        dic = newDict.getLocalDic()
        self.setDict(dic)

    def __seePartOfTable(self, row, column):
        dic = self.getDict()
        newDict = SeeSpecificElements(
            self.__file, self.__seperator, self.__dic, row, column)
        newDict.see()

    # Method to populate dictionary to create table
    def __populateHash(self, csvFile):
        i = 1
        # Iterate through rows
        for row in csvFile:
            self.getDict()[i] = row
            i += 1

    def __is_command_edit(self, command):
        return command == 'edit'

    def __is_command_see(self, command):
        return command == 'see'
