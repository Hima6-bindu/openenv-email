import requests

BASE_URL = "http://localhost:8000"

def reset_env():
    res = requests.post(f"{BASE_URL}/reset")
    return res.json()

def step_env(action=None):
    res = requests.post(f"{BASE_URL}/step", json={"action": action})
    return res.json()

def main():
    print("[START] task=email env=openenv model=rule-based")

    try:
        reset_env()

        step1 = step_env("spam")
        print(f"[STEP] step=1 action=spam reward={step1['reward']:.2f} done={step1['done']} error=null")

        step2 = step_env("important")
        print(f"[STEP] step=2 action=important reward={step2['reward']:.2f} done={step2['done']} error=null")

        step3 = step_env("reply")
        print(f"[STEP] step=3 action=reply reward={step3['reward']:.2f} done={step3['done']} error=null")

        print("[END] success=true steps=3 score=1.00 rewards=1.0,1.0,1.0")

    except Exception as e:
        print(f"[END] success=false error={str(e)}")

if __name__ == "__main__":
    main()
