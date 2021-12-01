from tkinter import *
import requests
import json

root = Tk()
root.title('Weather app')
root.iconbitmap('./icon.ico')
root.geometry('600x100')

# zip lookup function
def zipLookup():
 try:
  apiRequest = requests.get('https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=' + zip.get() + '&distance=5&API_KEY=C5F252C7-1F7B-4549-87E1-251DC1084F67')
  api = json.loads(apiRequest.content)
  city = api[0]['ReportingArea']
  quality = api[0]['AQI']
  category = api[0]['Category']['Name']
  
  if category == 'Good':
   weatherColor = '#0C0'
  elif category == 'Moderate':
   weatherColor = '#FFFF00'
  elif category == 'Unhealthy for Sensitive Groups':
   weatherColor = '#FF9900'
  elif category == 'Unhealthy':
   weatherColor = '#FF0000'
  elif category == 'Very Unhealthy':
   weatherColor = '#990066'
  elif category == 'Hazardous':
   weatherColor = '#660000'
  
  root.configure(background=weatherColor)
  
  myLabel = Label(root, text=city + ' Air Aquality ' + str(quality) + ' ' + category, font=('Helvetica', 20), background=weatherColor)
  myLabel.grid(row=1, column=0, columnspan=2) 
 except Exception as e:
  api = 'Error'


 
zip = Entry(root)
zip.grid(row=0, column=0, sticky=W+E+N+S)

zipButton = Button(root, text='Lookup zipcode', command=zipLookup)
zipButton.grid(row=0, column=1, sticky=W+E+N+S)

root.mainloop()