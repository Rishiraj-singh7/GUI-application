import tkinter as tk
from tkinter import font

import requests

HEIGHT = 500
WIDTH = 600

def test_function():
    print("This is the entry:", entry)

#138dd139ed444a6fc62fa8610d1a22ea
#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        
        final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)
    except:
        final_str = 'There was a problem retrieving that information'

    return final_str


def get_weather(city):
    weather_key = '138dd139ed444a6fc62fa8610d1a22ea'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)

    
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_image = tk.Lable(root, image=background_image)
background_image.pack(relwidth=1, relheight=1)

frame = tk.frame(root, bg='#80c1ff',bd=5)
frame.place(relx=0.5, rely=0.1, relwidht=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, ('courier', 15))
entry.place( relwidht=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get))
button.place(relx=0.7, relwidht=0.3, relheight=1)
#button.grid(row=0, column=0)
#button.pack(side='left', fill='both') aotherway

lower_frame = tk.Frame(root,bg='#80c1ff',bd=10 )
lower_frame.place(relx=0.5, rely=0.25, relwidht=0.75, relheight=0.6, anchor= 'n')

label = tk.Label(lower_frame, font=('courier', 15), anchor= 'nw', justify='left', bd=4)
label.place( relwidht=1, relheight=1)

root.mainloop()

