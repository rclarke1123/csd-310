use pysports;
CREATE TABLE Team (
    team_id int NOT NULL AUTO_INCREMENT,
    team_name varchar(75) NOT NULL,
    mascot varchar(75),
    PRIMARY KEY (team_id)
); 
CREATE TABLE Player (
    player_id int NOT NULL AUTO_INCREMENT,
    first_name varchar(75) NOT NULL,
    last_name varchar(75) NOT NULL,
    team_id int NOT NULL,
    PRIMARY KEY (player_id),
    CONSTRAINT fk_team
    FOREIGN KEY (team_id) REFERENCES Team(team_id)
); 
-- CREATE USER reba0310@localhost IDENTIFIED WITH mysql_native_password BY 'darlies10';
-- GRANT ALL PRIVILEGES ON pysports.* TO reba0310@localhost;
-- DROP USER IF EXISTS reba0310@localhost;
--  "C:\Users\reba0\Dropbox\My PC (LAPTOP-PGVTAU0P)\Documents\GitHub\csd-310\module_8\db_init.sql"
-- insert team records
INSERT INTO team(team_name, mascot)
VALUES ('Team Clarke', 'Dog');

INSERT INTO team(team_name, mascot)
VALUES ('Team Allen', 'Deer');

INSERT INTO player(first_name, last_name, team_id)
VALUES ('Joe', 'Player1', 1);

INSERT INTO player(first_name, last_name, team_id)
VALUES ('Tom', 'Player2', 1);

INSERT INTO player(first_name, last_name, team_id)
VALUES ('Paul', 'Player2', 1);

INSERT INTO player(first_name, last_name, team_id)
VALUES ('Mac', 'Player4', 2);
