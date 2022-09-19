#!/usr/bin/env python
# coding: utf-8

# In[ ]:


day_of_week = input("Enter the day of the week:");

if day_of_week in ('Monday', 'monday'):
    print("It is " + day_of_week + " today." )
    #print(day_of_week)
else:
    print("It is not Monday, it is " + day_of_week)
    #print(day_of_week)


# In[ ]:


day = 'monday'
if day == 'Monday':
    print('true')
else: 
    print('false')


# In[ ]:


day_of_week = input("What is the day today:")

if day_of_week in ('sunday', 'Sunday', 'Saturday', 'saturday'):
    print("It's a weekend")
else:
    print("It's a weekday")


# In[ ]:


number_of_hours_worked = 30
hourly_rate = 40
if number_of_hours_worked <= 40:
    paycheck_amount = number_of_hours_worked * hourly_rate
elif number_of_hours_worked > 40:
    paycheck_amount = ((40 * hourly_rate) + ((number_of_hours_worked - 40) * (hourly_rate * 1.5)))
print (paycheck_amount)


# # \#2 Loop basics

# In[ ]:


i = 5
while i <= 15:
    print(i)
    i += 1


# In[ ]:


i = 0
while i <= 100:
    print(i)
    print()
    i += 2


# In[ ]:


i = 100
while i >= -10:
    print(i)
    print()
    i -= 5


# In[ ]:


i = 2
while i <= 1000000:
    print(i)
    i = i * i


# In[ ]:


i = 100
while i >= 5:
    print(i)
    i -= 5


# # For loops

# In[ ]:


their_number = input('What number table do you want?:')
the_value = int(their_number)
n = 1
for x in range (10):
    result = the_value * n
  #  print(result)
    print(str(their_number) + " * " + str(n) + " = " + str((int(their_number) * n)))
  #  print(n)
    n += 1
    


# In[ ]:


i = 1
for i in range(10):
    print (i * str(i))


# # break and continue

# In[ ]:


user_num = int(input('Enter positive interger:'))
for x in range(user_num):
    print(user_num)
    user_num -= 1


# In[ ]:


user_num = int(input('Enter positive interger:'))
i = 0
while i <= user_num:
    print(i)
    i += 1


# In[1]:


test_value = int(input('Enter a positive odd number between 1 and 50:'))
base_value = 1
while test_value % 2 == 0 or test_value <= 0:
    test_value = int(input('Try again: enter a positive odd number between 1 and 50:'))
while base_value <= 50:
    if base_value == test_value:
        print('Skipping:' + str(test_value))
        base_value += 1
    elif base_value %2 != 0:
        print("Here's an odd number " + str(base_value))
        base_value += 1
    else:
        base_value += 1


# # fizzbuzz

# In[7]:


i = 1
while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz')
    elif i % 3 == 0 and i % 5 != 0:
        print('fizz')
    elif i % 5 == 0 and i % 3 != 0:
        print('buzz')
    else:
        print(i)
    i += 1


# In[57]:


i = int(input('Give me an interger:'))
start_num = 1
print('Here is your table:')
print('number | squared | cubed')
print('-------|---------|------')
while start_num <= i:
    print('{:<7}|{:<9}|{:<}'.format(start_num, start_num * start_num, start_num * start_num * start_num))
    start_num += 1


# # grades to letters

# In[4]:


#def grade_convert(
#user_grade = int(input("What is your grade (0-100):"))
    
#if user_grade.isdigit() == False:
#    print('I\'m not sure that\'s a valid grade, try again:')
#    int(input("What's your grade (0-100):"))
i = 10
while i > 1:
    user_grade = int(input("What is your grade (0-100):"))
    if user_grade >= 88:
            print('You made an A! Amazing')
    elif user_grade > 79 and user_grade < 88:
           print('You made a B! Beautiful')
    elif user_grade > 66 and user_grade < 80:
            print('You made a C! Close one')
    elif user_grade > 59 and user_grade < 76:
            print('You made a D! Dang')
    elif user_grade < 60:
            print('That is an F, I\'m sorry')
    else:
        print('I\'m not sure that\'s a valid grade, try again:')
        #int(input("What's your grade (0-100):"))

    continue_choice = input('Would you like to continue ((y/n):')
    if continue_choice == 'y':
        continue
    elif continue_choice != 'n':
        print('Nonvalid input, try again')
    else:
        print("Thanks for using the calculator")
        break
#)


# 

# In[25]:


readings={"title": "Dune", "publish_year": 1965, "author": "Frank Herbert", "genre": "sci-fi"}, {"title": 'Krondor the Betrayal', "publish_year": 1993, "author": "Raymond E. Feis", "genre": 'fantasy'}
i=0
for key in readings:
    print(readings[i])
    i += 1


# In[28]:


readings={"title": "Dune", "publish_year": 1965, "author": "Frank Herbert", "genre": "sci-fi"}, {"title": 'Krondor the Betrayal', "publish_year": 1993, "author": "Raymond E. Feis", "genre": 'fantasy'}
g_search = input('What genre should I look for?')
i=0
for key in readings:
    if (readings['genre'] == 'g_search'):
        print(readings[i])
        i += 1
    else:
        i += 1


# In[ ]:




