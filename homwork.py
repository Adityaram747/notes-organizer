file = open("notes.txt", "r")
preview = file.read(10)
print("Preview:", preview)
file.close()

file = open("notes.txt", "r")
lines = file.readlines()
file.close()

# Open the new file for writing
clean_file = open("clean_notes.txt", "w")

for line in lines:
    # 4. Filter with startswith()
    if line.startswith("IMPORTANT") or line.startswith("TODO"):
        # 5. Write selected lines to the new file
        clean_file.write(line)

clean_file.close()

print("Done organizing notes!")