# hello my forth task Weather App
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime
import pytz
import requests
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

# icon
image = PhotoImage(file="image/logo.png")
root.iconphoto(False, image)

def getWeather():

    city = textfield.get()
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text=f"{round(location.longitude, 4)} °N, {round(location.latitude,4)} °E")

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I: %M %p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")

    # weather
    api_key = ""
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp']-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    t.config(text=f"{temp}°")
    t.place(x=400, y=280)
    c.config(text=f"{condition}| FEELS LIKE {temp}°")
    # Create a Label widget
    c.config(fg="#555")
    # c.place(x=550, y=340)
    c.place(x=290, y=230)

    w.config(text=(wind,"m/s"))
    h.config(text=(humidity,"%"))
    d.config(text=description)
    p.config(text=(pressure, "hPa"))


# search
Search_image = PhotoImage(file="image/search.png")
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

# search_icon
search_icon_path = "image/search_icon.png"
search_icon = ImageTk.PhotoImage(Image.open(search_icon_path))

# Create a canvas with rounded corners
canvas = tk.Canvas(root, width=50, height=50, bg="#404040", cursor="hand2", highlightthickness=0, borderwidth=0, relief='ridge')
canvas.create_image(25, 25, anchor=tk.CENTER, image=search_icon)
canvas.place(x=400, y=34)

# Bind the canvas to the function
canvas.bind("<Button-1>", lambda event: getWeather())
# logo
resized_logo_path = "image/App_icon.png"
resized_logo = Image.open(resized_logo_path)
image_resized = resized_logo.resize((350, 350))
Logo_image = ImageTk.PhotoImage(image_resized)
logo = Label(image=Logo_image)
logo.place(x=545, y=-26)

# Box frame
resized_image_path = "image/pngkey.png"
resized_image = Image.open(resized_image_path)
image_resized = resized_image.resize((450, 170))
box_image = ImageTk.PhotoImage(image_resized)
# box_image = PhotoImage(file="image/boxFrame.png")
box_myimage = Label(image=box_image)
# frame_myimage.pack(padx=5,pady=5, side=BOTTOM)
box_myimage.place(x=60, y=270)

# bottom box
frame = Frame(root, width=900, height=140, bg="#fc6a03")
frame.place(x=0, y=470)

frame = Frame(root, width=30, height=900, bg="#1ab5ef")
frame.place(x=-10, y=-20)

frame = Frame(root, width=30, height=900, bg="#1ab5ef")
frame.place(x=880, y=-20)

# timezone
timezone = Label(root, font=("Helvetica", 18, 'bold'), fg="green")
timezone.place(x=300, y=120)
long_lat = Label(root, font=("Helvetica", 9), fg="#555")
long_lat.place(x=360, y=170)

# time
name = Label(root, font=("arial", 15, "bold"), fg="#1ab5ef")
name.place(x=60, y=100)
clock = Label(root, font=("Helvetica", 18))
clock.place(x=60, y=130)

# label

label1 = Label(root, text="WIND:", font=("Helvetica", 13, 'bold'), fg="#fc6a03")
label1.place(x=75, y=290)

label2 = Label(root, text="HUMIDITY:", font=("Helvetica", 13, 'bold'), fg="#fc6a03")
label2.place(x=75, y=325)

label3 = Label(root, text="DESCRIPTION:", font=("Helvetica", 13, 'bold'), fg="#fc6a03")
label3.place(x=75, y=360)

label4 = Label(root, text="PRESSURE:", font=("Helvetica", 13, 'bold'), fg="#fc6a03")
label4.place(x=75, y=400)

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
c = Label(font=("arial", 15, 'bold'))

w = Label(root, font=("ariel", 13, "bold"))
w.place(x=230, y=290)
h = Label(root, font=("ariel", 13, "bold"))
h.place(x=230, y=325)
d = Label(root, font=("Helvetica", 13, "bold"))
d.place(x=230, y=360)
p = Label(root, font=("ariel", 13, "bold"))
p.place(x=230, y=400)

root.mainloop()
# root.config(bg="white")

#happy coding!