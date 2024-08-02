import random

#question and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A. William Shakespeare", "B. Charles Dickens", "C. Mark Twain", "D. Jane Austen"],
        "answer": "A"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["A. 0", "B. 1", "C. 2", "D. 3"],
        "answer": "C"
    }
]

def ask_question(question):
    print("\n" + question["question"])
    for option in question["options"]:
        print(option)
    answer = input("Your answer (A, B, C, or D): ").strip().upper()
    return answer == question["answer"]

def run_quiz():
    random.shuffle(questions)
    score = 0
    for question in questions:
        if ask_question(question):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}")
    print(f"\nYour final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    print("Welcome to the quiz!")
    run_quiz()
