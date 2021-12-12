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
    -- team_id int NOT NULL,
    team_id int,
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

INSERT INTO team(team_name, mascot)
VALUES ('Team Hurley', 'Wolf');

INSERT INTO player(first_name, last_name, team_id)
VALUES ('Joe', 'Shmoe', 1);

INSERT INTO player(first_name, last_name)
VALUES ('Tom', 'Player2');

INSERT INTO player(first_name, last_name, team_id)
VALUES ('Paul', 'Platt', 1);

INSERT INTO player(first_name, last_name, team_id)
VALUES ('Mac', 'Miller', 2);

INSERT INTO player(first_name, last_name)
VALUES ('Chuck', 'Smith');

INSERT INTO player(first_name, last_name)
VALUES ('Rebecca', 'Clarke');

INSERT INTO player(first_name, last_name)
VALUES ('Frank', 'Yee');
