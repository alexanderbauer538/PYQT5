# -*- coding: utf-8 -*-
"""
Graphical User Interface that demonstrates how to connect a slider to with a separate spin box for the value.

Classes:
    SlidersGroup: This class just creates the slider and the methods to set its value and borders.
    Window: The main window of the application where the controls for the slider are created via a function and connected to the slider instance.

"""

from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import (QApplication, QBoxLayout, QComboBox, QTimeEdit,
        QGridLayout, QGroupBox, QHBoxLayout, QLabel,
        QSlider, QSpinBox, QStackedWidget, QWidget)


class SlidersGroup(QGroupBox):
    """
    Class to create a groupobject that contains the slider.
    
    The class creates a slider object and the methods to change the current
    value of the slider along with a signal telling an event has occured.
    
    Attributes:
        valueChanged: The signal denoting the the slider has been moved
        
    Methods:
        setValue: This changes the current value of the slider
        setMinimum: This sets the lower border of the slider
        setMaximum: This sets the upper border of the slider
    """    

    valueChanged = pyqtSignal(int)

    def __init__(self, title, parent=None):
        super(SlidersGroup, self).__init__(title, parent)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setFocusPolicy(Qt.StrongFocus)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.setTickInterval(10)
        self.slider.setSingleStep(1)

        self.slider.valueChanged.connect(self.valueChanged)


        slidersLayout = QBoxLayout(QBoxLayout.TopToBottom)
        slidersLayout.addWidget(self.slider)
        self.setLayout(slidersLayout)    

    def setValue(self, value):    
        self.slider.setValue(value)    

    def setMinimum(self, value):    
        self.slider.setMinimum(value)

    def setMaximum(self, value):    
        self.slider.setMaximum(value)




class Window(QWidget):
    """
    Main window which creates the slider controls via its method and creates the slider instance.
    
    Methods:
        createControls: creates 3 spinboxes for minimum-, maximum- and current value.
    
    """
    def __init__(self):
        super(Window, self).__init__()

        self.horizontalSliders = SlidersGroup('Slider')
        

        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(self.horizontalSliders)
        
        self.createControls("Controls")
        
        # These lines connect the sliders:
        # moves signal from value spin box (3rd on left side in gui) to the slider
        self.valueSpinBox.valueChanged.connect(self.horizontalSliders.setValue)
        # moves signal back from slider to the spin box
        self.horizontalSliders.valueChanged.connect(self.valueSpinBox.setValue)
        
        
        layout = QHBoxLayout()
        layout.addWidget(self.controlsGroup)
        layout.addWidget(self.stackedWidget)
        self.setLayout(layout)

        self.minimumSpinBox.setValue(0)
        self.maximumSpinBox.setValue(20)
        self.valueSpinBox.setValue(5)

        self.setWindowTitle("Only Connect")

    def createControls(self, title):
        """
        Function to create the controls on the left side of the GUI.
        """
        self.controlsGroup = QGroupBox(title)

        minimumLabel = QLabel("Start time:")
        maximumLabel = QLabel("Stop time:")
        valueLabel = QLabel("Current value:")


        self.minimumSpinBox = QSpinBox()
        self.minimumSpinBox.setRange(-100, 100)
        self.minimumSpinBox.setSingleStep(1)

        self.maximumSpinBox = QSpinBox()
        self.maximumSpinBox.setRange(-100, 100)
        self.maximumSpinBox.setSingleStep(1)

        self.valueSpinBox = QSpinBox()
        self.valueSpinBox.setRange(-100, 100)
        self.valueSpinBox.setSingleStep(1)

        orientationCombo = QComboBox()
        orientationCombo.addItem("Horizontal slider-like widgets")
        orientationCombo.addItem("Vertical slider-like widgets")

        orientationCombo.activated.connect(self.stackedWidget.setCurrentIndex)
        self.minimumSpinBox.valueChanged.connect(self.horizontalSliders.setMinimum)
        self.maximumSpinBox.valueChanged.connect(self.horizontalSliders.setMaximum)

        controlsLayout = QGridLayout()
        controlsLayout.addWidget(minimumLabel, 0, 0)
        controlsLayout.addWidget(maximumLabel, 1, 0)
        controlsLayout.addWidget(valueLabel, 2, 0)
        controlsLayout.addWidget(self.minimumSpinBox, 0, 1)
        controlsLayout.addWidget(self.maximumSpinBox, 1, 1)
        controlsLayout.addWidget(self.valueSpinBox, 2, 1)
        self.controlsGroup.setLayout(controlsLayout)




if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())