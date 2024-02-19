def get_user_answer(options_length):
    while True:
        user_input = input(f"Enter your answer (1-{options_length}): ")
        if user_input.isdigit():
            user_answer = int(user_input)
            if 1 <= user_answer <= options_length:
                return user_answer
            else:
                print("Please enter a valid number within the specified range.")
        else:
            print("Please enter a valid integer between 1 and 4.")

def quiz():
    user_name = input("Enter your name: ")
    print(f"Hello, {user_name}! Let's start the quiz.\n")

    score = 0
    questions = [
        {
            "question": "Which company developed the first commercially available computer mouse?",
            "options": ["Microsoft", "IBM", "Apple", "Xerox"],
            "answer": 3
        },
        {
            "question": "What is the primary purpose of an operating system?",
            "options": ["Run applications", "Manage hardware resources", "Provide internet access", "Create documents"],
            "answer": 1
        },
        {
            "question": "What does CPU stand for?",
            "options": ["Central Processing Unit", "Computer Personal Unit", "Central Processor Unit", "Central Personal Unit"],
            "answer": 0
        },
        {
            "question": "Which programming language is known for its readability and simplicity?",
            "options": ["Java", "Python", "C++", "Ruby"],
            "answer": 1
        },
        {
            "question": "What is the term for a malicious software that spreads from computer to computer?",
            "options": ["Virus", "Worm", "Trojan Horse", "Spyware"],
            "answer": 1
        },
        {
            "question": "In the context of programming, what does API stand for?",
            "options": ["Application Programming Interface", "Advanced Programming Instruction", "Automated Programming Interface", "Application Program Interface"],
            "answer": 0
        },
        {
            "question": "Which programming paradigm does Python follow?",
            "options": ["Procedural", "Object-Oriented", "Functional", "All of the above"],
            "answer": 3
        },
        {
            "question": "What is the term for a high-level programming language that is designed for web development?",
            "options": ["Java", "C#", "HTML", "JavaScript"],
            "answer": 3
        },
        {
            "question": "What does the acronym HTML stand for in web development?",
            "options": ["HyperText Markup Language", "High-Level Text Markup Language", "Hyper Transfer Markup Language", "Home Tool Markup Language"],
            "answer": 0
        },
        {
            "question": "Which social media platform was founded by Mark Zuckerberg?",
            "options": ["Twitter", "Instagram", "Facebook", "LinkedIn"],
            "answer": 2
        }
    ]

    for q in questions:
        print(q["question"])
        for i, o in enumerate(q["options"]):
            print(f"{i + 1}) {o}")
        
        user_answer = get_user_answer(len(q["options"]))

        if user_answer - 1 == q["answer"]:
            score += 1
            print("Correct!\n")
        else:
            print(f"Incorrect. The correct answer is: {q['options'][q['answer']]}\n")

    print(f"{user_name}, you got {score}/{len(questions)} correct!")

quiz()
