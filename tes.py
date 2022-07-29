import phonenumbers
num = '+79250438094'

number = phonenumbers.parse(num)
print(phonenumbers.is_valid_number(number))
print(number.raw_input)
print(number.national_number)