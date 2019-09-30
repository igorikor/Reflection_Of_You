from tkinter import *
import datetime

main = Tk()

main.attributes('-fullscreen', True)
main.bind('<Escape>', lambda e: main.destroy())

screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()

#frames
f_top = Frame(main)
f_tw = Frame(f_top,bg = 'black')
f_de = Frame(f_top, bg = 'red')
f_date = Frame(f_de,bg = 'blue')
f_events = Frame(f_de,bg = 'pink')

f_weather = Frame(f_tw,  bg = 'black',width=3*(screen_width/4))
f_weather_val = Frame(f_weather,  bg = f_weather['bg'])
f_val_1 = Frame(f_weather_val, bg=f_weather['bg'])
f_val_2 = Frame(f_weather_val, bg=f_weather['bg'])
f_weather_img = Frame(f_weather,  bg = f_weather['bg'])

f_time = Frame(f_tw, bg = 'black',width=screen_width/4)

f_bot = Frame(main,bg = 'yellow')
f_news = Frame(f_bot,bg = 'orange')
f_space = Frame(f_bot,bg = 'black')

#text
time = Label(f_time,bg=f_tw['bg'],text='20:00',fg='white',font='Arial 200')
weather_val = Label(f_val_1,bg=f_weather['bg'],text='5C',fg='white',font='Arial 75')


#content


#frames pack
f_top.pack(expand=1,fill=BOTH)
f_tw.pack(expand=1,fill=BOTH)
#Время
f_time.pack(expand=1,fill=BOTH,side=LEFT)
time.place(relx=0.5,rely=0.5,anchor=CENTER)
#Погода
f_weather.pack(side=LEFT,expand=1,fill=BOTH)
f_weather_val.pack(side=TOP,expand=1,fill=BOTH)
f_val_1.pack(side=LEFT,expand=1,fill=BOTH)
f_val_2.pack(side=LEFT,expand=1,fill=BOTH)
f_weather_img.pack(side=TOP,expand=1,fill=BOTH)
weather_val.place(relx=.5,rely=.5,anchor=CENTER)

f_de.pack(expand=1,fill=BOTH)
f_date.pack(side=LEFT,expand=1,fill=BOTH)
f_events.pack(side=LEFT,expand=1,fill=BOTH)

f_bot.pack(expand=1,fill=BOTH)
f_news.pack(side=LEFT,expand=1,fill=BOTH)
f_space.pack(side=LEFT,expand=1,fill=BOTH)


main.mainloop()
