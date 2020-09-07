#Created By :- Kumar Kad
# Company :- KD's Technologies

import os
import json
import urllib.request
import datetime
from tkinter import *

window= Tk() 
window.geometry('1200x1500')
window.title("IP-Tracer")

lbl = Label(window, text="IP Address : ",bg='red')
lbl.grid(column=0, row=2)
lbl1 = Label(window, text="                     ",bg='green')
lbl1.grid(column=1, row=2)

lbl2 = Label(window, text="Status : ",bg='yellow')
lbl2.grid(column=0, row=3)
lbl3= Label(window, text="                     ",bg='orange')
lbl3.grid(column=1, row=3)


lbl4= Label(window, text="Time : ",bg='red')
lbl4.grid(column=0, row=4)
lbl5= Label(window, text="                    ",bg='green')
lbl5.grid(column=1, row=4)

lbl6= Label(window, text="Continent : ",bg='yellow')
lbl6.grid(column=0, row=5)
lbl7 = Label(window, text="                     ",bg='orange')
lbl7.grid(column=1, row=5)

lbl8 = Label(window, text="Continent Code : ",bg='red')
lbl8.grid(column=0, row=6)
lbl9 = Label(window, text="                     ",bg='green')
lbl9.grid(column=1, row=6)

lbl10= Label(window, text="Country: ",bg='yellow')
lbl10.grid(column=0, row=7)
lbl11= Label(window, text="                     ",bg='orange')
lbl11.grid(column=1, row=7)

lbl12 = Label(window, text="Country Code : ",bg='red')
lbl12.grid(column=0, row=8)
lbl13= Label(window, text="                     ",bg='green')
lbl13.grid(column=1, row=8)

lbl14= Label(window, text="Region : ",bg='yellow')
lbl14.grid(column=0, row=9)
lbl15= Label(window, text="                     ",bg='orange')
lbl15.grid(column=1, row=9)

lbl16 = Label(window, text="Region Name : ",bg='red')
lbl16.grid(column=0, row=10)
lbl17= Label(window, text="                     ",bg='green')
lbl17.grid(column=1, row=10)

lbl18 = Label(window, text="City : ",bg='yellow')
lbl18.grid(column=0, row=11)
lbl19 = Label(window, text="                     ",bg='orange')
lbl19.grid(column=1, row=11)

lbl20 = Label(window, text="Location : ",bg='red')
lbl20.grid(column=0, row=12)
lbl21 = Label(window, text="                     ",bg='green')
lbl21.grid(column=1, row=12)

lbl22= Label(window, text="Zip Code : ",bg='yellow')
lbl22.grid(column=0, row=13)
lbl23 = Label(window, text="                     ",bg='orange')
lbl23.grid(column=1, row=13)

lbl24= Label(window, text="Timezone : ",bg='red')
lbl24.grid(column=0, row=14)
lbl25= Label(window, text="                     ",bg='green')
lbl25.grid(column=1, row=14)

lbl26= Label(window, text="National Currency : ",bg='yellow')
lbl26.grid(column=0, row=15)
lbl27 = Label(window, text="                     ",bg='orange')
lbl27.grid(column=1, row=15)

lbl28= Label(window, text="ISP Name : ",bg='red')
lbl28.grid(column=0, row=16)
lbl29= Label(window, text="                     ",bg='green')
lbl29.grid(column=1, row=16)

lbl30= Label(window, text="Organization Name : ",bg='yellow')
lbl30.grid(column=0, row=17)
lbl31 = Label(window, text="                     ",bg='orange')
lbl31.grid(column=1, row=17)

lbl32= Label(window, text="AS Number & org. : ",bg='red')
lbl32.grid(column=0, row=18)
lbl33 = Label(window, text="                     ",bg='green')
lbl33.grid(column=1, row=18)

lbl34 = Label(window, text="AS name : ",bg='yellow')
lbl34.grid(column=0, row=19)
lbl35 = Label(window, text="                     ",bg='orange')
lbl35.grid(column=1, row=19)

lbl36= Label(window, text="Mobile : ",bg='red')
lbl36.grid(column=0, row=20)
lbl37= Label(window, text="                     ",bg='green')
lbl37.grid(column=1, row=20)

lbl38= Label(window, text="Proxy , VPN : ",bg='yellow')
lbl38.grid(column=0, row=21)
lbl39= Label(window, text="                     ",bg='orange')
lbl39.grid(column=1, row=21)

lbl40= Label(window, text="Hosting : ",bg='red')
lbl40.grid(column=0, row=22)
lbl41 = Label(window, text="                     ",bg='green')
lbl41.grid(column=1, row=22)

txt = Entry(window,width=20)
txt.grid(column=0, row=0)

def clicked():
#	ip='49.35.196.106'
	ip = txt.get()
	url="http://ip-api.com/json/"
	fld='?fields=66846719'
	response=urllib.request.urlopen(url+ip+fld)
	data=response.read()
	values=json.loads(data)
	
	lbl1.configure(text= values['query'])
	lbl3.configure(text=values['status'])
	lbl5.configure(text=str(datetime.datetime.now()))
	lbl7.configure(text=values['continent'])
	lbl9.configure(text=values['continentCode'])
	lbl11.configure(text=values['country'])
	lbl13.configure(text=values['countryCode'])
	lbl15.configure(text=values['region'])
	lbl17.configure(text=values['regionName'])
	lbl19.configure(text=values['city'])
	lbl21.configure(text=str(values['lat'])+str(values['lon']))
	lbl23.configure(text=values['zip'])
	lbl25.configure(text=values['timezone'])
	lbl27.configure(text=values['currency'])
	lbl29.configure(text=values['isp'])
	lbl31.configure(text=values['org'])
	lbl33.configure(text=values['as'])
	lbl35.configure(text=values['asname'])

	lbl37.configure(text=str(values['mobile']))
	lbl39.configure(text=str(values['proxy']))
	lbl41.configure(text=str(values['hosting']))
	
btn = Button(window, text="Trace",command=clicked)
btn.grid(column=1, row=0)
window.mainloop() 