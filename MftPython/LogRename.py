#In this Program after we accept a file, we count records, write a small log, and move/rename the original file so it is not processed twice.
#The core Logic of this program is Read inbound file, count records, write a log, then rename the file
#Program name is LogRename.py and Written by Nayak Satya , Infra MFT certified specialist

import os #import os gives you file system helpers



inbound_file = "Nayak_INVOICE_20260829.txt"
log_file = "process_log.txt"
archived_file = "Nayak_INVOICE_20260829_DONE.txt"

if os.path.exists(inbound_file):     # it asks: “is this file here?


    print("Inbound file found:", inbound_file)

    record_count = 0
    data_file = open(inbound_file, "r")

    for line in data_file:
        clean_line = line.strip()
        if clean_line != "":
            record_count = record_count + 1     # it is a running counter.  


            print("Processed:", clean_line)
    data_file.close()

    log = open(log_file, "w")
    log.write("File: ", + inbound_file + "\n")
    log.write("Status: SUCCESS\n")
    log.write("Records processed: " + str(record_count) + "\n")     # it   turns the number into text so it can be written to the log. 


    log.close()

    os.rename(inbound_file, archived_file)

    print("Records processed:", record_count)
    print("Log created:", log_file)
    print("File archived as:", archived_file )
else:
    print("Inbound file not found:", inbound_file)
    print("Create Nayak_INVOICE_20260829.txt first, then run again.")