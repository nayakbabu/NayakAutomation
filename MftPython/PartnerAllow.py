# This program is for Allow only known trading partners in Real world its always required
#your B2BI/MFT gateway should accept files only from known partners. Unknown partner IDs get rejected.
# This Python program is written by Nayak Satya 

allowed_partners = ["FORD", "BOSCH", "INCTECH","Tech Mahindra"]
incoming_partenr = "FORD"

print("Incoming Partner:", incoming_partenr)
print("Allowlist", allowed_partners)

if incoming_partenr in allowed_partners:
    print("Decision approved: ACCEPT")
    print("Partner is known and valid")

else:
    print("Decision rejected: REJECT")
    print("Unknown partner")
