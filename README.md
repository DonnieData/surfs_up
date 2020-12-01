# surfs_up
Analyzing weather data with Pytohn, SQLite, and Flask.

## Resources 
- Python 3.7.6, JupyterLab 2.26, VS Code 1.51.1
- [SQLAlchemy ORM 1.3.19](https://docs.sqlalchemy.org/en/13/orm/), Python Database Abstraction Library.
- hawaii.sqlite: database file where temperature data is stored.

## Overview
The purspose of this project is to analyze weather data  for a stakeholder interested in investing in a surfing business located in Hawaii.
This data ha been collected by a Weather Observing System and stored in a flat database file(.db/.sqlite).

To ensure business is sustainable, year-round weather trends needs to be analyzed. 

In order to gain an understanding of hawaiis weather the stakeholder has expressed explicit interest in weather statistics for the months of June and December throughout recent years. 

## Results 
To access the observation data and analyze it, I have utilized SQLaclhemy ORM, which allows me to query the data by passing python objects as queries. 
The data is then transformed within a python environment and analyzed resulting in the below summary statistics.

 June Temperature Summary Statistics  <br>
![june_temp](https://github.com/DonnieData/surfs_up/blob/main/Reosurce/june_frame.png)

 December Temperature Summary Statistics  <br>
![december_temp](https://github.com/DonnieData/surfs_up/blob/main/Reosurce/december_frame.png)

### Analysis
Based on the statisical overview of the data we see that: 
- There is a higher max temperature for the month of June than December. However with only a differnece of 2 degrees. 
- June also has a leading average temperature than December by 3 degrees. 
- June also has a higher minimum temperature by a small margin. 

From analyzing the spread of weather for this data, it is safe to say that while December is colder it is still possible to run a business focussed on outdoor activites in Hawaii even in colder months.  


## Summary 

[query: count of temps higher than average for months]

