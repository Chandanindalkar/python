question_prompts = [
    "What color are Apples?\na) Blu\nb) Red\nc.py) orange\n\n",
    "What color are guavas?\na) green\nb) Red\nc.py) yellow\n\n",
    "What color are oranges?\na) orange\nb) black\nc.py) white\n\n"
]


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a")
]


def run_test(questions):
    score = 0
    for i in questions:
        answer = input(i.prompt)
        if answer == i.answer:
            score += 1
    print("you scored " + str(score) + "/" + str(len(questions)))


run_test(questions)