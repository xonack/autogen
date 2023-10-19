import tkinter as tk
import requests

API_KEY = "YOUR_API_KEY"

def check_data_breach():
    input_string = input_field.get()
    if not input_string:
        result_label.config(text="Please enter a string.")
        return

    api_url = f"https://haveibeenpwned.com/api/v2/breachedaccount/{input_string}"
    headers = {
        "User-Agent": "Python-Script",
        "hibp-api-key": API_KEY
    }
    
    response = requests.get(api_url, headers=headers)

    print("Response status code:", response.status_code)
    print("Response text:", response.text)

    if response.status_code == 200:
        result_label.config(text="Exposed!")
    elif response.status_code == 404:
        result_label.config(text="Not Exposed.")
    else:
        result_label.config(text="An error occurred.")

# Create UI
window = tk.Tk()
window.title("Data Breach Checker")

input_label = tk.Label(window, text="Enter a string to check:")
input_label.pack()

input_field = tk.Entry(window)
input_field.pack()

check_button = tk.Button(window, text="Check", command=check_data_breach)
check_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()