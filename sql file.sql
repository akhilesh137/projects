
# drop the schema first if any schema named as assignment
drop schema if exists assignment;
#create new schema names assignment
create schema assignment;
# using the schema assignment
use assignment;

drop table if exists bajaj_auto;
# creating a new table named bajaj_auto
create table bajaj_auto (
	Date  text not null,
 	Open_Price double not null,
	High_Price double not null,
	Low_Price	double not null,
    Close_Price	double not null,
    WAP	double not null,
    No_of_Shares double not null,
    No_of_Trades double not null,
	Total_Turnover double not null,
	Deliverable_Quantity VARCHAR(255) not null,	
    percent_Delivered_Qty_to_Traded_Qty VARCHAR(255) not null,
	Spread_High_Low	double not null,
    Spread_Close_Open double  not null
);
#loading csv data into table bajaj_auto
    load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Bajaj Auto.csv' INTO TABLE bajaj_auto  
  FIELDS TERMINATED BY "," enclosed by ' ' escaped by ''''  LINES TERMINATED BY '\r\n' ignore 1 rows ;
  
   select *from bajaj_auto;
   #shows the content of the table bajaj_auto
-- -------------------------------------------------------------------------

drop table if exists eicher_motors;
# creating a  second new table named eicher_motors
create table eicher_motors (
	Date  text not null,
 	Open_Price double not null,
	High_Price double not null,
	Low_Price	double not null,
    Close_Price	double not null,
    WAP	double not null,
    No_of_Shares double not null,
    No_of_Trades double not null,
	Total_Turnover double not null,
	Deliverable_Quantity VARCHAR(255) not null,	
    percent_Delivered_Qty_to_Traded_Qty VARCHAR(255) not null,
	Spread_High_Low	double not null,
    Spread_Close_Open double  not null
);
#loading csv data into table eicher_motors
    load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Eicher Motors.csv' INTO TABLE eicher_motors  
  FIELDS TERMINATED BY "," enclosed by ' ' escaped by ''''  LINES TERMINATED BY '\r\n' ignore 1 rows ;
  
  select * from eicher_motors;
  #the above statement shows the content of the eicher_motors table
-- ---------------------------------------------------------------------------------------
drop table if exists hero_motocorp;
# creating a third new table hero_motocorp
create table hero_motocorp (
	Date  text not null,
 	Open_Price double not null,
	High_Price double not null,
	Low_Price	double not null,
    Close_Price	double not null,
    WAP	double not null,
    No_of_Shares double not null,
    No_of_Trades double not null,
	Total_Turnover double not null,
	Deliverable_Quantity VARCHAR(255) not null,	
    percent_Delivered_Qty_to_Traded_Qty VARCHAR(255) not null,
	Spread_High_Low	double not null,
    Spread_Close_Open double  not null
);
#loading csv data into table hero_motocorp
    load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Hero Motocorp.csv' INTO TABLE  hero_motocorp
  FIELDS TERMINATED BY "," enclosed by ' ' escaped by ''''  LINES TERMINATED BY '\r\n' ignore 1 rows ;

select * from hero_motocorp;
#the above statement shows the content of the table hero_motocorp;
-- ---------------------------------------------------------------------------------------------

drop table if exists infosys;
# creating  the fourth new table named infosys
create table infosys(
	Date  text not null,
 	Open_Price double not null,
	High_Price double not null,
	Low_Price	double not null,
    Close_Price	double not null,
    WAP	double not null,
    No_of_Shares double not null,
    No_of_Trades double not null,
	Total_Turnover double not null,
	Deliverable_Quantity VARCHAR(255) not null,	
    percent_Delivered_Qty_to_Traded_Qty VARCHAR(255) not null,
	Spread_High_Low	double not null,
    Spread_Close_Open double  not null
);
#loading csv data into table infosys
    load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Infosys.csv' INTO TABLE infosys  
  FIELDS TERMINATED BY "," enclosed by ' ' escaped by ''''  LINES TERMINATED BY '\r\n' ignore 1 rows ;
