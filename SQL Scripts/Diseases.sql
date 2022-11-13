
SHOW DATABASES;

USE DIS;

/*
Creating a DB table for diseases
*/

CREATE TABLE Diseases (
    SLNO INT PRIMARY KEY,
    Disease_Name VARCHAR(500),
    URL VARCHAR(500),
    Symptoms TEXT,
    Cause_Of_Disease TEXT,
    Risk_Factors TEXT,
    Overview TEXT,
    Treatment TEXT,
    Medication TEXT,
    Home_Remedies TEXT
);


/*
imported CSV file from 
D:\MS in US\MS in US - Applications Documents\MS Applications - post submission\Northeastern University\1st Sem
 - courses\Data Management and Database Design\Assignment 2\Twitter Scraping\Diseases dataset\dataset
to my diseases db table by right clicking on diseases table on the right panel under 'schemas' and choosing import
*/

Select * from Diseases;



