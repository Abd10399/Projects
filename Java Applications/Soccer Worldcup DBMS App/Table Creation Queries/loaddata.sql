-- Include your INSERT SQL statements in this file.
-- Make sure to terminate each statement with a semicolon (;)

-- LEAVE this statement on. It is required to connect to your database.
-- CONNECT TO cs421;

-- Remember to put the INSERT statements for the tables with foreign key references
--    ONLY AFTER the parent tables!

-- This is only an example of how you add INSERT statements to this file.
--   You may remove it.
-- A more complex syntax that saves you typing effort.
INSERT INTO Participants (Oid, DOB, Pname)
VALUES
('P00000001', '1996-02-12', 'Heunga Minga Sona'),
('P00000002', '2000-05-30', 'Cristiana Ronalda'),
('P00000003', '2002-12-10', 'Lionela Messia'),
('P00000004', '1987-01-01', 'Alphonsa Daviesa'),
('P00000005', '1997-01-08', 'Riyada Mahreza'),
('C00000001', '1998-04-17', 'Heunga Minga Sonia'),
('C00000002', '1999-11-23', 'Cristiana Ronaldo'),
('C00000003', '2003-02-12', 'Lionela Messiya'),
('C00000004', '1988-05-08', 'Alphonsa Daviesb'),
('C00000005', '1994-03-21', 'Riyada Mahrezi'),
('R00000001', '1994-08-23', 'Hengha Munga Sona'),
('R00000002', '2001-03-18', 'Christiana Ronaldi'),
('R00000003', '1998-11-05', 'Lionela Messier'),
('R00000004', '1986-06-27', 'Alphonsia Davida'),
('R00000005', '2000-09-11', 'Riyad Mahrezia'),
('R00000006', '1987-02-14', 'Kofi Kodjia'),
('R00000007', '2000-01-01', 'Harry Maguire'),
('P00000006', '1997-01-08', 'benrahma'),
('P00000007', '1997-01-08', 'bennacer'),
('P00000008', '1997-01-08', 'slimani'),
('P00000009', '1997-01-08', 'belaili'),
('P00000010', '1997-01-08', 'chaibi'),
('P00000011', '1997-01-08', 'neymar');

INSERT INTO Referees (Oid, Experience, Country) 
VALUES 
('R00000001', 3, 'Pakistan'),
('R00000002', 2, 'Japan'),
('R00000003', 5, 'Canada'),
('R00000004', 1, 'Palestine'),
('R00000005', 4, 'Algeria'),
('R00000006', 10, 'Algeria'),
('R00000007', 1, 'Algeria');

INSERT INTO Teams (Country, URL, InGroup, Association)
VALUES 
('Brazil', 'https://www.jogabonito.com', 'Group A', 'Brazilian Football Association'),
('Germany', 'https://www.germany.com', 'Group A', 'German Football Association'),
('France', 'https://www.france.com', 'Group A', 'French Football Association'),
('Algeria', 'http://www.algeria.com', 'Group B', 'Algerian Football Association'),
('Palestine', 'http://www.freepalestine.com', 'Group A', 'Palestine Football Association'),
('Pakistan', 'http://www.pakistan.com', 'Group B', 'Pakistani Football Association');


INSERT INTO Players (Oid, KitNumber, TotalGoals, GenPosition, Country)
VALUES 
('P00000001', 10, 2, 'Forward', 'Brazil'),
('P00000002', 5, 3, 'Midfielder', 'Germany'),
('P00000003', 7, 1, 'Defender', 'Palestine'),
('P00000004', 3, 4, 'Goalkeeper', 'France'),
('P00000005', 9, 0, 'Forward', 'Algeria'),
('P00000006', 5, 0, 'Midfielder', 'Algeria'),
('P00000007', 1, 5, 'Defender', 'Algeria'),
('P00000008', 2, 0, 'Forward', 'Algeria'),
('P00000009', 3, 0, 'Forward', 'Algeria'),
('P00000010', 4, 0, 'Forward', 'Algeria'),
('P00000011', 11, 0, 'Forward', 'Brazil');


