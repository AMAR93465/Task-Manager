def main():
    try:
        # Initialize bookings list
        bookingsList = []
        with open("bookingsList.txt", "r") as infile:
            line = infile.readline()
            while line:
                bookingsList.append(line.rstrip("\n").split(","))
                line = infile.readline()

    except FileNotFoundError:
        print("The 'bookingsList.txt' file is not found.")
        print("Starting a new bookings list!")
        bookingsList = []
    
    choice = 0
    while choice != 5:
        print("\n*** Bus Ticket Booking System ***")
        print("1. Add a Booking")
        print("2. Get Booking Information")
        print("3. Display All Bookings")
        print("4. Delete a Booking")
        print("5. Quit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            print("Adding a booking...")
            passenger_name = input("Enter the passenger's name: ")
            booking_id = input("Enter the booking ID: ")
            destination = input("Enter the destination: ")
            seat_number = input("Enter the seat number: ")

            bookingsList.append([passenger_name, booking_id, destination, seat_number])

        elif choice == 2:
            print("Looking up a booking...")
            keyword = input("Enter the passenger's name: ")
            found = False
            for booking in bookingsList:
                if keyword.lower() in booking[0].lower():  # case-insensitive search for passenger name
                    print(booking)
                    found = True
            if not found:
                print("No booking found with that name.")

        elif choice == 3:
            print("Displaying all bookings...")
            if bookingsList:
                for i, booking in enumerate(bookingsList):
                    print(f"{i+1}. Name: {booking[0]}, Booking ID: {booking[1]}, Destination: {booking[2]}, Seat: {booking[3]}")
            else:
                print("No bookings in the list.")

        elif choice == 4:
            print("Deleting a booking...")
            delete_name = input("Enter the name of the passenger to delete booking: ")
            found = False
            for i, booking in enumerate(bookingsList):
                if delete_name.lower() == booking[0].lower():  # case-insensitive comparison
                    del bookingsList[i]
                    print(f"Deleted booking for passenger: {booking[0]}")
                    found = True
                    break
            if not found:
                print(f"No booking found for passenger '{delete_name}'.")

        elif choice == 5:
            print("Quitting Program")

    print("Program Terminated")

    # Saving the bookings to the external file
    with open("bookingsList.txt", "w") as outfile:
        for booking in bookingsList:
            outfile.write(",".join(booking) + "\n")

if __name__ == "__main__":
    main()
