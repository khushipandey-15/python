Day 10: Basic Arithmetic Operations
Inputting two integers and performing arithmetic operations: addition, subtraction, multiplication, modulus, and division.

Day 11: Iterating Over Strings
Using a for loop to iterate over each character in a string and print them individually.

Day 12: String Slicing
Demonstrates Python string slicing techniques with examples, including start, stop, and step values.

Day 13: String Methods
Examples of using string manipulation methods such as:
upper(), lower(), title()
Removing characters with rstrip() and lstrip()
Replacing substrings with replace()
Checking start and end patterns with startswith() and endswith()
Splitting strings and finding substrings.

Day 14: Conditional Statements
Using if-elif-else to build a program that checks age eligibility for driving.

Day 15: Time-Based Greetings
A program that takes the current time as input and prints context-based greetings such as "Good Morning," "Good Afternoon," etc.

Day 16: Pattern Matching
Demonstrates pattern matching using match-case to handle different cases.

Day 17: Iterations
Examples of using for loops with strings, tuples, and ranges:
Printing elements of a tuple.
Nested loops to iterate over characters in strings.

Day 18: While Loops
Demonstrates a basic while loop with a condition and increment.

Day 19: Loops with Control Statements
Using break and continue in loops with examples, such as printing multiplication tables.

Day 20: Functions (Part 1)
Defines simple functions for comparison (isgreater, issmaller) and demonstrates their usage.

Day 21: Functions (Part 2)
Functions for more complex tasks:
Calculating averages.
Generating multiplication tables.
Working with default arguments in function parameters.

Day 22: Lists
Introduces Python lists and operations:
Accessing elements using indexing and slicing.
Using in operator to check for membership in a list.
Storing mixed data types (integers, strings, booleans) in a list.

Day 23: Lists
Demonstrates key list operations:
Adding elements using append().
Counting occurrences of a specific element with count().
Sorting lists in ascending or descending order using sort().
Inserting elements at a specific index with insert().
Extending lists with another list using extend().
Copying lists with copy().
Finding the index of a specific element using index().

Day 24: Tuples
Introduction to tuples:
Defining tuples.
Accessing elements and slicing tuples.
Determining the length of a tuple with len().

Day 25: Tuple Methods
Practical usage of tuple-specific methods:

count(): Counts occurrences of a specific value.
index(): Finds the index of a specific value within a range.
Tuple Example:

Converting tuples to lists for modification (e.g., appending or removing elements).
Combining two tuples into a new tuple using concatenation.
Counting occurrences of a specific value in a tuple.
Demonstrating slicing and indexing for specific ranges.

Day 26: Time and Greetings
Using the time Module:
Fetching and formatting the current time using strftime().
Determining the current hour and printing context-based greetings like "Good Morning," "Good Afternoon," or "Good Night" based on the time of day.
College Code: Flask Web Application
A basic Flask application demonstrating database integration and a simple webpage for displaying student data.
Key Features:
Database Integration:

Uses SQLite as the database backend.
Implements SQLAlchemy for ORM (Object Relational Mapping).
Student Data Model:

Defines a student class with attributes:
id: Primary key.
name: Name of the student.
subject: Student's subject.
roll: Roll number.
contact: Contact information.
Data Insertion:

Provides a /upload route to upload predefined student data into the database.
Webpage Rendering:

Implements a home route that fetches student data from the database and displays it in an HTML table.
HTML Template:

Displays student information in a styled table with headers for ID, Name, Subject, and Contact.
Uses Jinja2 templating syntax for dynamically rendering rows of student data.
How to Run the Flask Application
Clone this repository.

Install dependencies:

bash
Copy
Edit
pip install flask flask_sqlalchemy
Run the Flask app:

bash
Copy
Edit
python app.py
Access the application:

Open your browser and navigate to http://127.0.0.1:5000/.
Routes:

/upload: Populates the database with sample student data.
/: Displays the student table on the homepage.
HTML Code Example
The web app uses an HTML template for rendering the student data. Key features:

Styled table with borders for clear presentation.
Dynamically rendered rows using Jinja2's {% for %} syntax.



How to Run the Code
Clone the repository.
Open any Python IDE or editor.
Copy and paste the code snippets from the relevant day into a .py file.
Run the file to see the output.


Purpose
This repository serves as a resource for beginners to:

Practice Python programming concepts.
Build a foundation in Python through step-by-step exercises.
Learn key language features interactively.
Feel free to contribute additional exercises, fix issues, or improve the structure of the examples.
