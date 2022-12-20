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