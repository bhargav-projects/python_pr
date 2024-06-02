# test ="this is testing spaces"
# l1 = test.split() # returning every words in str
# len_l = len(l1)
# new = []
# for val in range(len_l-1,-1,-1):
#     new.append(l1[val])

 

test ="a4b3c2"
output='' # aaaabbbbcc
for index,val in enumerate(test):

    """
    #! if val is 4 ,it is inside for its str 
    #^  but if we perform operation with #! val like isdigit() or isalnum()
    its working perfectly 

    """
    if val.isalpha(): 
        output+=val * int(test[index + 1])

def factori(n):
    if n == 0 or n==1:
        return 1
    else :
        return n*factori(n-1)
print(factori(5))

 

# with open("zip.py","r")as test_file:
#     line_count=column_count=words_count=0
#     for line in test_file:
#         line_count+=1
#         column_count+=len(line)
#         words = line.split()
#         words_count+=len(words)
# print(f'line count is {line_count} \n column count is {column_count} \n words count is {words_count}')



# which seats filled
# will get message he has taken
# dispaly all available seats 

class TicketBooking:
    seats = {}

    for seat in range(10):
        seats[seat] = "Available"
    
    def get_availabale_seats():
        available_seats = []
        for k,v in seats.itesm():
            if v != "Available":
                available_seats.append(k)
        return available_seats
    def book_seat():
        available_seats = TicketBooking.seats
        print(f"available seats:{available_seats}",)
        seat_number = int(input("please eneter seat number"))
        TicketBooking.seats[seat_number]="Booked"
        
        return print(f"Your have booked seat {seat_number}.\n Avaialble seats \n {TicketBooking.seats}")


TicketBooking.book_seat()