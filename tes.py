import phonenumbers
num = '+959559'

number = phonenumbers.parse(num)
print(phonenumbers.is_valid_number(number))
print(number.national_number)