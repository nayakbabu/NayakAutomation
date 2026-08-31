# In this program we will Split a mixed file into good records and bad records

# In real world a partner file is rarely perfect. Some lines are missing a field.So a Good mft Product does not crash. It keeps the clean records and isolates the dirty ones.

# This Program is written by Nayak Satya and named as Qualitycheck.py

incoming_file = "mixed_batch.txt"
good_file_name = "good_record.txt"
bad_file_name = "bad_record.txt"

setup = open(incoming_file, "w")
setup.write("INVOICE|1001|NAYAKINC|2500.00\n")
setup.write("INVOICE|1002|NAYAKINC|9999.00\n")
setup.write("INVOICE|Broken|blacklisted\n")
setup.write("INVOICE|1004|NAYAKINC|ABC\n")
setup.close()

good_count = 0
bad_count = 0

incoming = open(incoming_file, "r")
good_file = open(good_file_name, "w")
bad_file = open(bad_file_name, "w")

for line in incoming:
    clean_line = line.strip()
    parts = clean_line.split("|")

    if len(parts) != 4:    #A good invoice needs exactly 4 pieces: type, number, partner, amount.
        bad_file.write(clean_line + "\n")
        bad_count = bad_count + 1
        print("QUARANTINE: wrong number of fields ->", clean_line)
    else:
        try:
            amount = float(parts[3])
            good_file.write(clean_line + "\n")
            good_count = good_count + 1
            print("GOOD: invoice", parts[1], "amount", amount)
        except ValueError:   #When conversion fails, Python raises ValueError.It catches that and treats the line as bad instead of crashing.
            bad_file.write(clean_line + "\n")
            bad_count = bad_count + 1
            print("QUARANTINE: amount is not a number ->", clean_line)
incoming.close()
good_file.close()
bad_file.close()

print("Good Records:", good_count)
print("Bad Records:", bad_count)
print("Wrote:", good_file_name)
print("Wrote:", bad_file_name)


#Your output should display like below and must need to create Good_record.txt, bad_record.txt 
#GOOD: invoice 1001 amount 2500.0
#GOOD: invoice 1002 amount 9999.0
#QUARANTINE: wrong number of fields -> INVOICE|Broken|blacklisted
#QUARANTINE: amount is not a number -> INVOICE|1004|NAYAKINC|ABC
#Good Records: 2
#Bad Records: 2
#Wrote: good_record.txt
#Wrote: bad_record.txt
