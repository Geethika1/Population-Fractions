#Name: Geethika Sasikumar
#Date: October 18, 2017
#This program asks the user for the borough, names the file out put and displays
# the fraction of the population that has lived in that borough over time

#Libraries for plotting and data processing:
import matplotlib.pyplot as plt
import pandas as pd

borough = input("Enter borough name: ")

Outputfile = input("Enter output file name: ") 

#Open the CSV file and store in pop
pop = pd.read_csv('nycHistPop.csv',skiprows=5)

#Compute the fraction of the population in the Bronx, and save as new column:
pop['Fraction'] = pop[borough]/pop['Total']

#Create a plot of year versus fraction of pop. in Bronx (with labels):
pop.plot(x = 'Year', y = 'Fraction')

#Save to the file:  fractionBX.png
fig = plt.gcf()
fig.savefig(Outputfile)
