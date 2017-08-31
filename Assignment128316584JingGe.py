######################################################################################################
#                                                                                                    #
#                     FIT9133 Programming Foundations in Python ---- Assignment 1                    #
#                                                                                                    #
######################################################################################################

# STUDENT ID: 28316584
# NAME: JING GE


# This program is the answer of the Assignment 1 for Monash University Unit FIT9133 Programming Foundations
# in Python. After entering the necessary information, the program will firstly show the formatted passport
# containing new name, new ID, the new birth of date and the authorisation, then will show the encrypted
# method for the name and the encrypted name, lastly will show the formatted passport with the encrypted
# name and as well other unchanged information.


# The program is composed like this:

#  1. The commands are all explained by the comments (above the commands),
#  2. For most of time, there are two empty lines between the comment and the last command.
#  3. Some comments may be in the same line following the corresponding commands


# For convenience of understanding the meanings of the variables in the program,
# Abv. in variables are listed as follows:

# fir ---- first
# sec ---- second
# ls ---- list
# cur ---- current
# dgt ---- digits
# bir ---- birthday
# dict ---- dictionary
# alp ---- alphabet
# enc ---- encrypted


# ---- Question 1 ----


# Define and input 2 first names and 2 second names, and ensure these four variables to be string type
fir_name_1 = str(input("Please Enter the First Name 1: "))
fir_name_2 = str(input("Please Enter the First Name 2: "))
sec_name_1 = str(input("Please Enter the Second Name 1: "))
sec_name_2 = str(input("Please Enter the Second Name 2: "))


# Define a list for containing all the letters in the First Name 1
ls_fir_name_1 = []


# Append every letter in the First Name 1,
# and all the letters will be strings stored in the list designed for the First Name 1
for letter in fir_name_1:
    ls_fir_name_1.append(letter)


# Define a list for containing all the letters in the First Name 2
ls_fir_name_2 = []


# Append every letter in the First Name 2,
# and all the letters will be strings stored in the list designed for the First Name 2
for letter in fir_name_2:
    ls_fir_name_2.append(letter)


# Define a list for containing all the letters in the Second Name 1
ls_sec_name_1 = []

# Append every letter in the Second Name 1,
# and all the letters will be strings stored in the list designed for the Second Name 1
for letter in sec_name_1:
    ls_sec_name_1.append(letter)


# Define a list for containing all the letters in the Second Name 2
ls_sec_name_2 = []


# Append every letter in the Second Name 2,
# and all the letters will be strings stored in the list designed for the Second Name 2
for letter in sec_name_2:
    ls_sec_name_2.append(letter)


# Define two varibles for the new First Name and the new Second Name and set them as string type
new_fir_name = ''
new_sec_name = ''


# Define a variable which is an index representing the start position of the letter in the list.
# The letter is the letter of First Name 1.
# The list is the list containing all the letters of the First Name 1.
i_fir_name_1 = 0


