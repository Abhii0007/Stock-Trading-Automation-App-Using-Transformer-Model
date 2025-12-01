import pandas as pd
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from lightweight_charts.widgets import QtChart
import sys


from window1 import Ui_MainWindow
class window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.form = Ui_MainWindow()
        self.form.setupUi(self)
        
        
        layout = QVBoxLayout()
        self.form.widget.setLayout(layout)

        layout.setContentsMargins(0, 0, 0, 0)
        chart = QtChart(self.form.widget)

        df = pd.read_csv('ohlcv.csv')
        chart.set(df)
        layout.addWidget(chart.get_webview())
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget1 = window()
    widget1.show()
    sys.exit(app.exec())