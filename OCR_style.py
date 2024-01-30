# Form implementation generated from reading ui file 'OCR_style.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_OCR_Window(object):
    def setupUi(self, OCR_Window):
        OCR_Window.setObjectName("OCR_Window")
        OCR_Window.setEnabled(True)
        OCR_Window.resize(697, 452)
        OCR_Window.setMaximumSize(QtCore.QSize(864, 1000))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        OCR_Window.setFont(font)
        OCR_Window.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        OCR_Window.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(parent=OCR_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.OCRResultTextEdit = betterSelectionQPlainTextEdit(parent=self.centralwidget)
        self.OCRResultTextEdit.setGeometry(QtCore.QRect(10, 50, 571, 71))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setKerning(True)
        self.OCRResultTextEdit.setFont(font)
        self.OCRResultTextEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.OCRResultTextEdit.setPlainText("")
        self.OCRResultTextEdit.setObjectName("OCRResultTextEdit")
        self.TransResult_0 = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.TransResult_0.setGeometry(QtCore.QRect(10, 160, 571, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.TransResult_0.setFont(font)
        self.TransResult_0.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.TransResult_0.setAutoFillBackground(False)
        self.TransResult_0.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextSelectableByKeyboard|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.TransResult_0.setObjectName("TransResult_0")
        self.TransResult_1 = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.TransResult_1.setGeometry(QtCore.QRect(10, 230, 571, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.TransResult_1.setFont(font)
        self.TransResult_1.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextSelectableByKeyboard|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.TransResult_1.setObjectName("TransResult_1")
        self.ChooseAreaButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ChooseAreaButton.setGeometry(QtCore.QRect(380, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.ChooseAreaButton.setFont(font)
        self.ChooseAreaButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ChooseAreaButton.setStatusTip("")
        self.ChooseAreaButton.setWhatsThis("")
        self.ChooseAreaButton.setAccessibleDescription("")
        self.ChooseAreaButton.setObjectName("ChooseAreaButton")
        self.ChosenTitleTitle = QtWidgets.QLabel(parent=self.centralwidget)
        self.ChosenTitleTitle.setGeometry(QtCore.QRect(520, 10, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(8)
        self.ChosenTitleTitle.setFont(font)
        self.ChosenTitleTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ChosenTitleTitle.setObjectName("ChosenTitleTitle")
        self.PosText = QtWidgets.QLabel(parent=self.centralwidget)
        self.PosText.setGeometry(QtCore.QRect(470, 20, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(8)
        font.setKerning(True)
        self.PosText.setFont(font)
        self.PosText.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.PosText.setObjectName("PosText")
        self.OCRButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.OCRButton.setGeometry(QtCore.QRect(10, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.OCRButton.setFont(font)
        self.OCRButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.OCRButton.setObjectName("OCRButton")
        self.splitTextEdit = betterSelectionQPlainTextEdit(parent=self.centralwidget)
        self.splitTextEdit.setGeometry(QtCore.QRect(10, 120, 571, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setKerning(False)
        self.splitTextEdit.setFont(font)
        self.splitTextEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.splitTextEdit.setObjectName("splitTextEdit")
        self.SplitChooseBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.SplitChooseBox.setGeometry(QtCore.QRect(590, 140, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.SplitChooseBox.setFont(font)
        self.SplitChooseBox.setObjectName("SplitChooseBox")
        self.SplitChooseBox.addItem("")
        self.SplitChooseBox.addItem("")
        self.SplitChooseBox.addItem("")
        self.SplitChooseTitle = QtWidgets.QLabel(parent=self.centralwidget)
        self.SplitChooseTitle.setGeometry(QtCore.QRect(600, 120, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.SplitChooseTitle.setFont(font)
        self.SplitChooseTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.SplitChooseTitle.setObjectName("SplitChooseTitle")
        self.ShortcutKeyTitle = QtWidgets.QLabel(parent=self.centralwidget)
        self.ShortcutKeyTitle.setGeometry(QtCore.QRect(210, 10, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(8)
        self.ShortcutKeyTitle.setFont(font)
        self.ShortcutKeyTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ShortcutKeyTitle.setObjectName("ShortcutKeyTitle")
        self.ShortcutKeyText = QtWidgets.QLabel(parent=self.centralwidget)
        self.ShortcutKeyText.setGeometry(QtCore.QRect(220, 20, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(8)
        font.setUnderline(True)
        self.ShortcutKeyText.setFont(font)
        self.ShortcutKeyText.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ShortcutKeyText.setObjectName("ShortcutKeyText")
        self.TransResult_2 = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.TransResult_2.setGeometry(QtCore.QRect(10, 300, 571, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.TransResult_2.setFont(font)
        self.TransResult_2.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextSelectableByKeyboard|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.TransResult_2.setObjectName("TransResult_2")
        self.TransResult_3 = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.TransResult_3.setGeometry(QtCore.QRect(10, 370, 571, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.TransResult_3.setFont(font)
        self.TransResult_3.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextSelectableByKeyboard|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.TransResult_3.setObjectName("TransResult_3")
        self.OCRButtonPlus = QtWidgets.QPushButton(parent=self.centralwidget)
        self.OCRButtonPlus.setGeometry(QtCore.QRect(110, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.OCRButtonPlus.setFont(font)
        self.OCRButtonPlus.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.OCRButtonPlus.setObjectName("OCRButtonPlus")
        self.showDictWindowButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.showDictWindowButton.setGeometry(QtCore.QRect(590, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.showDictWindowButton.setFont(font)
        self.showDictWindowButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.showDictWindowButton.setObjectName("showDictWindowButton")
        self.autoDictCheckBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.autoDictCheckBox.setGeometry(QtCore.QRect(590, 80, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.autoDictCheckBox.setFont(font)
        self.autoDictCheckBox.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.autoDictCheckBox.setObjectName("autoDictCheckBox")
        self.autoTransCheckBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.autoTransCheckBox.setGeometry(QtCore.QRect(590, 210, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.autoTransCheckBox.setFont(font)
        self.autoTransCheckBox.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.autoTransCheckBox.setChecked(True)
        self.autoTransCheckBox.setObjectName("autoTransCheckBox")
        self.doTransButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.doTransButton.setGeometry(QtCore.QRect(590, 180, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.doTransButton.setFont(font)
        self.doTransButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.doTransButton.setObjectName("doTransButton")
        self.changeHotKeyButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.changeHotKeyButton.setGeometry(QtCore.QRect(340, 20, 21, 21))
        self.changeHotKeyButton.setObjectName("changeHotKeyButton")
        self.doTransButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.doTransButton_2.setGeometry(QtCore.QRect(590, 260, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.doTransButton_2.setFont(font)
        self.doTransButton_2.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.doTransButton_2.setObjectName("doTransButton_2")
        self.replaceListWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.replaceListWidget.setGeometry(QtCore.QRect(550, 50, 30, 70))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        self.replaceListWidget.setFont(font)
        self.replaceListWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.replaceListWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.replaceListWidget.setAutoScrollMargin(16)
        self.replaceListWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.DoubleClicked)
        self.replaceListWidget.setProperty("showDropIndicator", False)
        self.replaceListWidget.setTextElideMode(QtCore.Qt.TextElideMode.ElideMiddle)
        self.replaceListWidget.setObjectName("replaceListWidget")
        self.changeHotKeyButton.raise_()
        self.ShortcutKeyText.raise_()
        self.OCRResultTextEdit.raise_()
        self.TransResult_0.raise_()
        self.TransResult_1.raise_()
        self.ChooseAreaButton.raise_()
        self.ChosenTitleTitle.raise_()
        self.PosText.raise_()
        self.splitTextEdit.raise_()
        self.SplitChooseBox.raise_()
        self.SplitChooseTitle.raise_()
        self.ShortcutKeyTitle.raise_()
        self.OCRButton.raise_()
        self.TransResult_2.raise_()
        self.TransResult_3.raise_()
        self.OCRButtonPlus.raise_()
        self.showDictWindowButton.raise_()
        self.autoDictCheckBox.raise_()
        self.autoTransCheckBox.raise_()
        self.doTransButton.raise_()
        self.doTransButton_2.raise_()
        self.replaceListWidget.raise_()
        OCR_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(OCR_Window)
        self.ChooseAreaButton.clicked.connect(OCR_Window.getScreenPos) # type: ignore
        self.OCRButton.clicked.connect(OCR_Window.getOCRText) # type: ignore
        OCR_Window.ocrHotkeyPressed.connect(OCR_Window.getOCRText) # type: ignore
        self.SplitChooseBox.currentTextChanged['QString'].connect(OCR_Window.updateSplitMode) # type: ignore
        self.OCRButtonPlus.clicked.connect(OCR_Window.appendOCRText) # type: ignore
        self.showDictWindowButton.clicked.connect(OCR_Window.showDictWindow) # type: ignore
        self.OCRResultTextEdit.selectedFinish.connect(OCR_Window.updateSelectionText) # type: ignore
        self.splitTextEdit.selectedFinish.connect(OCR_Window.updateSelectionText) # type: ignore
        self.OCRResultTextEdit.focusOut.connect(self.OCRResultTextEdit.clearSelection) # type: ignore
        self.splitTextEdit.focusOut.connect(self.splitTextEdit.clearSelection) # type: ignore
        self.autoDictCheckBox.clicked['bool'].connect(OCR_Window.updateAutoDictBool) # type: ignore
        self.autoTransCheckBox.clicked['bool'].connect(OCR_Window.updateAutoTransBool) # type: ignore
        self.doTransButton.clicked.connect(OCR_Window.updateResults) # type: ignore
        self.OCRResultTextEdit.textChanged.connect(OCR_Window.updateSplitTextEdit) # type: ignore
        self.OCRResultTextEdit.textChanged.connect(OCR_Window.updateOCRText) # type: ignore
        self.changeHotKeyButton.clicked.connect(OCR_Window.getIntoHotKeyChangeMode) # type: ignore
        self.doTransButton_2.clicked.connect(OCR_Window.showConfig) # type: ignore
        self.OCRResultTextEdit.callContextMenu.connect(OCR_Window.showReplaceListWidget) # type: ignore
        self.OCRResultTextEdit.focusOut.connect(OCR_Window.hideReplaceListWidget) # type: ignore
        self.replaceListWidget.clicked['QModelIndex'].connect(OCR_Window.replaceKana) # type: ignore
        OCR_Window.ocrConcatHotkeyPressed.connect(OCR_Window.appendOCRText) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(OCR_Window)
        OCR_Window.setTabOrder(self.TransResult_0, self.ChooseAreaButton)
        OCR_Window.setTabOrder(self.ChooseAreaButton, self.OCRButton)
        OCR_Window.setTabOrder(self.OCRButton, self.OCRButtonPlus)
        OCR_Window.setTabOrder(self.OCRButtonPlus, self.showDictWindowButton)
        OCR_Window.setTabOrder(self.showDictWindowButton, self.autoDictCheckBox)
        OCR_Window.setTabOrder(self.autoDictCheckBox, self.autoTransCheckBox)
        OCR_Window.setTabOrder(self.autoTransCheckBox, self.doTransButton)
        OCR_Window.setTabOrder(self.doTransButton, self.SplitChooseBox)
        OCR_Window.setTabOrder(self.SplitChooseBox, self.TransResult_1)
        OCR_Window.setTabOrder(self.TransResult_1, self.TransResult_2)
        OCR_Window.setTabOrder(self.TransResult_2, self.TransResult_3)
        OCR_Window.setTabOrder(self.TransResult_3, self.OCRResultTextEdit)
        OCR_Window.setTabOrder(self.OCRResultTextEdit, self.splitTextEdit)

    def retranslateUi(self, OCR_Window):
        _translate = QtCore.QCoreApplication.translate
        OCR_Window.setWindowTitle(_translate("OCR_Window", "TransAssistant"))
        self.OCRResultTextEdit.setPlaceholderText(_translate("OCR_Window", "请先选取OCR区域，使用鼠标划选后按回车确认↑"))
        self.ChooseAreaButton.setToolTip(_translate("OCR_Window", "<html><head/><body><p><span style=\" font-size:10pt;\">按Enter确认选取区域</span></p></body></html>"))
        self.ChooseAreaButton.setText(_translate("OCR_Window", "选取区域"))
        self.ChosenTitleTitle.setText(_translate("OCR_Window", "已选择的区域"))
        self.PosText.setText(_translate("OCR_Window", "(0,0),(0,0)"))
        self.OCRButton.setText(_translate("OCR_Window", "识别"))
        self.SplitChooseBox.setItemText(0, _translate("OCR_Window", "sudachi"))
        self.SplitChooseBox.setItemText(1, _translate("OCR_Window", "MeCab"))
        self.SplitChooseBox.setItemText(2, _translate("OCR_Window", "kuromoji"))
        self.SplitChooseTitle.setText(_translate("OCR_Window", "分词库选择"))
        self.ShortcutKeyTitle.setText(_translate("OCR_Window", "当前全局OCR快捷键"))
        self.ShortcutKeyText.setText(_translate("OCR_Window", "Ctrl + Space"))
        self.OCRButtonPlus.setText(_translate("OCR_Window", "识别并拼接"))
        self.showDictWindowButton.setText(_translate("OCR_Window", "查词"))
        self.autoDictCheckBox.setText(_translate("OCR_Window", "自动查词"))
        self.autoTransCheckBox.setText(_translate("OCR_Window", "自动翻译"))
        self.doTransButton.setText(_translate("OCR_Window", "翻译"))
        self.changeHotKeyButton.setToolTip(_translate("OCR_Window", "<html><head/><body><p>更改快捷键</p></body></html>"))
        self.changeHotKeyButton.setText(_translate("OCR_Window", "⚙️"))
        self.doTransButton_2.setText(_translate("OCR_Window", "设置"))
from customerDefineQtClass import betterSelectionQPlainTextEdit
