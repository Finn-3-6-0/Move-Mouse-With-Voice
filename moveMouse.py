import pyautogui
import speech_recognition as sr

# # Move the mouse to position (100, 200)
# pyautogui.moveTo(100, 200, duration=1)  # duration is in seconds

# # print(pyautogui.position())

# x_pos = pyautogui.position().x
# y_pos = pyautogui.position().y
# up_right = 50
# down_left = -50

# print(x_pos)
# print(y_pos)

def recognise_voice():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak something...")
        
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("Sorry, I couldn't reach the recognition service.")

    return text

def move_mouse(text):

    if "left" in text.lower():
        pyautogui.moveRel(-100,0,duration=0.5)
        print("Moving left")

    if "right" in text.lower():
        pyautogui.moveRel(100,0,duration=0.5)
        print("Moving right")
         

    if "up" in text.lower():
        pyautogui.moveRel(0,-100,duration=0.5)
        print("Moving up")


    if "down" in text.lower():
        pyautogui.moveRel(0,100,duration=0.5)
        print("Moving down")
  
    else:
        print("No move recognised")

def main():
    for i in range(5):
        text = recognise_voice()
        move_mouse(text)

if __name__ == "__main__":
    main()