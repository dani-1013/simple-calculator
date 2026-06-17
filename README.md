# Simple Calculator

## Overview

This project is a graphical calculator application created in Python using the Tkinter library. The calculator allows users to perform basic arithmetic operations through an interactive button-based interface. It was developed as part of an AP Computer Science Principles project to demonstrate programming concepts such as functions, lists, user input handling, graphical user interfaces (GUI), and error handling.

## Features

* Addition, subtraction, multiplication, and division
* Parentheses for more complex expressions
* Decimal number support
* Clear (AC) button to reset calculations
* Error handling for invalid operations such as division by zero
* Automatic scientific notation formatting for very large or very small results
* User-friendly graphical interface built with Tkinter

## Technologies Used

* Python
* Tkinter GUI Library

## How It Works

The calculator uses buttons to collect user input and store each value in a list. As buttons are pressed, the current expression is displayed on the screen. When the equals (`=`) button is selected, the program combines the stored values into a mathematical expression and evaluates it.

The application includes:

* `show_num()` to record and display user input
* `delete_num()` to clear the current expression
* `calculate()` to evaluate expressions and display results

If the result is extremely large or small, the calculator automatically converts it to scientific notation for improved readability.

## Learning Objectives

This project demonstrates several important programming concepts:

* Event-driven programming
* Graphical user interface design
* Function creation and reuse
* List manipulation
* Exception handling
* Mathematical expression evaluation

## Future Improvements

Potential enhancements include:

* Adding exponent and square root operations
* Implementing a backspace/delete button
* Improving error messages for invalid expressions
* Adding keyboard input support
* Refactoring the code into classes for better organization
* Creating a calculator history feature

## Running the Program

1. Install Python 3.
2. Save the program as a `.py` file.
3. Run the file using Python:

   ```
   python calculator.py
   ```
4. The calculator window will open and be ready to use.

## Author

Created as an AP Computer Science Principles project to explore GUI development and calculator functionality using Python and Tkinter.
