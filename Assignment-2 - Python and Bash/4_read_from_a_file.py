"""
Read from a File
We used open in read mode and file.read to read and print to display.
"""

f = open("write_to_a_file.txt", "r") # Open the file in read mode.  
print(f.read()) # Read the file and print it.
f.close() # Close the file.
