# Program #3: US_Population


def main():
    # Have the user input (using a loop) various information that contains three pieces of data: 
    # year, name of state, and population.  
    # Store all of this information in a list of lists.  For example it might be stored like this:

    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]

    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    all_entered_values = []

    for r in range(rows):
        row = []
        for c in range(cols):
            value = (input(f"Enter information: "))
            row.append(value)
        all_entered_values.append(row)

    # Now have the user enter a year. 
    year = int(input('Enter a year: '))
    sum_population_for_year(all_entered_values, year)
    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year
    print(f'The total population in {year} was {sum_population_for_year(all_entered_values, year):,}')

def sum_population_for_year(all_entered_values, year_to_sum):
    population_total = []

    if year_to_sum in all_entered_values:
        add_pop = max(all_entered_values)
        population_total.append(add_pop)

    total_population = sum(population_total)

    return total_population


    # Loop through and sum the populations for the appropriate year. 
    # e.g. for the list on line 7 the total would be 8,860,637 if the user enterd 2010 for the year to sum,
    # or 3,421,988 if they enterd 2011 for the year to sum.

    # print the totalled population


# Call the main function.
if __name__ == '__main__':
    main()