import tkinter as tk
from PIL import Image, ImageTk
import requests
import time

def getWeather():
    try:
        city = textField.get()
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=45f0634c97257408725487537564366c"
    
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main'] if 'weather' in json_data else 'Weather data not available'
        main_data = json_data.get('main', {})
        temp = int(main_data.get('temp', 0) - 273.15)
        min_temp = int(main_data.get('temp_min', 0) - 273.15)
        max_temp = int(main_data.get('temp_max', 0) - 273.15)
        pressure = main_data.get('pressure', 'N/A')
        humidity = main_data.get('humidity', 'N/A')

        wind_data = json_data.get('wind', {})
        wind = wind_data.get('speed', 'N/A')

        sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
        sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

        final_info = condition + "\n" + str(temp) + "°C" 
        final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset

        # Clear previous results
        label1.config(text="")
        label2.config(text="")

        label1.config(text=final_info)
        label2.config(text=final_data)

    except Exception as e:
        label1.config(text="Error fetching data")
        label2.config(text=str(e))

def display_images():
    try:
        search_icon = Image.open("search_icon.png").resize((47 , 47))

        # Convert to RGBA mode with transparency
        search_icon = search_icon.convert("RGBA")

        # Create a Tkinter PhotoImage with transparency
        search_icon = ImageTk.PhotoImage(search_icon)

        # Create a Label widget for the search icon without background
        search_icon_label = tk.Label(canvas, image=search_icon, bg='#FFFFFF')  # Set the background color to match the canvas
        search_icon_label.image = search_icon
        search_icon_label.place(in_=textField, relx=1.0, rely=0, anchor='ne')  # Place the label on the right side of the text entry

    except Exception as e:
        print("Error displaying search icon:", str(e))

# Tkinter setup
canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
canvas.configure(bg='#340181')  # Set background color

f = ("Helvetica", 15, "bold")  # Use a different font
t = ("Sans Serif", 25, "bold")  # Use a different font

# Entry for city input
textField = tk.Entry(canvas, justify='center', width=20, font=t)
textField.pack(pady=20, ipady=5)  # Add inner padding to the entry widget
textField.focus()

# Call the function to display the search icon beside the text entry
display_images()

# Button for weather search
button = tk.Button(canvas, text="Get Weather", command=getWeather, font=t, bg='#101820', fg='#FEE715')  # Set button color
button.pack(pady=5)

# Labels for weather information
label1 = tk.Label(canvas, font=t, bg='#340181', fg='#ffffff')  # Set label colors
label1.pack()
label2 = tk.Label(canvas, font=f, bg='#340181', fg='#ffffff')  # Set label colors
label2.pack()

# Tkinter main loop
canvas.mainloop()
