# In this use case we will write a program in python which read Read every invoice in a batch and add the amounts

# This python program name is WholeInvoicebatch.py

# In real world partners almost never send one record. They send a file with many invoices. Your job is to walk every line, split it, and build a small totals report

# This Python code is written by Nayak Satya MFT certified resource 

batch_file = "batch_invoice.txt"   #Store the name of the file that will contain the invoice batch records.

output = open(batch_file, "w")  #Open the batch file in write mode, If the file already exists, write mode replaces its existing contents
output.write("NAYAK|1001|ACME|250.00\n") #Write invoice records into the file.
output.write("NAYAK|1002|ACME|199.00\n")
output.write("NAYAK|1003|ACME|255.00\n")

output.close() #Close the file after writing

print("Batch file invoice is ready:", batch_file)
print("--------Processing Start--------")

invoice_count = 0 #Initialize a counter to track how many invoice records are processed.
total_amount = 0.0 #A float is used because invoice amounts can contain decimal values

data_file = open(batch_file, "r") #Open the invoice batch file in read mode, This allows the program to retrieve and process its existing records
for line in data_file:            # Read the file one line at a time, Each iteration of the loop represents one invoice record from the batch file.
    clean_line = line.strip()
    parts = clean_line.split("|")

    invoice_number = parts[1]      #Extract the invoice number from index position 1
    partner = parts[2]
    amount = float(parts[3])

    invoice_count = invoice_count + 1   #Increase the invoice counter by one after successfully processing
    total_amount = total_amount + amount #Add the current invoice amount to the running total

    print("Invoice", invoice_number, "for", partner, "amount", amount)

data_file.close()                      #Close the file after all invoice records have been processed.

print("-------Processing End-------")   #Display the final processing summary
print("Invoice in batch:", invoice_count)
print("Total amount:", total_amount)



#your output should display as below 

#Batch file invoice is ready: batch_invoice.txt
#--------Processing Start--------
#Invoice 1001 for ACME amount 250.0
#Invoice 1002 for ACME amount 199.0
#Invoice 1003 for ACME amount 255.0
#-------Processing End-------
#Invoice in batch: 3
#Total amount: 704.0