from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QRadioButton
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.loadQuestions()
        self.score = 0
        self.initUI()

    def loadQuestions(self):
        with open("C:\\Users\\Public\\Documents\\questionsandanswer.txt") as f:
            lines = f.readlines()

        self.questions = []
        question = None
        options = []
        for line in lines:
            if line.startswith("#### Q"):
                if question:
                    self.questions.append({
                        "question": question,
                        "options": options,
                        "correct_answer": correct_answer
                    })
                question = line[5:].strip()
                options = []
                correct_answer = None
            elif line.startswith("- [x]"):
                correct_answer = line[5:].strip()
                options.append(correct_answer)
            elif line.startswith("- [ ]"):
                options.append(line[5:].strip())

        if question:
            self.questions.append({
                "question": question,
                "options": options,
                "correct_answer": correct_answer
            })

    def initUI(self):
        self.current_question = 0
        self.askQuestion()

    def askQuestion(self):
        question = self.questions[self.current_question]
        label = QLabel(question["question"])

        self.radio_buttons = []
        layout = QVBoxLayout()
        layout.addWidget(label)

        for option in question["options"]:
            radio_button = QRadioButton(option)
            self.radio_buttons.append(radio_button)
            layout.addWidget(radio_button)

        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.submit)
        layout.addWidget(submit_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def submit(self):
        for radio_button in self.radio_buttons:
            if radio_button.isChecked() and radio_button.text() == self.questions[self.current_question]["correct_answer"]:
                self.score += 1

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.askQuestion()
        else:
            self.showScore()

    def showScore(self):
        label = QLabel(f"Your score is: {self.score}/{len(self.questions)}")

        layout = QVBoxLayout()
        layout.addWidget(label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)




if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
