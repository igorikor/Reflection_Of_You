from tkinter import *
from PIL import Image, ImageTk
import datetime as dt
import requests
from feedparser import *
from threading import Thread
from time import sleep

img = ""

weather_icon_lib = {
	'clear-day':'weather_icons/sun.png',
	'clear-night':'weather_icons/sun.png',
	'rain':'weather_icons/rainy.png',
	'snow':'weather_icons/rainy.png',
	'wind':'weather_icons/cloudy.png',
	'fog':'weather_icons/cloudy.png',
	'cloudy':'weather_icons/cloudy.png',
	'partly-cloudy-day':'weather_icons/cloudy.png',
	'partly-cloudy-night':'weather_icons/cloudy.png'
}

#Функции

def calc_percentage():
	normal_width = 1920
	normal_height = 1080
	screen_width = main.winfo_screenwidth()
	screen_height = main.winfo_screenheight()
	percentage_width = screen_width / (normal_width / 100)
	percentage_height = screen_height / (normal_height / 100)
	scale_factor = ((percentage_width + percentage_height) / 2) / 100
	return scale_factor

#Получение данных
def weather(token): #Подтяжка погоды с DarkSky
	data = requests.get("http://ipinfo.io/json").json()
	location = data['loc'].split(',')
	location = list(map(float, location))
	weather = requests.get("https://api.darksky.net/forecast/%s/%f,%f" % (token, location[0], location[1])).json()

	temp = weather['currently']['temperature']
	weather_type = weather['currently']['icon']
	
	temp = (temp-32) * 5/9

	return str(int(temp))+' '+ weather_type

def img_parse(icon,w_lib=weather_icon_lib): #Преобразование изображение в изображение типа TK
	global img

	scale_factor = calc_percentage()

	stim = (w_lib[icon])
	PIL_Image = Image.open(stim)
	PIL_image_small = PIL_Image.resize((int(120 * scale_factor),int(120 * scale_factor)), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(PIL_image_small)
	return img

#Апдейты
def update(): #Обновление даты и времени
	scale_factor = calc_percentage()
	time.config(text = dt.datetime.now().strftime("%H:%M:%S"),font = 'Arial '+str(int(90 * scale_factor)))
	day_mounth.config(text = dt.datetime.now().strftime("%d.%m.%Y"), font = 'Arial '+str(int(55 * scale_factor)))


def update_weather(tmp,w_icn): #Отрисовка погоды
	scale_factor = calc_percentage()

	weather_val.config(text=tmp+"°С", font = 'Arial '+str(int(70 * scale_factor)))
	f_weather_img.config(image=w_icn)


def update_news(): #Получение хедлайнов с сайта кванториума
	site = parse('https://kvantorium-perm.ru/feed/')
	text = []
	for i in range(5):
		text.append(site.entries[i].published[5:12]+site.entries[i].published[16:22]+ "      " + site.entries[i].title)

	return text

#Основная часть
main = Tk()
main.config(cursor='none')

#Описание переменных
normal_width = 1920
normal_height = 1080
screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()
percentage_width = screen_width / (normal_width / 100)
percentage_height = screen_height / (normal_height / 100)
scale_factor = ((percentage_width + percentage_height) / 2) / 100

token = '5450a4138a3e282e322f96a369ce7c30'

#Полноэкранный режим + выход по нажатию Esc
main.attributes('-fullscreen', True)
main.bind('<Escape>', lambda e: main.destroy())


#------------------------------------------------------------------------------------------Описание фреймов----------------------------------------------------------------------------------------------
f_top = Frame(main)

#Погода
f_tw = Frame(f_top)
f_weather = Frame(f_tw, bg = 'black', width=3*(screen_width/3))
f_weather_val = Frame(f_weather,  bg = f_weather['bg'])
f_weather_freespace = Frame(f_weather,  bg = f_weather['bg'])
f_val_1 = Frame(f_weather_val, bg=f_weather['bg'])
f_val_2 = Frame(f_weather_val, bg=f_weather['bg'])

#Время
f_time = Frame(f_tw, bg = 'black',width=screen_width/10)

f_de = Frame(f_top)
#Дата
day_mounth = Label(f_weather_freespace, text="01.01.2002", fg='white', bg='black', font='Arial '+str(round(90 * scale_factor)))

f_kw_evetns = Frame(f_de, bg = 'grey', width = screen_width)

f_bot = Frame(main,bg = 'black')
f_news = Frame(f_bot,bg = 'black',height=screen_height/3)


f_space = Frame(f_bot,bg = 'black')

#Content
time = Label(f_time,bg=f_weather['bg'],text=dt.datetime.now().strftime("%H:%M:%S"),fg='white',font='Arial '+str(round(140 * scale_factor)))

weather_val = Label(f_val_1,bg=f_weather['bg'], fg='white',font='Arial '+str(round(70 * scale_factor)))
f_weather_img = Label(f_val_2, image=img_parse('clear-day') ,bg='black')

kw_evetns = Text(f_kw_evetns, height=0,width=0,font='Helvetica '+str(round(28 * scale_factor)),fg='white',bg='black', bd=0)

#-------------------------------------------------------------------------------------------------Упаковка-----------------------------------------------------------------------------------------------
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
#date
kw_evetns.pack(expand=1,fill=BOTH)
f_kw_evetns.pack(side=LEFT,expand=1,fill=BOTH)	
day_mounth.place(relx=.5,rely=.5,anchor=CENTER)


f_bot.pack(expand=1,fill=BOTH)
f_news.pack(side=LEFT,expand=1,fill=BOTH)
f_space.pack(side=LEFT,expand=1,fill=BOTH)

#-----------------------------------------------------------Подтяжка многопотока---------------------------------------------------------
def up():
	while True:
		update()
		sleep(0.2)

def text(text,token=token):
	while True:
		w = weather(token).split()
		update_weather(w[0],img_parse(w[1]))
		nw = update_news()
		text.delete('1.0','end')
		for i in range(len(nw)):
			text.insert('end',nw[i]+'\n')
		sleep(5*60)

draw_data = Thread(target=up,daemon=True)
draw_time = Thread(target=text, args=(kw_evetns,),daemon=True)
draw_data.start()
draw_time.start()

main.mainloop()
