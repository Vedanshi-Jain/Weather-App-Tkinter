import tkinter as tk
import requests
from PIL import Image, ImageTk

root=tk.Tk()

# WEATHER

def response(weather):
    b=weather['weather'][0]['description']
    c=weather['main']['temp']
    e=weather['main']['humidity']
    f=weather['wind']['speed']
    final='Condition : %s\nTemperature (°C) : %s\nRelative Humidity  : %s\nWind Speed (m/s) : %s'%(b.capitalize(),c-273.15,e,f)
    return final

def openImage(iconName):
    size=int(display.winfo_height()*0.25)
    img=ImageTk.PhotoImage(Image.open('.\weather_icons/'+iconName+'.png').resize((size,size)))
    weatherIconDisplay.create_image(0,0,anchor='nw',image=img)
    weatherIconDisplay.image=img

def getWeather(city):
    try:
        weatherKey = 'weather key'
        urlLatLon = 'URL Lat Lon'
        urlWeather='URL weather'

        paramsForLatLon={'APPID':weatherKey,'q':city}
        responseLatLon=requests.get(urlLatLon,paramsForLatLon)

        paramsWeather={'lat':responseLatLon.json()[0]['lat'],'lon':responseLatLon.json()[0]['lon'],'APPID':weatherKey}
        responseWeather=requests.get(urlWeather,params=paramsWeather)

        weather=responseWeather.json()

        result['text']=response(weather)
        iconName=weather['weather'][0]['icon']
        openImage(iconName)

    except:
        result['text']='There was a problem in retrieving the information.'

# TITLE AND BOX

root.title("Weather App")
root.geometry("900x600+500+220")
root.resizable(False,False)

# BACKGROUND

img=Image.open('.\bg.png')
img=img.resize((900,600))
imgPhoto=ImageTk.PhotoImage(img)

bgLabel=tk.Label(root,image=imgPhoto)
bgLabel.place(x=0,y=0,width=900,height=600)

# HEADING

title=tk.Label(bgLabel,bg="#A7EFFD",fg="#803D06",text='Access current weather data for any location on earth including over 200,000 cities!\nType the name of city :',font=('times new roman',15),padx=2,pady=2)
title.place(x=108,y=25)

# ICON

imgIcon=tk.PhotoImage(file='.\logo.png')
root.iconphoto(False,imgIcon)

# SEARCH BOX

search=tk.Frame(bgLabel,bg="#0A7F35",bd=5)
search.place(x=95,y=85,width=700,height=50)

searchBox=tk.Entry(search,font=("times new roman",18),bd=1)
searchBox.place(x=0,y=0,width=540,height=40)

btn=tk.Button(search,text="Get Weather",bd=1,font=('times new roman',15,'bold'),fg="#030587",bg="#EFF594",command=lambda: getWeather(searchBox.get()))
btn.place(x=550,y=0,width=140,height=40)

# DISPLAY BOX

display=tk.Frame(bgLabel,bg="#6A6FCC",bd=5)
display.place(x=95,y=155,width=700,height=410)

result=tk.Label(display,font=('times new roman',22),bg="white",justify='left',anchor='nw',bd=10,fg="#12564F")
result.place(x=0,y=0,width=690,height=400)

weatherIconDisplay=tk.Canvas(result,bg='white',border=None,highlightthickness=0)
weatherIconDisplay.place(x=545,y=10,width=101,height=101)

# MAINLOOP

root.mainloop()
