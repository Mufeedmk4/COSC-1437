# Mufeed Kamal
# W215659219
# Programming Fundamentals II COSC 1437

# This function takes those MEMBERS who are NOT registered and puts them into an initialized empty array 
def unRegisteredMembers(members, registered):
    notRegisteredMembers = []
    for member in members: # For loop for each member, runs an if statement to validate for registration
        email = member[1] # Since the emails are the second string in the array, its called at point 1
        if email not in registered:
            notRegisteredMembers.append(member) # Pushes current member into initialized array
    return notRegisteredMembers

# This function takes those REGISTERED who are NOT members and puts them into an initialized empty array 
def nonMemberRegistrants(members, registered):
    notMemberRegistrants = []
    for email in registered:
        found = False # found boolean initialized to Flase
        for member in members:
            if email == member[1]: # Inherent true statement, triggers found boolean to be true
                found = True
                break
        if not found:
            notMemberRegistrants.append(email) # Pushes current email into initialized array
    return notMemberRegistrants

# This function takes the given list and prints it line by line in a vertical fashion
def verticalSort(list):
    for item in list:
        print(item)

# Control Flow
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

    # This gets those who are not registered and are in the members group
    notRegisteredMembers = unRegisteredMembers(members, registered)

    # This gets those who are not members but are registered for the event
    notMemberRegistrants = nonMemberRegistrants(members, registered)

    # Name Card
    print("---------------------------------------")
    print("Mufeed Kamal")
    print("W215659219")
    print("Programming Fundamentals II COSC 1437")
    print("---------------------------------------")
    
    # Members ! Registered
    print("Members that have registered:")
    verticalSort(notRegisteredMembers)
    print("---------------------------------------")
    # Registered ! Members
    print("Registered but not members:")
    verticalSort(notMemberRegistrants)
    print("---------------------------------------")