import java.sql.* ;

import java.util.*;






class Soccer {
    public static void main(String[] args) throws SQLException {
        int sqlCode = 0;      // Variable to hold SQLCODE
        String sqlState = "00000";  // Variable to hold SQLSTATE

        // Registering driver, making connection, and creating statement
        try {
            DriverManager.registerDriver(new com.ibm.db2.jcc.DB2Driver());
        } catch (Exception cnfe) {
            System.out.println("Class not found");
        }
        String url = "jdbc:db2://winter2023-comp421.cs.mcgill.ca:50000/cs421";
        //REMEMBER to remove your user id and password before submitting your code!!
        String your_userid = null;
        String your_password = null;
        if (your_userid == null && (your_userid = System.getenv("SOCSUSER")) == null) {
            System.err.println("Error!! do not have a password to connect to the database!");
            System.exit(1);
        }
        if (your_password == null && (your_password = System.getenv("SOCSPASSWD")) == null) {
            System.err.println("Error!! do not have a password to connect to the database!");
            System.exit(1);
        }
        Connection driverCon = DriverManager.getConnection(url, your_userid, your_password);
        Statement driverStatement = driverCon.createStatement();


        runSoccer("9", sqlCode, sqlState, driverCon, driverStatement);

    }

    public static void runSoccer(String option, int code, String state, Connection con, Statement statement)
            throws SQLException {

        switch (option) {
            case "1":
                try {
                    int ok = 1;
                    while (ok == 1) {
                        Scanner scanner = new Scanner(System.in);
                        System.out.println("Please enter a country name: ");
                        String country = scanner.nextLine();

                        String query =
                                "SELECT Matches.Country1 AS HomeTeam, Matches.Country2 AS AwayTeam, Matches.InRound, Matches.Mdate, " +
                                        "SUM(CASE WHEN Goals.Country = Matches.Country1 THEN 1 WHEN Matches.IsCompleted = 0 THEN NULL ELSE 0 END) AS HomeGoals, " +
                                        "SUM(CASE WHEN Goals.Country = Matches.Country2 THEN 1 WHEN Matches.IsCompleted = 0 THEN NULL ELSE 0 END) AS AwayGoals, " +
                                        "COUNT(DISTINCT TicketForMatch.Cid) AS TicketsSold " +
                                        "FROM Matches " +
                                        "JOIN Teams ON (Matches.Country1 = Teams.Country OR Matches.Country2 = Teams.Country) " +
                                        "LEFT JOIN Goals ON Goals.Mid = Matches.Mid " +
                                        "LEFT JOIN TicketForMatch ON TicketForMatch.Mid = Matches.Mid " +
                                        "WHERE Teams.Country = '" + country + "' " +
                                        "GROUP BY Matches.Mid, Matches.Country1, Matches.Country2, Matches.InRound, Matches.Mdate";

                        java.sql.ResultSet rs = statement.executeQuery(query);

                        while (rs.next()) {
                            String country1 = rs.getString("HomeTeam");
                            String country2 = rs.getString("AwayTeam");
                            String round = rs.getString("InRound");
                            java.sql.Date date = rs.getDate("Mdate");
                            String goals1 = rs.getString("HomeGoals");
                            String goals2 = rs.getString("AwayGoals");
                            String tickets = rs.getString("TicketsSold");
                            System.out.println(country1 + " - " + country2 + " | " + date + " | " + round + " | " + goals1 + " - " + goals2 + " | " + tickets);
                        }


                        System.out.println("Enter [A] to find matches of another country, or cancel [P]: ");
                        String choice = scanner.nextLine();
                        if (choice.equals("P"))
                            runSoccer("9", code, state, con, statement);


                    }
                    break;
                } catch (SQLException e) {
                    code = e.getErrorCode(); // Get SQLCODE
                    state = e.getSQLState(); // Get SQLSTATE
                    // Your code to handle errors comes here;
                    // something more meaningful than a print would be good
                    System.out.println("Code: " + code + "  sqlState: " + state);
                    System.out.println(e);
                    break;
                }
            case "2":
                try {

                    insertLoop("first", code, state, con, statement, "", "");
                    runSoccer("9", code, state, con, statement);
                    break;
                } catch (SQLException e) {
                    code = e.getErrorCode(); // Get SQLCODE
                    state = e.getSQLState(); // Get SQLSTATE

                    // Your code to handle errors comes here;
                    // something more meaningful than a print would be good
                    System.out.println("Code: " + code + "  sqlState: " + state);
                    System.out.println(e);
                    break;
                }
            case "3":
                try {
                    Scanner scanner = new Scanner(System.in);
                    System.out.println("Enter the name of the country: ");
                    String country = scanner.nextLine();
                    String matchList = "SELECT * " +
                            "FROM Matches " +
                            "JOIN Teams ON Matches.Country1 = Teams.Country OR Matches.Country2 = Teams.Country " +
                            "WHERE Teams.Country = '" + country + "'";
                    java.sql.ResultSet rs = statement.executeQuery(matchList);
                    while (rs.next()) {
                        String mid = rs.getString("Mid");
                        String country1 = rs.getString("Country1");
                        String country2 = rs.getString("Country2");
                        System.out.println(mid + " | " + country1 + " - " + country2);
                    }
                    System.out.println("Enter the desired match ID: ");
                    String mid = scanner.nextLine();

                    //query the number of yellow or red cards for a team in a given match
                    String query = "SELECT SUM(Stats.RedCard) AS TotalRedCards, SUM(Stats.YellowCards) AS TotalYellowCards " +
                            "FROM Stats " +
                            "JOIN Players ON Stats.Oid = Players.Oid " +
                            "WHERE Players.Country = '" + country + "' AND Stats.Mid = '" + mid + "'";

                    java.sql.ResultSet queryRS = statement.executeQuery(query);
                    if (queryRS.next()) {
                        int totalRedCards = queryRS.getInt("TotalRedCards");
                        int totalYellowCards = queryRS.getInt("TotalYellowCards");
                        System.out.println("Total Red Cards: " + totalRedCards);
                        System.out.println("Total Yellow Cards: " + totalYellowCards);
                    } else {
                        System.out.println("Total Red Cards: 0");
                        System.out.println("Total Yellow Cards: 0");
                    }


                    runSoccer("9", code, state, con, statement);
                    break;
                } catch (SQLException e) {
                    code = e.getErrorCode(); // Get SQLCODE
                    state = e.getSQLState(); // Get SQLSTATE

                    // Your code to handle errors comes here;
                    // something more meaningful than a print would be good
                    System.out.println("Code: " + code + "  sqlState: " + state);
                    System.out.println(e);
                    break;
                }
            case "9":
                // recursively call the function with different input
                Scanner scanner = new Scanner(System.in);
                System.out.println("\nSoccer Main Menu\n" +
                        "\t1. List information of matches of a country\n" +
                        "\t2. Insert initial player information for a match\n" +
                        "\t3. Team fair play information\n" +
                        "\t4. Exit application\n" +
                        "Please Enter Your Option: ");
                String nextOption = scanner.nextLine();

                if (!nextOption.equals("1") & !nextOption.equals("2") & !nextOption.equals("3") & !nextOption.equals("4"))
                    System.err.println("Please input a valid entry: 1 | 2 | 3 | 4");

                runSoccer(nextOption, code, state, con, statement);
                break;
            default:
                //closing the connection if 4
                System.out.println("Program successfully exited!");
                statement.close();
                con.close();
                System.exit(0);
                break;
        }

    }

