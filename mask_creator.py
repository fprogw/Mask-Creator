#            "Verson: 1.0         Date: 07.04.2020"
#            "Dear User, thank you for using this little mask creator :D"
#            "Please note that this is my first written and published program."
#            "If you find any unknown bugs, feel free to contact me. :)"
#            "Autor: Frank Wittnich\nEmail: programming_fw@hotmail.com"



from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy as np

class Ui_MainWindow(object):

    img_white = np.ones((500,1000),np.uint8)*255
    img_original = cv2.cvtColor(img_white, cv2.COLOR_GRAY2BGR)
    img_height, img_width, img_channel = img_original.shape
    img_ratio = img_width/img_height
    img_hsv = cv2.cvtColor(img_original, cv2.COLOR_BGR2HSV)
    img_mask = img_white
    img_mask_result = img_original

    img_path = "path"

    value_hsv = []
    value_hsv_counter = 0

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(QtCore.QSize(1168, 577))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        ###
        ### Group Selection with Pixmap, Radiobutton, RGB, HSV and Coordinates
        ###
        ###
        self.Group_Selection = QtWidgets.QGroupBox(self.centralwidget)
        self.Group_Selection.setGeometry(QtCore.QRect(10, 10, 1021, 561))
        self.Group_Selection.setObjectName("Group_Selection")

        ### Main-Pixmap
        self.PM_mask_result = SUBC_PM_mask_result(self.Group_Selection)

        ### RadioButton
        self.RB_Result = QtWidgets.QRadioButton(self.Group_Selection)
        self.RB_Result.setGeometry(QtCore.QRect(10, 530, 100, 20))
        self.RB_Result.setChecked(True)
        self.RB_Result.setObjectName("RB_Result")
        self.RB_Mask = QtWidgets.QRadioButton(self.Group_Selection)
        self.RB_Mask.setGeometry(QtCore.QRect(110, 530, 100, 20))
        self.RB_Mask.setObjectName("RB_Mask")

        ### RGB area
        self.L_RGB = QtWidgets.QLabel(self.Group_Selection)
        self.L_RGB.setGeometry(QtCore.QRect(470, 530, 55, 20))
        self.L_RGB.setObjectName("L_RGB")
        self.LE_R = QtWidgets.QLineEdit(self.Group_Selection)
        self.LE_R.setGeometry(QtCore.QRect(530, 530, 40, 20))
        self.LE_R.setReadOnly(True)
        self.LE_R.setObjectName("LE_R")
        self.LE_G = QtWidgets.QLineEdit(self.Group_Selection)
        self.LE_G.setGeometry(QtCore.QRect(570, 530, 40, 20))
        self.LE_G.setReadOnly(True)
        self.LE_G.setObjectName("LE_G")
        self.LE_B = QtWidgets.QLineEdit(self.Group_Selection)
        self.LE_B.setGeometry(QtCore.QRect(610, 530, 40, 20))
        self.LE_B.setReadOnly(True)
        self.LE_B.setObjectName("LE_B")

        ### CurrentColour Pixmap
        self.PM_currentColour = QtWidgets.QLabel(self.Group_Selection)
        self.PM_currentColour.setGeometry(QtCore.QRect(660, 530, 20, 20))
        self.PM_currentColour.setFrameShape(QtWidgets.QFrame.Box)
        self.PM_currentColour.setScaledContents(True)
        self.PM_currentColour.setObjectName("PM_currentColour")

        ### HSV area
        self.L_HSV = QtWidgets.QLabel(self.Group_Selection)
        self.L_HSV.setGeometry(QtCore.QRect(690, 530, 55, 20))
        self.L_HSV.setObjectName("L_HSV")
        self.LE_H = QtWidgets.QLineEdit(self.Group_Selection)
        self.LE_H.setGeometry(QtCore.QRect(750, 530, 40, 20))
        self.LE_H.setReadOnly(True)
        self.LE_H.setObjectName("LE_H")
        self.LE_S = QtWidgets.QLineEdit(self.Group_Selection)
        self.LE_S.setGeometry(QtCore.QRect(790, 530, 40, 20))
        self.LE_S.setReadOnly(True)
        self.LE_S.setObjectName("LE_S")
        self.LE_V = QtWidgets.QLineEdit(self.Group_Selection)
        self.LE_V.setGeometry(QtCore.QRect(830, 530, 40, 20))
        self.LE_V.setReadOnly(True)
        self.LE_V.setObjectName("LE_V")
        
        ### coordinates area
        self.L_XY = QtWidgets.QLabel(self.Group_Selection)
        self.L_XY.setGeometry(QtCore.QRect(890, 530, 31, 20))
        self.L_XY.setObjectName("L_XY")
        self.LE_X = QtWidgets.QLineEdit(self.Group_Selection)
        self.LE_X.setGeometry(QtCore.QRect(930, 530, 40, 20))
        self.LE_X.setText("")
        self.LE_X.setReadOnly(True)
        self.LE_X.setObjectName("LE_X")
        self.LE_Y = QtWidgets.QLineEdit(self.Group_Selection)
        self.LE_Y.setGeometry(QtCore.QRect(970, 530, 40, 20))
        self.LE_Y.setText("")
        self.LE_Y.setReadOnly(True)
        self.LE_Y.setObjectName("LE_Y")
        ###
        ###
        ### GroupSettings right side of program
        ###
        ###
        self.Group_Setting = QtWidgets.QGroupBox(self.centralwidget)
        self.Group_Setting.setGeometry(QtCore.QRect(1040, 10, 121, 561))
        self.Group_Setting.setObjectName("Group_Setting")
        
        ### SELECTED COLOR Label and Pixmap
        self.L_SelectedColor = QtWidgets.QLabel(self.Group_Setting)
        self.L_SelectedColor.setGeometry(QtCore.QRect(10, 20, 100, 16))
        self.L_SelectedColor.setObjectName("L_SelectedColor")
        self.PM_selectedcolor = QtWidgets.QLabel(self.Group_Setting)
        self.PM_selectedcolor.setGeometry(QtCore.QRect(10, 40, 100, 100))
        self.PM_selectedcolor.setFixedSize(100,100)
        self.PM_selectedcolor.setFrameShape(QtWidgets.QFrame.Box)
        self.PM_selectedcolor.setObjectName("PM_selectedcolor")
        
        ### Label Singel, Add and Sub for RadioButton
        self.L_Single = QtWidgets.QLabel(self.Group_Setting)
        self.L_Single.setGeometry(QtCore.QRect(10, 150, 22, 22))
        self.L_Single.setAlignment(QtCore.Qt.AlignCenter)
        self.L_Single.setObjectName("L_Single")
        self.L_Add = QtWidgets.QLabel(self.Group_Setting)
        self.L_Add.setGeometry(QtCore.QRect(50, 150, 22, 22))
        self.L_Add.setAlignment(QtCore.Qt.AlignCenter)
        self.L_Add.setObjectName("L_Add")
        self.L_Sub = QtWidgets.QLabel(self.Group_Setting)
        self.L_Sub.setGeometry(QtCore.QRect(90, 150, 22, 22))
        self.L_Sub.setAlignment(QtCore.Qt.AlignCenter)
        self.L_Sub.setObjectName("L_Sub")
        
        ### RadioButton Singel, Add and Sub
        self.RB_SINGEL = QtWidgets.QRadioButton(self.Group_Setting)
        self.RB_SINGEL.setGeometry(QtCore.QRect(10, 170, 20, 20))
        self.RB_SINGEL.setText("")
        self.RB_SINGEL.setChecked(True)
        self.RB_SINGEL.setObjectName("RB_SINGEL")
        self.RB_ADD = QtWidgets.QRadioButton(self.Group_Setting)
        self.RB_ADD.setGeometry(QtCore.QRect(50, 170, 20, 20))
        self.RB_ADD.setText("")
        self.RB_ADD.setObjectName("RB_ADD")
        self.RB_SUB = QtWidgets.QRadioButton(self.Group_Setting)
        self.RB_SUB.setGeometry(QtCore.QRect(90, 170, 20, 20))
        self.RB_SUB.setText("")
        self.RB_SUB.setObjectName("RB_SUB")

        ### RADIUS Label, SpinBox and Slider
        """
        self.L_Radius = QtWidgets.QLabel(self.Group_Setting)
        self.L_Radius.setGeometry(QtCore.QRect(10, 220, 61, 22))
        self.L_Radius.setObjectName("L_Radius")
        self.SB_radius = QtWidgets.QSpinBox(self.Group_Setting)
        self.SB_radius.setGeometry(QtCore.QRect(70, 220, 42, 22))
        self.SB_radius.setMinimum(1)
        self.SB_radius.setSingleStep(2)
        self.SB_radius.setObjectName("SB_radius")
        self.slider_radius = QtWidgets.QSlider(self.Group_Setting)
        self.slider_radius.setGeometry(QtCore.QRect(10, 250, 100, 22))
        self.slider_radius.setMinimum(1)
        self.slider_radius.setSingleStep(2)
        self.slider_radius.setOrientation(QtCore.Qt.Horizontal)
        self.slider_radius.setObjectName("slider_radius")
        """

        ### TOLERANCE Lablel, SpinBox and Slider
        self.L_Tolerance = QtWidgets.QLabel(self.Group_Setting)
        self.L_Tolerance.setGeometry(QtCore.QRect(10, 300, 61, 22))
        self.L_Tolerance.setObjectName("L_Tolerance")
        self.SB_tolerance = QtWidgets.QSpinBox(self.Group_Setting)
        self.SB_tolerance.setGeometry(QtCore.QRect(70, 300, 42, 22))
        self.SB_tolerance.setObjectName("SB_tolerance")
        self.slider_tolerance = QtWidgets.QSlider(self.Group_Setting)
        self.slider_tolerance.setGeometry(QtCore.QRect(10, 330, 100, 22))
        self.slider_tolerance.setOrientation(QtCore.Qt.Horizontal)
        self.slider_tolerance.setObjectName("slider_tolerance")
        
        ### Buttons About, Save, Load, Reset and Exit
        self.B_About = QtWidgets.QPushButton(self.Group_Setting)
        self.B_About.setGeometry(QtCore.QRect(10, 360, 100, 28))
        self.B_About.setFixedSize(100,28)
        self.B_About.setObjectName("B_About")
        self.B_Save = QtWidgets.QPushButton(self.Group_Setting)
        self.B_Save.setGeometry(QtCore.QRect(10, 400, 100, 28))
        self.B_Save.setFixedSize(100,28)
        self.B_Save.setObjectName("B_Save")
        self.B_Load = QtWidgets.QPushButton(self.Group_Setting)
        self.B_Load.setGeometry(QtCore.QRect(10, 440, 100, 28))
        self.B_Load.setFixedSize(100,28)
        self.B_Load.setObjectName("B_Load")
        self.B_Reset = QtWidgets.QPushButton(self.Group_Setting)
        self.B_Reset.setGeometry(QtCore.QRect(10, 480, 100, 28))
        self.B_Reset.setFixedSize(100,28)
        self.B_Reset.setObjectName("B_Reset")
        self.B_Exit = QtWidgets.QPushButton(self.Group_Setting)
        self.B_Exit.setGeometry(QtCore.QRect(10, 520, 100, 28))
        self.B_Exit.setFixedSize(100,28)
        self.B_Exit.setObjectName("B_Exit")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.retranslateUi(MainWindow)
        ###
        ###
        ### SIGNALS and CONNECTIONS
        ###
        ###
        ### Signals of Button
        self.B_About.clicked.connect(self.about_popup)
        self.B_Load.clicked.connect(self.load_image)
        self.B_Save.clicked.connect(self.save_images)
        self.B_Reset.clicked.connect(self.btn_reset)
        self.B_Exit.clicked.connect(MainWindow.close)
        self.RB_Result.toggled.connect(self.update_RB_mask_result)
        ### Signal of Slider and SpinBox
        #self.SB_radius.valueChanged['int'].connect(self.slider_radius.setValue)
        #self.slider_radius.valueChanged['int'].connect(self.SB_radius.setValue)
        self.SB_tolerance.valueChanged['int'].connect(self.slider_tolerance.setValue)
        self.slider_tolerance.valueChanged['int'].connect(self.SB_tolerance.setValue)
        ### Signals from PM_mask_result
        self.PM_mask_result.signal_coords.connect(lambda: self.live_update_coords(int,int))
        self.PM_mask_result.signal_coords.connect(self.live_update_coords)
        self.PM_mask_result.signal_bgr.connect(self.live_update_bgr)
        self.PM_mask_result.signal_hsv.connect(self.live_update_hsv)
        self.PM_mask_result.signal_picked_bgr.connect(self.update_PM_selected_rgb)
        self.PM_mask_result.signal_picked_hsv.connect(self.process_search_hsv)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Replace Color"))
        self.Group_Selection.setTitle(_translate("MainWindow", "Selection"))
        self.RB_Result.setText(_translate("MainWindow", "Result"))
        self.RB_Mask.setText(_translate("MainWindow", "Mask"))
        self.L_HSV.setText(_translate("MainWindow", "H / S / V"))
        self.L_RGB.setText(_translate("MainWindow", "R / G / B"))
        self.L_XY.setText(_translate("MainWindow", "X / Y"))
        self.PM_currentColour.setText(_translate("MainWindow", "cc"))
        self.Group_Setting.setTitle(_translate("MainWindow", "Setting"))
        self.L_Sub.setText(_translate("MainWindow", "Sub"))
        self.PM_selectedcolor.setText(_translate("MainWindow", "PM_selectedcolor"))
        self.L_Tolerance.setText(_translate("MainWindow", "Tolerance"))
        self.L_Add.setText(_translate("MainWindow", "Add"))
        self.B_Save.setText(_translate("MainWindow", "Save"))
        self.B_About.setText(_translate("MainWindow", "About"))
        self.L_Single.setText(_translate("MainWindow", "0"))
        self.L_SelectedColor.setText(_translate("MainWindow", "Selected Color:"))
        self.B_Reset.setText(_translate("MainWindow", "Reset"))
        self.B_Exit.setText(_translate("MainWindow", "Exit"))
        self.B_Load.setText(_translate("MainWindow", "Load"))
        #self.L_Radius.setText(_translate("MainWindow", "Radius:"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    def about_popup(self):
        MSG = QtWidgets.QMessageBox()
        MSG.setWindowTitle("About")
        msg_text = (
            "Verson: 1.0         Date: 07.04.2020\n\n"
            "Dear User,\nthank you for using this little mask creator :D\n"
            "Please note that this is my first written and published program.\n"
            "If you find any unknown bugs, feel free to contact me. :)\n\n"
            "Autor: Frank Wittnich\nEmail: programming_fw@hotmail.com"
            )
        MSG.setText(msg_text)
        MSG.setIcon(QtWidgets.QMessageBox.Icon.Information)
        show = MSG.exec_()
        


    def load_image(self):
        file_origin = QtWidgets.QFileDialog.getOpenFileName()
        path = file_origin[0]
        self.img_path = file_origin[0]
        self.img_original = cv2.imread("{0}".format(path))
        self.img_height, self.img_width, self.img_channel = self.img_original.shape
        self.img_ratio = self.img_width/self.img_height
        self.img_hsv = cv2.cvtColor(self.img_original, cv2.COLOR_BGR2HSV)
        self.img_white = np.ones((self.img_height,self.img_width), np.uint8) *255
        
        SUBC_PM_mask_result.img_original = self.img_original
        SUBC_PM_mask_result.img_white = self.img_white
        SUBC_PM_mask_result.img_height, SUBC_PM_mask_result.img_width, SUBC_PM_mask_result.img_channel = self.img_original.shape
        SUBC_PM_mask_result.img_ratio = self.img_width/self.img_height
        SUBC_PM_mask_result.img_hsv = self.img_hsv
        SUBC_PM_mask_result.img_mask = self.img_mask
        SUBC_PM_mask_result.img_mask_result = self.img_mask_result
        SUBC_PM_mask_result.coord_factor_x = self.img_width/1000
        SUBC_PM_mask_result.coord_factor_y = self.img_height/500
        
        self.adjust_PM_mask_result()
        self.btn_reset()
        
    def adjust_PM_mask_result(self):
        if self.img_width > 1000 and self.img_ratio >= 1 and 1000/self.img_ratio <= 500:
            new_height = 1000/self.img_ratio
            self.PM_mask_result.setGeometry(QtCore.QRect(10,20,1000, new_height))
            SUBC_PM_mask_result.coord_factor_x = self.img_width/1000
            SUBC_PM_mask_result.coord_factor_y = self.img_height/new_height
        elif self.img_height > 500 and self.img_ratio <= 1 and 500*self.img_ratio <= 1000:
            new_width = 500*self.img_ratio
            self.PM_mask_result.setGeometry(QtCore.QRect(10,20,new_width,500))
            SUBC_PM_mask_result.coord_factor_x = self.img_width/new_width
            SUBC_PM_mask_result.coord_factor_y = self.img_height/500
        elif self.img_ratio == 1:
            self.PM_mask_result.setGeometry(QtCore.QRect(10,20,500,500))
            SUBC_PM_mask_result.coord_factor_x = self.img_width/500
            SUBC_PM_mask_result.coord_factor_y = self.img_height/500
        elif self.img_width < 1001 and self.img_height < 501:
            self.PM_mask_result.setGeometry(QtCore.QRect(10,20,self.img_width,self.img_height))
            SUBC_PM_mask_result.coord_factor_x, SUBC_PM_mask_result.coord_factor_y = 1,1

            


    def btn_reset(self):
        self.img_mask = self.img_white
        self.img_mask_result = self.img_original
        self.value_hsv = []
        self.value_hsv_counter = 0
        self.update_RB_mask_result()
    
    def save_images(self):
        cv2.imwrite("mask.jpg", self.img_mask)
        cv2.imwrite("mask_result.jpg", self.img_mask_result)
        print("Saved:\nPath: {0}\nMaskname: mask.jpg\nResultname: mask_result.jpg".format(self.img_path))

    def convert_img_pixmap(self, input):
        if len(input.shape) == 2:
            input = cv2.cvtColor(input, cv2.COLOR_GRAY2RGB)
            height, width, channel = input.shape
            bytesPerLine = 3 * width
            pixmap = QtGui.QImage(input.data, width, height, bytesPerLine, QtGui.QImage.Format(29))
        else:
            height, width, channel = input.shape
            bytesPerLine = 3 * width
            pixmap = QtGui.QImage(input.data, width, height, bytesPerLine, QtGui.QImage.Format(29))
        return pixmap

    def live_update_coords(self, x,y):
        x,y = str(x), str(y)
        self.LE_X.setText(x)
        self.LE_Y.setText(y)

    def live_update_bgr(self, b,g,r):
        self.PM_currentColour.setStyleSheet("background-color: rgb({0},{1},{2});".format(r,g,b))
        self.PM_currentColour.setText("")
        b,g,r = str(b), str(g),str(r)
        self.LE_R.setText(r)
        self.LE_B.setText(b)
        self.LE_G.setText(g)
    
    def live_update_hsv(self, h,s,v):
        h,s,v = str(h), str(s),str(v)
        self.LE_H.setText(h)
        self.LE_S.setText(s)
        self.LE_V.setText(v)
        
    def update_PM_selected_rgb(self, b,g,r):
        self.PM_selectedcolor.setStyleSheet("background-color: rgb({0},{1},{2})".format(r,g,b))
        self.PM_selectedcolor.setText("")

    def process_search_hsv(self, h,s,v):
        # nur einmal da mask und output locale variabeln in der Definition sind
        if self.RB_SINGEL.isChecked() == True:
            self.value_hsv.clear()
            lh, ls, lv = int(h*(1-self.SB_tolerance.value()/100)),int(s*(1-self.SB_tolerance.value()/100)),int(v*(1-self.SB_tolerance.value()/100))
            uh, us, uv = int(h*(1+self.SB_tolerance.value()/100)),int(s*(1+self.SB_tolerance.value()/100)),int(v*(1+self.SB_tolerance.value()/100))
            self.value_hsv.append([lh,ls,lv])
            self.value_hsv.append([uh,us,uv])
            #print(self.value_hsv[0], self.value_hsv[1])
            
            lowerb = np.array(self.value_hsv[0])
            upperb = np.array(self.value_hsv[1])

            mask = cv2.inRange(self.img_hsv,lowerb,upperb,255)
            mask = cv2.bitwise_not(mask)
            output = cv2.bitwise_and(self.img_original,self.img_original,mask=mask)

            self.img_mask = mask
            self.img_mask_result = output

            self.value_hsv_counter = 0
            self.update_RB_mask_result()
        # maske erweitern
        if self.RB_ADD.isChecked() == True:
            if len(self.value_hsv) == 2:
                self.value_hsv_counter = 2

            lh, ls, lv = int(h*(1-self.SB_tolerance.value()/100)),int(s*(1-self.SB_tolerance.value()/100)),int(v*(1-self.SB_tolerance.value()/100))
            uh, us, uv = int(h*(1+self.SB_tolerance.value()/100)),int(s*(1+self.SB_tolerance.value()/100)),int(v*(1+self.SB_tolerance.value()/100))
            self.value_hsv.append([lh,ls,lv])
            self.value_hsv.append([uh,us,uv])
            lowerb = np.array(self.value_hsv[self.value_hsv_counter])
            upperb = np.array(self.value_hsv[self.value_hsv_counter+1])

            mask = cv2.inRange(self.img_hsv,lowerb,upperb,255)  
            mask = cv2.bitwise_not(mask)                        

            self.img_mask = self.img_mask & mask
            output = cv2.bitwise_and(self.img_mask_result,self.img_mask_result,mask=mask)
            self.img_mask_result = output
            
            self.value_hsv_counter += 2
            self.update_RB_mask_result()
        #maske subtrahieren
        if self.RB_SUB.isChecked() == True:
            self.img_mask_result = self.img_original
            lh, ls, lv = int(h*(1-self.SB_tolerance.value()/100)),int(s*(1-self.SB_tolerance.value()/100)),int(v*(1-self.SB_tolerance.value()/100))
            uh, us, uv = int(h*(1+self.SB_tolerance.value()/100)),int(s*(1+self.SB_tolerance.value()/100)),int(v*(1+self.SB_tolerance.value()/100))
            self.value_hsv.append([lh,ls,lv])
            self.value_hsv.append([uh,us,uv])
            lowerb = np.array(self.value_hsv[self.value_hsv_counter])
            upperb = np.array(self.value_hsv[self.value_hsv_counter+1])

            mask = cv2.inRange(self.img_hsv,lowerb,upperb,255)
            #mask = cv2.bitwise_not(mask)

            sub_mask = cv2.bitwise_or(self.img_mask,mask)
            self.img_mask = sub_mask
            output = cv2.bitwise_and(self.img_mask_result,self.img_mask_result,mask=sub_mask)
            self.img_mask_result = output
            
            self.value_hsv_counter += 2
            self.update_RB_mask_result()
            
    def update_RB_mask_result(self):
        #wird geupdated wenn RB geändert oder geklicked wird
        if self.RB_Mask.isChecked() == True:
            self.PM_mask_result.setPixmap(QtGui.QPixmap(self.convert_img_pixmap(self.img_mask)))
        if self.RB_Result.isChecked() == True:
            self.PM_mask_result.setPixmap(QtGui.QPixmap(self.convert_img_pixmap(self.img_mask_result)))
        
            
            
        

