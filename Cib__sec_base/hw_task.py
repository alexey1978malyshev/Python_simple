"""Написать программу на Python, которая проверяет вводимый пользователем пароль на сложность:
— не менее 8 символов*
— наличие прописных и строчных букв*
— наличие цифр
и переводит его в хэш-значение."""


def check_user_pswd():
    result_check = False
    while result_check is False:
        input_str = input('Input the password:\n')
        #check_sym = [i.isdigit() or i.isalpha() for i in input_str]
        check_sym = []
        check_digigt = []
        check_alpha = []
        for i in input_str:
            if i.isdigit():
                check_digigt.append(i)
            elif i.isalpha():
                check_alpha.append(i)
            else:
                check_sym.append(False)
        #Проверяем длину
        if len(input_str) < 8:
            print(f'Password{input_str} is not valid. Password length must be more or equal 8 symbols... Try again:\n')
        #проверяем наличие букв или цифр и больше ничего
        elif False in check_sym:
            print(f'Password "{input_str}" is not valid. Must have letters and digits only...Try again:\n')
        # проверяем наличие как букв так и цифр
        elif len(check_digigt) == 0 or len(check_alpha) == 0:
            print(f'Password "{input_str}" is not valid. Password must has letters and digits...Try again:\n')
        # проверяем наличие букв в разных регистрах
        elif input_str.lower() == input_str or input_str.upper() == input_str:
            print(f'Password "{input_str}" is not valid. Letters must be upper and lower cases...Try again:\n')

        #если все Ok
        else:
            result_check = True

        if result_check is True:
            print(f'Your password is good! - {input_str}')

if __name__ == '__main__':
    check_user_pswd()


# s = 'JJeJJ'
# b = s.upper()
# if s==b:
#     print(True)
# else:
#     print(False)
