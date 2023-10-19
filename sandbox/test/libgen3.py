import tkinter as tk
from tkinter import messagebox
from libgen_api import LibgenSearch
import requests

# Create a LibgenSearch object
libgen = LibgenSearch()

# Function to handle the download button click event
def download_pdf():
    # Get the title and author from the input fields
    title = title_entry.get()
    author = author_entry.get()

    # Search for the specified title
    results = libgen.search_title(title)

    # Filter the results by the specified author
    filtered_results = [book for book in results if book['Author'] == author]

    if len(filtered_results) == 0:
        messagebox.showinfo("No Books Found", "No matching books found.")
    else:
        # Get the first result
        book = filtered_results[0]

        # Resolve the download links
        download_links = libgen.resolve_download_links(book)

        # Print the download link
        pdf_url = download_links['GET']

        try:
            response = requests.get(pdf_url)
            response.raise_for_status()
            filename = pdf_url.split("/")[-1]
            save_path = f'./books/{filename}'
            # Write the PDF content to a local file
            with open(save_path, 'wb') as pdf_file:
                pdf_file.write(response.content)
            messagebox.showinfo("Download Complete", f"PDF downloaded and saved as '{save_path}'")
        except requests.exceptions.HTTPError as http_err:
            messagebox.showerror("HTTP Error", f"HTTP error occurred: {http_err}")
        except Exception as err:
            messagebox.showerror("Error", f"An error occurred: {err}")

# Create the main window
window = tk.Tk()
window.title("Libgen PDF Downloader")

# Create the title label and entry field
title_label = tk.Label(window, text="Title:")
title_label.pack()
title_entry = tk.Entry(window)
title_entry.pack()

# Create the author label and entry field
author_label = tk.Label(window, text="Author:")
author_label.pack()
author_entry = tk.Entry(window)
author_entry.pack()

# Create the download button
download_button = tk.Button(window, text="Download PDF", command=download_pdf)
download_button.pack()

# Start the main event loop
window.mainloop()