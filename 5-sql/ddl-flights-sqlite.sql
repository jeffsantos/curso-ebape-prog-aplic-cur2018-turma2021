
CREATE TABLE locations (
    id INTEGER PRIMARY KEY,
    code VARCHAR NOT NULL,
    name VARCHAR NOT NULL
);

INSERT INTO locations (id, code, name) VALUES (NULL, 'JFK', 'New York');
INSERT INTO locations (id, code, name) VALUES (NULL, 'PVG', 'Shanghai');
INSERT INTO locations (id, code, name) VALUES (NULL, 'IST', 'Instanbul');
INSERT INTO locations (id, code, name) VALUES (NULL, 'LHR', 'London');
INSERT INTO locations (id, code, name) VALUES (NULL, 'SVO', 'Moscow');
INSERT INTO locations (id, code, name) VALUES (NULL, 'LIM', 'Lima');
INSERT INTO locations (id, code, name) VALUES (NULL, 'CDG', 'Paris');
INSERT INTO locations (id, code, name) VALUES (NULL, 'NRT', 'Shanghai');
INSERT INTO locations (id, code, name) VALUES (NULL, 'GIG', 'Rio de Janeiro');
INSERT INTO locations (id, code, name) VALUES (NULL, 'DEL', 'New Delhi');

CREATE TABLE flights (
    id INTEGER PRIMARY KEY,
    origin_id INTEGER NOT NULL REFERENCES locations,
    destination_id INTEGER NOT NULL REFERENCES locations, 
    duration INTEGER NOT NULL
);

INSERT INTO flights (id, origin_id, destination_id, duration) VALUES (NULL, 1, 4, 415);
INSERT INTO flights (id, origin_id, destination_id, duration) VALUES (NULL, 2, 7, 760);
INSERT INTO flights (id, origin_id, destination_id, duration) VALUES (NULL, 3, 8, 700);
INSERT INTO flights (id, origin_id, destination_id, duration) VALUES (NULL, 1, 7, 435);
INSERT INTO flights (id, origin_id, destination_id, duration) VALUES (NULL, 5, 7, 245);
INSERT INTO flights (id, origin_id, destination_id, duration) VALUES (NULL, 6, 1, 455);
--INSERT INTO flights (id, origin_id, destination_id, duration) VALUES (NULL, 9, 10, 1440);


CREATE TABLE passengers (
    id INTEGER PRIMARY KEY,
    name VARCHAR NOT NULL,
    flight_id INTEGER NOT NULL REFERENCES flights
);

INSERT INTO passengers (id, name, flight_id) VALUES (NULL, 'Alice', 1);
INSERT INTO passengers (id, name, flight_id) VALUES (NULL, 'Bob', 1);
INSERT INTO passengers (id, name, flight_id) VALUES (NULL, 'Charlie', 2);
INSERT INTO passengers (id, name, flight_id) VALUES (NULL, 'Dave', 2);
INSERT INTO passengers (id, name, flight_id) VALUES (NULL, 'Erin', 4);
INSERT INTO passengers (id, name, flight_id) VALUES (NULL, 'Frank', 6);
INSERT INTO passengers (id, name, flight_id) VALUES (NULL, 'Grace', 6);