INSERT INTO Coaches (Oid, Role, Country)
VALUES 
('C00000001', 'Head Coach', 'Palestine'),
('C00000002', 'Goalkeeper Coach', 'Palestine'),
('C00000003', 'Head Coach', 'Algeria'),
('C00000004', 'Assistant Coach', 'Palestine'),
('C00000005', 'Defender Coach', 'Palestine');


INSERT INTO Stadiums (Sname, Location, Capacity)
VALUES
('Al Janoub Stadium', 'Al Wakrah', 40000),
('Education City Stadium', 'Al Rayyan', 45000),
('Khalifa International Stadium', 'Al Rayyan', 40000),
('Lusail Iconic Stadium', 'Lusail', 80000),
('Al Bayt Stadium', 'Al Khor', 60000);


INSERT INTO Matches (Mid, InRound, Mtime, Mdate, Mlength, Sname, Country1, Country2, IsCompleted) 
VALUES
('M00000001', 'Group', '14:00', '2023-03-14', 93, 'Lusail Iconic Stadium', 'Brazil', 'Germany', 1),
('M00000002', 'Quarter', '17:00', '2023-03-16', null, 'Al Bayt Stadium', 'Germany', 'Algeria', 0),
('M00000003', 'Group', '20:00', '2023-03-14', 91, 'Al Janoub Stadium', 'Palestine', 'Brazil', 1),
('M00000008', 'Group', '20:00', '2023-03-13', 95, 'Al Janoub Stadium', 'Algeria', 'Pakistan', 1),
('M00000004', 'Semi', '14:00', '2023-03-17', null, 'Khalifa International Stadium', 'Germany', 'France', 0),
('M00000005', 'Semi', '17:00', '2023-03-17', null, 'Education City Stadium', 'Algeria', 'Palestine', 0),
('M00000006', 'Group', '17:00', '2023-03-13', 93, 'Al Janoub Stadium', 'France', 'Palestine', 1),
('M00000007', 'Final', '17:00', '2023-03-19', null, 'Al Janoub Stadium', 'France', 'Algeria', 0);

INSERT INTO Officiates (Oid, Mid, Role)
VALUES
('R00000001', 'M00000001', 'main'),
('R00000002', 'M00000001', 'linesman'),
('R00000003', 'M00000002', 'main'),
('R00000004', 'M00000003', 'linesman'),
('R00000005', 'M00000001', 'secondary'),
('R00000006', 'M00000007', 'main'),
('R00000007', 'M00000007', 'secondary');

INSERT INTO Stats (Oid, Mid, InTime, OutTime, PosInGame, RedCard, YellowCards)
VALUES
('P00000001', 'M00000001', '66:34', '93:03', 'Forward', 1, 1),
('P00000002', 'M00000001', '00:00', '93:03', 'Midfielder', 0, 0),
('P00000001', 'M00000003', '00:00', '91:00', 'Forward', 1, 0),
('P00000001', 'M00000006', '00:00', null, 'Forward', 0, 0),
('P00000003', 'M00000003', '45:00', '82:11', 'Defender', 1, 1),
('P00000004', 'M00000004', '00:00', null, 'Goalkeeper', 0, 0),
('P00000004', 'M00000006', '00:00','93:00', 'Goalkeeper', 1, 0),
('P00000005', 'M00000005', '00:00', null, 'Forward', 0, 0),
('P00000007', 'M00000008', '00:00', '91:00', 'Midfielder', 1, 0),
('P00000011', 'M00000001', '00:00', '93:03', 'Forward', 0, 1);