# Use while loop to add the first half of strings in the list,
# which contains all the letters of the First Name 1.
while i_fir_name_1 < (len(fir_name_1) // 2):
    new_fir_name += ls_fir_name_1[i_fir_name_1]
    i_fir_name_1 += 1


# Define a variable which is an index representing the start position of the letter in the list.
# The letter is the letter of First Name 2.
# The list is the list containing all the letters of the First Name 2.
i_fir_name_2 = len(fir_name_2) // 2


# Use while loop to add the second half of strings in the list,
# which contains all the letters of the First Name 2.
while i_fir_name_2 <= (len(fir_name_2) - 1):
    new_fir_name += ls_fir_name_2[i_fir_name_2]
    i_fir_name_2 += 1


# Define a variable which is an index representing the start position of the letter in the list.
# The letter is the letter of Second Name 1.
# The list is the list containing all the letters of the Second Name 1.
i_sec_name_1 = 0


# Use while loop to add the first half of strings in the list,
# which contains all the letters of the Second Name 1.
while i_sec_name_1 < (len(sec_name_1) // 2):
    new_sec_name += ls_sec_name_1[i_sec_name_1]
    i_sec_name_1 += 1


# Define a variable which is an index representing the start position of the letter in the list.
# The letter is the letter of Second Name 2.
# The list is the list containing all the letters of the Second Name 2.
i_sec_name_2 = len(sec_name_2) // 2


# Use while loop to add the second half of strings in the list,
# which contains all the letters of the Second Name 2.
while i_sec_name_2 <= (len(sec_name_2) - 1):
    new_sec_name += ls_sec_name_2[i_sec_name_2]
    i_sec_name_2 += 1


# Combine the new first name and the new second name together to obtain the new name.
new_name = new_fir_name + ' ' + new_sec_name


# ---- Question 2 ----


# Define and input two ages, and make them be string type for easily using them later.
age_1 = str(input("Please Enter the Age 1: "))
age_2 = str(input("Please Enter the Age 2: "))


# Define and input the current year, and set it as an integer.
cur_year = int(input("Please Enter the Current Year: "))


# Define two lists to store every digits of two old ages respectively.
dgt_1 = []
dgt_2 = []


# Separate Age 1 into digits, and all the digits are string type stored in the designed list.
for num in age_1:
    dgt_1.append(num)


# Separate Age 2 into digits, and all the digits are string type stored in the designed list.
for num in age_2:
    dgt_2.append(num)


# Define the data type of new four variables,
# the first two are indexes representing the position of digits in the list which are integer type,
# and the last two are the new two ages which are as well set as integer type.
i_1 = 0
i_2 = 0
new_age_1 = 0
new_age_2 = 0


# Use while loop to adding all the digits of Age 1 together.
# Each time of loop, increase the index by one.
# When the index smaller than the length of the Age 1, the loop continues.
while i_1 < len(age_1):
    new_age_1 += int(dgt_1[i_1])
    i_1 += 1


# Use while loop to adding all the digits of Age 2 together.
# Each time of loop, increase the index by one.
# When the index smaller than the length of the Age 2, the loop continues.
while i_2 < len(age_2):
    new_age_2 += int(dgt_2[i_2])
    i_2 += 1


# Combine the new age first digit and the new age second digit to obtain the new age.
new_age = new_age_1 + new_age_2


# Use current year minus the new age to obtain the birth year.
bir_year = cur_year - new_age


# Set a random integer range from 1 to 12, and obtain a random birth month from this range.
from random import randint
bir_month = randint(1, 12)


# Define a variable for the birth day and set this variable as an integer type.
bir_day = 0


# Set two different ranges of random month according to Gregorian Calendar.
month_31days = [1, 3, 5, 7, 8, 10, 12]  # Months with 31 days are Jan, Mar, May, Jul, Aug, Oct and Dec
month_30days = [4, 6, 9, 11]            # Months with 30 days are Apr, Jun, Sep and Nov


# Since there exists the leap year and the non-leap year,
# the months with 30 days and the month with 31 days,
# The day of birth will be chosen randomly according to both the year of birth and the month of birth.

# If the year of birth is a leap year, then the day of birth chosen enter in the following loop.
if bir_year % 4 == 0:

    if bir_month in month_31days:     # If the month of birth has 31 days

        bir_day = randint(1, 31)      # then the day of birth will be randomly chosen between 1st and 31st

    elif bir_month in month_30days:   # If the month of birth has 30 days,

        bir_day = randint(1, 30)      # then the day of birth will be randomly chosen between 1st and 30th

    elif bir_month == 2:              # If the month of birth is February in a leap year

        bir_day = randint(1, 29)      # then the day of birth will be randomly chosen between 1st and 29th

# If the year of birth is not a leap year, then the day of birth chosen enter in the following loop.
elif bir_year % 4 != 0:

    if bir_month in month_31days:     # If the month of birth has 31 days

        bir_day = randint(1, 31)      # then the day of birth will be randomly chosen between 1st and 31st

    elif bir_month in month_30days:   # If the month of birth has 30 days

        bir_day = randint(1, 30)      # then the day of birth will be randomly chosen between 1st and 30th

    elif bir_month == 2:              # If the month of birth is February not in a leap year

        bir_day = randint(1, 28)      # then the day of birth will be randomly chosen between 1st and 28th


# For obtaining the standard format of the month number,
# if the month of birth is between Jan and Sep (only one digit), add an '0' before the month number,
# if the month of birth is between Oct and Dec (two digits), there is no need to change.
if len(str(bir_month)) == 1:
    bir_month = '0' + str(bir_month)
else:
    bir_month = bir_month


# For obtaining the standard format of the day number,
# if the day of birth is between 1st and 9th (only one digit), then add an '0' before the month number,
# if the day of birth is later than 9th (two digits), then there is no need to change.
if len(str(bir_day)) == 1:
    bir_day = '0' + str(bir_day)
else:
    bir_day = bir_day


# Combine all the information obtained before together to obtain the new date of birth,
# and set it as the standard format of date.
date_of_birth = str(bir_day) + '/' + str(bir_month) + '/' + str(bir_year)


# Define the original ID through transferring the new age to string type.
ori_ID = str(new_age)


# Define a list for all the digits of the original ID.
ls_ID = []


# Append the original ID string and put all the letters of this string in the designed list.
for num in ori_ID:
    ls_ID.append(num)


# Define a variable which is an index representing the position of the digit in the list.
# The digit is the digit in the ID, and the list is the list containing all the digits of the ID.
i = 0

# Use while loop to process the calculation for obtaining the new New ID.
# Each time of loop, increase the index by one.
# Since there are already two digits existing in the ID, the loop conduct for 8 times,
# and when the index smaller than 8, the loop continues.
while i < 8:
    last_two_dgt = int(ls_ID[i]) + int(ls_ID[i+1])
    new_digit = int(last_two_dgt) % 10
    ls_ID = ls_ID + [str(new_digit)]
    i = i + 1


# Define a variable which is an index representing the position of the digit in the list.
# The digit is the digit of the new ID, and the list is the list containing all the digits of the new ID.
i = 0


# Define a variable for ID and set it as string type.
ID = ''


# Use while loop to add all the strings in the list containing ID digits to the ID string,
# then the new ID obtained.

while i < 10:
    ID = ID + str(ls_ID[i])
    i = i + 1


# ---- Question 4 ----


# Print the new name and new passport ID in the first line,
# and print the new date of birth in the second line,
# and print the "Authorised by ***" in the third line.
print('\n' +
      '---- Formatted Passport ----' +
      '\n' +
      '\n' +
      'Name: ' + new_name + '  ' + 'Passport ID: ' + str(ID) +
      '\n' +
      '\n' +
      'Date of Birth: ' + str(date_of_birth) +
      '\n' +
      '\n' +
      'Authorised by ' + 'Gavin Kroeger')


# ---- Question 5 ----


# Set a string containing all the lower letters in the alphabet.
alp_ori_lower = 'abcdefghijklmnopqrstuvwxyz'


# Define a list for containing all the letters in the alphabet which are string type.
ori_alp_lower = []


# Append the alphabet string and put all the strings into the designed list.
for letter in alp_ori_lower:
    ori_alp_lower.append(letter)


# Random a number for shift.
# Since there are 26 letters in total in the alphabet, it is meaningless to shift over 25 positions,
# which will turn back to the original position.
from random import randint
shift_num = randint(1,25)


# Set the start status of the new lower letter alphabet same as the original one.
new_alp_lower = ori_alp_lower


# Define a variable which is an index representing the position of the letter in the list.
# The letter is the letter of the lowercase alphabet,
# and the list is the list containing all the letters of the lowercase alphabet.
i = 0


# Left shift the alphabet. Since the random shift number contains all the possible situations,
# there is no need to specifically distinguish left shift and right shift.
# The number of positions shifted is randomly picked up before,
# and is a defined variable called shift_num.
while i < shift_num:
    new_alp_lower= new_alp_lower + [ori_alp_lower[i]]
    del new_alp_lower[0]
    i = i + 1


# Set a string containing all the upper letters in the alphabet through transferring
alp_ori_upper = alp_ori_lower.upper()


# Define a list for containing all the letters in the alphabet which are string type
ori_alp_upper = []


# Append the alphabet string and put all the strings into the designed list
for letter in alp_ori_upper:
    ori_alp_upper.append(letter)


# Set the start status of the new lower letter alphabet same as the original one
new_alp_upper = ori_alp_upper


# Define a variable which is an index representing the position of the letter in the list.
# The letter is the letter of the uppercase alphabet,
# and the list is the list containing all the letters of the uppercase alphabet.
i = 0


# Use while loop the add the
while i < shift_num:
    new_alp_upper = new_alp_upper + [ori_alp_upper[i]]
    del new_alp_upper[0]
    i = i + 1


# Combine the original list containing all the lower letters,
# and the original list containing all the upper letters
ori_alp = ori_alp_lower + ori_alp_upper


# Combine the new list containing all the lower letters,
# and the new list containing all the upper letters
new_alp = new_alp_lower + new_alp_upper


# Zip two lists and let all the strings in this two lists pair one by one
zip_dict = zip(ori_alp, new_alp)


# Set the zipped list as list type
ls_dict = list(zip_dict)


# Set the dictionary list as dictionary type
enc_dict = dict(ls_dict)


# Set a list for all the letters in the new first name
fir_name_dgt = []


# Append the new first name and put these letters in the designed list
for letter in new_fir_name:
    fir_name_dgt.append(letter)


# Set a list for all the letters in the new second name
sec_name_dgt = []


# Append the new second name and put these letters in the designed list
for letter in new_sec_name:
    sec_name_dgt.append(letter)


# Define a variable which is an index representing the position of the letter in list of the first name,
i = 0


# Define a variable representing the encrypted first name and set it as string type
enc_fir_name = ''


# Use the loop to find all the corresponding letters of new first name letters in the dictionary,
# and add these corresponding letters to the encrypted first name
while i < len(new_fir_name):
    enc_fir_name = enc_fir_name + enc_dict[fir_name_dgt[i]]
    i = i + 1


# Define a variable which is an index represent the position of the letter in list of the second name
i = 0


# Define a variable representing the encrypted second name and set it as string type
enc_sec_name = ''


# Use while loop to find all the corresponding letters of new second name letters in the dictionary,
# and add these corresponding letters to the encrypted second name
while i < len(new_sec_name):
    enc_sec_name = enc_sec_name + enc_dict[sec_name_dgt[i]]
    i = i + 1


# Combine the encrypted first name and encrypted second name to obtain the full encrypted name
enc_name = enc_fir_name + ' ' + enc_sec_name


# Print out the full encrypted name
print('\n' +
      'After left shifting ' + str(shift_num) +
      ' positions of the alphabet, the encrypted name is: ' + enc_name)

# Print the formatted passport with the encrypted name
print('\n' +
      '---- Formatted Passport with Encryption ----'
      '\n' +
      '\n' +
      'Name: ' + enc_name + '  ' + 'Passport ID: ' + str(ID) +
      '\n' +
      '\n' +
      'Date of Birth: ' + str(date_of_birth) +
      '\n' +
      '\n' +
      'Authorised by ' + 'Gavin Kroeger')