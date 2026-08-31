# In this python program we will learn to Create a simple ACK / receipt after processing of a successful file

# This program name is EDIackrevert.py and written by Nayak Satya 

# after you process a partner file, you often send back a small receipt like success, fail kind of ack

from datetime import datetime   # It will bring Python’s clock toolbox

original_file = "NAYAK_INVOICE_20260831.txt"
status = "SUCCESS"
record_count = 3

now = datetime.now()     # what is the current date and time? 
time_stamp = now.strftime("%Y-%m-%d %H:%M:%S")   # It is is just a dress code for that clock:

ack_file_name = "ACK_NAYAK_INVOICE.txt"

ack = open(ack_file_name, "w")
ack.write("ACKNOWLEDGMENT\n")
ack.write("OriginalFile=" + original_file + "\n")
ack.write("Status=" + status + "\n")
ack.write("Records:" + str(record_count) + "\n")   #This turns the number 3 into the text "3" so it can be written into a file
ack.write("ReceivedAT=" + time_stamp + "\n")
ack.close()

print("ACK Created:", ack_file_name)
print("Status:", status)
print("Time:", time_stamp)



#Your output should display like below 

#ACK Created: ACK_NAYAK_INVOICE.txt
#Status: SUCCESS
#Time: 2026-08-31 18:55:29