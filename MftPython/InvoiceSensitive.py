# This python program mask an account number before writing it to a log
#An invoice file may contain an account number. You can process it, but you must not print the full number in logs.
# This is a common practice for trade testing 
#This program written by Nayak Satya

partner = "FORD"
invoice_number = "1001"
account_number = "FD0231867546321x"
amount = "2000.00"

last_four = account_number[-4:]
masked_account = "**********" + last_four

print("Partner:", partner)
print("Invoice:", invoice_number)
print("Amount:", amount )
print("Account in log:", masked_account)
print("Full account is not printed")


#logic of this code account_number[-4:] means “last 4 characters.”  

#We keep those 4 and hide the rest with *.  

#he real number stays in the variable. Only the masked version is shown


