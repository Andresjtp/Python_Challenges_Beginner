# Quiz Game Engine

## Challenge Description

This beginner-level Python challenge focuses on building a **Quiz Game Engine** to practice core programming skills including **lists, dictionaries, loops, and functions**.

### Challenge Requirements

The program must implement two classes with the following structure:

#### Class: `Question`
- `prompt` - The question text
- `choices` - List of answer choices
- `answer` - The correct answer

#### Class: `Quiz`
- `list of questions` - Stores multiple Question objects
- `score tracking` - Keeps track of correct answers

#### Features Required:
1. **Ask questions** - Display questions and get user input
2. **Track score** - Keep count of correct answers
3. **Show final result** - Display the final score
4. **Percentage score** - Calculate and show score as a percentage

---

## Code Implementation Explanation

### 1. The `Question` Class

```python
class Question:
    def __init__(self, prompt, choices, answer):
        self.prompt = prompt
        self.choices = choices
        self.answer = answer
```

The `Question` class represents a single quiz question with three attributes:
- **prompt**: The question text (string)
- **choices**: A list of possible answers
- **answer**: The correct answer (string)

**Why use a class?** Encapsulating question data in a class keeps related information together and makes the code more organized and reusable.

---

#### Method: `display_question()`

```python
def display_question(self):
    print(f"\n{self.prompt}")
    for i, choice in enumerate(self.choices, 1):
        print(f"{i}. {choice}")
```

**Purpose**: Display the question and its choices in a formatted way.

**How it works**:
- Prints the question prompt with a newline for spacing
- Uses `enumerate(self.choices, 1)` to loop through choices with 1-based numbering
- The `enumerate()` function provides both the index and the value
- Starting at 1 makes the display more user-friendly (1, 2, 3... instead of 0, 1, 2...)

**Key concepts demonstrated**:
- **Loops**: Iterating through a list
- **enumerate()**: Getting both index and value while looping
- **String formatting**: Using f-strings for clean output

---

#### Method: `check_answer()`

```python
def check_answer(self, user_answer):
    return user_answer.lower() == self.answer.lower()
```

**Purpose**: Validate if the user's answer is correct.

**How it works**:
- Takes the user's answer as input
- Converts both the user's answer and correct answer to lowercase using `.lower()`
- Compares them for equality
- Returns `True` if correct, `False` if wrong

**Key concepts demonstrated**:
- **String methods**: `.lower()` for case-insensitive comparison
- **Boolean returns**: Method returns True/False for easy conditional checks
- **Comparison operators**: Using `==` to check equality

---

### 2. The `Quiz` Class

```python
class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0
```

The `Quiz` class manages the entire quiz game with two attributes:
- **questions**: An empty list that will store `Question` objects
- **score**: Integer starting at 0 to track correct answers

**Using lists allows us to**:
- Store multiple Question objects dynamically
- Iterate through questions in order
- Easily add or remove questions

---

#### Method: `add_question()`

```python
def add_question(self, question):
    self.questions.append(question)
```

**Purpose**: Add a Question object to the quiz.

**How it works**:
- Takes a `Question` object as parameter
- Uses `.append()` to add it to the end of the questions list
- Allows building the quiz dynamically

**Key concepts demonstrated**:
- **List manipulation**: Using `.append()` to add items
- **Object composition**: One class (Quiz) containing objects of another class (Question)

---

#### Method: `ask_questions()`

```python
def ask_questions(self):
    for question in self.questions:
        question.display_question()
        user_answer = input("Your answer: ")
        
        if question.check_answer(user_answer):
            print("Correct! ✓")
            self.score += 1
        else:
            print(f"Wrong! ✗ The correct answer was: {question.answer}")
```

**Purpose**: Loop through all questions, display them, get user input, and provide feedback.

**How it works**:
1. **Loop through questions**: Uses `for question in self.questions` to iterate
2. **Display question**: Calls the question's `display_question()` method
3. **Get user input**: Uses `input()` to capture the user's answer
4. **Check answer**: Calls `check_answer()` to validate
5. **Update score**: If correct, increments score by 1 using `+=`
6. **Provide feedback**: Prints whether the answer was right or wrong

**Key concepts demonstrated**:
- **Loops**: For loop to iterate through a list
- **Method calling**: Calling methods on objects within the list
- **User input**: Getting data from the user with `input()`
- **Conditionals**: If-else for decision making
- **Accumulation**: Building up the score with `+=`

---

#### Method: `track_score()`

```python
def track_score(self):
    print(f"\nYour score: {self.score}/{len(self.questions)}")
    return self.score
```

**Purpose**: Display the current score in a fraction format.

**How it works**:
- Uses `len(self.questions)` to get total number of questions
- Prints score as "correct/total" (e.g., "3/4")
- Returns the score value for potential further use

**Key concepts demonstrated**:
- **len() function**: Getting the length of a list
- **String formatting**: F-strings for clean output
- **Return values**: Returning data for use by other methods

---

#### Method: `show_final_result()`

```python
def show_final_result(self):
    print("\n" + "=" * 40)
    print("QUIZ COMPLETED!")
    print("=" * 40)
    self.track_score()
    self.percentage_score()
```

**Purpose**: Display the final quiz results with formatting.

**How it works**:
1. Prints a decorative header with repeated `=` characters
2. Announces quiz completion
3. Calls `track_score()` to show the score fraction
4. Calls `percentage_score()` to show percentage and grade

