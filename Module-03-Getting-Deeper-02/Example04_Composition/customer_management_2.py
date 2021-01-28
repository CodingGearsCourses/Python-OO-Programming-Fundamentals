# https://www.globaletraining.com/
# Simple Composition (Specific form of association)


class CustomerProfile:

    def __init__(self, first_name, last_name, profile_id, service_level, obj_address):
        self.first_name = first_name
        self.last_name = last_name
        self.profile_id = profile_id
        self.service_level = service_level
        self.obj_address = obj_address

    def print_customer_info(self):
        print("{}, {}, {}, {}".format(self.first_name, self.last_name, self.profile_id, self.service_level))

    def print_customer_address(self):
        print("{} {}, {}, {}, {}, {}, {}".format(self.obj_address.street_no,
                                                 self.obj_address.street_name,
                                                 self.obj_address.apt_suit_no,
                                                 self.obj_address.city,
                                                 self.obj_address.state,
                                                 self.obj_address.county,
                                                 self.obj_address.zip_code))


class CustomerAddress:
    def __init__(self, street_no, street_name, apt_suit_no, city, state, county, zip_code):
        self.street_no = street_no
        self.street_name = street_name
        self.apt_suit_no = apt_suit_no
        self.city = city
        self.state = state
        self.county = county
        self.zip_code = zip_code


def main():
    print("Customer object".center(40, "-"))

    obj_address1 = CustomerAddress("123", "Baker Street", "", "San Jose", "California", "USA", "95000-1234")
    obj_address2 = "123 Baker Street, Boston, MA"
    obj_customer1 = CustomerProfile("Tom", "Key", "P1001", "SL101", obj_address2)

    obj_customer1.print_customer_info()
    obj_customer1.print_customer_address()


if __name__ == '__main__':
    main()
