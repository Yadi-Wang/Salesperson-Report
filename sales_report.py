"""Generate sales report showing total melons each salesperson sold."""


salespeople = []         # create a blank list for sales person
melons_sold = []            # create a blank list for melons sold

f = open('sales-report.txt')
for line in f:
    line = line.rstrip()
    entries = line.split('|')  # split each line and make a list for each entry

    salesperson = entries[0]    # name of each sales person is the first word 
    melons = int(entries[2])      # number of melon sold is the third word in the line and convert it to integer

    if salesperson in salespeople:   # if the name already in the salespeople list
        position = salespeople.index(salesperson)    # find-out the index position of the person in the salespeople list 

        melons_sold[position] += melons    # in the same index of melons_sold list, add the number of melons to the existing number
    else:                     # if the person is the first time show up, add the name and number of lemons into both lists
        salespeople.append(salesperson)    
        melons_sold.append(melons)


for i in range(len(salespeople)):     # each person in the list print the name and numbet of melons 
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
