document = """
This is the content of the document.
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Nullam auctor, nunc id ultrices tincidunt, velit nisl ultricies nunc, id lacinia nunc justo id mauris.
"""

file_name = "document.txt"

with open(file_name, "w") as file:
    file.write(document)

print("Document saved successfully!")