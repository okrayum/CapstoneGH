from dotenv import load_dotenv
from tkinter import messagebox
import requests
import os
load_dotenv()
api_key = os.getenv("API_KEY")

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"API request failed: {e}")
        return None 