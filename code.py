import random 

# ----- Choosing the 5 columns out of 9 in which we will place numbers of the ticket -----
columns = []
i = 0
for i in range(3):
    columns.append(random.sample(range(9),5))

# print(columns)

# ----- Initilizing ticket with value 0 using list comprehension -----
ticket = [[0 for i in range(9)] for i in range(3)]
# print(ticket)

# ----- Replacing 0's of ticket with 1's where the numbers are supposed to placed according to columns we chose randomly -----
k = 0
for i in range(len(columns)):
    for j in range(len(columns[i])):
        ticket[k][columns[i][j]] = 1
    k += 1

# print(ticket)

# ----- Creating random rows values in the range 1-90 such that 1st column is in range 1-10, 2nd in range 11-20, and so on.... -----
# ----- Here cols list contains values of columns eg: [[2,9,5], [13,17,20], ..., [81,90,85]] -----
cols = []
i = 0
# initializing m = 1 and n = 11 as values start with 1 and ends at 10 for 1st column. And then incrementing by 10 for every new column.
m,n = 1,11
for i in range(9):
    cols.append(random.sample(range(m,n),3))
    m += 10
    n += 10

# print(rows)

# ----- Creating a transpose of cols so that the first element of every sub-list of cols now becomes a  single row -----
values = [[cols[j][i] for j in range(len(cols))] for i in range(len(cols[i]))]
# print(values)

# ----- Finally replacing the values in ticket where ticket number is '1' -----
for i in range(len(ticket)):
    for j in range(len(ticket[i])):
        if ticket[i][j] == 1:
            ticket[i][j] = values[i][j]

print()  
print()

# ----- Printing ticket -----
for i in range(len(ticket)):
    for j in range(len(ticket[i])):
        print(ticket[i][j], end=" | ")
    print()

print()
print()
