class Hotel:
    def _init_(self, name, location):
        self.name = name
        self.location = location
        self.total_rooms = 20 
        self.available_rooms = self.total_rooms
        
class Room:
    def _init_(self, number):
        self.number = number
        self.occupied = False

class Customer:
    def _init_(self, name, room):
        self.name = name
        self.room = room

    def check_in(self):
        if not self.room.occupied:
            self.room.occupied = True
            print(f"{self.name} has checked into Room {self.room.number}.")
        else:
            print(f"Room {self.room.number} is already occupied.")

    def check_out(self):
        if self.room.occupied:
            self.room.occupied = False
            print(f"{self.name} has checked out from Room {self.room.number}.")
        else:
            print(f"Room {self.room.number} is not occupied.")

hotel = Hotel("JG Hotel", "Chennai")

# Display Hotel Details
print(f"Welcome to {hotel.name} located in {hotel.location}.")

# Create Rooms
rooms = [Room(i) for i in range(1, hotel.total_rooms + 1)]

# Create Customers
customers = [Customer("Gopika J", rooms[0]), Customer("Divya J", rooms[1]), Customer("Kannagi J", rooms[2])]

# Check-in Customers
for customer in customers:
    customer.check_in()
    if not customer.room.occupied:
        hotel.available_rooms -= 1

# Check-out Customers
for customer in customers:
    customer.check_out()
    if not customer.room.occupied:
        hotel.available_rooms += 1

# Display Available Rooms
print(f"\nAvailable Rooms: {hotel.total_rooms}")
