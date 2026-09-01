# This program is written by Nayak Satya 
# Goal of this program convert comma files into pipe files.
# Why: different partners use different separators in B2B/MFT Space. Your hub needs one common shape.

# Create a CSV style inbound file.

csv_file = open("partner.csv", "w")
csv_file.write("INVOICE,1001,NAYAKINFOTECH,250.00\n")
csv_file.write("INVOICE,1002,NAYAKINFOTECH,99.50\n")
csv_file.write("INVOICE,1003,NAYAKINFOTECH,15.00\n")
csv_file.close()

# We will write the converted records into this new file.
pipe_file = open("partner_pipe.txt", "w")

print("Converting partner.csv -> partner_pipe.txt")
print("-----------------------------------------")

csv_in = open("partner.csv", "r")
for line in csv_in:
    clean_line = line.strip()

    # Skip a blank line if one appears.
    if clean_line == "":
        continue

    # split(",") cuts on commas because this inbound file is CSV.
    parts = clean_line.split(",")

    # Build the same 4 fields again, but join them with |.
    # Why not just replace commas? split + rebuild makes each field visible.
    pipe_line = parts[0] + "|" + parts[1] + "|" + parts[2] + "|" + parts[3]

    print("CSV :", clean_line)
    print("PIPE:", pipe_line)
    print("-----")

    # Write the converted record to the outbound file.
    pipe_file.write(pipe_line + "\n")

csv_in.close()
pipe_file.close()

print("Conversion finally finished")

#your output should like below 

#Converting partner.csv -> partner_pipe.txt
#-----------------------------------------
#CSV : INVOICE,1001,NAYAKINFOTECH,250.00
#PIPE: INVOICE|1001|NAYAKINFOTECH|250.00
#-----
#CSV : INVOICE,1002,NAYAKINFOTECH,99.50
#PIPE: INVOICE|1002|NAYAKINFOTECH|99.50
#-----
#CSV : INVOICE,1003,NAYAKINFOTECH,15.00
#PIPE: INVOICE|1003|NAYAKINFOTECH|15.00
#-----
#Conversion finally finished