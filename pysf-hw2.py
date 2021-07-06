plain_text =  input("please enter the text\n")
shift = int(input("please enter the size of shift\n"))
a_code = ord('a')
z_code = ord('z')

cipher_text = ""
for character in plain_text:
	code = ord(character)
	cipher_text = cipher_text + chr(a_code + (code- a_code+shift)%(z_code- a_code))
print("\n" + cipher_text)
