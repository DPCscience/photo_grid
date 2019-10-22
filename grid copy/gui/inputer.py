# 3rd party imports 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# self imports
from ..grid import *


class PnInputer(QWidget):
    """
    """
    def __init__(self, grid):
        """
        """

        super().__init__()
        self.grid = grid
        # user define
        self.gr_user = QGroupBox("User's Input")
        self.lo_user = QGridLayout()
        self.lb_img = QLabel()
        self.lb_map = QLabel()
        self.fd_img = QLineEdit()
        self.fd_map = QLineEdit()
        self.bt_img = QPushButton()
        self.bt_map = QPushButton()
        # demo
        self.gr_demo = QGroupBox("Demo")
        self.lo_demo = QVBoxLayout()
        self.lb_demo = QLabel("Will use sample files to demo the program")
        # self
        self.layout = QVBoxLayout()
        
        self.initUI()

    def initUI(self):
        """
        """

        # USER
        ## GUI components
        self.gr_user.setCheckable(True)
        self.gr_user.setChecked(False)
        self.gr_user.clicked.connect(lambda: self.toggle(self.gr_user))
        self.lb_img.setText("Image (.tif, .jpg, .png):")
        self.lb_map.setText("Map (.csv, .txt)(OPTIONAL):")
        font = self.fd_img.font()
        font.setPointSize(25)
        fm = QFontMetrics(font)
        self.fd_img.setFixedHeight(fm.height())
        self.fd_map.setFixedHeight(fm.height())
        self.bt_img.setText("Browse")
        self.bt_img.clicked.connect(self.assign_PathImg)
        self.bt_map.setText("Browse")
        self.bt_map.clicked.connect(self.assign_PathMap)
        ## layout
        self.lo_user.addWidget(self.lb_img, 0, 0)
        self.lo_user.addWidget(self.fd_img, 0, 1)
        self.lo_user.addWidget(self.bt_img, 0, 2)
        self.lo_user.addWidget(self.lb_map, 1, 0)
        self.lo_user.addWidget(self.fd_map, 1, 1)
        self.lo_user.addWidget(self.bt_map, 1, 2)
        self.gr_user.setLayout(self.lo_user)
        
        # DEMO
        ## GUI components
        self.gr_demo.setCheckable(True)
        self.gr_demo.setChecked(True)
        self.gr_demo.clicked.connect(lambda: self.toggle(self.gr_demo))
        ## layout
        self.lo_demo.addWidget(self.lb_demo)
        self.gr_demo.setLayout(self.lo_demo)
        
        # LAYOUT
        self.layout.setContentsMargins(400, 50, 400, 50)
        self.layout.addWidget(self.gr_user)
        self.layout.addWidget(self.gr_demo)
        
        # FINALIZE
        self.setLayout(self.layout)
        self.show()

    def toggle(self, groupbox):
        """
        """

        if (groupbox.title() == "Demo"):
            self.gr_user.setChecked(not self.gr_user.isChecked())
        elif (groupbox.title() != "Demo"):
            self.gr_demo.setChecked(not self.gr_demo.isChecked())

    def assign_PathImg(self):
        """
        """

        fileter = "Images (*.tif *.jpg *.jpeg *.png)"
        path = QFileDialog().getOpenFileName(self, "", "", fileter)[0]
        self.fd_img.setText(path)

    def assign_PathMap(self):
        """
        """

        fileter = "Map (*.csv *.txt)"
        path = QFileDialog().getOpenFileName(self, "", "", fileter)[0]
        self.fd_map.setText(path)

    def run(self):
        """
        """

        if self.gr_user.isChecked():
            self.grid.loadData(pathImg=self.fd_img.text(),
                               pathMap=self.fd_map.text())
        else:
            self.grid.loadData(pathImg="http://www.zzlab.net/James_Demo/seg_img.jpg",
                               pathMap="http://www.zzlab.net/James_Demo/seg_map.csv")
