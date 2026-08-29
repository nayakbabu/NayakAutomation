#This program reject file names that look like path tricks
#a bad file name can try to leave the drop folder, any MFT software should reject names that contain path tricks.
#This program is written by Nayak Satya 

file_name = "Nayak_INVOICE_20260830.txt"

print("Checking file name:", file_name)

if file_name == "":
    print("Decision Loading: REJECT")
    print("Reason: empty name")
elif ".." in file_name:
    print("Decision Loading: REJECT")
    print("Reason: contains ..")
elif "/" in file_name or "\\" in file_name:
    print("Decision Loading: REJECT")
    print("Reason: contains a path separator")
else:
    print("Decision: ACCEPT")
    print("Reason: name looks like a perfect simple file")


    #logic of this program is to reject empty file, .. file, / or \ file and only accept correct file format