class Question:
    def __init__(self, prompt, choices, answer):
        self.prompt = prompt
        self.choices = choices
        self.answer = answer

    def display_question(self):
        print(f"\n{self.prompt}")
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}. {choice}")

    def check_answer(self, user_answer):
        return user_answer.lower() == self.answer.lower()


class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def ask_questions(self):
        for question in self.questions:
            question.display_question()
            user_answer = input("Your answer: ")

            if question.check_answer(user_answer):
                print("Correct! ✓")
                self.score += 1
            else:
                print(f"Wrong! ✗ The correct answer was: {question.answer}")

    def track_score(self):
        print(f"\nYour score: {self.score}/{len(self.questions)}")
        return self.score

    def show_final_result(self):
        print("\n" + "=" * 40)
        print("QUIZ COMPLETED!")
        print("=" * 40)
        self.track_score()
        self.percentage_score()

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


# Example usage
if __name__ == "__main__":
    # Create quiz instance
    quiz = Quiz()

    # Create questions
    q1 = Question(
        "What is the capital of France?",
        ["London", "Berlin", "Paris", "Madrid"],
        "Paris",
    )

    q2 = Question("What is 2 + 2?", ["3", "4", "5", "6"], "4")

    q3 = Question(
        "Which planet is known as the Red Planet?",
        ["Venus", "Mars", "Jupiter", "Saturn"],
        "Mars",
    )

    q4 = Question(
        "What is the largest ocean on Earth?",
        ["Atlantic", "Indian", "Arctic", "Pacific"],
        "Pacific",
    )

    # Add questions to quiz
    quiz.add_question(q1)
    quiz.add_question(q2)
    quiz.add_question(q3)
    quiz.add_question(q4)

    # Run the quiz
    print("=" * 40)
    print("WELCOME TO THE QUIZ GAME!")
    print("=" * 40)

    quiz.ask_questions()
    quiz.show_final_result()
