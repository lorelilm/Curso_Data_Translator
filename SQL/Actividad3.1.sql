
SELECT first_name, last_name
FROM actor;


SELECT
UPPER(first_name)||' '||UPPER(last_name) AS 'Actor Name'
FROM actor;


SELECT actor_id, first_name, last_name
FROM actor
WHERE first_name LIKE 'JOE';


SELECT actor_id, first_name, last_name
FROM actor
WHERE last_name LIKE '%GEN%';


SELECT first_name, last_name
FROM actor
WHERE last_name LIKE '%LI%'
ORDER BY last_name ASC, first_name ASC;


SELECT country_id, country
FROM country
WHERE country IN ('Afghanistan', 'Bangladesh', 'China');


SELECT last_name, COUNT (*)
FROM actor
GROUP BY last_name


SELECT last_name, COUNT (*)
FROM actor
GROUP BY last_name
HAVING COUNT(*) >= 2


SELECT first_name, last_name, address
FROM staff
INNER JOIN address ON staff.address_id=address.address_id