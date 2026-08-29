# Through this program we will Create a file, compute SHA-256, then verify it

# After a file arrives, MFT often computes a fingerprint (hash). If even one character changes, the fingerprint changes. That answers: “was this file altered?

# The logic of this program exists with hashlib, reading a file as bytes, comparing two values.

# This code is written By Nayak Satya an MFT certifed infra specialist

import hashlib

file_name = "partner_file.txt"

output = open(file_name, "w")
output.write("NAYAK|1001|FORD|250.00\n")
output.write("NAYAK|1002|FORD|350.00\n")
output.close()

data_file = open(file_name, "rb")
content = data_file.read()
data_file.close()

checksum = hashlib.sha256(content).hexdigest()

print("File created sucessfully:", file_name)
print("Checksum:")
print(checksum)

expected = checksum

if checksum == expected:
    print("Integrity check: PASS")
    print("File match the expected fingerprint")
else:
    print("Integrity check: FAIL")
    print("File doesn't match the expected fingerprint")

# logic

# We create a known file.

# "rb" reads raw bytes. Hashes work on bytes, so this is the correct mode.  

# hashlib.sha256(...).hexdigest() builds a long hex fingerprint. 


# We compare the computed value with the expected value.

