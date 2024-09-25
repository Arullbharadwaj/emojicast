import tkinter as tk
from tkinter import messagebox
import requests

# Function to fetch weather data
def get_weather(city):
    api_key = "2ca7e4008cf4127d1dde19ed6316a1e5"  # Replace with your OpenWeatherMap API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(base_url)
        response.raise_for_status()  # Raise an exception for bad responses (e.g., 404, 401)
        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        messagebox.showerror("HTTP Error", f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        messagebox.showerror("Connection Error", "Failed to connect to the server. Please check your connection.")
    except requests.exceptions.Timeout:
        messagebox.showerror("Timeout Error", "The request timed out. Please try again later.")
    except requests.exceptions.RequestException as err:
        messagebox.showerror("Error", f"An error occurred: {err}")
    
    return None

# Function to fetch relevant emoji based on weather
def get_weather_emoji(weather_description):
    weather_description = weather_description.lower()
    if "cloud" in weather_description:
        return "☁️"
    elif "clear" in weather_description:
        return "☀️"
    elif "rain" in weather_description:
        return "🌧️"
    elif "snow" in weather_description:
        return "❄️"
    elif "storm" in weather_description:
        return "🌩️"
    else:
        return "🌥️"

# Function to update the weather information
def update_weather():
    city = city_entry.get()
    weather_data = get_weather(city)
    
    if weather_data:
        weather_description = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        weather_emoji = get_weather_emoji(weather_description)
        
        result_label.config(text=f"Weather: {weather_description.capitalize()}\n"
                                 f"Temperature: {temperature}°C")
        emoji_label.config(text=weather_emoji, font=("Arial", 100))

# Set up the GUI
root = tk.Tk()
root.title("Weather Checker")
root.geometry("400x400")

# City entry field
city_label = tk.Label(root, text="Enter City:")
city_label.pack(pady=10)
city_entry = tk.Entry(root, width=20)
city_entry.pack(pady=10)

# Button to check weather
check_button = tk.Button(root, text="Check Weather", command=update_weather)
check_button.pack(pady=10)

# Labels to display weather info
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)
emoji_label = tk.Label(root, text="", font=("Arial", 50))
emoji_label.pack(pady=10)

root.mainloop()

