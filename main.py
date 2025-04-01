from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, 
    QSizePolicy, QLineEdit, QPushButton, QSpacerItem
)
from PySide6.QtCore import Qt, QSize
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import sys
import os

class MatplotlibWidget(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        super().__init__(self.fig)
        self.plot()

    def plot(self):
        x = [0, 1, 2, 3, 4]
        y = [0, 1, 4, 9, 16]
        self.ax.plot(x, y)
        self.draw()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QueryScope")
        self.setGeometry(100, 100, 800, 600)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        main_layout = QHBoxLayout()

        # Left Layout (Graph + Log)
        left_layout = QVBoxLayout()
        self.graph_widget = MatplotlibWidget(self)
        left_layout.addWidget(self.graph_widget)
        
        self.log_widget = QTextEdit()
        self.log_widget.setReadOnly(True)
        self.log_widget.setStyleSheet("background-color: black; color: white;")
        left_layout.addWidget(self.log_widget)
        
        # Right Layout (for Input Field & Button)
        right_layout = QVBoxLayout()

        # Adjusted spacing to lift input field & button slightly higher
        right_layout.addStretch(1.2)  # Push input field up
        
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("XPath query...")
        self.input_field.setFixedWidth(200)
        self.input_field.setAlignment(Qt.AlignCenter)
        right_layout.addWidget(self.input_field, alignment=Qt.AlignHCenter)

        self.submit_button = QPushButton("Submit")
        self.submit_button.setFixedWidth(150)
        right_layout.addWidget(self.submit_button, alignment=Qt.AlignHCenter)

        right_layout.addStretch(3)  # Push remaining space down

        # Add layouts to main layout
        main_layout.addLayout(left_layout, stretch=2)
        main_layout.addLayout(right_layout, stretch=1)

        self.central_widget.setLayout(main_layout)

        self.setMinimumSize(800, 600)
        self.setMaximumSize(1200, 900)
    
        self.adjust_widget_sizes()

        self.load_command_history()

    def resizeEvent(self, event):
        """Resize widgets properly when window resizes."""
        super().resizeEvent(event)
        self.adjust_widget_sizes()
    
    def adjust_widget_sizes(self):
        """Ensure graph and log take up half of the left side."""
        half_height = self.height() // 2
        half_width = self.width() // 2 
        self.graph_widget.setFixedSize(half_width, half_height)
        self.log_widget.setFixedSize(half_width, half_height)

    def log_message(self, message):
        """Log messages to the text edit widget."""
        self.log_widget.append(message)
    
    def load_command_history(self):
        """Load shell history from .bash_history file."""
        history_file = os.path.expanduser("~/.bash_history")
        
        if not os.path.exists(history_file):
            self.log_widget.setPlainText("No command history file found.")
            return
        
        with open(history_file, "r", encoding="utf-8") as file:
            history_output = file.read().strip()
        
        self.log_widget.setPlainText(history_output if history_output else "No history found.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

