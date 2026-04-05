from my_env.models import Observation, Action
from my_env.tasks import TASKS, grade

class EmailEnv:

    def __init__(self):
        self.current_task = 0
        self.done = False

    def reset(self):
        self.current_task = 0
        self.done = False

        task = TASKS[self.current_task]

        return {
            "observation": Observation(
                email_text=task["email"],
                sender="unknown"
            ),
            "done": False
        }

    def step(self, action: Action):
        task = TASKS[self.current_task]

        reward = grade(task, action.value)

        self.current_task += 1

        if self.current_task >= len(TASKS):
            self.done = True

        next_obs = None
        if not self.done:
            next_task = TASKS[self.current_task]
            next_obs = Observation(
                email_text=next_task["email"],
                sender="unknown"
            )

        return {
            "observation": next_obs,
            "reward": reward,
            "done": self.done,
            "info": {}
        }

    def state(self):
        return {"task_index": self.current_task}