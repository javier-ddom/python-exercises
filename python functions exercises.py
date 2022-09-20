#!/usr/bin/env python
# coding: utf-8

# # is 2

# In[ ]:


def is_two(n):
    if n == 2 or n == '2':
        print("It's a 2")
        return True
    else:
        print("This is not a 2")
        return False
    
is_two(input())


# In[ ]:


is_two(5)


# # is vowel

# In[ ]:


def is_vowel(thing):
 #   to_check = thing
    if to_check in ('a,e,i,o,u'):
        print('Its a vowel')
        return True
    else:
        print('Is not a vowel')
        return False
    
is_vowel(input())


# # is consonant

# In[ ]:


"""
def is_con(thing):
    to_check = thing
    if to_check in ('a,e,i,o,u'):
        print('Its a vowel')
        return False
    else:
        print('Is a consonant')
        return True
    
is_con(input())
"""

def check_conson(checkable):
   # thing = input("Give a letter : ")
    if checkable.lower() in ('a e i o u'):
        print('Itsa vowel')
        return False
    
    else: 
        print('Itsa conson')
        return True
print("where now")



# In[ ]:


check_conson('b')


# In[ ]:


check_conson('b')


# # capitalize first letter if consonant

# In[ ]:


def cap_first(word):
    if check_conson(word[0]) == True:
        print(word[0].upper() + word[1:])


# In[ ]:


cap_first('banna')


# In[ ]:





# # tip calculator
# Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[ ]:


def calculate_tip(bill_amount, tip_percentage):
    amount_to_tip = bill_amount * tip_percentage
    print(amount_to_tip)


# In[ ]:


calculate_tip(100, .2)


# # apply discount

# In[ ]:


def apply_discount(original_price, discount_percentage):
    new_price = original_price - (original_price * (discount_percentage/100))
    print(new_price)


# In[ ]:


apply_discount(100, 15)


# # NEED TO COMPLETE handle commas

# In[ ]:


def handle_commas(number_string):
    


# # Get letter grade

# In[ ]:


def get_letter_grade():
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


# In[ ]:


get_letter_grade()


# # Remove vowels

# In[18]:


prestrip = input()
def remove_vowels(prestrip):
    leftovers = []
    n = 0
    for letter in prestrip:
       
        if prestrip[n].lower() in ('aeiou'):
            n += 1
          
        elif n < len(prestrip):
            leftovers.append(prestrip[n])
            n += 1
        
    result = ''.join(leftovers)
    print(result)


# In[19]:


remove_vowels('bird')


# # normalize name

# In[49]:


def normalize_name(unnormal):
    step1 = unnormal.strip().lower()
    step2 = step1.replace(" ","_")
    final = step2.isidentifier()
   # remove non-valid python identifiers
   # DONE remove whitespace at front and back
   # DONE lowercase
   # DONE spaces to underscores
    if final == True:
        print(step2)
    else:
        print('Nope')
    
normalize_name('Fred Douglas')


# In[50]:


normalize_name('Fred Douglas')


# # cumulative sum

# In[35]:


def cumulative_sum(to_sum):
    print(to_sum)
    rising_numbers = []
    for x in to_sum:
        if x == 1:
            rising_numbers.append(to_sum[x-1])
        else:
            rising_numbers.append(rising_numbers[x-2] + to_sum[x-1])
    print(rising_numbers)


# In[37]:


cumulative_sum([1,2,3,4])


# In[ ]:




