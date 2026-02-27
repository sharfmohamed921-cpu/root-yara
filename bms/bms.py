
print("Welcome")
print("Please choose an option:")
print("1. Login")
print("2. Sign up")


choice = input("Enter for Login (1) or Sign up (2): ")


if choice == "1":
    print("You chose to Login.")
    username = input("Enter username: ")
    password = input("Enter password (8 uppercase and lowercase letters): ")
    if len(password) == 8 and password.isalpha() and any(c.isupper() for c in password) and any(c.islower() for c in password):
        print(f"Welcome, {username}")
    else:
        print("Incorrect username or password")
        exit()
elif choice == "2":
    print("You chose to Sign up.")
    username = input("Enter username: ")
    password = input("Enter password (8 uppercase and lowercase letters): ")
    if len(password) == 8 and password.isalpha() and any(c.isupper() for c in password) and any(c.islower() for c in password):
        confirm_password = input("Confirm password: ")
        if password == confirm_password:
            print("Successful registration")
        else:
            print("Passwords mismatched, please try again")
    else:
        print("Weak password, please try again")
        exit()
else:
    print("Error: Invalid option. Please choose 1 or 2.")
    exit()


services = ["New Car ID", "Renew Car License", "New Driving License", "Renew Driving License", "Lost ID"]
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
new_car_id = [
    ["13-04-2025", "Sunday", [6, 10, 1, 10, 7]],
    ["14-04-2025", "Monday", [10, 2, 10, 6, 4]],
    ["15-04-2025", "Tuesday", [3, 1, 10, 10, 9]],
    ["16-04-2025", "Wednesday", [10, 8, 10, 7, 3]],
    ["17-04-2025", "Thursday", [2, 10, 4, 10, 1]]
]
slots = ["9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM"]


def calculate_average_bookings(service_data):
    total_bookings = sum(service_data)
    return total_bookings / len(service_data)

def most_crowded_day(service_data):
    return days[service_data.index(max(service_data))]

def least_crowded_day(service_data):
    return days[service_data.index(min(service_data))]

service1_data = [day[2][0] for day in new_car_id]
average_bookings = calculate_average_bookings(service1_data)
most_crowded = most_crowded_day(service1_data)
least_crowded = least_crowded_day(service1_data)

print("\nAnalysis for Service #1 (New Car ID):")
print(f"Average number of bookings: {average_bookings:.2f}")
print(f"Most crowded day: {most_crowded}")
print(f"Least crowded day: {least_crowded}")


if choice == "1" and len(password) == 8 and password.isalpha() and any(c.isupper() for c in password) and any(c.islower() for c in password):
    print("\nAvailable Services:")
    for i, service in enumerate(services, 1):
        print(f"{i}. {service}")

    service_choice = input("Enter the number of the service you want (1-5): ")
    if service_choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid service selection.")
        exit()
    service_index = int(service_choice) - 1
    chosen_service = services[service_index]

    print("\nAvailable Days:")
    for i, day in enumerate(days, 1):
        print(f"{i}. {day}")

    day_choice = input("Enter the number of the day you want (1-5): ")
    if day_choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid day selection.")
        exit()
    day_index = int(day_choice) - 1
    chosen_day_data = new_car_id[day_index]
    chosen_date = chosen_day_data[0]
    chosen_day_name = chosen_day_data[1]
    bookings_for_services = chosen_day_data[2]

    booked_slots = bookings_for_services[service_index]
    available_slots = 10 - booked_slots

    print("\nAvailable Slots:")
    if available_slots == 0:
        print("Sorry, no available slots for this service on this day.")
    else:
        for i in range(min(available_slots, 5)):
            remaining = 10 - booked_slots
            print(f"slot {slots[i]}, only {booked_slots} bookings, so there are {remaining} remaining free bookings.")

        slot_choice = input("Choose your preferred slot number (1-5): ")
        if not slot_choice.isdigit() or int(slot_choice) < 1 or int(slot_choice) > min(available_slots, 5):
            print("Invalid slot selection.")
            exit()
        slot_index = int(slot_choice) - 1
        chosen_slot = slots[slot_index]


        full_name = input("Enter full name: ")
        id_number = input("Enter ID number: ")
        print("\nYour Booking Summary:")
        print(f"Full name: {full_name}")
        print(f"ID number: {id_number}")
        print(f"Service: {chosen_service}")
        print(f"Date: {chosen_date} ({chosen_day_name})")
        print(f"Time: {chosen_slot}")
        print("Your booking is confirmed.")
        with open("booking.txt", "w") as file:
            file.write(f"Name: {full_name}\nID: {id_number}\nService: {chosen_service}\nDate: {chosen_date}\nTime: {chosen_slot}")