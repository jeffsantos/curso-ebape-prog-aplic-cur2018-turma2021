------------------------------------------------------------------------------
-- AULA 01
------------------------------------------------------------------------------

CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
);

INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'London', 415);
INSERT INTO flights (origin, destination, duration) VALUES ('Shangai', 'Paris', 760);
INSERT INTO flights (origin, destination, duration) VALUES ('Istanbul', 'Tokyo', 700);
INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'Paris', 435);
INSERT INTO flights (origin, destination, duration) VALUES ('Moscow', 'Paris', 245);
INSERT INTO flights (origin, destination, duration) VALUES ('Lima', 'New York', 455);
--INSERT INTO flights (origin, destination, duration) VALUES ('Rio de Janeiro', 'New Delhi', 1440);

SELECT * FROM flights;

SELECT origin, destination FROM flights;

SELECT * FROM flights WHERE id = 3;

SELECT * FROM flights WHERE origin = 'New York';

SELECT * FROM flights WHERE duration > 700;

SELECT * FROM flights WHERE destination = 'Paris' AND duration > 700;

SELECT * FROM flights WHERE destination = 'Paris' OR duration >= 700;

SELECT AVG(duration) FROM flights;

SELECT AVG(duration) FROM flights WHERE origin = 'New York';

SELECT COUNT(duration) FROM flights;

SELECT COUNT(duration) FROM flights WHERE origin = 'New York';

SELECT * FROM flights WHERE origin IN ('New York', 'Lima');

SELECT * FROM flights WHERE origin LIKE 'New%';

------------------------------------------------------------------------------
-- AULA 02
------------------------------------------------------------------------------

SELECT * FROM flights LIMIT 3;

SELECT * FROM flights ORDER BY duration ASC;

SELECT origin, COUNT(*) FROM flights GROUP BY origin;

SELECT origin, COUNT(*) FROM flights GROUP BY origin HAVING COUNT(*) > 1;

UPDATE flights
  SET duration = 430
  WHERE origin = 'New York'
  AND destination = 'London';

DELETE FROM flights WHERE origin = 'New York';

-- DROP TABLE fligts;

------------------------------------------------------------------------------
-- AULA 03 (JOINS)
------------------------------------------------------------------------------

SELECT name, duration
FROM passengers
JOIN flights ON passengers.flight_id = flights.id;

SELECT name, duration
FROM flights
JOIN passengers ON flights.id = passengers.flight_id;

-- alias
SELECT p.id id_passengers, f.id id_flights
FROM passengers p
JOIN flights f ON p.flight_id = f.id;

-- 2 joins simultâneos
SELECT * 
FROM flights 
JOIN locations ori on ori.id = flights.origin_id
JOIN locations dest on dest.id = flights.destination_id;

SELECT ori.name origin, dest.name destination, duration
FROM flights 
JOIN locations ori on ori.id = flights.origin_id
JOIN locations dest on dest.id = flights.destination_id;

-- left join

SELECT flights.id, name
FROM flights LEFT JOIN passengers on passengers.flight_id = flights.id
ORDER BY id;

-- Todos juntos
SELECT ori.name origin, dest.name destination, passengers.name 
FROM flights 
INNER JOIN passengers on passengers.flight_id = flights.id
INNER JOIN locations ori on ori.id = flights.origin_id
INNER JOIN locations dest on dest.id = flights.destination_id;