INSERT INTO Goals (Mid, GoalOccurrence, Oid, Country, PlayerName, IsPenalty, Time)
VALUES
('M00000001', 1, 'P00000001', 'Brazil', 'Heunga Minga Sona', 0, '74:30'),
('M00000001', 2, 'P00000001', 'Brazil', 'Heunga Minga Sona', 0, '75:00'),
('M00000001', 3, 'P00000002', 'Germany', 'Cristiana Ronalda', 0, '15:00'),
('M00000001', 4, 'P00000002', 'Germany', 'Cristiana Ronalda', 0, '25:00'),
('M00000001', 5, 'P00000002', 'Germany', 'Cristiana Ronalda', 0, '35:00'),
('M00000006', 1, 'P00000004', 'France', 'Alphonsa Daviesa', 0, '24:30'),
('M00000006', 2, 'P00000004', 'France', 'Alphonsa Daviesa', 0, '34:30'),
('M00000006', 3, 'P00000004', 'France', 'Alphonsa Daviesa', 0, '44:30'),
('M00000006', 4, 'P00000004', 'France', 'Alphonsa Daviesa', 0, '54:30'),
('M00000006', 5, 'P00000003', 'Palestine', 'Lionela Messia', 0, '71:30'),
('M00000008', 1, 'P00000007', 'Algeria', 'bennacer', 0, '24:30'),
('M00000008', 2, 'P00000007', 'Algeria', 'bennacer', 0, '34:30'),
('M00000008', 3, 'P00000007', 'Algeria', 'bennacer', 0, '44:30'),
('M00000008', 4, 'P00000007', 'Algeria', 'bennacer', 0, '54:30'),
('M00000008', 5, 'P00000007', 'Algeria', 'bennacer', 0, '71:30');

INSERT INTO Customers (Cid, Cname, BillAddress, PaymentInfo)
VALUES
('fedb3535G', 'LeFavoriteSaying James', '1 road, Springfield, Algeria', 'Credit Card'),
('rw2D3f3fF', 'Um Kung Jim', '1 road, Jerusalem, Palestine', 'PayPal'),
('2249rffwe', 'Poe Jiden', '1 road, Tel Aviv, Palestine', 'Cash'),
('hbkrs3355', 'Trump Donal', '2 road, Washington, Palestine', 'Credit Card'),
('fegreRF65', 'Mr Beast', '4 curry road, Kashmere, Pakistan', 'Venmo'),
('qeiv83fhf', 'Freeze Corleon', '93 Saint Denis, Paris, France', 'Venmo'),
('ywjb43hb5', 'Alpha Wann', '9 Maffe Bissap, Bamako, Mali', 'Venmo');

INSERT INTO Tickets (Cid, Tnumber, Price)
VALUES
('fedb3535G','000001', 250.00),
('rw2D3f3fF','000001', 124.99),
('2249rffwe','000001', 52.99),
('hbkrs3355','000001', 40.00),
('qeiv83fhf','000001', 1200.00),
('ywjb43hb5','000001', 3000.00),
('fegreRF65','000001', 991.99);

INSERT INTO TicketForMatch (Mid, Tnumber, Cid)
VALUES
('M00000001', '000001', 'fedb3535G'),
('M00000002', '000001', 'rw2D3f3fF'),
('M00000003', '000001', '2249rffwe'),
('M00000004', '000001', 'hbkrs3355'),
('M00000005', '000001', 'fegreRF65'),
('M00000007', '000001', 'qeiv83fhf'),
('M00000007', '000001', 'ywjb43hb5');


INSERT INTO Seats (Sname, Snumber, Tier)
VALUES
('Al Janoub Stadium', 1, 'Premium'),
('Al Janoub Stadium', 1000, 'Premium'),
('Education City Stadium', 43000, 'Normal'),
('Khalifa International Stadium', 2304, 'Premium'),
('Lusail Iconic Stadium', 124, 'VIP'),
('Al Janoub Stadium', 290, 'Normal'),
('Al Janoub Stadium', 143, 'Normal');

INSERT INTO SeatOfTicket (Cid, Tnumber, Sname, Snumber)
VALUES 
('fedb3535G', '000001', 'Al Janoub Stadium', 1),
('rw2D3f3fF', '000001', 'Education City Stadium', 43000),
('2249rffwe', '000001', 'Khalifa International Stadium', 2304),
('hbkrs3355', '000001', 'Lusail Iconic Stadium', 124),
('fegreRF65', '000001', 'Al Janoub Stadium', 1000),
('qeiv83fhf', '000001', 'Al Janoub Stadium', 290),
('ywjb43hb5', '000001', 'Al Janoub Stadium', 143);

