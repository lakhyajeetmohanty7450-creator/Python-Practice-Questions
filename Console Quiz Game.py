# Write a Python program to create a console-based quiz application that asks multiple-choice questions, 
# calculates the user's score, and displays the final result.

quiz = [
    {
        "question": "What is the output of print(2 + 3)?",
        "options": ["4", "5", "6", "7"],
        "answer": "5"
    },
    {
        "question": "Which data type is used to store text in Python?",
        "options": ["int", "float", "str", "bool"],
        "answer": "str"
    },
    {
        "question": "Which keyword is used to create a loop that continues while a condition is true?",
        "options": ["for", "while", "if", "def"],
        "answer": "while"
    },
    {
        "question": "What is the result of 10 % 3?",
        "options": ["1", "2", "3", "0"],
        "answer": "1"
    },
    {
        "question": "Which collection stores data in key-value pairs?",
        "options": ["List", "Tuple", "Set", "Dictionary"],
        "answer": "Dictionary"
    },
    {
        "question": "Which function is used to find the length of a list?",
        "options": ["count()", "length()", "len()", "size()"],
        "answer": "len()"
    },
    {
        "question": "Which keyword is used to stop a loop?",
        "options": ["stop", "exit", "break", "continue"],
        "answer": "break"
    },
    {
        "question": "What is the result of 5 * 4?",
        "options": ["9", "15", "20", "25"],
        "answer": "20"
    },
    {
        "question": "Which symbol is used for equality comparison in Python?",
        "options": ["=", "==", "!=", ">="],
        "answer": "=="
    },
    {
        "question": "Which data structure automatically removes duplicate values?",
        "options": ["List", "Tuple", "Set", "String"],
        "answer": "Set"
    }
]

mark = 0

for i in range(0,len(quiz)):
    print(f"Question is  {quiz[i]['question']}")
    print(f"Option is A {quiz[i]['options'][0]}")
    print(f"Option is B {quiz[i]['options'][1]}")
    print(f"Option is C {quiz[i]['options'][2]}")
    print(f"Option is D {quiz[i]['options'][3]}")

    option = {"A":quiz[i]["options"][0] ,"B":quiz[i]["options"][1] ,"C":quiz[i]["options"][2] , "D":quiz[i]["options"][3] }
    ans = input("Your answer: ")
    if option[ans.upper()] == quiz[i]["answer"]:
        print("Correct!")
        mark += 1
    else :
        print("Incorrect")
        
    print("-" * 100)
print(f" Your total mark is : {mark}")
    