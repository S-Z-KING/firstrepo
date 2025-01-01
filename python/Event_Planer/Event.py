def get_event_details():
    """Function to get event details from the user."""
    print("Welcome to the Event Planner!\n")
    
    # Collect event details
    event_name = input("Enter the event name: ")
    venue_cost = float(input("Enter the venue cost ($): "))
    catering_cost_per_person = float(input("Enter the catering cost per person ($): "))
    
    return event_name, venue_cost, catering_cost_per_person

def add_guest(guest_list):
    """Function to add a guest to the guest list."""
    guest_name = input("Enter guest name to add: ")
    guest_list.append(guest_name)
    print(f"Guest '{guest_name}' added to the guest list.")

def calculate_total_cost(venue_cost, catering_cost_per_person, guest_list):
    """Function to calculate the total cost based on the number of guests."""
    total_guests = len(guest_list)
    total_catering_cost = catering_cost_per_person * total_guests
    total_cost = venue_cost + total_catering_cost
    return total_cost, total_guests, total_catering_cost

def main():
    # Step 1: Get event details
    event_name, venue_cost, catering_cost_per_person = get_event_details()

    # Step 2: Create an empty guest list
    guest_list = []

    # Step 3: Add guests to the event
    while True:
        add_more_guests = input("\nDo you want to add a guest? (y/n): ").strip().lower()
        if add_more_guests == 'y':
            add_guest(guest_list)
        elif add_more_guests == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    # Step 4: Calculate the total event cost
    total_cost, total_guests, total_catering_cost = calculate_total_cost(venue_cost, catering_cost_per_person, guest_list)

    # Step 5: Display event details and cost
    print(f"\nEvent Summary for {event_name}")
    print(f"Total Guests: {total_guests}")
    print(f"Guest List: {', '.join(guest_list)}")
    print(f"\nVenue Cost: ${venue_cost}")
    print(f"Catering Cost: ${total_catering_cost}")
    print(f"Total Event Cost: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
