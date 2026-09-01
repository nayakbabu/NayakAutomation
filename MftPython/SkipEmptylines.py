# This program read a partner file and ignore empty lines

# The logic is simple blank lines are common and should not be treated as invoices for MFT/EDI env

# This code is written by Nayak Satya


sample = open("Partner_batch.txt", "w")
sample.write("INVOICE|1001|NAYAKINFOTECH|2500.00\n")
sample.write("\n")
sample.write("INVOICE|1002|NAYAKINFOTECH|9999.00\n")
sample.write("\n")
sample.write("INVOICE|1003|NAYAKINFOTECH|9979.00\n")
sample.close()

print("Reading Partner_batch.txt")
print("-------------------")

line_number = 0
invoice_count = 0

data_file = open("Partner_batch.txt", "r")

for line in data_file:
    line_number = line_number + 1

    clean_line = line.strip()

    if clean_line == "":
        print("Line", line_number, "is empty -> skip")
        continue

    parts = clean_line.split("|")
    invoice_number = parts[1]
    amount = parts[3]

    invoice_count = invoice_count + 1
    print("Line", line_number, "invoice", invoice_number, "amount", amount)

data_file.close()

print("-------------------------")
print("Physical lines in file:", line_number)
print("Real invoices processed:", invoice_count)