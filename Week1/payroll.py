class Employee:
    def __init__(self, fname, lname, id, hourlyPay) -> None:
        self.fname = fname
        self.lname = lname
        self.id = id
        self.hourlyPay = float(hourlyPay)

    def pay(self, totalHours):
        string = f"{self.fname} {self.lname} paycheck amount is "
        if((float(totalHours)) <= 40):
            return print(f"{string} {float(self.hourlyPay * (float(totalHours)))}")
        elif((float(totalHours)) > 40):
            a = (self.hourlyPay * 40)
            b = ((float(totalHours)) - 40)
            return print(f"{string} {float(a + ((b * self.hourlyPay)* 1.5))}")
    
ID = input("Please enter the Employee's ID: ")
fname = input("Please enter the Employee's First Name: ")
lname = input("Please enter the Employee's Last Name: ")
hourlyPay = input("Please enter the Employee's Hourly Pay Rate: ")
hoursWorked = input("How many hours did she/he work this week? ")
float(hoursWorked)

employee1 = Employee(fname, lname, ID, hourlyPay)
employee1.pay(hoursWorked)