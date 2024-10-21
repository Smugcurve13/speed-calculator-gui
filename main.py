from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QComboBox
import sys

class SpeedCaclulator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        # Create Widget
        distance_label = QLabel("Distance: ")
        distance_input = QLineEdit()

        time_label = QLabel("Time (hours): ")
        time_input = QLineEdit()

        unit_dropdown = QComboBox()
        unit_dropdown.addItems(['Metric (kms)','Imperial (miles)'])

        calculate_button = QPushButton("Calculate")
        output_label = QLabel("")

        # Add Widgets to grid
        grid.addWidget(distance_label ,0 ,0)
        grid.addWidget(distance_input ,0 ,1)
        grid.addWidget(time_label ,1 ,0)
        grid.addWidget(time_input ,1 ,1)
        grid.addWidget(unit_dropdown ,0 ,2)
        grid.addWidget(calculate_button ,2 ,1)
        grid.addWidget(output_label ,3 ,0, 1,2)
        self.setLayout(grid)
        
app = QApplication(sys.argv)
speed_calc = SpeedCaclulator()
speed_calc.show()
sys.exit(app.exec())