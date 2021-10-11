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
