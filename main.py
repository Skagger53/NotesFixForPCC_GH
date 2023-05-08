from PyQt5.QtWidgets import \
    QApplication,\
    QMainWindow,\
    QVBoxLayout,\
    QWidget,\
    QTextEdit,\
    QLabel,\
    QPushButton,\
    QGridLayout,\
    QPlainTextEdit,\
    QShortcut
from PyQt5.QtGui import QTextCursor, QKeySequence
from PyQt5.QtCore import Qt, QMimeData
import sys
import re

class TextProcessor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Text Processor')
        self.setGeometry(100, 100, 600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        instructions = QLabel('Enter text in the input field and click "Create output text".')
        layout.addWidget(instructions)

        self.input_text = QPlainTextEdit()
        layout.addWidget(self.input_text)

        self.output_text = QTextEdit()
        self.output_text.setAcceptRichText(False)
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

        buttons_layout = QGridLayout()

        create_output_button = QPushButton('<u>C</u>reate output text')
        create_output_button.clicked.connect(self.create_output)
        buttons_layout.addWidget(create_output_button, 0, 0)

        copy_output_button = QPushButton('&Copy output text')
        copy_output_button.clicked.connect(self.copy_output)
        buttons_layout.addWidget(copy_output_button, 0, 1)

        exit_button = QPushButton('E&xit')
        exit_button.clicked.connect(self.close)
        buttons_layout.addWidget(exit_button, 0, 2)

        layout.addLayout(buttons_layout)

        # Create output text shortcut (Alt + R)
        create_output_shortcut = QShortcut(QKeySequence('Alt+R'), self)
        create_output_shortcut.activated.connect(self.create_output)

        # Copy output text shortcut (Alt + C)
        copy_output_shortcut = QShortcut(QKeySequence('Alt+C'), self)
        copy_output_shortcut.activated.connect(self.copy_output)

        # Exit shortcut (Alt + X)
        exit_shortcut = QShortcut(QKeySequence('Alt+X'), self)
        exit_shortcut.activated.connect(self.close)

        central_widget.setLayout(layout)

    def create_output(self):
        input_text = self.input_text.toPlainText()
        output_text = input_text.replace('/', '.')
        output_text = re.sub(r'\n+', ' ', output_text)
        self.output_text.setPlainText(output_text)
        self.output_text.setReadOnly(False)

    def copy_output(self):
        mime_data = QMimeData()
        mime_data.setText(self.output_text.toPlainText())
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mime_data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = TextProcessor()
    main_window.show()
    sys.exit(app.exec_())