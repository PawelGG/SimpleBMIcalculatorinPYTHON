# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 13:02:33 2023

@author: PawelGG
"""


# Simple BMI calculator in PYTHON


print("Please type your WEIGHT")
weight = float(input())

print("Please type your HEIGHT")
height = float(input())
    
BMI = float((weight/(height/100)**2))

print(" \n \n \n \n \n \t Your BMI is:", BMI)


if BMI <= 18.4:
    print(" \t \n its below 18.4 - Underweight")      
                
elif BMI <= 24.9:
    print(" \t \n its between 18.5 and 24.9 - Normal")
        
elif BMI <= 39.9:
    print(" \t \n its between 25.0 and 39.9 - Overweight")
            
elif BMI >= 40:
    print(" \t \n its more that 40 - Obese")
    
else:
    print()
    
print("\n \n ______ Thank You for using!")

                
            