select * from infosys;
#the above statement shows the content of the table infosys
-- ------------------------------------------------------------------------------------------
drop table if exists tcs;
# creating the fifth new table named tcs
create table tcs(
	Date  text not null,
 	Open_Price double not null,
	High_Price double not null,
	Low_Price	double not null,
    Close_Price	double not null,
    WAP	double not null,
    No_of_Shares double not null,
    No_of_Trades double not null,
	Total_Turnover double not null,
	Deliverable_Quantity VARCHAR(255) not null,	
    percent_Delivered_Qty_to_Traded_Qty VARCHAR(255) not null,
	Spread_High_Low	double not null,
    Spread_Close_Open double  not null
);
#loading csv data into table tcs
    load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/TCS.csv' INTO TABLE tcs  
  FIELDS TERMINATED BY "," enclosed by ' ' escaped by ''''  LINES TERMINATED BY '\r\n' ignore 1 rows ;
select * from tcs;
#the above statement shows the content of the table tcs

-- -------------------------------------------------------------------------------------------

drop table if exists tvs_motors;
# creating the last  new table named tvs_motors
create table tvs_motors(
	Date  text not null,
 	Open_Price double not null,
	High_Price double not null,
	Low_Price	double not null,
    Close_Price	double not null,
    WAP	double not null,
    No_of_Shares double not null,
    No_of_Trades double not null,
	Total_Turnover double not null,
	Deliverable_Quantity VARCHAR(255) not null,	
    percent_Delivered_Qty_to_Traded_Qty VARCHAR(255) not null,
	Spread_High_Low	double not null,
    Spread_Close_Open double  not null
);
#loading csv data into table tvs_motors
    load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/TVS Motors.csv' INTO TABLE tvs_motors  
  FIELDS TERMINATED BY "," enclosed by ' ' escaped by ''''  LINES TERMINATED BY '\r\n' ignore 1 rows ;

select * from tvs_motors;
#the above statememt shows the content of the table tvs_motors
-- ---------------------------------------------------------------------------------------------------
show tables;
 #shows the tables in assignment schema


#------------------- question 1------------------------------------------------------------------

#Create a new table named 'bajaj1' containing the date, close price, 20 Day MA and 50 Day MA.

drop table if exists bajaj1;
# the above statememt drops the table if it is already exists
#now creating a new table which contains date ,close price ,20_day_MA and 50_day_MA as its columns
CREATE TABLE bajaj1
  AS 
  (SELECT date,close_price,
  AVG(close_price) OVER (ORDER BY date ASC ROWS 19 PRECEDING) AS 20_day_MA,
  AVG(close_price) OVER (ORDER BY date ASC ROWS 49 PRECEDING) AS 50_day_MA
  FROM bajaj_auto);
 select * from bajaj1;
 
 #***** for table eicher_motors
 #Create a new table named 'eicher_motors1' containing the date, close price, 20 Day MA and 50 Day MA.

drop table if exists eicher_motors1;
# the above statememt drops the table if it is already exists
#now creating a new table which contains date ,close price ,20_day_MA and 50_day_MA as its columns
CREATE TABLE eicher_motors1
  AS 
  (SELECT date,close_price,
  AVG(close_price) OVER (ORDER BY date ASC ROWS 19 PRECEDING) AS 20_day_MA,
  AVG(close_price) OVER (ORDER BY date ASC ROWS 49 PRECEDING) AS 50_day_MA
  FROM eicher_motors);
  
 select * from eicher_motors1;

#********for table hero_motocorp
#Create a new table named 'hero_motocorp1' containing the date, close price, 20 Day MA and 50 Day MA.
drop table if exists hero_motocorp1;
# the above statememt drops the table if it is already exists
#now creating a new table which contains date ,close price ,20_day_MA and 50_day_MA as its columns
CREATE TABLE hero_motocorp1
  AS 
  (SELECT date,close_price,
  AVG(close_price) OVER (ORDER BY date ASC ROWS 19 PRECEDING) AS 20_day_MA,
  AVG(close_price) OVER (ORDER BY date ASC ROWS 49 PRECEDING) AS 50_day_MA
  FROM hero_motocorp);
  select * from hero_motocorp1;
  
  #*********** for table infosys
