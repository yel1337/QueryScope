from PySide6.QtWidgets import (
    QMainWindow, QWidget, 
    QVBoxLayout, QHBoxLayout, 
    QTextEdit, QLineEdit, QPushButton
)
from PySide6.QtCore import Qt, QSize
from mp.matplotlib import MatplotlibWidget
from test.checklist import Test
import os

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

        self.load_test_graph()

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
    
    def load_test_graph(self):
        """Load test datas from test.checklist"""
        test_instance = Test()
        
        test_data = str(test_instance.to_mp_graph(test_instance.check()))
        self.log_widget.setPlainText(test_data)

