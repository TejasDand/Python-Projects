# Robo Speaker
import pyttsx3

if __name__ == "__main__":
    engine = pyttsx3.init()
    print("Welcome to Robo Speaker!")

    while True:
        command = input("Enter what you want to speak (for exit type 'z'): ")

        if command.lower() == 'z':
            engine.say("Bye Bye Friend!")
            engine.runAndWait()
            break

        engine.say(command)
        engine.runAndWait()