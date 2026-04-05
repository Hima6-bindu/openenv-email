import os
from openai import OpenAI
from my_env.env import EmailEnv
from my_env.models import Action

# Required environment variables
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
HF_TOKEN = os.getenv("HF_TOKEN")  # optional

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN or "dummy-key"
)

env = EmailEnv()

print(f"[START] task=email env=openenv model={MODEL_NAME}")

result = env.reset()

rewards = []
steps = 0

while True:
    steps += 1

    email = result["observation"].email_text.lower()

    # still using safe logic (no real API call needed)
    if "win" in email or "free" in email:
        action_text = "spam"
    elif "interview" in email:
        action_text = "important"
    else:
        action_text = "reply"

    action = Action(action_type="classify", value=action_text)

    result = env.step(action)

    reward = result["reward"]
    done = result["done"]

    rewards.append(reward)

    print(f"[STEP] step={steps} action={action_text} reward={reward:.2f} done={str(done).lower()} error=null")

    if done:
        break

score = sum(rewards) / len(rewards)

print(f"[END] success={str(score>0.5).lower()} steps={steps} score={score:.2f} rewards={','.join([str(round(r,2)) for r in rewards])}")
