from tkinter import *
from PIL import Image, ImageTk
import datetime as dt
import requests

#Функции

#Получение данных
def weather():
	token = '5450a4138a3e282e322f96a369ce7c30'
	data = requests.get("http://ipinfo.io/json").json()
	location = data['loc'].split(',')
	location = list(map(float, location))
	weather = requests.get("https://api.darksky.net/forecast/%s/%f,%f" % (token, location[0], location[1])).json()
	temp = weather['currently']['temperature']
	temp = (temp-32) * 5/9
	return str(int(temp))

#Апдейты
def update():
	time.config(text = dt.datetime.now().strftime("%H:%M:%S"))
	main.after(1000, update)

def update_weather():
	weather_val.config(text = weather())
	main.after(15000, update)


#Основная часть
main = Tk()

#Описание переменных
screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()



#Полноэкранный режим + выход по нажатию Esc
main.attributes('-fullscreen', True)
main.bind('<Escape>', lambda e: main.destroy())


#Описание фреймов
f_top = Frame(main)

#Погода
f_tw = Frame(f_top)
f_weather = Frame(f_tw, bg = 'black', width=3*(screen_width/4))
f_weather_val = Frame(f_weather,  bg = f_weather['bg'])
f_weather_freespace = Frame(f_weather,  bg = f_weather['bg'])
f_val_1 = Frame(f_weather_val, bg=f_weather['bg'])
f_val_2 = Frame(f_weather_val, bg=f_weather['bg'])

#Время
f_time = Frame(f_tw, bg = 'black',width=screen_width/4)

f_de = Frame(f_top)

f_date = Frame(f_de,bg = 'blue')
f_events = Frame(f_de,bg = 'pink')

f_bot = Frame(main,bg = 'yellow')
f_news = Frame(f_bot,bg = 'orange')


f_space = Frame(f_bot,bg = 'black')

#text
time = Label(f_time,bg=f_weather['bg'],text=dt.datetime.now().strftime("%H:%M:%S"),fg='white',font='Arial 100')
weather_val = Label(f_val_1,bg=f_weather['bg'],text=weather()+"°C",fg='white',font='Arial 75')

stim = ("weather_icons\\sun.png")
PIL_Image = Image.open(stim)
PIL_image_small = PIL_Image.resize((120,120), Image.ANTIALIAS)
img = ImageTk.PhotoImage(PIL_image_small)
f_weather_img = Label(f_val_2, bg='black',image = img)

#Упаковка

#top
f_top.pack(expand=1,fill=BOTH)

#time/weather
f_tw.pack(expand=1,fill=BOTH)

#Время
f_time.pack(expand=1,fill=BOTH,side=LEFT)
time.place(relx=0.5,rely=0.5,anchor=CENTER)

#Погода
f_weather.pack(side=LEFT,expand=1,fill=BOTH)
f_weather_val.pack(side=TOP,expand=1,fill=BOTH)
f_weather_freespace.pack(side=TOP,expand=1,fill=BOTH)
f_val_1.pack(side=LEFT,expand=1,fill=BOTH)
f_val_2.pack(side=LEFT,expand=1,fill=BOTH)
weather_val.place(relx=.5,rely=.5,anchor=CENTER)
f_weather_img.place(relx=.5,rely=.5,anchor=CENTER)

f_de.pack(expand=1,fill=BOTH)
f_date.pack(side=LEFT,expand=1,fill=BOTH)
f_events.pack(side=LEFT,expand=1,fill=BOTH)

f_bot.pack(expand=1,fill=BOTH)
f_news.pack(side=LEFT,expand=1,fill=BOTH)
f_space.pack(side=LEFT,expand=1,fill=BOTH)

main.after(1000, update)
main.after(15000, update_weather)

main.mainloop()
