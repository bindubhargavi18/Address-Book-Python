import logging
from address_book import AddressBook

logging.basicConfig(filename="address_book_system.log", filemode="w")
log = logging.getLogger()

if __name__ == '__main__':
    print("Welcome to address book program")
    address_book = AddressBook()
    address_book.add_contact()
    while True:
        try:
            choice = int(input("Which operation you want to perform..\n1.Add new contact\n2.Edit contact\n"
                               "3.Display Contact\n4.Delete Contact\n5.Write Data into csv file\n"))
            if choice == 1:
                address_book.add_contact()
            elif choice == 2:
                address_book.display_contacts()
            elif choice == 3:
                exit(0)
            else:
                log.warning("Invalid option")
        except ValueError:
            logging.warning("Invalid Option selected")
