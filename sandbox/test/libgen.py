from libgen_api import LibgenSearch
import requests

# Create a LibgenSearch object
libgen = LibgenSearch()

# Search for "The Art of War"
results = libgen.search_title('The Art of War')

# Filter the results by author "Sun Tzu"
filtered_results = [book for book in results if book['Author'] == 'Sun Tzu']

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
    print(f"PDF downloaded and saved as '{save_path}'")
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"An error occurred: {err}")
