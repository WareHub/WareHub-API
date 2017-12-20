
CREATE DATABASE WareHubDB
go
USE WareHubDB

CREATE TABLE USERS(ID INTEGER check(ID between 10000000 and 99999999),PASS varchar(100) not null,PRIMARY KEY (ID))
CREATE TABLE STUDENT( ID INTEGER check(ID between 10000000 and 99999999),NAME varchar(20) not null,PHONE bigint,TA BIT not null,POINTS INTEGER not null,PRIMARY KEY (ID),FOREIGN KEY (ID) REFERENCES USERS ON DELETE CASCADE ON UPDATE CASCADE)
CREATE TABLE MANAGER(ID INTEGER check(ID between 10000000 and 99999999),NAME varchar(20) not null, PHONE bigint, PRIMARY KEY (ID),FOREIGN KEY (ID) REFERENCES USERS ON DELETE CASCADE ON UPDATE CASCADE)
CREATE TABLE TECHNICIAN( ID INTEGER check(ID between 10000000 and 99999999),NAME varchar(20) not null,PHONE bigint,POINTS INTEGER,PRIMARY KEY (ID),FOREIGN KEY (ID) REFERENCES USERS ON DELETE CASCADE ON UPDATE CASCADE)
	
CREATE TABLE DEVICE( ID INTEGER check(ID between 10000000 and 99999999),DTYPE varchar(50),LOCATION INTEGER not null,STAT INTEGER check(STAT between 0 and 2) not null,OVERALL_REVIEW INTEGER not null,NUM_REVIEWS INTEGER not null, TECH_ID INTEGER check(TECH_ID between 10000000 and 99999999) DEFAULT 10000000,PRIMARY KEY (ID),FOREIGN KEY (TECH_ID) REFERENCES TECHNICIAN ON DELETE SET DEFAULT)

CREATE TABLE IC_TYPE( CODE varchar(6) ,LINK varchar(100),PRIMARY KEY (CODE))
CREATE TABLE ICS(ID INTEGER check(ID between 10000000 and 99999999),CODE varchar(6), PRIMARY KEY (ID),FOREIGN KEY (ID) REFERENCES DEVICE ON DELETE CASCADE ON UPDATE CASCADE,FOREIGN KEY (CODE) REFERENCES IC_TYPE ON DELETE CASCADE ON UPDATE CASCADE)

CREATE TABLE OS(ID INTEGER CHECK (ID between 1 and 10),NAME varchar(10) not null,LINK varchar(100),PRIMARY KEY (ID))
CREATE TABLE SOFTWARE(ID INTEGER CHECK (ID between 1 and 9999),NAME varchar(50) not null, LINK varchar(100) ,PRIMARY KEY (ID))
CREATE TABLE PCS(ID INTEGER check(ID between 10000000 and 99999999),GPU varchar(50),CPU varchar(50) not null,RAM varchar(50), PRIMARY KEY(ID),FOREIGN KEY (ID) REFERENCES DEVICE ON DELETE CASCADE ON UPDATE CASCADE)
CREATE TABLE HAS_OS(PC_ID INTEGER check(pc_ID between 10000000 and 99999999), OS_ID INTEGER CHECK (os_ID between 1 and 10), PRIMARY KEY(PC_ID,OS_ID),FOREIGN KEY (PC_ID) REFERENCES PCS ON DELETE CASCADE ON UPDATE CASCADE, FOREIGN  KEY (OS_ID) REFERENCES OS ON DELETE CASCADE ON UPDATE CASCADE)

CREATE TABLE HAS_SOFTWARE(PC_ID INTEGER check(pc_ID between 10000000 and 99999999) , SOFTWARE_ID INTEGER  CHECK (software_ID between 1 and 9999), PRIMARY KEY(PC_ID,SOFTWARE_ID),FOREIGN KEY (PC_ID) REFERENCES PCS ON DELETE CASCADE ON UPDATE CASCADE, FOREIGN  KEY (SOFTWARE_ID) REFERENCES SOFTWARE ON DELETE CASCADE ON UPDATE CASCADE)

CREATE TABLE REVIEW (STUDENT_ID INTEGER check(student_ID between 10000000 and 99999999) ,DEVICE_ID INTEGER check(DEVICE_ID between 10000000 and 99999999),R_TIME DATETIME ,OPININON varchar(200) , RATE INTEGER check(RATE between 0 and 5) ,PRIMARY KEY(STUDENT_ID,DEVICE_ID,R_TIME),FOREIGN KEY (STUDENT_ID) REFERENCES STUDENT ON DELETE CASCADE,FOREIGN KEY (DEVICE_ID) REFERENCES DEVICE ON DELETE CASCADE)


CREATE TABLE DEMAND (STUDENT_ID INTEGER check(student_ID between 10000000 and 99999999),DEVICE_ID INTEGER check(DEVICE_ID between 10000000 and 99999999), START_TIME DATETIME ,END_TIME DATETIME ,RESERVED BIT, INUSE integer, PRIMARY KEY(STUDENT_ID,DEVICE_ID,START_TIME),FOREIGN KEY (STUDENT_ID) REFERENCES STUDENT ON DELETE CASCADE,FOREIGN KEY (DEVICE_ID) REFERENCES DEVICE ON DELETE CASCADE)
