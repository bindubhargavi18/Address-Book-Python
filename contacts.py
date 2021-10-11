class ContactPerson:

    def __init__(self, contact):
        self.first_name = contact.get("first_name")
        self.last_name = contact.get("last_name")
        self.address = contact.get("address")
        self.state = contact.get("state")
        self.city = contact.get("city")
        self.zip_code = contact.get("zip_code")
        self.email = contact.get("email")
        self.phone_number = contact.get("phone_number")

    def __str__(self):
        return "FirstName:{0}\nLastName:{1}\nAddress:{2}\nState:{3}\nCity:{4}\nZip:{5}\nPhoneNumber:{6}\nEmail:{7}" \
            .format(self.first_name, self.last_name, self.address, self.state, self.city, self.zip_code,
                    self.phone_number,
                    self.email)

    @staticmethod
    def create_contact():
        """
            Creating a new contact in address book which contain fields:
            firstname,lastname,address,state,city,zipcode,phone number,email
            stored in a dictionary...
            :return: contacts dictionary
        """
        first_name = input("Enter first name:")
        last_name = input("Enter last name:")
        address = input("Enter address:")
        state = input("Enter State:")
        city = input("Enter city:")
        zip_code = input("Enter zip:")
        phone_number = input("Enter phone number:")
        email = input("Enter email:")
        contact_details = {
            "first_name": first_name,
            "last_name": last_name,
            "address": address,
            "state": state,
            "city": city,
            "zip_code": zip_code,
            "phone_number": phone_number,
            "email": email,
        }
        contact = ContactPerson(contact_details)
        return contact
