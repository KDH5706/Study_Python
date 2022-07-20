import numpy as np

class Contents:
    def __init__(self):
        self.name_s = []
        self.phone_s = []
        self.email_s = []
        self.address_s = []

    def input_addr(self):
        print(" ")
        self.name_s.append(input('이름을 입력하세요. '))
        self.phone_s.append(input('전화번호를 입력하세요. '))
        self.email_s.append(input('이메일을 입력하세요. '))
        self.address_s.append(input('주소를 입력하세요. '))

    def delete_addr(self, name, phone, email, address):
        print(" ")
        name_pos = np.where(np.array(self.name_s) == name)[0]
        phone_pos = np.where(np.array(self.phone_s) == phone)[0]
        email_pos = np.where(np.array(self.email_s) == email)[0]
        address_pos = np.where(np.array(self.address_s) == address)[0]

        min_pos_list = name_pos
        if len(min_pos_list) > len(phone_pos):
            min_pos_list = phone_pos
        if len(min_pos_list) > len(email_pos):
            min_pos_list = email_pos
        if len(min_pos_list) > len(address_pos):
            min_pos_list = address_pos

        all_true_pos = []
        for pos_index in min_pos_list:
            if pos_index in name_pos and pos_index in phone_pos and pos_index in email_pos and pos_index in address_pos :
                all_true_pos.append(pos_index)

        if not all_true_pos:
            print("모든 조건을 만족하는 목록이 없습니다.")
            return

        all_true_pos.sort(reverse = True)

        for delete_pos in all_true_pos:
            del self.name_s[delete_pos]
            del self.phone_s[delete_pos]
            del self.email_s[delete_pos]
            del self.address_s[delete_pos]

    def delete_addr_all(self):
        print(" ")
        self.name_s.clear()
        self.phone_s.clear()
        self.email_s.clear()
        self.address_s.clear()

    def print_info(self, name):
        print(" ")
        name_pos = np.where(np.array(self.name_s) == name)[0]
        for i in name_pos :
            print(" ")
            print("name : ", self.name_s[i])
            print("phone : ", self.phone_s[i])
            print("email : ", self.email_s[i])
            print("address : ", self.address_s[i])

    def print_info_all(self):
        for name, phone, email, address in zip(self.name_s, self.phone_s, self.email_s, self.address_s):
            print(" ")
            print("name : ", name)
            print("phone : ", phone)
            print("email : ", email)
            print("address : ", address)
def Menu():
    while True:
        print(" ")
        print("1. 주소 입력")
        print("2. 주소 삭제(개인)")
        print("3. 주소 삭제(전체)")
        print("4. 주소 출력(개인)")
        print("5. 주소 출력(전체)")
        print("6. 종료")
        print(" ")

        try:
            num = int(input('원하는 메뉴를 입력하세요 '))
            if 1 <= num <= 6 :
                return num
            else:
                print("")
                print("범위를 벗어난 숫자를 입력했습니다.")

        except ValueError :
            print("")
            print("잘못된 입력입니다.")


if __name__ == '__main__':
    pass

info = Contents()

while True :
    num = Menu()

    if num == 1 :
        info.input_addr()
    elif num == 2 :
        name = input("삭제할 이름을 입력하세요 ")
        phone = input("삭제할 전화번호를 입력하세요 ")
        email = input("삭제할 이메일을 입력하세요 ")
        address = input("삭제할 주소를 입력하세요 ")
        info.delete_addr(name, phone, email, address)
    elif num == 3 :
        info.delete_addr_all()
    elif num == 4 :
        name = input("검색할 이름을 입력하세요 ")
        info.print_info(name)
    elif num == 5 :
        info.print_info_all()
    elif num == 6 :
        print('프로그램을 종료합니다')
        break
