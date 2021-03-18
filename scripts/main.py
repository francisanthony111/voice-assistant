import JarvisAI
import re
import pprint
import random
import datetime
import os
import smtplib

def sendmail(to,message):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login(senderid,password)
    server.sendmail(senderid,to,message)
    server.close()









obj = JarvisAI.JarvisAssistant()


def t2s(text):
    obj.text2speech(text)
senderid =#email
password=#pass


def sendemail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login(senderid,password)
    server.sendmail(senderid,to,content)
    server.close()
def wish():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        t2s("Good Morning Rishika")
    elif hour>12 and hour<18:
        t2s("Good Afternoon Rishika")
    else:
        t2s("Good Evening Rishika")

if __name__=="__main__":
    wish()
    while True:


        res = obj.mic_input()

        if re.search('weather|temperature', res):
            city = res.split(' ')[-1]
            weather_res = obj.weather(city=city)
            print(weather_res)
            t2s(weather_res)

        if re.search("jokes|joke|Jokes|Joke", res):
            joke_ = obj.tell_me_joke('en', 'neutral')
            print(joke_)
            t2s(joke_)
            break

        if re.search('news', res):
            news_res = obj.news()
            pprint.pprint(news_res)
            t2s(f"I have found {len(news_res)} news. You can read it. Let me tell you first 3 of them")
            t2s(news_res[0])
            t2s(news_res[1])
            t2s(news_res[2])

        if re.search('google photos', res):
            photos = obj.show_google_photos()
            print(photos)
            break

        if re.search('local photos', res):
            photos = obj.show_me_my_images()
            print(photos)
            break


        if re.search('tell me about', res):
            topic = res.split(' ')[-1]
            wiki_res = obj.tell_me(topic)
            print(wiki_res)
            t2s(wiki_res)

        if re.search('date', res):
            date = obj.tell_me_date()
            print(date)
            print(t2s(date))

        if re.search('time', res):
            time = obj.tell_me_time()
            print(time)
            t2s(time)

        if re.search('open', res):
            domain = res.split(' ')[-1]
            open_result = obj.website_opener(domain)
            print(open_result)
            t2s("")

        if re.search('launch', res):
            dict_app = {
                'chrome': 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
                'epic games': 'C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe'
            }

            app = res.split(' ', 1)[1]
            path = dict_app.get(app)
            if path is None:
                t2s('Application path not found')
                print('Application path not found')
            else:
                t2s('Launching: ' + app)
                obj.launch_any_app(path_of_app=path)

        if re.search('hello', res):
            print('Hi')
            t2s('Hi')

        if re.search('how are you', res):
            li = ['good', 'fine', 'great']
            response = random.choice(li)
            print(f"I am {response}")
            t2s(f"I am {response}")

        if re.search('your name|who are you', res):
            print("My name is Jarvis, I am your personal assistant")
            t2s("My name is Jarvis, I am your personal assistant")

        if re.search('send email',res):
            try:
                t2s( "Sure,Just let me know some details.Enter receiver's email and your message:")
                to = input("Receiver email:")
                content = input("Your msg:")
                sendemail(to, content)
                t2s("sent mail")
            except Exception as e:
                t2s(e)


        if re.search('thank you|thanks', res):
            t2s("Anytime Rishika,Anything else i can do?")

        if re.search('what can you do', res):
            li_commands = {
                "open websites": "Example: 'open youtube.com",
                "time": "Example: 'what time it is?'",
                "date": "Example: 'what date it is?'",
                "launch applications": "Example: 'launch chrome'",
                "tell me": "Example: 'tell me about India'",
                "weather": "Example: 'what weather/temperature in Mumbai?'",
                "news": "Example: 'news for today' ",
            }
            ans = """I can do lots of things, for example you can ask me time, date, weather in your city,
            I can open websites for you, launch application and more. See the list of commands-"""
            print(ans)
            pprint.pprint(li_commands)
            t2s(ans)
