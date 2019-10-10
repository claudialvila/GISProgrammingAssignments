# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 11:15:06 2019

@author: Claudia Vila

In the first script, Make a class called Account. 
Create two attributes called first_name and last_name. 
Then create several other attributes that are typically stored in a user account profile. (You can determine what kind of account it is.)
Make a method called summary() that prints a summary of the account and user's information.
Make another method called greeting() that prints a personalized greeting to the user.
Create several instances representing different users and call both methods for each user.

"""

class Account:
    def __init__(self, first_name, last_name, fav_food, hp_house, zodiac, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.fav_food = fav_food
        self.hp_house = hp_house
        self.zodiac = zodiac
        self.login_attempts = 0
    
    def summary(self):
        return "Summary for " + self.first_name + " " + self.last_name + ": " + self.first_name + " is a " + self.fav_food + "-loving " + self.hp_house + "/" + self.zodiac + "." 

    def greeting(self):
        return "Howdy, " + self.first_name + " " + self.last_name + "!"
    
    def increment_login_attempts(self): 
        self.login_attempts = self.login_attempts + 1

    def reset_login_attempts(self):
        self.login_attempts = 0 
    
User1 = Account('Hansel', 'Anderson', 'French Fries', 'Ravenclaw', 'Capricorn', 1)
User2 = Account('Anna', 'Garcia', 'Chana Masala', 'Hufflepuff', 'Leo', 1)
User3 = Account('Miki', 'Pierrot', 'Avocado Toast', 'Hufflepuff', 'Virgo', 1)    
