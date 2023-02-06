# Australia, Sponsored Visas and Income by economic activity

To know what is the perfect eceonomic activity to apply for a job, I wanted to know how many visas were sponsored for each sector and also how much money do they make. So I have a picture of the situation that I might be facing in the future. I will go through all the steps I followed in this analysis. But if you want to know more about the process and the conclusions, you can check the folder called "notebooks" within this same repo. 

### *Step 1 - Find the perfect website. *
And I found it. The Australian Bureau of Statistics. It contains all the information I need, but the way to get may be different. But it is not a problem for us Ironhackers!
 
### *Step 2 - Download the data. *
On one hand, I just downloaded an excel file from the site that contained the median of income for year and activity. On the other hand, I requested an excel file through an API to the same site, to get the number of visas sponsored for each year and activity. It was confusing at the beginning, but they have specific documentation as a guide to perform an API request. Introducing the required arguments and parameters I managed to extract the data I wanted.
 
### *Step 3 - Clean the excel files. *
Both had titles and blank rows, a weird format basically. I wanted both to have a similar format, so I can merge them once I have finished the cleaning part. So, I got rid of blanks, and I stack the data frames to have the information in the way I wanted to.
 
### *Step 4 - Merge. *
Left join on the table containing the visa's information, since I have more years of data, I wanted to keep as much as possible. To do so, I already prepared the tables in my cleaning part, so my data frames have the same column names for the year and the economic activity, as well as the same format for the values in them. This way I managed to merge both table using two columns, and I have accurate data for year and activity. 
 
### *Step 5 - Visualization*
This is the part that gives us the fancy graphs and the conclusions as well. I created different plots to visualise the information I got in a way that was useful and meaningful, we will go through all of them, analysing and extracting conclusions
