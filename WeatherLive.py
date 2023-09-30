# import all functions from the tkinter
from tkinter import *
from tkinter import messagebox
import requests
import json

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return round(celsius, 2)

def toggle_units():
    current_text = temp_field.get()
    if "Celsius" in current_text:
        # Convert to Fahrenheit
        celsius = float(current_text.split()[0])
        fahrenheit = (celsius * 9/5) + 32
        temp_field.delete(0, END)
        temp_field.insert(0, f"{fahrenheit:.2f} Fahrenheit")
        toggle_button.config(text="Switch to Celsius")
    else:
        # Convert to Celsius
        fahrenheit = float(current_text.split()[0])
        celsius = (fahrenheit - 32) * 5/9
        temp_field.delete(0, END)
        temp_field.insert(0, f"{celsius:.2f} Celsius")
        toggle_button.config(text="Switch to Fahrenheit")

def tell_weather():
    api_key = "a601cdd237e9ddd31f2806ae20f763fd"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = city_field.get()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature_kelvin = y["temp"]
        current_temperature_celsius = kelvin_to_celsius(current_temperature_kelvin)
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        temp_field.insert(15, str(current_temperature_celsius) + " Celsius")
        atm_field.insert(10, str(current_pressure) + " hPa")
        humid_field.insert(15, str(current_humidity) + " %")
        desc_field.insert(10, str(weather_description))
    else:
        messagebox.showerror("Error", "City Not Found\nPlease enter a valid city name")
        city_field.delete(0, END)

def clear_all():
    city_field.delete(0, END)
    temp_field.delete(0, END)
    atm_field.delete(0, END)
    humid_field.delete(0, END)
    desc_field.delete(0, END)
    city_field.focus_set()

if __name__ == "__main__":
    root = Tk()
    root.title("Weather Application")

    # Set the background colour of GUI window
    root.configure(background="light blue")

    # Set the configuration of GUI window
    root.geometry("425x175")

    # Create a Weather Gui Application label
    headlabel = Label(root, text="Weather Gui Application", fg='white', bg='Black')

    # Create a City name : label
    label1 = Label(root, text="City name: ", fg='white', bg='dark gray')

    # Create a City name : label
    label2 = Label(root, text="Temperature:", fg='white', bg='dark gray')

    # Create an atm pressure : label
    label3 = Label(root, text="Atmospheric Pressure:", fg='white', bg='dark gray')

    # Create a humidity : label
    label4 = Label(root, text="Humidity:", fg='white', bg='dark gray')

    # Create a description : label
    label5 = Label(root, text="Description:", fg='white', bg='dark gray')

    headlabel.grid(row=0, column=1)
    label1.grid(row=1, column=0, sticky="E")
    label2.grid(row=3, column=0, sticky="E")
    label3.grid(row=4, column=0, sticky="E")
    label4.grid(row=5, column=0, sticky="E")
    label5.grid(row=6, column=0, sticky="E")

    city_field = Entry(root)
    temp_field = Entry(root)
    atm_field = Entry(root)
    humid_field = Entry(root)
    desc_field = Entry(root)

    city_field.grid(row=1, column=1, ipadx="100")
    temp_field.grid(row=3, column=1, ipadx="100")
    atm_field.grid(row=4, column=1, ipadx="100")
    humid_field.grid(row=5, column=1, ipadx="100")
    desc_field.grid(row=6, column=1, ipadx="100")

    button1 = Button(root, text="Submit", bg="pink", fg="black", command=tell_weather)
    button2 = Button(root, text="Clear", bg="pink", fg="black", command=clear_all)
    button1.grid(row=2, column=1)
    button2.grid(row=7, column=1)

    # Create a button to toggle between Celsius and Fahrenheit
    toggle_button = Button(root, text="Switch to Fahrenheit", bg="light blue", fg="black", command=toggle_units)
    toggle_button.grid(row=3, column=2, padx=10, pady=10)

    # Start the GUI
    root.mainloop()