#Create a new table named 'infosys1' containing the date, close price, 20 Day MA and 50 Day MA.
drop table if exists infosys1;
# the above statememt drops the table if it is already exists
#now creating a new table which contains date ,close price ,20_day_MA and 50_day_MA as its columns
CREATE TABLE infosys1
  AS 
  (SELECT date,close_price,
  AVG(close_price) OVER (ORDER BY date ASC ROWS 19 PRECEDING) AS 20_day_MA,
  AVG(close_price) OVER (ORDER BY date ASC ROWS 49 PRECEDING) AS 50_day_MA
  FROM infosys);
 select * from infosys1;
 
 #**********for table tcs
 #Create a new table named 'tcs1' containing the date, close price, 20 Day MA and 50 Day MA.
drop table if exists tcs1;
# the above statememt drops the table if it is already exists
#now creating a new table which contains date ,close price ,20_day_MA and 50_day_MA as its columns
CREATE TABLE tcs1
  AS 
  (SELECT date,close_price,
  AVG(close_price) OVER (ORDER BY date ASC ROWS 19 PRECEDING) AS 20_day_MA,
  AVG(close_price) OVER (ORDER BY date ASC ROWS 49 PRECEDING) AS 50_day_MA
  FROM tcs);
 select * from tcs1;
 
 #**********for table tvs_motors
 #Create a new table named 'tvs_motors1' containing the date, close price, 20 Day MA and 50 Day MA.
 drop table if exists tvs_motors1;
# the above statememt drops the table if it is already exists
 #now creating a new table which contains date ,close price ,20_day_MA and 50_day_MA as its columns
 CREATE TABLE tvs_motors1
  AS 
  (SELECT date,close_price,
  AVG(close_price) OVER (ORDER BY date ASC ROWS 19 PRECEDING) AS 20_day_MA,
  AVG(close_price) OVER (ORDER BY date ASC ROWS 49 PRECEDING) AS 50_day_MA
  FROM tvs_motors);
 select * from tvs_motors1;
#------------------question 2-------------------------------------------------------------

# creating a master table containing the data and close price of all six stocks

use assignment;
# now creating a master table 
create table master_table as
select b.date, b.close_price as bajaj,
 e.close_price as eicher ,
 h.close_price as hero,
 i.close_price as infosys,
 t.close_price as tcs,
 m.close_price as tvs from bajaj_auto b
 inner join eicher_motors e
on b.date = e.date inner join hero_motocorp h 
on e.date = h.date inner join infosys i
on h.date =i.date inner join tcs t
on i.date =t.date inner join tvs_motors m
on t.date=m.date ;

# it shows the table  containing column header for the price as the name of the stock 
select * from master_table;
#--------------------------question 3-------------------------------------------------------------------------------------------------------------------------

# Using  the table created in Part(1) to generate buy and sell signal. 
 # Store this in another table named 'bajaj2'.
 
 drop  table if exists bajaj2;
 # the above statememt drops the table if it is already exists
  #now creating a new table which contains date ,close price and signal as its columns by comparing the 20_day_MA and 50_day_MA
 CREATE TABLE bajaj2
 AS
 (SELECT date,close_price,
 CASE 
	WHEN 20_day_MA>50_DAY_MA THEN 'Buy'
    WHEN 20_day_MA<50_day_MA THEN 'Sell'
    WHEN 20_day_MA = 50_day_MA THEN 'Hold'
END as _Signal
FROM bajaj1 ORDER BY date);

select * from bajaj2;

#******for table eicher_motors
 # Using the table created in Part(1) to generate buy and sell signal. 
 # Store this in another table named 'eicher_motors2'.
 
  drop table if exists eicher_motors2;
  # the above statememt drops the table if it is already exists
   #now creating a new table which contains date ,close price and signal as its columns by comparing the 20_day_MA and 50_day_MA
 CREATE TABLE eicher_motors2
 AS
 (SELECT date,close_price,
 CASE 
	WHEN 20_day_MA>50_DAY_MA THEN 'Buy'
    WHEN 20_day_MA<50_day_MA THEN 'Sell'
    WHEN 20_day_MA = 50_day_MA THEN 'Hold'
END as _Signal
FROM eicher_motors1 ORDER BY date);

