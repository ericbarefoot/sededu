import sys, os
import numpy as np
import json
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

import sededu.utilities as utls


class NavigationPageWidget(QWidget):
    # class for navigation button page
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setLayout(QGridLayout())

        mainList = self.parent().categoryList
        
        nList = len(mainList)
        gridSize = [3, 2]
        # xPos = np.tile( range(gridSize[1]), (1, int(np.ceil(nList/gridSize[1]))) )
        cPos = [0, 1, 0, 1, 0, 1]
        rPos = [0, 0, 1, 1, 2, 2] # this needs to be figured out how to make in numpy...
        navLayout = QGridLayout()
        for i in range(nList):
            iButton = self._NavigationCategoryButtonWidget(mainList[i], self.parent().thisPath)
            iButton.clicked.connect(lambda x, i=i: self.parent().parent().parent().navToCategory(i+2))
            self.layout().addWidget(iButton, rPos[i], cPos[i])


    class _NavigationCategoryButtonWidget(QPushButton):
        # the navigation buttons
        def __init__(self, category, thisPath, parent=None):
            QPushButton.__init__(self, parent)

            iPath = os.path.join(thisPath, 'sededu', 'private', \
                utls.category2path(category) + '.png')
            iIcon = QtGui.QIcon()
            iIcon.addPixmap(QtGui.QPixmap(iPath))
            self.setIcon(iIcon)
            self.setIconSize(QtCore.QSize(300, 200))
            self.setSizePolicy(QSizePolicy(
                               QSizePolicy.Maximum,
                               QSizePolicy.Maximum))