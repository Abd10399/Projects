-- Include your create table DDL statements in this file.
-- Make sure to terminate each statement with a semicolon (;)

-- LEAVE this statement on. It is required to connect to your database.
-- CONNECT TO cs421;

-- Remember to put the create table ddls for the tables with foreign key references
--    ONLY AFTER the parent tables has already been created.

-- This is only an example of how you add create table ddls to this file.
--   You may remove it.

CREATE TABLE Participants
(
	Oid CHAR(9) NOT NULL,
	DOB DATE,
	Pname VARCHAR(99),
	PRIMARY KEY (Oid)
);

CREATE TABLE Referees
(
	Oid CHAR(9) NOT NULL,
	Experience FLOAT,
	Country VARCHAR(56),
	PRIMARY KEY (Oid),
	FOREIGN KEY (Oid) REFERENCES Participants(Oid)

);

CREATE TABLE Teams 
(
  	Country VARCHAR(56) NOT NULL,
  	URL VARCHAR(255),
  	InGroup CHAR(7),
  	Association VARCHAR(255),
	PRIMARY KEY (Country)
);

CREATE TABLE Players 
(
  	Oid CHAR(9) NOT NULL,
 	KitNumber INTEGER CHECK(KitNumber > 0 AND KitNumber < 100),
  	TotalGoals INTEGER,
  	GenPosition VARCHAR(10),
  	Country VARCHAR(56) NOT NULL,
	FOREIGN KEY (Country) REFERENCES Teams(Country),
	PRIMARY KEY (Oid),
	FOREIGN KEY (Oid) REFERENCES Participants(Oid)
);

CREATE TABLE Coaches
(
	Oid CHAR(9) NOT NULL,
	Role VARCHAR(50),
	Country VARCHAR(56) NOT NULL,
	FOREIGN KEY (Country) REFERENCES Teams(Country),
	PRIMARY KEY (Oid),
	FOREIGN KEY (Oid) REFERENCES Participants(Oid)
);

CREATE TABLE Stadiums
(
	Sname VARCHAR(255) NOT NULL,
	Location VARCHAR(255),
	Capacity INTEGER,
	PRIMARY KEY (Sname)
);

CREATE TABLE Matches
(
	Mid CHAR(9) NOT NULL,
	InRound VARCHAR(10), 
	Mtime CHAR(7),
	Mdate DATE,
	Mlength INTEGER,
	Sname VARCHAR(99) NOT NULL,
	Country1 VARCHAR(56) NOT NULL,
	Country2 VARCHAR(56) NOT NULL,
	IsCompleted BOOLEAN NOT NULL,
	PRIMARY KEY (Mid),
	FOREIGN KEY (Sname) REFERENCES Stadiums(Sname),
	FOREIGN KEY (Country1) REFERENCES Teams(Country),
	FOREIGN KEY (Country2) REFERENCES Teams(Country)
);

CREATE TABLE Officiates
(
	Oid CHAR(9) NOT NULL,
	Mid CHAR(9) NOT NULL,
	Role VARCHAR(50),
	PRIMARY KEY (Oid, Mid),
	FOREIGN KEY (Oid) REFERENCES Participants(Oid),
	FOREIGN KEY (Mid) REFERENCES Matches(Mid)
);


CREATE TABLE Stats
(
	Oid CHAR(9) NOT NULL,
	Mid CHAR(9) NOT NULL,
	InTime CHAR(7),
	OutTime CHAR(7),
	PosInGame VARCHAR(50),
	RedCard INTEGER,
	YellowCards INTEGER,
	PRIMARY KEY (Oid, Mid),
	FOREIGN KEY (Oid) REFERENCES Participants(Oid),
	FOREIGN KEY (Mid) REFERENCES Matches(Mid)
);


CREATE TABLE Goals
(
	Mid CHAR(9) NOT NULL,
	GoalOccurrence INTEGER NOT NULL,
	Oid CHAR(9) NOT NULL,
	Country VARCHAR(56),
	PlayerName VARCHAR(99),
	IsPenalty BOOLEAN,
	Time CHAR(7),
	PRIMARY KEY (Mid, GoalOccurrence),
	FOREIGN KEY (Mid) REFERENCES Matches(Mid),
	FOREIGN KEY (Oid) REFERENCES Players(Oid),
	FOREIGN KEY (Country) REFERENCES Teams(Country)
);

CREATE TABLE Customers
(
	Cid CHAR(9) NOT NULL,
	Cname VARCHAR(99),
	BillAddress VARCHAR(255),
	PaymentInfo VARCHAR(255),
	PRIMARY KEY (Cid)
);

CREATE TABLE Tickets
(
	Cid CHAR(9) NOT NULL,
	Tnumber CHAR(6) NOT NULL,
	Price FLOAT,
	PRIMARY KEY (Cid, Tnumber),
	FOREIGN KEY (Cid) REFERENCES Customers(Cid)
);

CREATE TABLE TicketForMatch
(
        Mid CHAR(9) NOT NULL,
        Tnumber CHAR(6) NOT NULL,
	Cid CHAR(9) NOT NULL,
        PRIMARY KEY (Cid, Tnumber, Mid),
        FOREIGN KEY (Mid) REFERENCES Matches(Mid),
        FOREIGN KEY (Cid, Tnumber) REFERENCES Tickets(Cid, Tnumber),
	FOREIGN KEY (Cid) REFERENCES Customers(Cid)
);

CREATE TABLE Seats
(
	Sname VARCHAR(255) NOT NULL,
	Snumber INTEGER NOT NULL,
	Tier VARCHAR(10),
	PRIMARY KEY (Sname, Snumber),
	FOREIGN KEY (Sname) REFERENCES Stadiums(Sname)
);

CREATE TABLE SeatOfTicket
(
        Cid CHAR(9) NOT NULL,
        Tnumber CHAR(6) NOT NULL,
        Sname VARCHAR(255) NOT NULL,
        Snumber INTEGER NOT NULL,
        PRIMARY KEY (Cid, Tnumber, Sname, Snumber),
        FOREIGN KEY (Cid) REFERENCES Customers(Cid),
        FOREIGN KEY (Cid, Tnumber) REFERENCES Tickets(Cid, Tnumber),
        FOREIGN KEY (Sname, Snumber) REFERENCES Seats(Sname, Snumber)
);







