from contacts import ContactPerson
import logging

logging.basicConfig(filename="address_book_system.log", filemode="w")
log = logging.getLogger()


class AddressBook:

    def __int__(self):
        self.contact_list = []

    def add_contact(self):
        """
        adding contacts into address book
        calling dictionary from contact class...
        :return:added contact to address book
        """
        contact = ContactPerson.create_contact()
        self.contact_list.append(contact)

    def display_contacts(self):
        """
        This method displays all the contacts in address book...
        :return: contacts in address book
        """
        contacts = "\n".join(str(contact) for contact in self.contact_list)
        print(contacts)

    def edit_contact(self):
        """
        This method is called whenever user wants to edit the existing contact
        in address book based on first name...
        :return: particular field that user want to edit
        """
        name = str(input("Enter first name of contact:"))
        for contact in self.contact_list:
            if contact.first_name == name:
                try:
                    user_choice = int(input(
                        "Enter the number that you want to edit field in details"
                        " \n 1. First Name 2. Last name 3. Address 4. city 5. state 6.zip 7. Phone number 8.Email \n"))
                    if user_choice == 1:
                        first_name = input("Enter new first name\n")
                        contact.first_name = first_name
                    elif user_choice == 2:
                        last_name = input("Enter new last name\n")
                        contact.last_name = last_name
                    elif user_choice == 3:
                        address = input("Enter new address\n")
                        contact.address = address
                    elif user_choice == 4:
                        city = input("Enter new city\n")
                        contact.city = city
                    elif user_choice == 5:
                        state = input("Enter new state\n")
                        contact.state = state
                    elif user_choice == 6:
                        zip_code = input("Enter new zip\n")
                        contact.zip_code = zip_code
                    elif user_choice == 7:
                        phone_number = input("Enter new phone number\n")
                        contact.phone_number = phone_number
                    elif user_choice == 8:
                        email = input("Enter new email\n")
                        contact.email = email
                    else:
                        print("Please enter a valid input")
                except TypeError:
                    print("Invalid type entered... please provide integer values only....")
            else:
                print("Please enter a valid name")