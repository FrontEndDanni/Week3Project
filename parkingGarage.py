class Parking_Garage:
    
  def __init__(self,parking_spaces):
    self.tickets = [x for x in range(1,parking_spaces+1)]
    self.parking_spaces = [x for x in range(1,parking_spaces+1)]
    self.current_ticket = {}
      
  def take_ticket(self):     
    if self.parking_spaces: 
      print("You have parked!")
      print(f"Your ticket number is {self.tickets[0]}")
      self.current_ticket[self.tickets[0]] = ''
      self.parking_spaces.remove(self.tickets[0])
      self.tickets.remove(self.tickets[0])
      
    else:
      print("The Garage is full! Please go away!")

  def pay_for_parking(self):
    while True:
      paid_ticket = int(input("Please enter ticket you want to pay for: "))
      if paid_ticket in self.current_ticket:
        self.current_ticket[paid_ticket] = "paid"
        
        break
      else:
        print("Please enter a valid ticket number.")

  def leave_garage(self):
    while True:
        ticket_num = int(input("Please enter your ticket number: "))
        if ticket_num in self.current_ticket:
          if self.current_ticket[ticket_num] == "paid":
            print("Thank you have a nice day!")
            del self.current_ticket[ticket_num]
            self.tickets.append(self.current_ticket[ticket_num])
            self.tickets.sort()
            break
          else:
            self.pay_for_parking()
            del self.current_ticket[ticket_num]
            self.tickets.append(ticket_num)
            self.tickets.sort()
            print("Thank you have a nice day!")
            break

        else:
          print(f"{ticket_num} is not a current ticket number!")

garage = Parking_Garage(10)

def run(gara):
  
  print("Welcome to the World's Best Parking Lot!")
  while True:
    enter_lot = input("What would you like to do? Park, Pay, Leave")
    if enter_lot.lower() == "park":
      gara.take_ticket()
    elif enter_lot.lower() == "pay":
      gara.pay_for_parking()
      print("Thank you for paying! You have 15 minutes to leave!")
    elif enter_lot.lower() == "leave":
      gara.leave_garage()
      print("Thanks for stopping by!")
    else:
      print("Please enter a valid input.")

run(garage)