**Key concepts demonstrated**:
- **String multiplication**: `"=" * 40` creates a line of 40 equal signs
- **Method orchestration**: One method calling other methods to coordinate functionality
- **Code organization**: Breaking down complex functionality into smaller methods

---

#### Method: `percentage_score()`

```python
def percentage_score(self):
    if len(self.questions) > 0:
        percentage = (self.score / len(self.questions)) * 100
        print(f"Percentage: {percentage:.1f}%")
        
        if percentage >= 90:
            print("Grade: A - Excellent! 🌟")
        elif percentage >= 80:
            print("Grade: B - Great job! 👍")
        elif percentage >= 70:
            print("Grade: C - Good effort! ✓")
        elif percentage >= 60:
            print("Grade: D - Keep practicing! 📚")
        else:
            print("Grade: F - Don't give up! 💪")
    else:
        print("Percentage: 0%")
```

**Purpose**: Calculate percentage score and assign a letter grade.

**How it works**:
1. **Edge case check**: First checks if there are questions to avoid division by zero
2. **Calculate percentage**: Divides score by total questions and multiplies by 100
3. **Format output**: Uses `:.1f` to show one decimal place
4. **Grade assignment**: Uses if-elif-else chain to determine letter grade
5. **Grade ranges**:
   - A: 90-100%
   - B: 80-89%
   - C: 70-79%
   - D: 60-69%
   - F: Below 60%
6. **Friendly messages**: Each grade includes an encouraging message

**Key concepts demonstrated**:
- **Mathematical operations**: Division and multiplication
- **Conditionals**: Chained if-elif-else for multiple conditions
- **Edge case handling**: Checking for empty list before calculation
- **String formatting**: Using `:.1f` for decimal precision
- **Range-based logic**: Checking ranges with `>=` comparisons

---

## Key Programming Concepts Practiced

### 1. **Lists**
- Creating empty lists: `self.questions = []`
- Appending items: `.append(question)`
- Iterating through lists: `for question in self.questions`
- Storing objects in lists
- Getting list length: `len(self.questions)`

### 2. **Loops**
- For loops to iterate through collections
- enumerate() for index-value pairs
- Loop-based accumulation (score tracking)
- Iterating through objects in a list

### 3. **Functions/Methods**
- Defining methods with parameters
- Calling methods on objects
- Methods calling other methods
- Return values from functions
- Code organization through methods

### 4. **Object-Oriented Programming (OOP)**
- Creating classes with `class` keyword
- Constructor methods with `__init__`
- Instance attributes with `self`
- Methods operating on instance data
- Object composition (Quiz contains Question objects)

### 5. **Conditionals**
- If-else statements for binary decisions
- If-elif-else chains for multiple conditions
- Comparison operators (`==`, `>=`)
- Boolean returns

### 6. **Additional Concepts**
- User input with `input()`
- String methods (`.lower()`)
- String formatting with f-strings
- enumerate() for indexed iteration
- Mathematical calculations

---

## Example Usage and Output

### Running the Quiz

```python
# Create quiz instance
quiz = Quiz()

# Create and add questions
quiz.add_question(Question(
    "What is the capital of France?",
    ["London", "Berlin", "Paris", "Madrid"],
    "Paris"
))

quiz.add_question(Question(
    "What is 2 + 2?",
    ["3", "4", "5", "6"],
    "4"
))

# Run the quiz
quiz.ask_questions()
quiz.show_final_result()
```

### Sample Output

```
========================================
WELCOME TO THE QUIZ GAME!
========================================

What is the capital of France?
1. London
2. Berlin
3. Paris
4. Madrid
Your answer: Paris
Correct! ✓

What is 2 + 2?
1. 3
2. 4
3. 5
4. 6
Your answer: 4
Correct! ✓

What is the largest ocean on Earth?
1. Atlantic
2. Indian
3. Arctic
4. Pacific
Your answer: Atlantic
Wrong! ✗ The correct answer was: Pacific

========================================
QUIZ COMPLETED!
========================================

Your score: 2/3
Percentage: 66.7%
Grade: D - Keep practicing! 📚
```

---

## Code Architecture

### Class Relationships

```
Quiz
├── questions: List[Question]
│   └── Question
│       ├── prompt: str
│       ├── choices: List[str]
│       └── answer: str
└── score: int
```

### Method Flow

1. **Setup Phase**:
   - Create `Quiz` object
   - Create `Question` objects
   - Add questions to quiz with `add_question()`

2. **Execution Phase**:
   - Call `ask_questions()` which:
     - Loops through each question
     - Displays question
     - Gets user input
     - Checks answer
     - Updates score

3. **Results Phase**:
   - Call `show_final_result()` which:
     - Displays completion message
     - Shows score with `track_score()`
     - Shows percentage with `percentage_score()`

---

## Summary

This implementation successfully completes all requirements of the Quiz Game Engine challenge:

✅ **Class: Question** - Stores question data and provides display/validation methods  
✅ **Class: Quiz** - Manages questions list and score tracking  
✅ **Ask questions** - Interactive question loop with user input  
✅ **Track score** - Maintains and displays correct answer count  
✅ **Show final result** - Formatted final results display  
✅ **Percentage score** - Calculates percentage and assigns letter grades  

The code demonstrates clean object-oriented design, effective use of lists and loops, proper separation of concerns, and user-friendly interaction patterns. The modular structure makes it easy to extend with more questions or features.
