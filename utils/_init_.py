import tkinter as tk
from tkinter import messagebox
#import requests
import csv

# Create main window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")

# Add widgets
city_label = tk.Label(root, text="Enter City:")
city_label.pack(pady=10)

city_entry = tk.Entry(root, width=30)
city_entry.pack()

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)