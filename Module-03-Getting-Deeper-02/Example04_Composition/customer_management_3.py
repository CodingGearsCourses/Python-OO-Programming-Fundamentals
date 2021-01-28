# https://www.globaletraining.com/
# Simple Composition (Specific form of association)
# Using Properties


class CustomerProfile:

    def __init__(self, first_name, last_name, profile_id, service_level):
        self.first_name = first_name
        self.last_name = last_name
        self.profile_id = profile_id
        self.service_level = service_level
        self.__customer_address = None

    @property
    def customer_address(self):
        return self.__customer_address

    @customer_address.setter
    def customer_address(self, obj_address):
        check_obj = isinstance(obj_address, CustomerAddress)
        if check_obj:
            self.__customer_address = obj_address
        else:
            print("You did not pass a valid customer address object!")

    def print_customer_info(self):
        print("{}, {}, {}, {}".format(self.first_name, self.last_name, self.profile_id, self.service_level))

    def print_customer_address(self):
        print("{} {}, {}, {}, {}, {}, {}".format(self.__customer_address.street_no,
                                                 self.__customer_address.street_name,
                                                 self.__customer_address.apt_suit_no,
                                                 self.__customer_address.city,
                                                 self.__customer_address.state,
                                                 self.__customer_address.county,
                                                 self.__customer_address.zip_code))


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
    try:
        print("Customer object".center(40, "-"))
        obj_address1 = CustomerAddress("123", "Baker Street", "", "San Jose", "California", "USA", "95000-1234")
        obj_address2 = "123"
        obj_customer1 = CustomerProfile("Tom", "Key", "P1001", "SL101")
        obj_customer1.customer_address = obj_address2
        obj_customer1.print_customer_info()
        obj_customer1.print_customer_address()
    except ValueError as ve:
        print("Value Error!")
    except AttributeError as ae:
        print("Attribute Error!")
    except Exception as e:
        print("Generic Exception!")
        print(e)


if __name__ == '__main__':
    main()
