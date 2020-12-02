# surfs_up
Analyzing weather data with Python, SQLite, and Flask.

## Resources 
- Python 3.7.6, JupyterLab 2.26, VS Code 1.51.1
- [SQLAlchemy ORM 1.3.19](https://docs.sqlalchemy.org/en/13/orm/), Python Database Abstraction Library.
- hawaii.sqlite: database file where temperature data is stored.

## Overview
The purpose of this project is to analyze weather data  for a stakeholder interested in investing in a surfing business located in Hawaii.
This data has been collected by a Weather Observing System and stored in a flat database file(.db/.sqlite).

To ensure business is sustainable, year-round weather trends need to be analyzed. 

In order to gain an understanding of Hawaii's weather the stakeholder has expressed explicit interest in weather statistics for the months of June and December throughout recent years. 

## Results 
To access the observation data and analyze it, I have utilized SQLAlchemy ORM, which allows me to query the data by passing python objects as queries. 
The data is then transformed within a python environment and analyzed resulting in the below summary statistics.

 <b>June Temperature Summary Statistics</b>  <br>
![june_temp](https://github.com/DonnieData/surfs_up/blob/main/Reosurce/june_frame.png)

 <b>December Temperature Summary Statistics</b> <br>
![december_temp](https://github.com/DonnieData/surfs_up/blob/main/Reosurce/december_frame.png)

Based on the statistical overview of the data we see that: 
- There is a higher max temperature for the month of June than December. However with only a difference of 2 degrees. 
- June also has a leading average temperature by less than 3 degrees.  
- June also has a higher minimum temperature by 8 degrees. 



## Summary 


<b>June Temperature Observations by group</b><br>
![june_spread](https://github.com/DonnieData/surfs_up/blob/main/Reosurce/june_temp_spread.png)

<b>December Temperature Observations by group</b><br>
![december spread](https://github.com/DonnieData/surfs_up/blob/main/Reosurce/december_temp_spread.png)

Through querying and analyzing the spread of weather for this data, it is safe to say that while December is colder it is still possible to run a business focussed on outdoor activities in Hawaii even in colder months.  
