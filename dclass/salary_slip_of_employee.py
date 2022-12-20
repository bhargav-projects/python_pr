

employee_records_count = int(input("Please specify number of employee records:"))
employee_data = {}

while True:
    employe_details = input("Please enter Employee name, Basic pay and age with comma(,):").split(",")
    employee_name = employe_details[0]
    basic_pay = int(employe_details[1])
    age = int(employe_details[2])
    

    def salary_slip_of_the_employee(employee_name, basic_pay, age):
        
        house_rent_allowances = basic_pay*10/100
        medical_allowances = basic_pay*5/100
        spouse_allowences = basic_pay*2/100
        professional_tax = 500.00
        
        net_salary = basic_pay + house_rent_allowances + medical_allowances + spouse_allowences
        annual_ctc = int(net_salary*12)

        income_tax = 0 
        if annual_ctc < 25000:
            income_tax = 0
        elif annual_ctc>25000 or annual_ctc <50000:
            income_tax = annual_ctc*5/100

        elif annual_ctc>50000 and annual_ctc<100000:
            income_tax = annual_ctc*10/100

        elif annual_ctc>100000:
            income_tax = annual_ctc*25/100 

        insurance = 0
        if age > 50 :
            insurance = 3400
        else:
            insurance = 2600

        deductions = net_salary - professional_tax - income_tax - insurance
        gross_salary = net_salary - deductions
        
        employee_data.update({employee_name:[{"Net salary":format(net_salary,".2f")},
            {"Gross salary":format(gross_salary,".2f")}]})
         
    salary_slip_of_the_employee(employee_name, basic_pay, age)
    
    employee_records_count-=1

    if employee_records_count <=0:
        break

print(employee_data)
