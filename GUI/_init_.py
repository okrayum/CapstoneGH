import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import random

class WeatherDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Dashboard")
        self.root.geometry("900x700")
        
        # Initialize data storage
        self.weather_data = self.generate_sample_data()
        self.current_city = "New York"

        self.temperature_unit = tk.StringVar(value="F")
        self.city_var = tk.StringVar(value="New York")
        self.time_range_var = tk.StringVar(value="Last 7 Days")
        self.create_widgets()

    def create_widgets(self):
        # City selection
        city_label = ttk.Label(self.root, text="Select City:")
        city_label.pack(pady=5)
        self.city_combobox = ttk.Combobox(self.root, textvariable=self.city_var, values=["New York", "Los Angeles", "Chicago"])
        self.city_combobox.pack(pady=5)
        self.city_combobox.bind("<<ComboboxSelected>>", self.update_city)

        # Temperature unit selection
        unit_label = ttk.Label(self.root, text="Temperature Unit:")
        unit_label.pack(pady=5)
        self.unit_combobox = ttk.Combobox(self.root, textvariable=self.temperature_unit, values=["F", "C"])
        self.unit_combobox.pack(pady=5)
        self.unit_combobox.bind("<<ComboboxSelected>>", self.update_temperature_unit)

        # Time range selection
        time_range_label = ttk.Label(self.root, text="Time Range:")
        time_range_label.pack(pady=5)
        self.time_range_combobox = ttk.Combobox(self.root, textvariable=self.time_range_var, values=["Last 7 Days", "Last 30 Days"])
        self.time_range_combobox.pack(pady=5)
        self.time_range_combobox.bind("<<ComboboxSelected>>", self.update_time_range)

        # Plot area
        self.plot_frame = ttk.Frame(self.root)
        self.plot_frame.pack(fill=tk.BOTH, expand=True)

        # Control frame for inputs
        control_frame = ttk.Frame(self.root)
        control_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=10, pady=10)

        # Initial plot
        self.plot_weather_data()

        ttk.Label(control_frame, text="City:").grid(row=0, column=0, sticky=tk.W, pady=5)

        ttk.Label(control_frame, text="City:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.city_entry = ttk.Entry(control_frame, textvariable=self.city_var)
        self.city_entry.grid(row=0, column=1, sticky=tk.W, pady=5)

        ttk.Label(control_frame, text="Time Range:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.time_dropdown = ttk.Combobox
        control_frame,
        textvariable=self.time_range_var,
        values=["Last 7 Days", "Last 14 Days", "Last 30 Days"],
        state="readonly"

        self.time_dropdown.grid(row=1, column=1, sticky=tk.W, pady=5)
        self.time_dropdown.current(0)  # Set default value

        ttk.Label(control_frame, text="Units:").grid(row=2, column=0, sticky=tk.W, pady=5)
        ttk.Radiobutton(control_frame, text="Fahrenheit", variable=self.temperature_unit, value="F").grid(row=2, column=1, sticky=tk.W)
        ttk.Radiobutton(control_frame, text="Celsius", variable=self.temperature_unit, value="C").grid(row=2, column=2, sticky=tk.W)


        update_btn = ttk.Button(control_frame, text="Update", command=self.on_update_clicked)
        update_btn.grid(row=3, column=0, pady=10)

        clear_btn = ttk.Button(control_frame, text="Clear", command=self.on_clear_clicked)
        clear_btn.grid(row=3, column=1, pady=10)
        

        display_frame = ttk.LabelFrame(self.root, text="Current Weather", padding="10")
        display_frame.grid(row=1, column=1, sticky=(tk.N, tk.S, tk.W, tk.E), padx=10)

        self.temp_label = ttk.Label(display_frame, text="Temperature: --")
        self.temp_label.grid(row=0, column=0, sticky=tk.W, pady=5)

        self.humidity_label = ttk.Label(display_frame, text="Humidity: --")
        self.humidity_label.grid(row=1, column=0, sticky=tk.W, pady=5)

        self.precip_label = ttk.Label(display_frame, text="Precipitation: --")
        self.precip_label.grid(row=2, column=0, sticky=tk.W, pady=5)

        self.condition_label = ttk.Label(display_frame, text="Conditions: --")
        self.condition_label.grid(row=3, column=0, sticky=tk.W, pady=5)
        
        # Visualization Frame (Bottom)
        viz_frame = ttk.LabelFrame(self.root, text="Weather Trends", padding="10")
        viz_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)
        
        
        self.figure = Figure(figsize=(8, 4), dpi=100)
        self.plot = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, viz_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Configure grid weights for resizing - 
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        
        self.update_display()
        
        
    def generate_sample_data(self):
        """Generate sample weather data - DO NOT MODIFY THIS METHOD"""
        data = {}
        cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", 
                 "Seattle", "Miami", "Denver", "Boston", "Atlanta"]
        
        for city in cities:
            city_data = []
            base_temp = random.randint(40, 85)
            
            for i in range(30):  # 30 days of data
                date = datetime.now() - timedelta(days=29-i)
                temp = base_temp + random.randint(-15, 15)
                humidity = random.randint(30, 90)
                precipitation = random.choice([0, 0, 0, 0.1, 0.2, 0.5, 1.0, 2.0])
                
                city_data.append({
                    'date': date,
                    'temperature': temp,
                    'humidity': humidity,
                    'precipitation': precipitation,
                    'conditions': random.choice(['Sunny', 'Cloudy', 'Rainy', 'Partly Cloudy']),
                    'wind_speed': random.randint(0, 25),
                    'pressure': round(random.uniform(29.5, 30.5), 2)
                })
            
            data[city] = city_data
            
        return data
    
    def update_display(self):

        city = self.city_var.get().strip()
        if city not in self.weather_data:
            messagebox.showerror("City Not Found", f"No data for city: {city}")
        return

        self.current_city = city
        weather_list = self.weather_data[city]
        date_range = self.get_date_range()
        filtered = [entry for entry in weather_list if entry['date'].date() in date_range]

        if not filtered:
            messagebox.showinfo("No Data", "No weather data for selected date range.")
        return

        latest = filtered[-1]
        temp = latest['temperature']
        if self.temperature_unit.get() == "C":
            temp = self.convert_temperature(temp)

        self.temp_label.config(text=f"Temperature: {temp:.1f} °{self.temperature_unit.get()}")
        self.humidity_label.config(text=f"Humidity: {latest['humidity']}%")
        self.precip_label.config(text=f"Precipitation: {latest['precipitation']} in")
        self.condition_label.config(text=f"Conditions: {latest['conditions']}")

        self.update_chart()

        """Update all weather displays with current selections"""
       


    
    def update_chart(self):
        

        self.plot.clear()

        city = self.city_var.get().strip()
        if city not in self.weather_data:
            return

        data = self.weather_data[city]
        date_range = self.get_date_range()
        filtered = [d for d in data if d['date'].date() in date_range]

        dates = [entry['date'] for entry in filtered]
        temps = [entry['temperature'] for entry in filtered]

        if self.temperature_unit.get() == "C":
            temps = [self.convert_temperature(t) for t in temps]

        self.plot.plot(dates, temps, marker='o', label="Temperature")
        self.plot.set_title(f"{city} - Temperature Trend")
        self.plot.set_xlabel("Date")
        self.plot.set_ylabel(f"Temperature (°{self.temperature_unit.get()})")
        self.plot.legend()
        self.figure.autofmt_xdate()

        self.canvas.draw()