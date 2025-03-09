# print('Hello World!')

# name = input('Enter your name: ')
# print('Hello, ' + name + '!')
# print(name.capitalize())


# Sting Format
# first_name = input("Your first name: ")
# last_name = input("Enter your last name: ")
# print(f"Hello {first_name} {last_name}")



# Type conversion
# print(str(3) + " days left!")

# str1 = '3'
# str2 = '6'
# print(int(str1)+ int(str2))



from datetime import datetime, timedelta

# today = datetime.now()
# print(f"Today is {str(today)}")

# # timedelta is used to define a period of time
# one_day = timedelta(days=1)
# print(f"Yesderday was {str(today-one_day)}")

# # parts of date
# print(f"Day: {today.day}")
# print(f"Month: {today.month}")
# print(f"Year: {today.year}")

# Taking date as input from user
birthday=input("Enter your birthday(mm/dd/yyyy): ")
birthday_date=datetime.strptime(birthday, "%d/%m/%Y")
print(f"Birthday: {birthday_date}")