# This program will Accept only small .txt / .csv / .edi files

# You have to make a test data inbound.txt with proper input fields for testing the program

# This program only accept expected file types, and reject a file that is far too big. That protects the server from junk uploads.

# This program is written by MFT certifed Nayak Satya 

import os
file_name = "inbound.txt" # here you have to create the test data 
max_size = 500 
allowed_endings = [".txt", ".csv", ".edi"]

print("Checking:", file_name)

if os.path.exists(file_name) == False:
    print("Decision Loading: REJECT")
    print("Reason: file not found")
else:
    file_size = os.path.getsize(file_name)
    print("File Size in bytes:", file_size)
    print("Max allowed bytes:", max_size)

    has_allowed_ending = False
    if file_name.endswith(".txt") or file_name.endswith(".csv") or file_name.endswith(".edi"):
        has_allowed_ending = True
    if has_allowed_ending == False:
        print("Decision Loading: REJECT")
        print("Reason: extension is not allowed")
    elif file_size > max_size:
        print("Decision Loading: REJECT")
        print("Reason: file is too large")
    else:
        print("Decision Loading: ACCEPT")
        print("Reason: type and size both looks perfect or OK ")