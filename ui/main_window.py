# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(719, 537)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(425, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.imageComboLeft = QtWidgets.QComboBox(self.centralwidget)
        self.imageComboLeft.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageComboLeft.sizePolicy().hasHeightForWidth())
        self.imageComboLeft.setSizePolicy(sizePolicy)
        self.imageComboLeft.setObjectName("imageComboLeft")
        self.imageComboLeft.addItem("")
        self.imageComboLeft.addItem("")
        self.imageComboLeft.addItem("")
        self.imageComboLeft.addItem("")
        self.imageComboLeft.addItem("")
        self.imageComboLeft.addItem("")
        self.imageComboLeft.addItem("")
        self.imageComboLeft.addItem("")
        self.imageComboLeft.addItem("")
        self.imageComboLeft.addItem("")
        self.imageComboLeft.addItem("")
        self.imageComboLeft.addItem("")
        self.imageComboLeft.addItem("")
        self.verticalLayout.addWidget(self.imageComboLeft)
        self.imagePreviewLeft = ImageWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imagePreviewLeft.sizePolicy().hasHeightForWidth())
        self.imagePreviewLeft.setSizePolicy(sizePolicy)
        self.imagePreviewLeft.setMinimumSize(QtCore.QSize(0, 0))
        self.imagePreviewLeft.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.imagePreviewLeft.setText("")
        self.imagePreviewLeft.setScaledContents(False)
        self.imagePreviewLeft.setAlignment(QtCore.Qt.AlignCenter)
        self.imagePreviewLeft.setObjectName("imagePreviewLeft")
        self.verticalLayout.addWidget(self.imagePreviewLeft)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.imageComboRight = QtWidgets.QComboBox(self.centralwidget)
        self.imageComboRight.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageComboRight.sizePolicy().hasHeightForWidth())
        self.imageComboRight.setSizePolicy(sizePolicy)
        self.imageComboRight.setObjectName("imageComboRight")
        self.imageComboRight.addItem("")
        self.imageComboRight.addItem("")
        self.imageComboRight.addItem("")
        self.imageComboRight.addItem("")
        self.imageComboRight.addItem("")
        self.imageComboRight.addItem("")
        self.imageComboRight.addItem("")
        self.imageComboRight.addItem("")
        self.imageComboRight.addItem("")
        self.imageComboRight.addItem("")
        self.imageComboRight.addItem("")
        self.imageComboRight.addItem("")
        self.imageComboRight.addItem("")
        self.verticalLayout_2.addWidget(self.imageComboRight)
        self.imagePreviewRight = ImageWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imagePreviewRight.sizePolicy().hasHeightForWidth())
        self.imagePreviewRight.setSizePolicy(sizePolicy)
        self.imagePreviewRight.setMinimumSize(QtCore.QSize(0, 0))
        self.imagePreviewRight.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.imagePreviewRight.setText("")
        self.imagePreviewRight.setScaledContents(False)
        self.imagePreviewRight.setAlignment(QtCore.Qt.AlignCenter)
        self.imagePreviewRight.setObjectName("imagePreviewRight")
        self.verticalLayout_2.addWidget(self.imagePreviewRight)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.algorithmTabs = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.algorithmTabs.sizePolicy().hasHeightForWidth())
        self.algorithmTabs.setSizePolicy(sizePolicy)
        self.algorithmTabs.setObjectName("algorithmTabs")
        self.refAlgorithmTab = QtWidgets.QWidget()
        self.refAlgorithmTab.setObjectName("refAlgorithmTab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.refAlgorithmTab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.sThresholdLabel = QtWidgets.QLabel(self.refAlgorithmTab)
        self.sThresholdLabel.setObjectName("sThresholdLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.sThresholdLabel)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.sThresholdSlider = QtWidgets.QSlider(self.refAlgorithmTab)
        self.sThresholdSlider.setMaximum(256)
        self.sThresholdSlider.setTracking(True)
        self.sThresholdSlider.setOrientation(QtCore.Qt.Horizontal)
        self.sThresholdSlider.setInvertedAppearance(False)
        self.sThresholdSlider.setInvertedControls(False)
        self.sThresholdSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.sThresholdSlider.setObjectName("sThresholdSlider")
        self.horizontalLayout_10.addWidget(self.sThresholdSlider)
        self.sThresholdSpin = QtWidgets.QSpinBox(self.refAlgorithmTab)
        self.sThresholdSpin.setMinimumSize(QtCore.QSize(86, 0))
        self.sThresholdSpin.setWrapping(False)
        self.sThresholdSpin.setFrame(True)
        self.sThresholdSpin.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.sThresholdSpin.setMaximum(256)
        self.sThresholdSpin.setDisplayIntegerBase(10)
        self.sThresholdSpin.setObjectName("sThresholdSpin")
        self.horizontalLayout_10.addWidget(self.sThresholdSpin)
        self.label_4 = QtWidgets.QLabel(self.refAlgorithmTab)
        self.label_4.setMinimumSize(QtCore.QSize(33, 0))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_10.addWidget(self.label_4)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_10)
        self.vThresholdLabel = QtWidgets.QLabel(self.refAlgorithmTab)
        self.vThresholdLabel.setObjectName("vThresholdLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.vThresholdLabel)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.vThresholdSlider = QtWidgets.QSlider(self.refAlgorithmTab)
        self.vThresholdSlider.setMaximum(256)
        self.vThresholdSlider.setTracking(True)
        self.vThresholdSlider.setOrientation(QtCore.Qt.Horizontal)
        self.vThresholdSlider.setInvertedAppearance(False)
        self.vThresholdSlider.setInvertedControls(False)
        self.vThresholdSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.vThresholdSlider.setObjectName("vThresholdSlider")
        self.horizontalLayout_9.addWidget(self.vThresholdSlider)
        self.vThresholdSpin = QtWidgets.QSpinBox(self.refAlgorithmTab)
        self.vThresholdSpin.setMinimumSize(QtCore.QSize(86, 0))
        self.vThresholdSpin.setMaximum(256)
        self.vThresholdSpin.setObjectName("vThresholdSpin")
        self.horizontalLayout_9.addWidget(self.vThresholdSpin)
        self.label_5 = QtWidgets.QLabel(self.refAlgorithmTab)
        self.label_5.setMinimumSize(QtCore.QSize(33, 0))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_9)
        self.refMinSizeLabel = QtWidgets.QLabel(self.refAlgorithmTab)
        self.refMinSizeLabel.setEnabled(True)
        self.refMinSizeLabel.setObjectName("refMinSizeLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.refMinSizeLabel)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.refMinSizeSlider = QtWidgets.QSlider(self.refAlgorithmTab)
        self.refMinSizeSlider.setMaximum(10000)
        self.refMinSizeSlider.setTracking(True)
        self.refMinSizeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.refMinSizeSlider.setInvertedAppearance(False)
        self.refMinSizeSlider.setInvertedControls(False)
        self.refMinSizeSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.refMinSizeSlider.setObjectName("refMinSizeSlider")
        self.horizontalLayout_7.addWidget(self.refMinSizeSlider)
        self.refMinSizeSpin = QtWidgets.QSpinBox(self.refAlgorithmTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refMinSizeSpin.sizePolicy().hasHeightForWidth())
        self.refMinSizeSpin.setSizePolicy(sizePolicy)
        self.refMinSizeSpin.setMinimumSize(QtCore.QSize(86, 0))
        self.refMinSizeSpin.setMaximum(10000)
        self.refMinSizeSpin.setObjectName("refMinSizeSpin")
        self.horizontalLayout_7.addWidget(self.refMinSizeSpin)
        self.label_3 = QtWidgets.QLabel(self.refAlgorithmTab)
        self.label_3.setMinimumSize(QtCore.QSize(33, 0))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.formLayout_2.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_7)
        self.verticalLayout_5.addLayout(self.formLayout_2)
        self.sThresholdInvertCheck = QtWidgets.QCheckBox(self.refAlgorithmTab)
        self.sThresholdInvertCheck.setObjectName("sThresholdInvertCheck")
        self.verticalLayout_5.addWidget(self.sThresholdInvertCheck)
        self.algorithmTabs.addTab(self.refAlgorithmTab, "")
        self.customAlgorithmTab = QtWidgets.QWidget()
        self.customAlgorithmTab.setObjectName("customAlgorithmTab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.customAlgorithmTab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.customMinSizeLabel = QtWidgets.QLabel(self.customAlgorithmTab)
        self.customMinSizeLabel.setEnabled(True)
        self.customMinSizeLabel.setObjectName("customMinSizeLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.customMinSizeLabel)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.customMinSizeSlider = QtWidgets.QSlider(self.customAlgorithmTab)
        self.customMinSizeSlider.setMaximum(10000)
        self.customMinSizeSlider.setProperty("value", 133)
        self.customMinSizeSlider.setSliderPosition(133)
        self.customMinSizeSlider.setTracking(True)
        self.customMinSizeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.customMinSizeSlider.setInvertedAppearance(False)
        self.customMinSizeSlider.setInvertedControls(False)
        self.customMinSizeSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.customMinSizeSlider.setObjectName("customMinSizeSlider")
        self.horizontalLayout_5.addWidget(self.customMinSizeSlider)
        self.customMinSizeSpin = QtWidgets.QSpinBox(self.customAlgorithmTab)
        self.customMinSizeSpin.setMinimumSize(QtCore.QSize(86, 0))
        self.customMinSizeSpin.setMaximum(10000)
        self.customMinSizeSpin.setProperty("value", 133)
        self.customMinSizeSpin.setObjectName("customMinSizeSpin")
        self.horizontalLayout_5.addWidget(self.customMinSizeSpin)
        self.label_2 = QtWidgets.QLabel(self.customAlgorithmTab)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.safeAreaLabel = QtWidgets.QLabel(self.customAlgorithmTab)
        self.safeAreaLabel.setObjectName("safeAreaLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.safeAreaLabel)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.safeAreaSlider = QtWidgets.QSlider(self.customAlgorithmTab)
        self.safeAreaSlider.setMaximum(10000)
        self.safeAreaSlider.setSingleStep(10)
        self.safeAreaSlider.setPageStep(100)
        self.safeAreaSlider.setProperty("value", 2000)
        self.safeAreaSlider.setSliderPosition(2000)
        self.safeAreaSlider.setOrientation(QtCore.Qt.Horizontal)
        self.safeAreaSlider.setObjectName("safeAreaSlider")
        self.horizontalLayout_4.addWidget(self.safeAreaSlider)
        self.safeAreaSpin = QtWidgets.QDoubleSpinBox(self.customAlgorithmTab)
        self.safeAreaSpin.setMinimumSize(QtCore.QSize(86, 0))
        self.safeAreaSpin.setMaximum(100.0)
        self.safeAreaSpin.setProperty("value", 20.0)
        self.safeAreaSpin.setObjectName("safeAreaSpin")
        self.horizontalLayout_4.addWidget(self.safeAreaSpin)
        self.label = QtWidgets.QLabel(self.customAlgorithmTab)
        self.label.setMinimumSize(QtCore.QSize(33, 0))
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.verticalLayout_4.addLayout(self.formLayout)
        self.safeAreaDisplayCheck = QtWidgets.QCheckBox(self.customAlgorithmTab)
        self.safeAreaDisplayCheck.setEnabled(True)
        self.safeAreaDisplayCheck.setObjectName("safeAreaDisplayCheck")
        self.verticalLayout_4.addWidget(self.safeAreaDisplayCheck)
        self.algorithmTabs.addTab(self.customAlgorithmTab, "")
        self.verticalLayout_3.addWidget(self.algorithmTabs)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.formLayout_3 = QtWidgets.QFormLayout(self.frame)
        self.formLayout_3.setObjectName("formLayout_3")
        self.detectedLabel = QtWidgets.QLabel(self.frame)
        self.detectedLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.detectedLabel.setMidLineWidth(0)
        self.detectedLabel.setObjectName("detectedLabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.detectedLabel)
        self.detectedValueLabel = QtWidgets.QLabel(self.frame)
        self.detectedValueLabel.setObjectName("detectedValueLabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.detectedValueLabel)
        self.executionTimeLabel = QtWidgets.QLabel(self.frame)
        self.executionTimeLabel.setObjectName("executionTimeLabel")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.executionTimeLabel)
        self.executionTimeValueLabel = QtWidgets.QLabel(self.frame)
        self.executionTimeValueLabel.setObjectName("executionTimeValueLabel")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.executionTimeValueLabel)
        self.verticalLayout_3.addWidget(self.frame)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.algorithmCombo = QtWidgets.QComboBox(self.centralwidget)
        self.algorithmCombo.setEnabled(False)
        self.algorithmCombo.setObjectName("algorithmCombo")
        self.algorithmCombo.addItem("")
        self.algorithmCombo.addItem("")
        self.horizontalLayout_3.addWidget(self.algorithmCombo)
        self.countButton = QtWidgets.QPushButton(self.centralwidget)
        self.countButton.setEnabled(False)
        self.countButton.setObjectName("countButton")
        self.horizontalLayout_3.addWidget(self.countButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 719, 29))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSaveLeft = QtWidgets.QAction(MainWindow)
        self.actionSaveLeft.setObjectName("actionSaveLeft")
        self.actionSaveRight = QtWidgets.QAction(MainWindow)
        self.actionSaveRight.setObjectName("actionSaveRight")
        self.actionShowHistogramLeft = QtWidgets.QAction(MainWindow)
        self.actionShowHistogramLeft.setObjectName("actionShowHistogramLeft")
        self.actionShowHistogramRight = QtWidgets.QAction(MainWindow)
        self.actionShowHistogramRight.setObjectName("actionShowHistogramRight")
        self.actionShowImageLeft = QtWidgets.QAction(MainWindow)
        self.actionShowImageLeft.setObjectName("actionShowImageLeft")
        self.actionShowImageRight = QtWidgets.QAction(MainWindow)
        self.actionShowImageRight.setObjectName("actionShowImageRight")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.imageComboRight.setCurrentIndex(0)
        self.algorithmTabs.setCurrentIndex(0)
        self.sThresholdSlider.valueChanged['int'].connect(self.sThresholdSpin.setValue) # type: ignore
        self.vThresholdSlider.valueChanged['int'].connect(self.vThresholdSpin.setValue) # type: ignore
        self.sThresholdSpin.valueChanged['int'].connect(self.sThresholdSlider.setValue) # type: ignore
        self.vThresholdSpin.valueChanged['int'].connect(self.vThresholdSlider.setValue) # type: ignore
        self.customMinSizeSlider.valueChanged['int'].connect(self.customMinSizeSpin.setValue) # type: ignore
        self.refMinSizeSlider.valueChanged['int'].connect(self.refMinSizeSpin.setValue) # type: ignore
        self.refMinSizeSpin.valueChanged['int'].connect(self.refMinSizeSlider.setValue) # type: ignore
        self.customMinSizeSpin.valueChanged['int'].connect(self.customMinSizeSlider.setValue) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.imageComboLeft, self.imageComboRight)
        MainWindow.setTabOrder(self.imageComboRight, self.algorithmTabs)
        MainWindow.setTabOrder(self.algorithmTabs, self.sThresholdSlider)
        MainWindow.setTabOrder(self.sThresholdSlider, self.sThresholdSpin)
        MainWindow.setTabOrder(self.sThresholdSpin, self.vThresholdSlider)
        MainWindow.setTabOrder(self.vThresholdSlider, self.vThresholdSpin)
        MainWindow.setTabOrder(self.vThresholdSpin, self.refMinSizeSlider)
        MainWindow.setTabOrder(self.refMinSizeSlider, self.refMinSizeSpin)
        MainWindow.setTabOrder(self.refMinSizeSpin, self.customMinSizeSlider)
        MainWindow.setTabOrder(self.customMinSizeSlider, self.customMinSizeSpin)
        MainWindow.setTabOrder(self.customMinSizeSpin, self.safeAreaSlider)
        MainWindow.setTabOrder(self.safeAreaSlider, self.safeAreaSpin)
        MainWindow.setTabOrder(self.safeAreaSpin, self.algorithmCombo)
        MainWindow.setTabOrder(self.algorithmCombo, self.countButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Zliczanie obiektów"))
        self.imageComboLeft.setItemText(0, _translate("MainWindow", "Oryginalny obraz"))
        self.imageComboLeft.setItemText(1, _translate("MainWindow", "Oryginalny obraz (przestrzeń H)"))
        self.imageComboLeft.setItemText(2, _translate("MainWindow", "Oryginalny obraz (przestrzeń S)"))
        self.imageComboLeft.setItemText(3, _translate("MainWindow", "Oryginalny obraz (przestrzeń V)"))
        self.imageComboLeft.setItemText(4, _translate("MainWindow", "Wstępne przetwarzanie"))
        self.imageComboLeft.setItemText(5, _translate("MainWindow", "Wstępne przetwarzanie (przestrzeń H)"))
        self.imageComboLeft.setItemText(6, _translate("MainWindow", "Wstępne przetwarzanie (przestrzeń S)"))
        self.imageComboLeft.setItemText(7, _translate("MainWindow", "Wstępne przetwarzanie (przestrzeń V)"))
        self.imageComboLeft.setItemText(8, _translate("MainWindow", "Progowanie (przestrzeń H)"))
        self.imageComboLeft.setItemText(9, _translate("MainWindow", "Progowanie (przestrzeń S)"))
        self.imageComboLeft.setItemText(10, _translate("MainWindow", "Progowanie (przestrzeń V)"))
        self.imageComboLeft.setItemText(11, _translate("MainWindow", "Operacje morfologiczne"))
        self.imageComboLeft.setItemText(12, _translate("MainWindow", "Zliczanie"))
        self.imageComboRight.setCurrentText(_translate("MainWindow", "Oryginalny obraz"))
        self.imageComboRight.setItemText(0, _translate("MainWindow", "Oryginalny obraz"))
        self.imageComboRight.setItemText(1, _translate("MainWindow", "Oryginalny obraz (przestrzeń H)"))
        self.imageComboRight.setItemText(2, _translate("MainWindow", "Oryginalny obraz (przestrzeń S)"))
        self.imageComboRight.setItemText(3, _translate("MainWindow", "Oryginalny obraz (przestrzeń V)"))
        self.imageComboRight.setItemText(4, _translate("MainWindow", "Wstępne przetwarzanie"))
        self.imageComboRight.setItemText(5, _translate("MainWindow", "Wstępne przetwarzanie (przestrzeń H)"))
        self.imageComboRight.setItemText(6, _translate("MainWindow", "Wstępne przetwarzanie (przestrzeń S)"))
        self.imageComboRight.setItemText(7, _translate("MainWindow", "Wstępne przetwarzanie (przestrzeń V)"))
        self.imageComboRight.setItemText(8, _translate("MainWindow", "Progowanie (przestrzeń H)"))
        self.imageComboRight.setItemText(9, _translate("MainWindow", "Progowanie (przestrzeń S)"))
        self.imageComboRight.setItemText(10, _translate("MainWindow", "Progowanie (przestrzeń V)"))
        self.imageComboRight.setItemText(11, _translate("MainWindow", "Operacje morfologiczne"))
        self.imageComboRight.setItemText(12, _translate("MainWindow", "Zliczanie"))
        self.sThresholdLabel.setText(_translate("MainWindow", "Próg S"))
        self.vThresholdLabel.setText(_translate("MainWindow", "Próg V"))
        self.refMinSizeLabel.setText(_translate("MainWindow", "Minimalny rozmiar"))
        self.label_3.setText(_translate("MainWindow", "piks"))
        self.sThresholdInvertCheck.setText(_translate("MainWindow", "Odwróć progowanie S"))
        self.algorithmTabs.setTabText(self.algorithmTabs.indexOf(self.refAlgorithmTab), _translate("MainWindow", "Algorytm referencyjny"))
        self.customMinSizeLabel.setText(_translate("MainWindow", "Minimalny rozmiar"))
        self.label_2.setText(_translate("MainWindow", "piks"))
        self.safeAreaLabel.setText(_translate("MainWindow", "Strefa bezpieczna"))
        self.label.setText(_translate("MainWindow", "%"))
        self.safeAreaDisplayCheck.setText(_translate("MainWindow", "Pokaż strefę bezpieczną"))
        self.algorithmTabs.setTabText(self.algorithmTabs.indexOf(self.customAlgorithmTab), _translate("MainWindow", "Algorytm własny"))
        self.detectedLabel.setText(_translate("MainWindow", "Wykryte obiekty:"))
        self.detectedValueLabel.setText(_translate("MainWindow", "-"))
        self.executionTimeLabel.setText(_translate("MainWindow", "Czas wykonywania:"))
        self.executionTimeValueLabel.setText(_translate("MainWindow", "-"))
        self.algorithmCombo.setItemText(0, _translate("MainWindow", "Algorytm referencyjny"))
        self.algorithmCombo.setItemText(1, _translate("MainWindow", "Algorytm własny"))
        self.countButton.setText(_translate("MainWindow", "Zlicz obiekty"))
        self.menuFile.setTitle(_translate("MainWindow", "Plik"))
        self.actionOpen.setText(_translate("MainWindow", "Wczytaj obraz..."))
        self.actionExit.setText(_translate("MainWindow", "Zamknij"))
        self.actionSaveLeft.setText(_translate("MainWindow", "Zapisz..."))
        self.actionSaveLeft.setToolTip(_translate("MainWindow", "Zapisz obraz"))
        self.actionSaveRight.setText(_translate("MainWindow", "Zapisz..."))
        self.actionSaveRight.setToolTip(_translate("MainWindow", "Zapisz obraz"))
        self.actionShowHistogramLeft.setText(_translate("MainWindow", "Histogram"))
        self.actionShowHistogramLeft.setToolTip(_translate("MainWindow", "Wyświetl histogram"))
        self.actionShowHistogramRight.setText(_translate("MainWindow", "Histogram"))
        self.actionShowHistogramRight.setToolTip(_translate("MainWindow", "Wyświetl histogram"))
        self.actionShowImageLeft.setText(_translate("MainWindow", "Podgląd"))
        self.actionShowImageLeft.setToolTip(_translate("MainWindow", "Wyświetl obraz w nowym oknie"))
        self.actionShowImageRight.setText(_translate("MainWindow", "Podgląd"))
        self.actionShowImageRight.setToolTip(_translate("MainWindow", "Wyświetl obraz w nowym oknie"))
from ui.image_widget import ImageWidget
