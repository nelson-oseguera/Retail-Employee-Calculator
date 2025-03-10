# Nelson Oseguera
 
# February 25th, 2023

# Project 2

# The program will ask for the monthly sales of a store owned by a company. If the store's monthly sales equal or exceed $100,000 then the company will reward the store with a $5000 bonus. Aditionally, if the store's monthly sales equal or exceed 125% of their monthly goal of $90,000, then all employees will receive a message stating that they will get a day off.

print('welcome to the program')

monthlySales=float(input('Enter the monthly sales $'))

if monthlySales >= 100000:
                   print('You have earned a $5000 bonus!!!')

                   
if monthlySales >= 112500:
                   print('All employees get a day off!!!')
