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
        self.selected_days = tk.StringVar(value="7")

        
        # TODO: Add instance variables for storing user selections
        # Example: self.temperature_unit = "F"  # or "C"
        
        # Create the GUI
        self.create_widgets()
        self.update_display()

        
    def create_widgets(self):
        """Create and arrange all GUI widgets"""
        
          # Title Frame
        title_frame = ttk.Frame(self.root, padding="10")
        title_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E))
        title_label = ttk.Label(title_frame, text="Weather Dashboard", font=('Arial', 16, 'bold'))
        title_label.pack()

        # Control Frame
        control_frame = ttk.LabelFrame(self.root, text="Controls", padding="10")
        control_frame.grid(row=1, column=0, sticky=(tk.N, tk.S, tk.W, tk.E), padx=10)

        # City input
        ttk.Label(control_frame, text="City:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.city_entry = ttk.Entry(control_frame, width=25)
        self.city_entry.insert(0, "New York")
        self.city_entry.grid(row=0, column=1, pady=5)

        # Date range dropdown
        ttk.Label(control_frame, text="Date Range:").grid(row=1, column=0, sticky=tk.W)
        self.range_combobox = ttk.Combobox(control_frame, textvariable=self.selected_days, values=["7", "14", "30"], state="readonly")
        self.range_combobox.grid(row=1, column=1, pady=5)

        # Temp unit radio buttons
        ttk.Label(control_frame, text="Units:").grid(row=2, column=0, sticky=tk.W)
        ttk.Radiobutton(control_frame, text="Fahrenheit", variable=self.temperature_unit, value="F").grid(row=2, column=1, sticky=tk.W)
        ttk.Radiobutton(control_frame, text="Celsius", variable=self.temperature_unit, value="C").grid(row=3, column=1, sticky=tk.W)

        # Buttons
        update_button = ttk.Button(control_frame, text="Update", command=self.on_update_clicked)
        update_button.grid(row=4, column=0, pady=10)

        clear_button = ttk.Button(control_frame, text="Clear", command=self.on_clear_clicked)
        clear_button.grid(row=4, column=1, pady=10)

        # Display Frame
        display_frame = ttk.LabelFrame(self.root, text="Current Weather", padding="10")
        display_frame.grid(row=1, column=1, sticky=(tk.N, tk.S, tk.W, tk.E), padx=10)

        self.temp_label = ttk.Label(display_frame, text="Temperature: --")
        self.temp_label.grid(row=0, column=0, sticky=tk.W, pady=5)

        self.humidity_label = ttk.Label(display_frame, text="Humidity: --")
        self.humidity_label.grid(row=1, column=0, sticky=tk.W, pady=5)

        self.condition_label = ttk.Label(display_frame, text="Conditions: --")
        self.condition_label.grid(row=2, column=0, sticky=tk.W, pady=5)

        # Visualization Frame
        viz_frame = ttk.LabelFrame(self.root, text="Weather Trends", padding="10")
        viz_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)

        self.figure = Figure(figsize=(8, 4), dpi=100)
        self.plot = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, viz_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        
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
        """Update all weather displays with current selections"""
        # TODO: Implement this method
        # Requirements:
        # 1. Get the current city from the entry field
        # 2. Get the selected date range from your dropdown
        # 3. Update all weather information labels
        # 4. Handle the case where city doesn't exist in data
        # 5. Call update_chart() to refresh the visualization

        city = self.city_entry.get().strip()
        if city not in self.weather_data:
            messagebox.showerror("Error", f"No data available for '{city}'")
            return

        self.current_city = city
        data = self.weather_data[city][-int(self.selected_days.get()):]
        if not data:
            messagebox.showinfo("Notice", "No data for selected range.")
            return

        latest = data[-1]
        temp = latest['temperature']
        if self.temperature_unit.get() == "C":
            temp = self.convert_temperature(temp, to_celsius=True)

        self.temp_label.config(text=f"Temperature: {temp:.1f}°{self.temperature_unit.get()}")
        self.humidity_label.config(text=f"Humidity: {latest['humidity']}%")
        self.condition_label.config(text=f"Conditions: {latest['conditions']}")

        self.update_chart()
        #pass
    
    def update_chart(self):
        """Update the matplotlib chart based on current selections"""
        # TODO: Implement this method
        # Requirements:
        # 1. Clear the current plot using self.plot.clear()
        # 2. Get weather data for the selected city and date range
        # 3. Extract dates and temperatures (or other metrics)
        # 4. Create a line plot or other visualization
        # 5. Add proper labels, title, and formatting
        # 6. Call self.canvas.draw() to refresh the display
        
        # Hint: Use self.figure.autofmt_xdate() for date formatting

        self.plot.clear()
        city = self.current_city
        if city not in self.weather_data:
            return

        data = self.weather_data[city][-int(self.selected_days.get()):]
        dates = [entry['date'] for entry in data]
        temps = [entry['temperature'] for entry in data]

        if self.temperature_unit.get() == "C":
            temps = [self.convert_temperature(t, to_celsius=True) for t in temps]

        self.plot.plot(dates, temps, label='Temperature', marker='o')
        self.plot.set_title(f"Temperature Trends - {city}")
        self.plot.set_ylabel(f"Temp (°{self.temperature_unit.get()})")
        self.plot.set_xlabel("Date")
        self.plot.legend()
        self.figure.autofmt_xdate()
        self.canvas.draw()
        #pass
    
    def on_update_clicked(self):
        """Handle update button click"""
        # TODO: Implement this method
        # Requirements:
        # 1. Validate user input (check if city exists, etc.)
        # 2. Show error message if validation fails
        # 3. Update the display if validation passes
        # 4. You may want to store the current city as self.current_city

        city = self.city_entry.get().strip()
        if not city:
            messagebox.showwarning("Input Error", "Please enter a city.")
            return
        if city not in self.weather_data:
            messagebox.showerror("City Not Found", f"'{city}' is not in the database.")
            return
        self.update_display()
        #pass
    
    def on_clear_clicked(self):
        """Handle clear/reset button click"""
        # TODO: Implement this method
        # Requirements:
        # 1. Reset all input fields to default values
        # 2. Reset the display to show default city
        # 3. Clear or reset the chart

        self.city_entry.delete(0, tk.END)
        self.city_entry.insert(0, "New York")
        self.temperature_unit.set("F")
        self.selected_days.set("7")
        self.update_display()
        #pass
    
    def convert_temperature(self, temp_f, to_celsius=True):
        """Helper method to convert between temperature units"""
        # TODO: Implement temperature conversion
        # F to C: (F - 32) * 5/9
        # C to F: C * 9/5 + 32

        return (temp_f - 32) * 5/9 if to_celsius else (temp_f * 9/5) + 32
        #pass
    
    def get_date_range(self):
        """Helper method to get the selected date range"""
        # TODO: Implement based on your date range selector
        # Should return a list of dates based on user selection
        # For example: last 7 days, last 14 days, last 30 days

        days = int(self.selected_days.get())
        return [datetime.now() - timedelta(days=i) for i in range(days)][::-1]
        #pass

def main():
    root = tk.Tk()
    app = WeatherDashboard(root)
    root.mainloop()

if __name__ == "__main__":
    main()
