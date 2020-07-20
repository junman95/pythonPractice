class Contact:
    def __init__(self,name,phone_number,e_mail,addr):
        self.name=name
        self.phone_number= phone_number
        self.e_mail= e_mail
        self.addr= addr

    def print_info(self):
        print("Name: " ,self.name)
        print("Ph_Number: " ,self.phone_number)
        print("E_mail:",self.e_mail)
        print("Address",self.addr)


if __name__=="__main__":
    addr1=Contact("junman","010-4901-9506","junman95@naver.com","7corps")
    addr1.print_info()
