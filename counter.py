def countEmail():
    # This first line is provided for you
    sender = []
    countEmails = dict()
    name = input("Enter file:")
    #if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)
    for line in handle:
        if line.startswith("From "):
            words = line.split()
            sender.append(words[1])
            #print (sender)
            for person in sender: 
                countEmails[person] = countEmails.get(person, 0) + 1
            maxSender = None
            maxCount = None
    for person, count in countEmails.items():
        if maxCount is None or count > maxCount:
            maxSender = person
            maxCount = count
        

    #mostFrom = max(countEmails, key=countEmails.get)   
    print (maxSender, maxCount)
    print (countEmails)
## if you want to test locally before you try to sync
## uncomment countEmail() and run > python counter.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
##countEmail()
