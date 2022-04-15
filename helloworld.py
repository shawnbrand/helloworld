from Question import Question

question_prompts = [
    "What color are apples? \n(a)Red/Green \n(b)Purple \n(c)Orange \n\n",
    "What colors are bananas? \n(a)Green\n(b)Yellow\n(c)Black \n\n",
    "What colors are peachs?\n(a)Red\n(b)Pink\n(c)Orange\n\n"
]

questions = [
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"b"),
    Question(question_prompts[2],"b")
]

def run_test(questions):
    my_score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            my_score += 1
    print("You got" + str(my_score) + "/" + str(len(questions)) + "Correct")

run_test(questions)
