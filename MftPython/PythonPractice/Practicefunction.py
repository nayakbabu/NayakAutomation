# This is a practice of function and its a comment line

def check_disk_usage(percent):
    if percent > 90:
        print("CRITICAL")
    elif percent > 75:
        print("WARNING")
    else:
        print("Ok")

#now we have to call the function
usages = [45, 82, 95, 60]
for usage in usages:
    check_disk_usage(usage)