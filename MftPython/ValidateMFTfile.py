#partners often drop files with a naming rule, for example Nayak_INVOICE_20260829.txt
# In this program we will check whether a filename follows as per Partner instruction
# Python program name ValidateMFTfile.py , you can learn string methods, split(), if / else, len(). 

file_name = "Nayak_INVOICE_20260829.txt"

print("Checking file name with caution:", file_name)

if file_name.endswith(".txt"):
    print("Extension is .txt  -> OK")
else:
    print("Extension is not .txt -> REJECT")

name_without_ext = file_name.replace(".txt", "")
parts = name_without_ext.split("_")

print("Name parts:", parts)
print("Number of parts:", len(parts))

if len(parts) == 3:
    partner = parts[0]
    doc_type = parts[1]
    file_data = parts[2]
    print("Partner:", partner)
    print("Document type:", doc_type)
    print("date:", file_data)
    print("Filename convention -> OK")
else:
    print("Expected 3 parts: PARTNER_DOCTYPE_DATE")
    print("Filename convention -> REJECT")


#test this code both good file name and a bad file name 

