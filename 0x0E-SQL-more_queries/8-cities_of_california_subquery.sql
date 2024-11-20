-- list all cities of carlifornia
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'california') ORDER BY cities.id ASC;