select * from eicher_motors2;

#*******for table hero_motocorp
# Use the table created in Part(1) to generate buy and sell signal. 
 # Store this in another table named 'hero_motocorp2'.
  drop table if exists hero_motocorp2;
  # the above statememt drops the table if it is already exists
   #now creating a new table which contains date ,close price and signal as its columns by comparing the 20_day_MA and 50_day_MA
 CREATE TABLE hero_motocorp2
 AS
 (SELECT date,close_price,
 CASE 
	WHEN 20_day_MA>50_DAY_MA THEN 'Buy'
    WHEN 20_day_MA<50_day_MA THEN 'Sell'
    WHEN 20_day_MA = 50_day_MA THEN 'Hold'
END as _Signal
FROM hero_motocorp1 ORDER BY date);

select * from hero_motocorp2;

#**** for table infosys
 # Using the table created in Part(1) to generate buy and sell signal. 
 # Store this in another table named 'infosys2'.
  drop table if exists infosys2;
  # the above statememt drops the table if it is already exists
   #now creating a new table which contains date ,close price and signal as its columns by comparing the 20_day_MA and 50_day_MA
 CREATE TABLE infosys2
 AS
 (SELECT date,close_price,
 CASE 
	WHEN 20_day_MA>50_DAY_MA THEN 'Buy'
    WHEN 20_day_MA<50_day_MA THEN 'Sell'
    WHEN 20_day_MA = 50_day_MA THEN 'Hold'
END as _Signal
FROM infosys1 ORDER BY date);

select * from infosys2;

#*******for table tcs
 # Use the table created in Part(1) to generate buy and sell signal. 
 # Store this in another table named 'tcs2'.
  drop table if exists tcs2;
  # the above statememt drops the table if it is already exists
 #now creating a new table which contains date ,close price and signal as its columns by comparing the 20_day_MA and 50_day_MA
 CREATE TABLE tcs2
 AS
 (SELECT date,close_price,
 CASE 
	WHEN 20_day_MA>50_DAY_MA THEN 'Buy'
    WHEN 20_day_MA<50_day_MA THEN 'Sell'
    WHEN 20_day_MA = 50_day_MA THEN 'Hold'
END as _Signal
FROM tcs1 ORDER BY date);

select * from tcs2;

#********* for table tvs_motors
 # Use the table created in Part(1) to generate buy and sell signal. 
 # Store this in another table named 'tvs_motors2'.
 drop table if exists tvs_motors2;
 # the above statememt drops the table if it is already exists
 #now creating a new table which contains date ,close price and signal as its columns by comparing the 20_day_MA and 50_day_MA
 CREATE TABLE tvs_motors2
 AS
 (SELECT date,close_price,
 CASE 
	WHEN 20_day_MA>50_DAY_MA THEN 'Buy'
    WHEN 20_day_MA<50_day_MA THEN 'Sell'
    WHEN 20_day_MA = 50_day_MA THEN 'Hold'
END as _Signal
FROM tvs_motors1 ORDER BY date);

select * from tvs_motors2;

#--------------------------question 4 ------------------------------------------------------------------------------------------------------------------

# Create a User defined function and taking date as input
# and the function returns the signal for that particular day (Buy/Sell/Hold) for the Bajaj stock
drop function if exists bajaj_stock ;
# the above statememt drops the function if it is already exists
DELIMITER $$
# we are creating a new function named bajaj_stock as it will take date as input and returns the signal 
CREATE FUNCTION  bajaj_stock(a text) returns varchar(4)
DETERMINISTIC
BEGIN
DECLARE b varchar(4);
select  _signal into b from bajaj2 where date=a;
return (b);
end;

select bajaj_stock('10-december-2015');
 #it will returns the signal for the particular date
