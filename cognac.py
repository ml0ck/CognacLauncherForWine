import tkinter as tk
from tkinter import ttk
import subprocess
import os
import webbrowser
import time

# Function to display a message in the text area
def show_message(message):
    message_area.config(state=tk.NORMAL)
    message_area.delete(1.0, tk.END)
    message_area.insert(tk.END, message)
    message_area.config(state=tk.DISABLED)

# Typewriter effect for the credit message
def typewriter_effect(text):
    message_area.config(state=tk.NORMAL)
    message_area.delete(1.0, tk.END)
    for char in text:
        message_area.insert(tk.END, char)
        message_area.update()
        time.sleep(0.05)  # Adjust speed for typewriter effect
    message_area.config(state=tk.DISABLED)

# Function to show credits with clickable GitHub link
def show_credits():
    credit_message = (
        "Cognac Wine Manager\n"
        "Created by: Fun\n"
        "Purpose: Manage Windows applications via Wine on Linux\n"
        "Potential: Simplifies running and managing Windows apps for Linux users\n"
        "Credits: This program was developed for the open-source community.\n"
        "GitHub: https://github.com/ml0ck"
    )
    typewriter_effect(credit_message)

# Function to check if Wine is installed
def check_wine_installed():
    try:
        subprocess.run(["wine", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

# Function to launch a .exe with Wine
def on_launch_exe():
    exe_path = "C:/path/to/your/exe/file.exe"  # Update with actual path
    if check_wine_installed():
        show_message(f"Launching {exe_path} with Wine...")
        subprocess.run(["wine", exe_path])
    else:
        show_message("Wine is not installed or not configured correctly.")

# Function to navigate Wine directory
def on_navigate_wine_directory():
    wine_directory = os.path.expanduser("~/.wine")
    if os.path.exists(wine_directory):
        subprocess.run(["xdg-open", wine_directory])
        show_message(f"Opened Wine directory: {wine_directory}")
    else:
        show_message("Wine directory not found.")

# Function to show Wine version
def on_show_wine_version():
    if check_wine_installed():
        result = subprocess.run(["wine", "--version"], stdout=subprocess.PIPE)
        show_message(f"Wine version: {result.stdout.decode('utf-8').strip()}")
    else:
        show_message("Wine is not installed.")

# Function to show Wine path
def on_show_wine_path():
    try:
        result = subprocess.run(["which", "wine"], stdout=subprocess.PIPE)
        wine_path = result.stdout.decode('utf-8').strip()
        show_message(f"Wine path: {wine_path}")
    except Exception as e:
        show_message(f"Error finding Wine path: {str(e)}")

# Function to open a URL
def open_url(url):
    webbrowser.open(url, new=1)

# Tkinter application initialization
root = tk.Tk()
root.title("Cognac Wine Manager")
root.geometry("1000x700")  # Wider window at startup
root.config(bg="#2e3b44")

# Main interface with stylized buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=20)

# Buttons with modern styling
launch_exe_button = ttk.Button(button_frame, text="Launch .exe", width=25, command=on_launch_exe)
launch_exe_button.grid(row=0, column=0, padx=10, pady=10)

navigate_wine_button = ttk.Button(button_frame, text="Open Wine Directory", width=25, command=on_navigate_wine_directory)
navigate_wine_button.grid(row=1, column=0, padx=10, pady=10)

show_wine_version_button = ttk.Button(button_frame, text="Show Wine Version", width=25, command=on_show_wine_version)
show_wine_version_button.grid(row=2, column=0, padx=10, pady=10)

show_wine_path_button = ttk.Button(button_frame, text="Show Wine Path", width=25, command=on_show_wine_path)
show_wine_path_button.grid(row=3, column=0, padx=10, pady=10)

credit_button = ttk.Button(button_frame, text="Credit", width=25, command=show_credits)
credit_button.grid(row=4, column=0, padx=10, pady=10)

# Text area for displaying messages with scroll bar
message_frame = ttk.Frame(root)
message_frame.pack(pady=20)

# Message area and scrollbar
message_area = tk.Text(message_frame, height=8, width=85, wrap=tk.WORD, bg="#1e2a32", fg="white", font=("Arial", 12))
scrollbar = ttk.Scrollbar(message_frame, orient="vertical", command=message_area.yview)
message_area.config(yscrollcommand=scrollbar.set)

message_area.pack(side="left", padx=(10, 0))
scrollbar.pack(side="right", fill="y")

message_area.config(state=tk.DISABLED)

# Link buttons
links_frame = ttk.Frame(root)
links_frame.pack(pady=10)

wine_website_button = ttk.Button(links_frame, text="Wine Official Site", width=20, command=lambda: open_url("https://www.winehq.org"))
wine_website_button.grid(row=0, column=0, padx=10, pady=5)

wine_github_button = ttk.Button(links_frame, text="Wine GitHub", width=20, command=lambda: open_url("https://github.com/wine-mirror/wine"))
wine_github_button.grid(row=0, column=1, padx=10, pady=5)

# Style buttons
style = ttk.Style()
style.configure("TButton",
                font=("Arial", 12),
                padding=10,
                relief="flat",
                background="#5f6368",
                foreground="white")
style.map("TButton",
          background=[("active", "#4a4d54")],
          foreground=[("active", "white")])

# Run the application
root.mainloop()
