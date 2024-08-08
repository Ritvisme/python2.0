
import os

# Directory name
directory = "numero uno.txt"

# Parent Directory
parent = "Users/ritvikbhatnagar/Desktop/numero uno.txt"

# Path 
path = os.path.join(parent, directory)

# Remove the Directory
# "Geeks"
os.rmdir(path)
