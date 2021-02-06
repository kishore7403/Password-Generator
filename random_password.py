import random as rd

def generate_spl_chr():
	randint_special_set = rd.randint(1, 4)			#ASCII values of special characters are available in 4 ranges.
	if (randint_special_set==1):
		spl_chr = chr(rd.randint(33,47))
	elif(randint_special_set==2):
		spl_chr = chr(rd.randint(58,64))
	elif(randint_special_set==3):
		spl_chr = chr(rd.randint(91,96))
	else:
		spl_chr = chr(rd.randint(123,126))
	return spl_chr

def generate_upper():
	upper=chr(rd.randint(65,90))                 #ASCII of uppercase lie between 65-90.
	return upper

def generate_lower():
	lower=chr(rd.randint(97,122))                 #ASCII of lowercase lie between 97-122.
	return lower


def generate_digit():
	digit=chr(rd.randint(48,57))				#ASCII of digits lie between 48-57.
	return digit

def generate_any_valid_chr():
	any_char=chr(rd.randint(33,126))			#ASCII of any valid char lie between 33-126.
	return any_char

def password_generator(number,length):
	passwords_generated=[]
	for i in range(0,number):
		the_password=[0 for x in range(length)]
		one_special=generate_spl_chr()
		one_upper=generate_upper()
		one_lower=generate_lower()
		one_digit=generate_digit()
		strong_guys=[one_special,one_upper,one_lower,one_digit]			#passwords with atleast one symbol,uppercase,lowercase letter and digit is strong
		for i in strong_guys:
			j=0
			while j==0:
				random_insert=rd.randint(0,length-1)
				if the_password[random_insert]==0:
					the_password[random_insert]=i
					j=1
		for j in range(0,length):
			if the_password[j]==0:
				the_password[j]= generate_any_valid_chr()
		passwords_generated.append(''.join(the_password))
	return passwords_generated

password_length=0
while password_length<6:
	password_length=int(input("Enter the password length(minimum-6 characters):"))			#a password with minimum 6 characters is considered strong
	if password_length<6:
		print("INFO: Minimum 6 characters required,try again!")
no_of_passwords=(int(input("number of passwords you need:")))
print("Below are passwords you can use")
for i in password_generator(no_of_passwords,password_length):
	print(i)