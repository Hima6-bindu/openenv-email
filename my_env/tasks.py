TASKS = [
    {
        "name": "easy",
        "email": "Win a free iPhone now!!!",
        "answer": "spam"
    },
    {
        "name": "medium",
        "email": "Your interview is scheduled tomorrow at 10 AM.",
        "answer": "important"
    },
    {
        "name": "hard",
        "email": "Client meeting request for project discussion.",
        "answer": "reply"
    }
]

def grade(task, action):
    correct = task["answer"]

    if action == correct:
        return 1.0
    elif correct in action:
        return 0.5
    else:
        return 0.0