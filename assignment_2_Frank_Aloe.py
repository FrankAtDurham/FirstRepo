#Assignment #2   (Francesco) Frank Aloe   
import datetime
#print('Question_1:- Print the following variables as a concatenated string using the "old-style" formatting. The result should be "Hello World".')
#print('word1 = "Hello"')
#print('word2 = "World"')
#answer Question 1
print('Question 1 Answer')
word1 = 'Hello'
word2 = 'World'
print('%s %s'%(word1,word2))


#print('Question_2:- Print the following variables as a concatenated string\n using the "new-style" formatting. The result should be "Hello World".')
#print('word1 = "Hello"')
#print('word2 = "World"')
#answer Question 2
print('Question 2 Answer')
word1 = 'Hello'
word2 = 'World'
print('{} {}'.format(word1,word2))

#print('Question_3:- Print the following variables as a concatenated string using an f-string. The result should be "Hello World".')
#print('word1 = "Hello"')
#print('word2 = "World"')
#answer Question 3
print('Question 3 Answer')
word1 = 'Hello'
word2 = 'World'
print(f'{word1} {word2}')
    
#print('Question_4:- Print the following variable 1234.9 as a dollar currency value.')
#print('It should be prepended by the $ symbol and have 2   decimal places.')
#print('amount = 1234.9')
#answer Question 4
print('Question 4 Answer')
amount = 1234.9
print(f'${amount:.2f}')

#print('Question_5    Print the following variable as a percentage value (i.e. 25%).')
#print('value = 0.25')
#answer Question 5
print('Question 5 Answer')
value_5 = 0.25
print(f'{value_5:2%}')

#print('Question_6:-    Print the following as a string including the positive sign.')
#print('value = 1234')
#answer Question 6
print('Question 6 Answer')
value_6 = 1234
print(f'{value_6:+4}')

#print('Question_7:-    Print the following value as a dollar currency value including')
#print('comma separators. (E.g. $123,567,90.00)')
#print('amount = 29430435872349.3283')
#answer Question 7
print('Question 7 Answer')
amount_7 = 29430435872349.3283
print(f'${amount_7:,}')

#print('Question_8 :-    Print the following integer as a North American telephone')
#print('number (e.g. (xxx) xxx-xxxx)')
#print('number = 4165551234')
#answer Question 8
print('Question 8 Answer')
number_8= '4165551234'
area = number_8[0:3]
prefix = number_8[3:6]
address = number_8[6:10]
print(f'(%s) %s %s'%(area,prefix,address))

#print('Question_9:-    Print the following integer with leading zeros so that   it occupies 4 characters (e.g. 0001)')
#print('number = 72')
#answer Question 9
print('Question 9 Answer')
number_9 = 72
print(f'{number_9:04}')

#print('Question_10:- Print a string which repeats the * character exactly 50 times.')
#answer Question 10
print('Question 10 Answer')
star10 ='*'
print(f'{star10:*^50}')

#print('Question_11:-Print the phrase "Hello World" centered within a series of *')
#print('characters. The total length of the string should be 79 characters.')
#print('E.g. *** Hello World ***')
#answer Question 11
print('Question 11 Answer')
line11 ='Hello World'
print(f'{line11:*^79}')

#print("Question_12:-Print today's date in the following format: Nov 01, 2022")
#answer Question 12
print('Question 12 Answer')
date12 = datetime.datetime.today()
print(date12.strftime('%b %d,%Y'))

#print("Question_13:-    Print today's date in the following format: November 01, 2022")
#answer Question 13
print('Question 13 Answer')
date13 = datetime.datetime.today()
print(date13.strftime('%B %d,%Y'))

#print("Question_14:-    Print the today's date in the following format: YYYY-MM-DD format.")
#answer Question 14
print('Question 14 Answer')
date14 = datetime.datetime.today()
print(date14.strftime('%Y-%d,%d'))

#print('Question_15:-    Print the current time in 24 hour format with seconds.')
#print('(i.e. 23:21:03)')
#answer Question 15
print('Question 15 Answer')
time15 = datetime.datetime.today()
print(time15.strftime('%H:%M:%S'))

#print('Question_16:- Print the current time using AM/PM (e.g 01:34 PM)')
print('Question 16 Answer')
time16 = datetime.datetime.today()
print(time15.strftime('%H:%M %p'))

#print("Question_17:-Print tomorrow's weekday name ")
#('.e. if today is Friday,tomorrow is Saturday')
print('Question 17 Answer')
date17 = datetime.datetime.today() + datetime.timedelta(days=1)
print(date17.strftime('%A'))

#print('Question_18:- Using the strptime function, print the following string')
#print('as a date object.')
#print("'my_date = '2014-12-20'")
print('Question 18 Answer')
date18 = '2014-12-20'
print(datetime.datetime.strptime(date18,"%Y-%m-%d"))


#print('Question_19:-  Using the strptime function, convert and print the following')
#print('as a datetime object.')
#print("my_datetime = '2014-12-20 23:12'")
print('Question 19 Answer')
date19 = '2014-12-20 23:12'
print(datetime.datetime.strptime(date19,"%Y-%m-%d %H:%M"))

#print('Question_20:-  Subtract 5 hours from the current datetime and print.')
print('Question 20 Answer')
datetime20 = datetime.datetime.today()
print(datetime20 - datetime.timedelta(hours=5))

#print('Question_21:-    Add 7 days to the current datetime and print.')
print('Question 21 Answer')
datetime21 = datetime.datetime.today()
print(datetime21 + datetime.timedelta(days=7))

#print('Question_22:-    Print the following string as a date object. Assume that')
#print('a week begins on a Sunday.')
#print("'my_date = 'Day 2 of week 23, 2020'")
print('Question 22 Answer')
datetime22 = 'Day 2 of week 23, 2020'
myDate22 = datetime.datetime.strptime(datetime22,'Day %w of week %W, %Y')
print(myDate22)

#print('Question_23:- Print the last three characters of the following string.')
#print("alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'")
print('Question 23 answer')
alpha23 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(f'{alpha23[23:26]}')
    
#print('Question_24:-Print the current date and time in ISO-8601 format.')
print('Question 24 answer')
dtvalue24 = datetime.datetime.today()
print(dtvalue24)

#print("Question_25:-Using today's date, how many days have elapsed since the")
#print('beginning of the year? (e.g. If today is Jan 3, there would')
#print('be 2 days). Return as an integer.')
print('Question 25 Answer')
value25 = '2023 1 1 00:00:00'
value25a = datetime.datetime.strptime(value25,'%Y %m %d %H:%M:%S')
value25b = datetime.datetime.today()
diff25 = value25b-value25a
print(diff25.days)

#print('Question_26:-How much time is left this year? Print a timedelta')
print('Question 26 Answer')
value26 = '2023 12 31 23:59:59'
value26a = datetime.datetime.strptime(value26,'%Y %m %d %H:%M:%S')
value26b = datetime.datetime.today()
delta26 = value26a-value26b
print(delta26)

#print('Question_27:-How many seconds are left this year? Return an integer.')
  #'(Hint: look for a helper function on timedelta)')
print('Question 27 Answer')
value27 = '2023 12 31 23:59:59'
value27a = datetime.datetime.strptime(value27,'%Y %m %d %H:%M:%S')
value27b = datetime.datetime.today()
difference = value27a - value27b
differenceSec = difference.total_seconds()
print(int(difference.total_seconds()))

#print("Question_28:- Print today's year, month and day")
print('Question 28 Answer')
value28 = datetime.datetime.today()
print(f'%s %s %s'%(value28.year,value28.month,value28.day))




