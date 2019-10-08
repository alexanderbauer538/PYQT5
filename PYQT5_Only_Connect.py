"""
Graphical User Interface that demonstrates how to connect a slider to with a separate spin box for the value.

Classes:
    SlidersGroup: This class just creates the slider and the methods to set its value and borders.
    Window: The main window of the application where the controls for the slider are created via a function and connected to the slider instance.

"""

from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import (QApplication, QBoxLayout, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QSlider, QSpinBox, QStackedWidget, QWidget)


class sliders_group(QGroupBox):
    """
    Class to create a groupobject that contains the slider.
    
    The class creates a slider object and the methods to change the current
    value of the slider along with a signal telling an event has occured.
    
    Attributes:
        slider_signal: The signal denoting the the slider has been moved
        
    Methods:
        setValue: This changes the current value of the slider
        setMinimum: This sets the lower border of the slider
        setMaximum: This sets the upper border of the slider
    """    

    slider_signal = pyqtSignal(int)

    def __init__(self, title, parent=None):
        super(sliders_group, self).__init__(title, parent)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setFocusPolicy(Qt.StrongFocus)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.setTickInterval(10)
        self.slider.setSingleStep(1)

        self.slider.valueChanged.connect(self.slider_signal)


        sliders_layout = QBoxLayout(QBoxLayout.TopToBottom)
        sliders_layout.addWidget(self.slider)
        self.setLayout(sliders_layout)    

    def set_value(self, value):    
        self.slider.setValue(value)    

    def set_minimum(self, value):    
        self.slider.setMinimum(value)

    def set_maximum(self, value):    
        self.slider.setMaximum(value)


class Window(QWidget):
    """
    Main window which creates the slider controls via its method and creates the slider instance.
    
    Attributes:
        horizontal_sliders: instance of the class sliders_group which creates the slider on the right side.
        layout: horizontal QBox which stores the controls (left side) and the slider (right side)
        stackedWidget: widget to hold the slider
    
    Methods:
        createControls: creates 3 spinboxes for minimum-, maximum- and current value of the slider.
    
    """
    def __init__(self):
        super(Window, self).__init__()

        self.horizontal_sliders = sliders_group('Slider')
        

        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(self.horizontal_sliders)
        
        self.create_controls("Controls")
        
        # These lines connect the slider to the current value box:
        # moves signal from value spin box (3rd on left side in gui) to the slider
        self.value_spinbox.valueChanged.connect(self.horizontal_sliders.set_value)
        # moves signal back from slider to the spin box
        self.horizontal_sliders.slider_signal.connect(self.value_spinbox.setValue)
        
        
        layout = QHBoxLayout()
        layout.addWidget(self.controls_group)
        layout.addWidget(self.stackedWidget)
        self.setLayout(layout)

        self.minimum_spinbox.setValue(0)
        self.maximum_spinbox.setValue(10)
        self.value_spinbox.setValue(5)

        self.setWindowTitle("Only Connect")

    def create_controls(self, title):
        """
        Function to create the controls on the left side of the GUI.
        
        Attributes:
            minimum_spinbox: control to set the lower boundary of the slider
            maximum_spinbox: control to set the upper boundary of the slider
            value_spinbox: control to set and display the current value of the slider
            labels: labels for the spinboxes
            controls_layout: QGrid that sets all the control widgets
            
        """
        self.controls_group = QGroupBox(title)

        minimum_label = QLabel("Start time:")
        maximum_label = QLabel("Stop time:")
        value_label = QLabel("Current value:")


        self.minimum_spinbox = QSpinBox()
        self.minimum_spinbox.setRange(-100, 100)
        self.minimum_spinbox.setSingleStep(1)

        self.maximum_spinbox = QSpinBox()
        self.maximum_spinbox.setRange(-100, 100)
        self.maximum_spinbox.setSingleStep(1)

        self.value_spinbox = QSpinBox()
        self.value_spinbox.setRange(-100, 100)
        self.value_spinbox.setSingleStep(1)

        self.minimum_spinbox.valueChanged.connect(self.horizontal_sliders.set_minimum)
        self.maximum_spinbox.valueChanged.connect(self.horizontal_sliders.set_maximum)

        controls_layout = QGridLayout()
        controls_layout.addWidget(minimum_label, 0, 0)
        controls_layout.addWidget(maximum_label, 1, 0)
        controls_layout.addWidget(value_label, 2, 0)
        controls_layout.addWidget(self.minimum_spinbox, 0, 1)
        controls_layout.addWidget(self.maximum_spinbox, 1, 1)
        controls_layout.addWidget(self.value_spinbox, 2, 1)
        self.controls_group.setLayout(controls_layout)




if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())