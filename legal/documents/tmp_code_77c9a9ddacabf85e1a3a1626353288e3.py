document = """
Dies ist ein Beispieltext.
Hier können Sie Ihren Text einfügen.
"""

file_name = "mein_dokument.txt"

with open(file_name, "w") as file:
    file.write(document)

print("Das Dokument wurde erfolgreich gespeichert.")