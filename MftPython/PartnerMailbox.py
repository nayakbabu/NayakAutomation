# This program Look up each partner's mailbox from a directory

# In Real world every partner has a mailbox or folder. You should not write 50 separate if lines, we should keep a directory and look the partner up

# This program is written by Nayak Satya , a MFT certified secialist 

mailbox = {
    "NAYAKINFOTECH": "/inbox/nayakinfotech",
    "GLOBALINDIA": "/inbox/globalindia",
    "INIINFOTECH": "/inbox/iniinfotech"
}

incoming_partners = ["NAYAKINFOTECH", "GLOBALINDIA", "INIINFOTECH"]
print("Partner Directory:")
print(mailbox)
print("---------------------")

for partner in incoming_partners:
    print("Incoming partner:", partner)

    if partner in mailbox:
        mailbox = mailbox[partner]
        print("Mailbox found:", mailbox)
        print("Decision: Accept")
    else:
        print("Mailbox found: NONE")
        print("Decision: REJECT")

    print("------")