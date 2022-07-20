class Contents:
    def __init__(self):
        self.name = None
        self.phone = None
        self.email = None
        self.address = None

    def input_addr(self):
        print(" ")
        self.name = input('이름을 입력하세요. ')
        self.phone = input('전화번호를 입력하세요. ')
        self.email = input('이메일을 입력하세요. ')
        self.address = input('주소를 입력하세요. ')

    def delete_addr(self):
        print(" ")
        self.name = None
        self.phone = None
        self.email = None
        self.address = None

    def print_info(self):
        print(" ")
        print("name : ", self.name)
        print("phone : ", self.phone)
        print("email : ", self.email)
        print("address : ", self.address)

def Menu():
    print(" ")
    print("1. 주소 입력")
    print("2. 주소 삭제")
    print("3. 주소 출력")
    print("4. 종료")
    print(" ")

    num = int(input('원하는 메뉴를 입력하세요 '))
    return num

if __name__ == '__main__':
    pass


info = Contents()

while True :
    num = Menu()

    if num == 1 :
        info.input_addr()
    elif num == 2 :
        info.delete_addr()
    elif num == 3 :
        info.print_info()
    elif num == 4 :
        print('프로그램을 종료합니다')
        break
