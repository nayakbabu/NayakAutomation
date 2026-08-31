# In real world One mailbox can receive mixed files. Ivoice should go to billing, PO to purchasing, ASN to the warehouse. That decision is called routing
# We will write a Python Program on concept of Route to Send each document type to the correct lane
# This program is written by Nayak Satya , a senior MFT certified resource 

records = [                # writing a List for several items in one box, in order
    "INV|2001|ACME|2500.00",
    "PO|3001|GLOBE|4000.00",
    "ASN|4001|INDIATECH|3400.00,"
    "XYZ|5001|Unknown|0.0"
]

print("Routing incoming documents")
print("--------------------")

for record in records:   #writing a loop for split and then print 
    parts = record.split("|")
    doc_type = parts[0]
    doc_number = parts[1]
    partner = parts[2]


    print("Document:", doc_type, doc_number, "From", partner)

    if doc_type == "INV":
        lane = "BILLING"
    elif doc_type == "PO":
        lane = "PURCHASING"
    elif doc_type == "ASN":
        lane = "WAREHOUSE"
    else:
        lane = "UNKNOWN_REJECT"
    print("LANE:", lane)
    print("------")