# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.
import statistics

def main():
    rainfall =[]
    rainfall_total = 0.0
    for r in range(12):

        rain =  (float(input('how many inches of rainfall for the month:')))
        rainfall.append(rain)


    avg_rainfall = (sum(rainfall)/12)

    print('Total inches of rainfall for the year: ',rainfall_total)
    print('Average rainfall per month: ',avg_rainfall)
    print('The highest rainfall was ', max(rainfall))
    print('The lowest rainfall was ', min(rainfall))

main()
