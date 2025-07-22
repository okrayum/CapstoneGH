import tkinter as tk
from tkinter import ttk

class PortalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My Dashboard")
        self.root.geometry("1000x700")
        self.create_main_layout()

    def create_main_layout(self):
        title = ttk.Label(self.root, text="Forecast & Chill", font=("Arial", 20, "bold"))
        title.pack(pady=10)

        # Create different rows for each portal
        self.create_portal("Weather Trends", ["7-Day Forecast", "Humidity Levels", "Temperature Chart"])
        self.create_portal("Music Picks", ["Morning Chill", "Top 10 Hits", "Local Vibes"])
        self.create_portal("Things To Do", ["Events Near You", "Free Activities", "Family Friendly"])
        self.create_portal("Daily Insight", ["Quote of the Day", "Fun Fact", "Today in History"])

    def create_portal(self, title_text, cards):
        frame = ttk.LabelFrame(self.root, text=title_text)
        frame.pack(fill=tk.X, padx=15, pady=10)

        canvas = tk.Canvas(frame, height=120)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(frame, orient=tk.HORIZONTAL, command=canvas.xview)
        scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        scrollable_frame = ttk.Frame(canvas)
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(xscrollcommand=scrollbar.set)

        # Add cards to the portal
        for item in cards:
            card = ttk.Frame(scrollable_frame, width=200, height=100, relief="raised", borderwidth=2)
            card.pack(side=tk.LEFT, padx=10, pady=10)
            label = ttk.Label(card, text=item)
            label.pack(expand=True)

def main():
    root = tk.Tk()
    app = PortalApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