    public static void insertLoop(String option, int code, String state, Connection con, Statement statement, String c_in, String mid_in) throws SQLException {
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        if (option.equals("first")) {
            String closeMatches = "SELECT * FROM Matches " +
                    "WHERE Mdate BETWEEN CURRENT DATE AND CURRENT DATE + 3 DAYS";

            java.sql.ResultSet rs = statement.executeQuery(closeMatches);

            System.out.println("Matches: \n");
            while (rs.next()) {
                String mid = rs.getString("Mid");
                String country1 = rs.getString("Country1");
                String country2 = rs.getString("Country2");
                String date = rs.getString("Mdate");
                String round = rs.getString("InRound");

                System.out.println(mid + " | " + country1 + " - " + country2 + " | " + date + " | " + round);
            }
            insertLoop("second", code, state, con, statement, "", "");
        }
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        else if (option.equals("second")) {
            Scanner scanner = new Scanner(System.in);
            System.out.println("Please select a Country or cancel [P]: ");
            String country = scanner.nextLine();
            if (country.equals("P")) {
                runSoccer("9", code, state, con, statement);
            }
            System.out.println("Please select a match ID or cancel [P]: ");
            String matchID = scanner.nextLine();
            if (matchID.equals("P")) {
                runSoccer("9", code, state, con, statement);
            }


            String starters = "SELECT p.Pname, plyr.KitNumber, stats.PosInGame, stats.InTime, stats.OutTime, stats.YellowCards, stats.RedCard " +
                    "FROM Players plyr " +
                    "JOIN Participants p ON plyr.Oid = p.Oid " +
                    "LEFT JOIN Stats stats ON plyr.Oid = stats.Oid AND stats.Mid = '" + matchID + "' " +
                    "WHERE plyr.Country = '" + country + "' " +
                    "AND EXISTS ( SELECT * FROM Stats " +
                    "WHERE Stats.Mid = '" + matchID + "' " +
                    "AND Stats.Oid = plyr.Oid )";

            java.sql.ResultSet rs1 = statement.executeQuery(starters);

            System.out.println("The following players from " + country + " are already entered for match " + matchID + ":");
            while (rs1.next()) {
                String pname = rs1.getString("Pname");
                int kitNumber = rs1.getInt("KitNumber");
                String posInGame = rs1.getString("PosInGame");
                String inTime = rs1.getString("InTime");
                String outTime = rs1.getString("OutTime");
                int yellowCards = rs1.getInt("YellowCards");
                int redCard = rs1.getInt("RedCard");
                System.out.println(pname + "\t" + kitNumber + "\t" + posInGame + "\t" + inTime + "\t" + outTime + "\t" + yellowCards + "\t" + redCard);
            }

            String benchers = "SELECT plyr.Oid, p.Pname, plyr.KitNumber, plyr.GenPosition " +
                    "FROM Players plyr JOIN Participants p ON plyr.Oid = p.Oid " +
                    "WHERE plyr.Country = '" + country + "' " +
                    "AND NOT EXISTS ( SELECT * FROM Stats " +
                    "WHERE Stats.Mid = '" + matchID + "' " +
                    "AND Stats.Oid = plyr.Oid )";

            java.sql.ResultSet rs2 = statement.executeQuery(benchers);

            System.out.println("\nPossible players from " + country + " not selected:");
            while (rs2.next()) {
                String pname = rs2.getString("Pname");
                int kitNumber = rs2.getInt("KitNumber");
                String position = rs2.getString("GenPosition");
                System.out.println(kitNumber + "\t|\t" + pname + "\t" + position);
            }
            insertLoop("third", code, state, con, statement, country, matchID);

        }
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        else if (option.equals("third")) {
            Scanner scanner = new Scanner(System.in);
            System.out.println("Enter the number of the player you want to insert or cancel [P]: ");
            String newKit = scanner.nextLine();
            if (newKit.equals("P")) {
                runSoccer("9", code, state, con, statement);
            }
            System.out.println("Enter the specific position of the player or cancel [P]: ");
            String newPos = scanner.nextLine();
            if (newPos.equals("P")) {
                runSoccer("9", code, state, con, statement);
            }

            //get player oid
            String getPlayerOid = "SELECT Oid FROM Players WHERE Country = '" + c_in + "' AND KitNumber = '" + newKit + "'";
            java.sql.ResultSet oidRS = statement.executeQuery(getPlayerOid);
            String poid = "";
            while (oidRS.next()) {
                poid = oidRS.getString("Oid");
            }

            //if the number of players playing == 11, then decline
            String countPlayers = "SELECT COUNT(*) FROM Stats WHERE Mid = '" + mid_in + "' AND Oid IN " +
                    "(SELECT Oid FROM Players WHERE Country = '" + c_in + "')";
            java.sql.ResultSet countRS = statement.executeQuery(countPlayers);
            int count = 0;
            while (countRS.next()) {
                count = countRS.getInt(1);
            }

            if (count < 11) {
                String addPlayer = "INSERT INTO Stats (Oid, Mid, InTime, OutTime, PosInGame, RedCard, YellowCards) " +
                        "VALUES ('" + poid + "','" + mid_in + "', '00:00', null,'" + newPos + "', 0, 0)";
                statement.executeUpdate(addPlayer);

                String starters = "SELECT p.Pname, plyr.KitNumber,  stats.PosInGame, stats.InTime, stats.OutTime, stats.YellowCards, stats.RedCard " +
                        "FROM Players plyr " +
                        "JOIN Participants p ON plyr.Oid = p.Oid " +
                        "LEFT JOIN Stats stats ON plyr.Oid = stats.Oid AND stats.Mid = '" + mid_in + "' " +
                        "WHERE plyr.Country = '" + c_in + "' " +
                        "AND EXISTS ( SELECT * FROM Stats " +
                        "WHERE Stats.Mid = '" + mid_in + "' " +
                        "AND Stats.Oid = plyr.Oid )";

                java.sql.ResultSet rs1 = statement.executeQuery(starters);

                System.out.println("The following players from " + c_in + " are already entered for match " + mid_in + ":");
                while (rs1.next()) {
                    String pname = rs1.getString("Pname");
                    int kitNumber = rs1.getInt("KitNumber");
                    String posInGame = rs1.getString("PosInGame");
                    String inTime = rs1.getString("InTime");
                    String outTime = rs1.getString("OutTime");
                    int yellowCards = rs1.getInt("YellowCards");
                    int redCard = rs1.getInt("RedCard");
                    System.out.println(pname + "\t" + kitNumber + "\t" + posInGame + "\t" + inTime + "\t" + outTime + "\t" + yellowCards + "\t" + redCard);
                }

                String benchers = "SELECT plyr.Oid, p.Pname, plyr.KitNumber, plyr.GenPosition " +
                        "FROM Players plyr JOIN Participants p ON plyr.Oid = p.Oid " +
                        "WHERE plyr.Country = '" + c_in + "' " +
                        "AND NOT EXISTS ( SELECT * FROM Stats " +
                        "WHERE Stats.Mid = '" + mid_in + "' " +
                        "AND Stats.Oid = plyr.Oid )";

                java.sql.ResultSet rs2 = statement.executeQuery(benchers);

                System.out.println("\nPossible players from " + c_in + " not selected:");
                while (rs2.next()) {
                    String pname = rs2.getString("Pname");
                    int kitNumber = rs2.getInt("KitNumber");
                    String position = rs2.getString("GenPosition");
                    System.out.println(kitNumber + "\t|\t" + pname + "\t" + position);
                }


            } else {
                System.out.println("Error: Team is full");

                String starters = "SELECT p.Pname, plyr.KitNumber, stats.PosInGame, stats.InTime, stats.OutTime, stats.YellowCards, stats.RedCard " +
                        "FROM Players plyr " +
                        "JOIN Participants p ON plyr.Oid = p.Oid " +
                        "LEFT JOIN Stats stats ON plyr.Oid = stats.Oid AND stats.Mid = '" + mid_in + "' " +
                        "WHERE plyr.Country = '" + c_in + "' " +
                        "AND EXISTS ( SELECT * FROM Stats " +
                        "WHERE Stats.Mid = '" + mid_in + "' " +
                        "AND Stats.Oid = plyr.Oid )";

                java.sql.ResultSet rs1 = statement.executeQuery(starters);

                System.out.println("The following players from " + c_in + " are already entered for match " + mid_in + ":");
                while (rs1.next()) {
                    String pname = rs1.getString("Pname");
                    int kitNumber = rs1.getInt("KitNumber");
                    String posInGame = rs1.getString("PosInGame");
                    String inTime = rs1.getString("InTime");
                    String outTime = rs1.getString("OutTime");
                    int yellowCards = rs1.getInt("YellowCards");
                    int redCard = rs1.getInt("RedCard");
                    System.out.println(pname + "\t" + kitNumber + "\t" + posInGame + "\t" + inTime + "\t" + outTime + "\t" + yellowCards + "\t" + redCard);
                }

                String benchers = "SELECT plyr.Oid, p.Pname, plyr.KitNumber, plyr.GenPosition " +
                        "FROM Players plyr JOIN Participants p ON plyr.Oid = p.Oid " +
                        "WHERE plyr.Country = '" + c_in + "' " +
                        "AND NOT EXISTS ( SELECT * FROM Stats " +
                        "WHERE Stats.Mid = '" + mid_in + "' " +
                        "AND Stats.Oid = plyr.Oid )";

                java.sql.ResultSet rs2 = statement.executeQuery(benchers);

                System.out.println("\nPossible players from " + c_in + " not selected:");
                while (rs2.next()) {
                    String pname = rs2.getString("Pname");
                    int kitNumber = rs2.getInt("KitNumber");
                    String position = rs2.getString("GenPosition");
                    System.out.println(kitNumber + "\t|\t" + pname + "\t" + position);
                }


            }
            System.out.println("Enter [A] to continue adding players, or cancel [P]: ");
            String choice = scanner.nextLine();
            if (choice.equals("P"))
                runSoccer("9", code, state, con, statement);
            else
                insertLoop("third", code, state, con, statement, c_in, mid_in);
        }
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


    }
}
