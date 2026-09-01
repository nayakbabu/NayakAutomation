# This program accept the first invoice number and reject a repeat of the same number.

# The logic for B2B and MFT domain duplicate documents are a common 

# This program is written by Nayak Satya 


#This list starts empty. It is our memory of invoices we already processed.

seen_invoices = []

# a batch of invoice details 

records = [
    "INVOICE|1001|NAYAKINFOTECH|2555.00",
    "INVOICE|1002|NAYAKINFOTECH|3555.50",
    "INVOICE|1003|NAYAKINFOTECH|4444.44",
    "INVOICE|1002|NAYAKINFOTECH|3555.50"
]

print("Checking the batch of Invoices if any duplicate")
print("----------------------------")

accepted = 0
rejected = 0

for record in records:
    parts = record.split("|")
    invoice_number = parts[1]

    print("Incoming invoice:", invoice_number)
    if invoice_number in seen_invoices:
        rejected = rejected + 1
        print("Decision: REJECT because this invoice was already seen")
    else:
        seen_invoices.append(invoice_number)
        accepted = accepted + 1
        print("Decision: ACCEPT")
        print("Memory now holds:", seen_invoices)
    print("------")
print("Accepted:", accepted)
print("Rejected as duplicate:", rejected)