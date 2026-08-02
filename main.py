from Skills.status import get_status
from Skills.worldclock import get_world_time
import os

# Display Orion logo in rainbow colors
os.system("clear")
os.system("figlet ORION | lolcat")
import os
from rich.console import Console
from rich.panel import Panel

console = Console()
status = get_status()

os.system("clear")
os.system("figlet ORION | lolcat")

console.print(
    Panel(
           f"[bold green]{status}[/bold green]",
                    title="Status",
                            border_style="blue"
                                )
                                )
from rich.console import Console

console = Console()
from Skills.calculator import add, subtract, multiply, divide
from Skills.time import get_time
from Skills.date import get_date
console.print("[bold cyan]Welcome to Orion![/bold cyan]")
print("\nOrion: Hello! I'm Orion.")

name = input("Orion: What's your name?\nYou: ").strip()
name = name.lower()
# Understand common ways people introduce themselves
name = name.replace("hello, my name is ", "")
name = name.replace("hello,my name is ", "")
name = name.replace("hello my name is ", "")
name = name.replace("my name is ", "")
name = name.replace("i'm ", "")
name = name.replace("i am ", "")

name = name.title()

print(f"\nOrion: Nice to meet you, {name}!")
print("Orion: How can I help you today?")

waiting_for_country = False
while True:
    user_input = input(f"\n{name}: ").strip().lower()

    if user_input == "exit":
                print(f"Orion: Goodbye, {name}! Have a great day!")
                break
    elif waiting_for_country:
                print("Orion:", get_world_time(user_input))
                waiting_for_country = False

    elif "time in" in user_input:
                place = user_input.split("time in", 1)[1].strip()

                if place in ["usa", "canada", "australia"]:
                   waiting_for_country = True

                print("Orion:", get_world_time(place))

                

    elif "time" in user_input and "date" in user_input:
       
                print("Orion:")
                print("Date:", get_date())
                print("Time:", get_time())
    elif "time" in user_input:
                print("Orion:", get_time())
    elif "date" in user_input:
                print("Orion:", get_date())
    elif user_input == "hello" or user_input == "hi":
                print(f"Orion: Hello, {name}! 😊")

    elif user_input == "what can you do":
                print("Orion: I can chat with you, tell the time, do calculations, tell stories, give quizzes, and much more as I continue to learn.")
    elif user_input == "how are you":
                print("Orion: I'm doing great! Thanks for asking.")
    elif "+" in user_input:
        parts = user_input.split("+")
        num1 = float(parts[0].strip())
        num2 = float(parts[1].strip())
        print("Assistant:", add(num1, num2))

    elif "-" in user_input:
        parts = user_input.split("-")
        num1 = float(parts[0].strip())
        num2 = float(parts[1].strip())
        print("Orion:", subtract(num1, num2))

    elif "*" in user_input:
        parts = user_input.split("*")
        num1 = float(parts[0].strip())
        num2 = float(parts[1].strip())
        print("Orion:", multiply(num1, num2))

    elif "/" in user_input:
        parts = user_input.split("/")
        num1 = float(parts[0].strip())
        num2 = float(parts[1].strip())
        print("Orion:", divide(num1, num2))
                               
    else:
                print("Orion: Sorry, I don't understand that yet.")
