import tkinter as tk
from tkinter import font
import requests
import PIL
from PIL import Image, ImageTk

HEIGHT = 300
WIDTH = 400


# https://home.openweathermap.org/api_keys
# api.openweathermap.org/data/2.5/forecast?q={city name}&appid={your api key}
# 57cb9da61fdd7b88043f4e59b148d268

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        feels = weather['main']['feels_like']
        final_str = 'City: %s \nConditions: %s \nTemperature: %s °C \nFeels like: %s °C' % (name, desc, temp, feels)
    except:
        final_str = "There was a problem getting that information"
    return final_str


def get_weather(city):
    weather_key = '57cb9da61fdd7b88043f4e59b148d268'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'appid': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()
    print(response.json())
    # print(weather['name'])
    # print(weather['weather'][0]['description'])
    # print(weather['main']['temp'])
    # print(weather['main']['feels_like'])
    label['text'] = format_response(weather)

    icon_name = weather['weather'][0]['icon']
    open_image(icon_name)

# https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
def open_image(icon):
    size = int(lower_frame.winfo_height() * 0.5)
    img = ImageTk.PhotoImage(Image.open('./img/' + icon + '.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0, 0, anchor='nw', image=img)
    weather_icon.image = img


root = tk.Tk()

# Canvas
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='pattern-wallpaper.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Top frame
frame = tk.Frame(root, bg='#566573', bd=10)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.15, anchor='n')

entry = tk.Entry(frame, font=('Helvetica', 10))
entry.insert(0, ' ')
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get weather", font=('Helvetica', 10), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

# Lower frame
lower_frame = tk.Frame(root, bg='#566573', bd=10)
lower_frame.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.55, anchor='n')

label = tk.Label(lower_frame, font=('Helvetica', 10), anchor='nw', justify='left', bd=10)
label.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(label, bd=0, highlightthickness=0)
weather_icon.place(relx=0.65, rely=0, relwidth=1, relheight=0.75)

root.title('Weather App')

root.mainloop()
