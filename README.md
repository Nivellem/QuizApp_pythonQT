# QuizApp_pythonQT
C:\\Users\\Public\\Documents\\questionsandanswer.txt

# GitHub Documentation for the Python QR Code

This Python code reads a file named questionsandanswer.txt that contains multiple choice questions and options with one correct answer. The user interface is created using the PyQt5 module.

## Getting Started

To run this program, you need to have Python 3 and the PyQt5 module installed on your machine. You can install the module by running the following command in your terminal or command prompt:

```powershell code

pip install PyQt5 
```
Next, you need to download the questionsandanswer.txt file and place it in the directory where the Python script is located.

## Usage

To use this code, run the following command in your terminal or command prompt:

```powershell code

python <filename.py> 
```
where <filename.py> is the name of the Python script.

After running the code, a window will appear with the first question and its options. Select the option you think is correct and click the "Submit" button. The program will move to the next question and continue until all questions have been answered. At the end, the program will display your score.

## Code Structure

The code consists of a single class named MainWindow that inherits from the QMainWindow class. The __init__ method loads the questions and initializes the score. The loadQuestions method reads the questions and options from the questionsandanswer.txt file and stores them in a list. The initUI method initializes the user interface by calling the askQuestion method, which displays the first question and its options.

The askQuestion method creates a label with the question and a set of radio buttons with the options. It also creates a "Submit" button that calls the submit method when clicked. The submit method checks the selected radio button for the correct answer and updates the score. If there are more questions, it calls the askQuestion method again with the next question. Otherwise, it calls the showScore method.

The showScore method displays the final score.

## Example File: questionsandanswer.txt

The questionsandanswer.txt file contains two sample questions with their options and correct answers. Each question is represented by a heading starting with #### Q, followed by the question text. Each option is represented by a bullet point starting with - [ ] or - [x], depending on whether the option is correct or not.

The example questionsandanswer.txt file is shown below:

```test Imput

#### Q1. Wt? - [ ] A - [ ] B - [ ] C - [x] D #### Q2. Wh A? - [x] A - [ ] B - [ ] C - [ ] D 
```
Note that you can create your own questionsandanswer.txt file with your own questions and options.

