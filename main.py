from voice import listen, speak
from llm import get_response
from actions import perform_action


speak("Hello! I am Echo, your personal voice assistant. How can I help you?")

confirm_shutdown = False

while True:
    command = listen()

    if not command:
        continue

    command = command.lower().strip()

    if "stop assistant" in command or command == "exit":
        speak("Goodbye!")
        break

    if not command.startswith("echo") and not confirm_shutdown:
        continue

    if command.startswith("echo"):
        command = command[4:].strip()

    if not command:
        speak("Yes, how can I help?")
        continue

    if confirm_shutdown:
        if command in ["yes", "yeah", "confirm", "confirm shutdown", "do it"]:
            result = perform_action("shutdown")
            speak(result)
        else:
            speak("Shutdown cancelled.")
        confirm_shutdown = False
        continue

    response = get_response(command)

    if "are you sure you want to shut down" in response.lower():
        speak(response)
        confirm_shutdown = True
    else:
        speak(response)