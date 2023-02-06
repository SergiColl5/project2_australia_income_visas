# I import all the libraries in the same place.

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# I import the excel file that I prepared in previous steps, all the code is within other files.

all_together = pd.read_excel('../data/all_together.xlsx')


def line_income_years():
    # Group the data by year and calculate the mean median income
    mean_median_income_by_year = all_together.groupby('Year')['Median_income'].mean().reset_index()

    # Plot the mean median income over the years
    plt.plot(mean_median_income_by_year['Year'], mean_median_income_by_year['Median_income'])

    # Add labels and title to the plot and save it
    plt.xlabel('Year')
    plt.ylabel('Mean Median Income in USD')
    plt.title('Mean Median Income over the Years')
    plt.savefig('../Plots/line_Income_Years.jpg')
    pass 
line_income_years()

def bar_income_activity ():
    # Group the data by activity and calculate the mean number of sponsored visas
    mean_sponsored_visas_by_activity = all_together.groupby('Activity')['Median_income'].mean().reset_index()

    # Sort the data in descending order based on the mean number of sponsored visas
    mean_sponsored_visas_by_activity = mean_sponsored_visas_by_activity.sort_values(by='Median_income', ascending=False)

    # Plot the mean number of sponsored visas for each activity as a bar plot
    plt.bar(mean_sponsored_visas_by_activity['Activity'], mean_sponsored_visas_by_activity['Median_income'],width=0.9)

    # Add labels and title to the plot
    plt.xlabel('Economic Activity')
    plt.ylabel('Mean Income in USD')
    plt.title('Mean Income by Economic Activity (Sorted)')


    # Rotate the x-axis labels to improve readability
    plt.xticks(rotation=90)

    # Show the plot
    plt.savefig('../Plots/bar_Income_activity.jpg')
    pass
bar_income_activity()


def line_visas_years():
    # Group the data by year and calculate the mean number of sponsored visas
    mean_sponsored_visas_by_year = all_together.groupby('Year')['Sponsored_visas'].mean().reset_index()

    # Plot the mean number of sponsored visas over the years
    plt.plot(mean_sponsored_visas_by_year['Year'], mean_sponsored_visas_by_year['Sponsored_visas'])

    # Add labels and title to the plot
    plt.xlabel('Year')
    plt.ylabel('Mean Sponsored Visas')
    plt.title('Mean Sponsored Visas over the Years')

    # Show the plot
    plt.savefig('../Plots/line_Visas_Years.jpg')
    pass
line_visas_years()


def bar_visas_activity ():

    # Group the data by activity and calculate the mean number of sponsored visas
    mean_sponsored_visas_by_activity = all_together.groupby('Activity')['Sponsored_visas'].mean().reset_index()

    # Sort the data in descending order based on the mean number of sponsored visas
    mean_sponsored_visas_by_activity = mean_sponsored_visas_by_activity.sort_values(by='Sponsored_visas', ascending=False)

    # Plot the mean number of sponsored visas for each activity as a bar plot
    plt.bar(mean_sponsored_visas_by_activity['Activity'], mean_sponsored_visas_by_activity['Sponsored_visas'],)


    # Add labels and title to the plot
    plt.xlabel('Economic Activity')
    plt.ylabel('Mean Sponsored Visas')
    plt.title('Mean Sponsored Visas by Economic Activity (Sorted)')

    # Rotate the x-axis labels to improve readability
    plt.xticks(rotation=90)

    # Show the plot
    plt.savefig('../Plots/bar_Visas_activity.jpg')
    pass
bar_visas_activity()



def scatter_income_activity ():

    mean_median_income_and_sponsored_visas_by_activity = all_together.groupby('Activity').agg({'Median_income': 'mean', 'Sponsored_visas': 'mean'}).reset_index()

    # Create a color map
    cmap = plt.get_cmap('viridis')

    # Plot the relationship between median income and number of sponsored visas as a scatter plot
    plt.scatter(mean_median_income_and_sponsored_visas_by_activity['Median_income'], mean_median_income_and_sponsored_visas_by_activity['Sponsored_visas'], 
                c=mean_median_income_and_sponsored_visas_by_activity.index, cmap=cmap)

    # Add labels and title to the plot
    plt.xlabel('Mean Median Income')
    plt.ylabel('Mean Sponsored Visas')
    plt.title('Relationship between Median Income and Sponsored Visas by Economic Activity')

    plt.savefig('../Plots/scatter_income_activity.jpg')
    pass
scatter_income_activity()


def box_income ():
    boxplot_df = all_together.dropna(subset=['Median_income'])
    plt.boxplot(boxplot_df['Median_income'])
    plt.ylabel('Income in USD')
    plt.title('Distribution of Income')
    plt.savefig('../Plots/box_income.jpg')
    pass
box_income()



def heat_income():
    # Create a pivot table with year, median income, and number of sponsored visas as columns
    pivot_table = all_together.pivot_table(index='Year', columns='Activity', values=['Median_income'])

    # Plot the pivot table as a heatmap
    sns.heatmap(pivot_table)

    # Add labels and title to the plot
    plt.xlabel('Economic Activity')
    plt.ylabel('Year')
    plt.title('Relationship between Year, Median Income')
    plt.savefig('../Plots/heat_Income.jpg')
    pass
heat_income()