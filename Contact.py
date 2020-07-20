class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print("Name: ", self.name)
        print("Ph_Number: ", self.phone_number)
        print("E_mail:", self.e_mail)
        print("Address", self.addr)


def set_contact():
    name = input("Name: ")
    phone_number = input("Ph_Number: ")
    e_mail = input("E_mail: ")
    addr = input("Address: ")
    contact = Contact(name, phone_number, e_mail, addr)
    return contact


def print_menu():
    print("1. 연락처 입력 ")
    print("2. 연락처 출력 ")
    print("3. 연락처 삭제 ")
    print("4. 종료 ")
    menu = input("메뉴를 선택해 주세요 : ")
    return int(menu)


def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()


def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]


def run():
    contact_list = []
    while 1:
        menu_choice = print_menu()
        if menu_choice == 1:
            contact = set_contact()
            contact_list.append(contact)
        elif menu_choice == 2:
            print_contact(contact_list)
        elif menu_choice == 3:
            name = input("삭제할 연락처의 Name :")
            delete_contact(contact_list, name)
        elif menu_choice == 4:
            break


if __name__ == "__main__":
    run()
