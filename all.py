# Question 1 Task 1: Vehicle Registration System.
class Vehicle:
    def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner
    def update_owner(self, new_owner):
              self.owner = new_owner
              print(f"Owner updated to {new_owner} for vehicle with registration number {self.registration_number}")
if __name__ == "__main__":
      
    Vehicle1 = Vehicle("ABCD123", "Car", "Doe Jhon")
    Vehicle2 = Vehicle("XYS893", "Motorcycle", "Smith Alice")
    Vehicle3 = Vehicle("LNM743", "Truck", "Alice Johnson")

    print(f"Vehicle 1: {Vehicle1.registration_number}, Type: {Vehicle1.type}, Owner: {Vehicle1.owner}")
    print(f"Vehicle 2: {Vehicle2.registration_number}, Type: {Vehicle2.type}, Owner: {Vehicle2.owner}")
    print(f"Vehicle 3: {Vehicle3.registration_number}, Type: {Vehicle3.type}, Owner: {Vehicle3.owner}")

    Vehicle1.update_owner("Browen Michael")
    Vehicle2.update_owner("Davis Wilson")
    Vehicle3.update_owner("Browen Robert")

    print(f"Vehicle 1: {Vehicle1.registration_number}, Type: {Vehicle1.type}, Owner: {Vehicle1.owner}")
    print(f"Vehicle 2: {Vehicle2.registration_number}, Type: {Vehicle2.type}, Owner: {Vehicle2.owner}")
    print(f"Vehicle 3: {Vehicle3.registration_number}, Type: {Vehicle3.type}, Owner: {Vehicle3.owner}")

# Question 2 Task 1:  Event Management System Enhancement.
class Event:
    def __init__(self, name, date):
            self.name = name
            self.date = date
            self.participant_count = 0
    def add_participant(self):
          self.participant_count = 1
    def get_participant_count(self):
          return self.participant_count
event = Event("OOP workshop", "2024-2-21")
print(event.get_participant_count())
event.add_participant()
event.add_participant()
print(event.get_participant_count())



          


      

      



