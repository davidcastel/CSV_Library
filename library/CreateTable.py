import numpy as np
import matplotlib.pyplot as plt
from CSVLibrary import *


class CreateTable(CSVLibrary):
    def __init__(self, file, seperator, dic):
        super().__init__(file, seperator)
        self.__fig = None
        self.__dic = dic

    # *** Getters ***
    def getFigure(self):
        return self.__fig

    def getLocalDict(self):
        return self.__dic

    # *** Setters ***
    def setFigure(self, newFig):
        self.__fig = newFig

    # *** Create and show table ***
    def createTable(self):
        np.random.seed(0)

        fig, ax = plt.subplots()

        table_data = list(self.getLocalDict().values())

        table = ax.table(cellText=table_data, loc='center')
        table.set_fontsize(14)
        table.scale(1, 4)
        ax.axis('off')

        plt.show()
