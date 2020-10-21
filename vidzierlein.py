import time
from selenium import webdriver

''' #Accept input from user
number = int(input("Enter a number: "))

def factorial_without_recursion(number):
    fact = 1
    while(number > 0):
        fact = fact * number
        number = number - 1
    print('Factorial of', number,'is: '+ str(fact))
    return(fact)

# Create an instance of Firefox WebDriver
driver = webdriver.Firefox() '''

#Accept input from user
HeightInMeters = (int(input("Enter your height in cm: "))) / 100
print(HeightInMeters)
''' height = float(input("Input your height in meters: "))
weight = float(input("Input your weight in kilogram: "))
bmi = weight/(height*height)
print("Your body mass index is: ", bmi)

if 
while input == 'metric':
    height = float(input('Please enter your height input meters(decimals): '))
    weight = int(input('Please enter your weight input kg: '))
    bmi = weight/(height*height)

    if bmi <= 18.5:
        print('Your BMI is', bmi,'which means you are underweight.')

    elif bmi > 18.5 and bmi < 25:
        print('Your BMI is', bmi,'which means you are normal.')

    elif bmi > 25 and bmi < 30:
        print('your BMI is', bmi,'overweight.')

    elif bmi > 30:
        print('Your BMI is', bmi,'which means you are obese.')

    else:
        print('There is an error with your input')
        print('Please check you have entered whole numbers\n'
              'and decimals were asked.') '''