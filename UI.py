from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QImage, QWindow, QPixmap
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from faceswap import function
import sys
import cv2

class AddressBar(QLineEdit):
    def __init__(self):
        super().__init__()

    def mousePressEvent(self, e):
        self.selectAll()

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FaceSwap")
        self.createApp()
        
    def createApp(self):
        self.faceImg=""
        self.sourceImg=""
        self.layout = QVBoxLayout()
        #self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.toolbar = QWidget()
        self.toolbarLayout = QHBoxLayout()
        self.toolbar.setFixedHeight(60)

        self.toolbar.setLayout(self.toolbarLayout)

        # new tab button
        self.btnOpenSourceImg = QPushButton("Open Image Source")
        self.btnOpenFaceImg = QPushButton("Open Image Face")
        self.btnOpenSourceImg.setFixedSize(120,30)
        self.btnOpenFaceImg.setFixedSize(120,30)
        self.btnOpenSourceImg.clicked.connect(self.openFileNameDialogImgSource)
        self.btnOpenFaceImg.clicked.connect(self.openFileNameDialogImgFace)
        self.toolbarLayout.addWidget(self.btnOpenSourceImg)
        self.toolbarLayout.addWidget(self.btnOpenFaceImg)
        self.btnFaceSwap=QPushButton("Swap!!")
        self.btnFaceSwap.setFixedSize(90,30)
        self.toolbarLayout.addWidget(self.btnFaceSwap)
        self.btnFaceSwap.clicked.connect(self.functionFaceSwap)

        # set main view
        self.container = QWidget()
        self.container.layout = QHBoxLayout()
        self.container.setLayout(self.container.layout)

        self.label = QLabel()
        pixmap = QPixmap()
        self.label.setPixmap(pixmap)

        self.label1 = QLabel()
        self.label1.setPixmap(pixmap)

        self.container.layout.addWidget(self.label)
        #del label1
        self.container.layout.addWidget(self.label1)

        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.container)

        self.setLayout(self.layout)
        self.setGeometry(0,0,820,600)

        self.show()

    def openFileNameDialogImgSource(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Image", "",
                                                  "All Files (*);;JPG Files (*.jpg);;JPG Files (*.jpg);;PNG Files (*.png)", options=options)
        if fileName:
            print(fileName)
            
        self.sourceImg=fileName
        pixmap = QPixmap(fileName)
        if pixmap.height() > 400:
            ratio=400/pixmap.height()
            pixmap=pixmap.scaled(pixmap.width()*ratio, pixmap.height()*ratio);
        self.label.setPixmap(pixmap)
    
    def openFileNameDialogImgFace(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Image", "",
                                                  "All Files (*);;JPG Files (*.jpg);;JPG Files (*.jpg);;PNG Files (*.png)", options=options)
        if fileName:
            print(fileName)
        self.faceImg=fileName
        pixmap = QPixmap(fileName)
        if pixmap.height() > 400:
            ratio=400/pixmap.height()
            pixmap=pixmap.scaled(pixmap.width()*ratio, pixmap.height()*ratio);
        self.label1.setPixmap(pixmap)
    #faceswap    
    
    def functionFaceSwap(self):
        if self.sourceImg!="":
            if self.faceImg!="":
                output = function(self.sourceImg, self.faceImg)  
                if output!="":
                    # output=output.split()
                    # i=1
                    # for x in output:
                    #     print(x)
                    #     outputImg=cv2.imread(x)
                    #     cv2.imshow(x, outputImg)
                    #     i=i+1
                    # cv2.waitKey(0)    
                    # cv2.destroyAllWindows()
                    outputImg=cv2.imread(output)
                    cv2.imshow('Image Output',outputImg)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()

    sys.exit(app.exec_())
