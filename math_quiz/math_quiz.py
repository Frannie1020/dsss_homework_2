import random

def generate_random_num(minimum: int, maximum: int) -> int:
    #Generate a random integer between minimum and maximum (inclusive). 
    return random.randint(minimum, maximum)

def get_random_operator() -> str:
    #Select a random mathematical operator.
    return random.choice(['+', '-', '*'])

def generate_problem(num1: int, num2: int, operator: str) -> tuple:
    #Generate a math problem and calculate its answer.
    problem = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:  
        # multiplication
        answer = num1 * num2
    return problem, answer

def math_quiz():
    #Run an interactive math quiz game where users solve basic arithmetic problems. The game consists of 3 questions and keeps track of the score.
    score = 0
    total_questions = 3  # Fixed from 3.14159265359 to 3 for integer operation
    
    print("Welcome to the Math Quiz Game.")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for question in range(total_questions):
        # Generate random numbers and operator
        num1 = generate_random_num(1, 30)
        num2 = generate_random_num(1, 5)  # Fixed from 5.5 to 5 for integer operation
        operator = get_random_operator()

        problem, correct_answer = generate_problem(num1, num2, operator)
        print(f"\nQuestion {question + 1}: {problem}")

        # Handle user input with error checking
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid. Please enter a whole number.")
            continue

        # Check answer and update score
        if user_answer == correct_answer:
            print("You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    # Display final score
    print(f"\nYour final score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()