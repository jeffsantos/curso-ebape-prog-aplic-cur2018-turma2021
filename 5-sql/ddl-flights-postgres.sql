
CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    code VARCHAR NOT NULL,
    name VARCHAR NOT NULL
);

INSERT INTO locations (code, name) VALUES ('JFK', 'New York');
INSERT INTO locations (code, name) VALUES ('PVG', 'Shanghai');
INSERT INTO locations (code, name) VALUES ('IST', 'Instanbul');
INSERT INTO locations (code, name) VALUES ('LHR', 'London');
INSERT INTO locations (code, name) VALUES ('SVO', 'Moscow');
INSERT INTO locations (code, name) VALUES ('LIM', 'Lima');
INSERT INTO locations (code, name) VALUES ('CDG', 'Paris');
INSERT INTO locations (code, name) VALUES ('NRT', 'Shanghai');
INSERT INTO locations (code, name) VALUES ('GIG', 'Rio de Janeiro');
INSERT INTO locations (code, name) VALUES ('DEL', 'New Delhi');

CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin_id INTEGER NOT NULL REFERENCES locations,
    destination_id INTEGER NOT NULL REFERENCES locations, 
    duration INTEGER NOT NULL
);

INSERT INTO flights (origin_id, destination_id, duration) VALUES (1, 4, 415);
INSERT INTO flights (origin_id, destination_id, duration) VALUES (2, 7, 760);
INSERT INTO flights (origin_id, destination_id, duration) VALUES (3, 8, 700);
INSERT INTO flights (origin_id, destination_id, duration) VALUES (1, 7, 435);
INSERT INTO flights (origin_id, destination_id, duration) VALUES (5, 7, 245);
INSERT INTO flights (origin_id, destination_id, duration) VALUES (6, 1, 455);
--INSERT INTO flights (origin_code, destination_code, duration) VALUES (9, 10, 1440);


CREATE TABLE passengers (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    flight_id INTEGER NOT NULL REFERENCES flights
);

INSERT INTO passengers (name, flight_id) VALUES ('Alice', 1);
INSERT INTO passengers (name, flight_id) VALUES ('Bob', 1);
INSERT INTO passengers (name, flight_id) VALUES ('Charlie', 2);
INSERT INTO passengers (name, flight_id) VALUES ('Dave', 2);
INSERT INTO passengers (name, flight_id) VALUES ('Erin', 4);
INSERT INTO passengers (name, flight_id) VALUES ('Frank', 6);
INSERT INTO passengers (name, flight_id) VALUES ('Grace', 6);
