# EDI / integration files are often fields separated by | or ,
# We will split a line into pieces and use each field in this python program
# Program name ParseDelimated.py , Parse a simple pipe-delimited invoice record
# Wriiten my MFT expert Nayak satya 

record = "INV|1001|NAYAK|2500.00"
parts = record.split("|")

# the logic of this code is take a string, split it, use the fields.


doc_type = parts[0]
invoice_number = parts[1]
partner = parts[2]
amount_text = parts[3]
amount = float(amount_text)

print("Here is the Raw Record:", record)
print("Here is the Document Type:", doc_type)
print("Invoice number:", invoice_number)
print("Partner is:", partner)
print("Amount is:", amount)

if amount > 2000:
    print("This invoice is above 2k")
else:
    print("This invouce is 2k below")