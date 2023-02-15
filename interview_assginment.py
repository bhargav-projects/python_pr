
"""
# Function to get keys of dictionary in reverse sorted order of values.
"""
def get_values(data):
    
    final_list = []
    sorted_data = sorted([value for value in data.values()],reverse=True)
    temp = []
    
    for values in sorted_data:
        for k,v in data.items():
            if v == values:
                final_list.append(k)
            
    return final_list 


if __name__ == '__main__':
    case1 = get_values({'a':1234, 'b':111, 'c':2345})
    print(case1)
    assert case1 == ['c', 'a', 'b']
    case2 = get_values({'a':5, 'b':10, 'c':-2, 'd': 0, 'e': 0 })
    print(case2)
    assert case2 == ['b', 'a', 'd',  'e',  'c']
    print('Success')



"""
Below is the item class. unique_id identifies each item. The task is to build a class for shopping Cart.
 Cart can have any number of items, cart must have the facility to add items, remove items 
 and calculate the total price of the cart. 
"""

"""

15
"""

class Item:
    def __init__(self, unique_id, name, price):
        self.unique_id = unique_id
        self.name = name
        self.price = price


class Cart():

    cart_list = []
    # def __init__(self, unique_id, name, price):
    #     super().__init__(unique_id, name, price)

    def add_item(self,item):
        cart_data = {}
        cart_data[item.unique_id] = [item.name,item.price]
        Cart.cart_list.append(cart_data)
        return

    def remove_item(self,item):

        for index,value in enumerate(Cart.cart_list):
            for data in value:
                if data == item.unique_id:
                    del Cart.cart_list[index]

    def get_total(self):
        count = 0
        for value in Cart.cart_list:
            for k,v in value.items():
                # print(value.get(k))
                count=count+int(value.get(k))
        print(count)
        return count
    # print(cart_list)


if __name__ == '__main__':
    book = Item('001', 'Book', 10)
    pen = Item('002', 'Pen', 5)
    
    cart1 = Cart()
    cart1.add_item(book)
    cart1.add_item(book)
    cart1.add_item(pen)
    cart1.add_item(pen)
    cart1.remove_item(pen)
    assert cart1.get_total() == 25

    cart2 = Cart()
    cart2.add_item(book)
    cart2.add_item(pen)
    assert cart2.get_total() == 15


class Subject(models.Model):
  name = models.CharField(max_length=128, unique=True)


class Student(models.Model):
   name = models.CharField(max_length=128)
   reg_no = models.CharField(max_length=16, unique=True)
   modified = models.DateTimeField(auto_now=True)


class StudentMarks(models.Model):
   student = models.ForeignKey(Student)
   subject = models.ForeignKey(Subject)
   score = models.IntegerField()
   exam_date = models.DateField()



"""
>>> get_total_score(exam_date_year=2019)
  { 'REGNO001': 625.00, 'REGNO002': 325.00, ..... }
"""

# Assuming data already exists in the System.
# Complete code using Django ORM to find total marks across all subjects in a given year.
def get_total_score(exam_date_year):  # Returns reg_no : total_marks
   pass


"""
>>> get_subjectwise_ranks(exam_date_year=2019)
  {
    'Physics': ['REGNO005','REGNO004','REGNO003'... ],
    'Chemistry': ['REGNO004','REGNO005','REGNO003'... ],
    ..
}
"""
# Assuming data already exists in the System. 
# Complete code using Django ORM to find reg no of students Subject wise ranking 
def get_subjectwise_ranks(exam_date_year, subject_name):
   pass


"""
>>> get_highest_scorer_details_for_subject(exam_date_year=2019, subject_name='Physics')
  [ {'name':'Ramesh','reg_no':'REGNO005'}, ... ]
"""
# Assuming data already exists in the System. 
# Complete code using Django ORM to find details of highest scorer in a given subject for a given year.
def get_highest_scorer_details_for_subject(exam_date_year, subject_name):
   pass



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