class SUBC_PM_mask_result(QtWidgets.QLabel, Ui_MainWindow):
    #img_original = cv2.imread("TestTisch_v2.jpg")
    #img_height, img_width, img_channel = img_original.shape
    #img_hsv = cv2.cvtColor(img_original, cv2.COLOR_BGR2HSV)
    #img_black = np.zeros((img_height,img_width), np.uint8)
    #img_white = cv2.bitwise_not(img_black)
    #img_mask = img_white

    img_white = np.ones((500,1000),np.uint8)*255
    img_original = cv2.cvtColor(img_white, cv2.COLOR_GRAY2BGR)
    img_height, img_width, img_channel = img_original.shape
    img_ratio = img_width/img_height
    img_hsv = cv2.cvtColor(img_original, cv2.COLOR_BGR2HSV)
    img_mask = img_white
    img_mask_result = img_original
    coord_factor_x = img_width/1000
    coord_factor_y = img_height/500
    
    signal_coords = QtCore.pyqtSignal(int,int)
    signal_bgr = QtCore.pyqtSignal(int,int,int)
    signal_hsv = QtCore.pyqtSignal(int,int,int)
    signal_picked_bgr = QtCore.pyqtSignal(int,int,int)
    signal_picked_hsv = QtCore.pyqtSignal(int,int,int)

    def __init__(self,parent=None):
        super(SUBC_PM_mask_result, self).__init__(parent)
        self.createPIXMAP()

    def convert_img_pixmap(self, input):
        if len(input.shape) == 2:
            input = cv2.cvtColor(input, cv2.COLOR_GRAY2RGB)
            height, width, channel = input.shape
            bytesPerLine = 3 * width
            pixmap = QtGui.QImage(input.data, width, height, bytesPerLine, QtGui.QImage.Format(29))
        else:
            height, width, channel = input.shape
            bytesPerLine = 3 * width
            pixmap = QtGui.QImage(input.data, width, height, bytesPerLine, QtGui.QImage.Format(29))
        return pixmap

    def createPIXMAP(self):
        #self = QtWidgets.QLabel(self.Group_Selection)
        self.setMouseTracking(True)
        self.setGeometry(QtCore.QRect(10, 20, 1000, 500))
        self.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.setMouseTracking(True)
        self.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.setFrameShape(QtWidgets.QFrame.Box)
        self.setText("")
        self.setPixmap(QtGui.QPixmap(self.convert_img_pixmap(self.img_original)))
        #self.setPixmap(QtGui.QPixmap("TestTisch_v2.jpg"))
        self.setScaledContents(True)
        self.setObjectName("PM_mask_result")


    def mouseMoveEvent(self, event):
        x,y = int(event.x()*self.coord_factor_x), int(event.y()*self.coord_factor_y)
        self.signal_coords.emit(x,y)

        b,g,r = self.img_original[y,x]
        self.signal_bgr.emit(b,g,r)

        h,s,v = self.img_hsv[y][x]
        self.signal_hsv.emit(h,s,v)

    def mousePressEvent(self, event):
        x,y = int(event.x()*self.coord_factor_x), int(event.y()*self.coord_factor_y)
        b,g,r = self.img_original[y][x]
        self.signal_picked_bgr.emit(b,g,r)

        h,s,v = self.img_hsv[y][x]
        self.signal_picked_hsv.emit(h,s,v)

class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        ui = Ui_MainWindow()
        ui.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Window()
    MainWindow.show()
    sys.exit(app.exec_())
