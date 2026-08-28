# a use case for Python for MFT team's file transfer testing
# Create a simple outbound file for a trading partner , its used many times for testing

partner_id = "Nayak"
document_type = "INVOICE"
file_name = "outbound_invoice.txt"

line1 = "INV|1001|Nayak|2500.00"
line2 = "INV|1002|Nayak|1500.00"


output_file = open(file_name, "w")
output_file.write(line1 + "\n")
output_file.write(line2 + "\n")
output_file.close()

print("Outbound file created:", file_name )
print("Partner:", partner_id)
print("document type:", document_type)