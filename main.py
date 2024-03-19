import speech_recognition as sr
import os
import webbrowser
import datetime
import openai
import random
import pyautogui
import win32com.client
import screen_brightness_control as sbc
speaker = win32com.client.Dispatch("SAPI.SpVoice")
#todo: api key
#from config import apikey
#def ai(prompt):
 #  text=f"OpenAI response for Prompt: {prompt}\n ***************************\n\n"
 #   response = openai.ChatCompletion.create(
#      model="gpt-3.5-turbo",
#       prompt=prompt,
 #       temperature=1,
  #      max_tokens=256,
   #     top_p=1,
#    frequency_penalty=0,
 #       presence_penalty=0
  #  )
   # print(response["choices"][0]["text"])
#   text+= response["choices"][0]["text"]
    #if not os.path.exists("Openai"):
     #   os.mkdir("Openai")

   # with open(f"Openai/prompt- {random.randint(1,999999999999)}")as f:
    #    f.write(text)
def say(text):
    speaker.Speak(text)
def takeaadesh():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User: {query}")
            return query
        except Exception as e:
            return "Sorry I couldn't understand what you said! Can You repeat please?"
def toggle_bluetooth():
    # Press Win + A to open the Action Center
    pyautogui.hotkey("win", "a")

    # Wait for the Action Center to open
    pyautogui.sleep(1)

    # Use arrow keys to navigate to the Bluetooth tile and press Enter
    pyautogui.press("right")
    #pyautogui.press("down")
    pyautogui.press("enter")

    # Close the Action Center
    pyautogui.hotkey("esc")
def toggle_bs():
    # Press Win + A to open the Action Center
    pyautogui.hotkey("win", "a")

    # Wait for the Action Center to open
    pyautogui.sleep(1)

    # Use arrow keys to navigate to the Bluetooth tile and press Enter
    #pyautogui.press("right")
    pyautogui.press("down")
    pyautogui.press("enter")

    # Close the Action Center
    pyautogui.hotkey("esc")
def toggle_am():
    # Press Win + A to open the Action Center
    pyautogui.hotkey("win", "a")

    # Wait for the Action Center to open
    pyautogui.sleep(1)

    # Use arrow keys to navigate to the Bluetooth tile and press Enter
    pyautogui.press("right")
    pyautogui.press("right")
    pyautogui.press("enter")

    # Close the Action Center
    pyautogui.hotkey("esc")
def toggle_wf():
    # Press Win + A to open the Action Center
    pyautogui.hotkey("win", "a")

    # Wait for the Action Center to open
    pyautogui.sleep(1)
    pyautogui.press("enter")

    # Close the Action Center
    pyautogui.hotkey("esc")
while 1:
    s = "Hello I am Nebula A.I."
    say(s)
    while True:
        print("Listening...")
        query = takeaadesh()
        #say(query)
        #todo: add more sites
        sites = [["whatsapp in chrome","https://web.whatsapp.com/"],["youtube","https://youtube.com"], ["wikipedia","https://wikipedia.com"],["google","https://google.com"]]
        for site in sites:
            if f"{site[0]}".lower() in query.lower():
                say(f"Sure,Opening {site[0]} ma'am...")
                webbrowser.open(site[1])

        if "music" in query.lower():
            musicPath = r'\Users\Ishika Shukla\Sia - Unstoppable_64-(PagalWorld.Ink).mp3'
            os.startfile(musicPath)

        if "time" in query:
            hour= datetime.datetime.now().strftime("%H")
            min= datetime.datetime.now().strftime("%M")
            say(f"Ma'am, The time right now is {hour} hours and {min} minutes, Perfect time for a nap for you :)")

        apps=["Spotify","WhatsApp","PowerPoint","Instagram","Word","Paint","Google","Calculator","Camera"]
        for app in apps:
            if f"{app}".lower() in query.lower():
                say(f"Sure, Opening {app} ma'am...")
                from AppOpener import open
                open(app)

        if "kaisi ho".lower() in query.lower():
            say("Mai achi hu, tum kaisi ho?")
        if "how are you".lower() in query.lower():
            say("I am really good, What about you?")
        create=["creator","who made you","birth","created","who are you","born"]
        for c in create:
            if f"{c}".lower() in query.lower():
                say("I am the daughter of Luphomoid Warlord Zorr, but I am famously known as the grand daughter of the Mad Titan Thanos!")
        if "Machine".lower() in query.lower():
            ai(prompt=query)
        #todo: connect to specific wifi network
        if query and "wi-fi network" in query.lower():
            networks = os.popen('netsh wlan show networks').read()
            print(networks)

            say("Please input the name of the wifi network you want to connect with!")
            name_of_router = input()

            ssid_lines = networks.split('\nSSID ')
            for line in ssid_lines[1:]:
                ssid = line.split()[0]
                if name_of_router in ssid:
                    os.system(f'netsh wlan connect name="{ssid}"')
                    say(f"Connecting to {ssid} Wi-Fi network...")
                    break
            else:
                say("Wi-Fi network not found.")

        if "on" and "bluetooth" in query.lower():
            toggle_bluetooth()
            say("Bluetooth turned on.")
        elif "off" and "bluetooth" in query.lower():
            toggle_bluetooth()
            say("Bluetooth has been turned off.")
        if "on" and "wi-fi" in query.lower():
            toggle_wf()
            say("Wi_Fi turned on.")
        elif "off" and "wi_fi" in query.lower():
            toggle_wf()
            say("Wi_Fi has been turned off.")
        if "on" and "battery saver" in query.lower():
            toggle_bs()
            say("Battery saver turned on.")
        elif "off" and "battery saver" in query.lower():
            toggle_bs()
            say("Battery saver has been turned off.")
        if "on" and "airplane mode" in query.lower():
            toggle_am()
            say("Airplane mode turned on.")
        elif "off" and "airplane mode" in query.lower():
            toggle_am()
            say("Airplane mode has been turned off.")

        if "increase brightness" in query.lower():
            sbc.set_brightness(75)
        elif "decrease brightness" in query.lower():
            sbc.set_brightness(25)