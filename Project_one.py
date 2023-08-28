# Mufeed Kamal
# W215659219
# Programming Fundamentals II COSC 1437


# Function to print a list vertically
def print_list_vertically(lst):
    for item in lst:
        print(item)

# This is the control flow
if __name__ == "__main__":
    # Membership list
    members = [
        ["John Smith", "john.smith@hotmail.com"],
        ["John Doe", "john.doe@aol.com"],
        ["Bill Jack", "billy.jack@aol.com"],
        ["Chuck Connors", "chuck.conors@hotmail.com"],
        ["Lucy Ball", "lucy.ball@yahoo.com"],
        ["Bing Hope", "bing.hope@aol.com"],
        ["Bob Crosby", "bob.crosby@aol.com"],
        ["Piers Anthony", "piers.anthony@hotmail.com"]
    ]

    # Registered list
    registered = [
        "john.smith@hotmail.com",
        "john.doe@aol.com",
        "al.deniro@aol.com",
        "bob.crosby@aol.com",
        "billy.crystal@aol.com",
        "robert.pacino@aol.com"
    ]

    # Get members who have not registered
    members_not_registered = []
    for member in members:
        email = member[1]
        if email not in registered:
            members_not_registered.append(member)
        elif email in registered:
            continue

    # Get registrants who are not members
    registrants_not_members = []
    for email in registered:
        found = False
        for member in members:
            if email == member[1]:
                found = True
                break
        if found:
            continue
        elif not found:
            registrants_not_members.append([email])

    # Print members who have not registered
    print("\nMembers who have not registered for the event:")
    print_list_vertically(members_not_registered)

    # Print registrants who are not members
    print("\nRegistrants who are not members:")
    print_list_vertically(registrants_not_members)
