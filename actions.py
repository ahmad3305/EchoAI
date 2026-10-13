
import subprocess
import webbrowser
from datetime import datetime
import os


def perform_action(action, argument=""):
    if action == "time":
        return "The current time is " + datetime.now().strftime("%I:%M %p")

    elif action == "date":
        return "Today's date is " + datetime.now().strftime("%B %d, %Y")

    elif action == "search":
        webbrowser.open("https://www.google.com/search?q=" + argument.replace(" ", "+"))
        return "Here are the search results for " + argument

    elif action == "youtube":
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."

    elif action == "notepad":
        subprocess.Popen(["notepad.exe"])
        return "Opening Notepad."

    elif action == "calculator":
        subprocess.Popen(["calc.exe"])
        return "Opening Calculator."

    elif action == "vscode":
        subprocess.Popen(["code"])
        return "Opening Visual Studio Code."

    elif action == "whatsapp":
        os.startfile("whatsapp:")
        return "Opening WhatsApp."

    elif action == "shutdown":
        subprocess.Popen(["shutdown", "/s", "/t", "60"])
        return "Your PC will shut down in 60 seconds. Say cancel shutdown to stop it."

    elif action == "cancel_shutdown":
        subprocess.Popen(["shutdown", "/a"])
        return "Shutdown cancelled."

    else:
        return "Sorry, I don't have that action available yet."
