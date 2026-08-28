#This python code written to read a file
#This can read the inbound/outbound file line by line

file_name = "outbound_invoice.txt"

input_file = open(file_name, "r")

print("Reading your file:", file_name)
print("-----start of file-----")

for line in input_file:
    clean_line = line.strip()
    print(clean_line)

print("-------end of file-----")

input_file.close()