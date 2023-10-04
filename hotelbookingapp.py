#COURSE NAME: PROGRAMMING OF INFORMATION CENTRE APPLICATION 
#PROJECT GROUP: 14
#PROJECT NAME: HOSTEL/ROOM BOOKING APP (PYTHON)
#MAIN CAMPUS

#NAMES OF GROUP MEMBERS AND ROLES
#1.OSAE DORIS ADUBEA – 10811298
#Worked on the input codes, logic (main blocks /blocks of codes) of the project and the output codes.

#2.OPOKU DANIEL YAW - 10822155
#Worked on the input codes, logic (main blocks /blocks of codes) of the project and the output codes.

#3.AKESSE LINDA – 10848237
#Worked on the write ups and editing of presentation (PowerPoint).



# Define the available rooms and their prices
rooms = {
    "single": {
        "single bed": {"count": 5, "price": "GHs5,000.0"},
        "double beds": {"count": 8, "price": "GHs7,000.0"},
        "4 beds": {"count": 12, "price": "GHs8,500.0"},
        "more than 4 beds": {"count": 5, "price": "GHs10,000.0"},
    },
    "double": {
        "single bed": {"count": 5, "price": "GHs60,000.0"},
        "double beds": {"count": 10, "price": "GHs80,000.0"},
        "4 beds": {"count": 15, "price": "GHs95,000.0"},
        "more than 4 beds": {"count": 10, "price": "GHs100,000.0"}
    },
    "flats": {
        "single bed": {"count": 8, "price": "GHs90,000.0"},
        "double beds": {"count": 12, "price": "GHs200,000.0"},
        "4 beds": {"count": 5, "price": "GHs300,000.0"},
        "more than 4 beds": {"count": 5, "price": "GHs500,000.0"}
    }}

# Define the function for displaying available rooms
def display_rooms():
    print("Available rooms:")
    for category, types in rooms.items():
        print(category.capitalize() + ":")
        for bed_type, info in types.items():
            print(f"- {bed_type.capitalize()}: {info['count']} available, price: {info['price']} Per Year")

# Define the function for booking a room
def book_room(category, bed_type):
    if category in rooms and bed_type in rooms[category]:
        if rooms[category][bed_type]["count"] > 0:
            price = rooms[category][bed_type]["price"]
            rooms[category][bed_type]["count"] -= 1
            print(f"Booking confirmed! Price for a year: {price}.\nPlease take note that if payments are not made within 48hrs of booking,room will be made unavailable.\nThank you for choosing us.\n\n")
        else:
            print("Sorry, the selected room is not available.\n")
    else:
        print("Invalid room category or type.\n")

# Main program loop
while True:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    #Diaplay the available rooms
    display_rooms()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    #Ask the user for their room selection
    category = input("\nEnter the category of room you want to book: ").lower()
    bed_type = input("Enter the type of bed you want: ").lower()

    # Book the room
    book_room(category, bed_type)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    #Ask if the user wants to book another room
    another_booking = input("Do you want to book another room? (y/n) ").lower()
    if another_booking != "y":
        break
            
            
