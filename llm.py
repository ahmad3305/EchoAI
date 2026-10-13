import os
from groq import Groq
from dotenv import load_dotenv
from actions import perform_action

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def get_response(command):
    command = command.lower().strip()

    if "cancel shutdown" in command:
        return perform_action("cancel_shutdown")

    if "shutdown" in command or "shut down" in command:
        return "Are you sure you want to shut down your computer? Please say yes to confirm."

    if "time" in command:
        return perform_action("time")

    if "date" in command:
        return perform_action("date")

    if "notepad" in command:
        return perform_action("notepad")

    if "calculator" in command or "calc" in command:
        return perform_action("calculator")

    if "vs code" in command or "vscode" in command or "visual studio code" in command:
        return perform_action("vscode")

    if "whatsapp" in command:
        return perform_action("whatsapp")

    if "youtube" in command:
        return perform_action("youtube")

    if command.startswith("search for "):
        return perform_action("search", command.replace("search for ", "", 1).strip())

    if command.startswith("search "):
        return perform_action("search", command.replace("search ", "", 1).strip())

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Echo, a personal voice assistant running on Windows. "
                        "Answer naturally and briefly."
                    )
                },
                {
                    "role": "user",
                    "content": command
                }
            ]
        )

        return response.choices[0].message.content or "Sorry, I didn't understand that."

    except Exception as e:
        print("LLM Error:", e)
        return "Sorry, something went wrong while processing your request."