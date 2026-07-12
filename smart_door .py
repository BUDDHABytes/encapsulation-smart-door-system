class Staff:
    def __init__(self, s_name, access_code):
        self.s_name = s_name
        self.__access_code = access_code

    @property
    def access_code(self):
        return self.__access_code

    @access_code.setter
    def access_code(self, new_code):
        if len(new_code) >= 6:
            self.__access_code = new_code
            print("Access code updated successfully.")
        else:
            print("Error: Access code must be at least 6 characters long.")

    def display_info(self):
        print(f"Staff Name: {self.s_name}")
        print(f"Access Code: {self.access_code}")

staff_member = Staff("Arhin Pearl Sarfo",FOE.41.006.045.25)
staff_member.display_info()

staff_member.access_code = "secure987"
staff_member.display_info()
