
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

--2.1
SELECT last_name, COUNT (*)
FROM actor
GROUP BY last_name;

--2.2
SELECT last_name, COUNT (*)
FROM actor
GROUP BY last_name
HAVING COUNT(*) >= 2;

--2.3
SELECT st.first_name, st.last_name, ad.address
FROM staff st
INNER JOIN address ad
ON st.address_id=ad.address_id;

--2.4
SELECT st.first_name, st.last_name, ROUND(SUM(pay.amount),2) AS amount
FROM staff st
LEFT JOIN payment payment
ON st.staff.id=py.staff_id
GROUP BY st.staff_id;

--2.5
SELECT fi.title as FilmTitle, count(fa.actor_id) as NumActors
FROM film fi
INNER JOIN film_actor fa 
ON fi.film_id=fa.film_id 
GROUP BY fi.title

--2.6
SELECT fi.film_id AS ID, fi.title as FilmTitle, count(inv.inventory_id) as NCopies
FROM film fi
INNER JOIN inventory inv 
ON inv.film_id=fi.film_id
WHERE fi.film_id=439
GROUP BY fi.film_id;

--2.7
SELECT cu.customer_id, cu.last_name, cu.first_name, round(sum(py.amount),2) AS Total_paid
FROM customer cu 
INNER JOIN payment py 
ON cu.customer_id=py.customer_id 
GROUP BY cu.customer_id
ORDER BY cu.last_name ASC;


--3.1

SELECT *
FROM language l
JOIN (SELECT f.title, f.language_id 
    FROM film f 
    WHERE f.title LIKE 'Q%'
    ) Q 
    ON l.language_id=q.language_id 
WHERE l.name = 'English'


--3.2
SELECT fi.title, ac.first_name, ac.last_name
FROM actor ac
INNER JOIN film_actor fa ON ac.actor_id=fa.actor_id
INNER JOIN film fi ON fi.film_id=fa.film_id
WHERE fi.title in (SELECT fi.title FROM film WHERE fi.title = 'ALONE TRIP')

--3.3
SELECT co.country, cu.first_name, cu.last_name, cu.email
FROM customer cu 
INNER JOIN address ad ON cu.address_id=ad.address_id
INNER JOIN city ci ON ci.city_id=ad.city_id
INNER JOIN country co ON co.country_id=ci.country_id
WHERE co.country = 'Canada';


--3.4
SELECT ca.name AS 'Category', fi.title AS 'FilmTitle'
FROM film fi 
INNER JOIN film_category fc ON fc.film_id=fi.film_id
INNER JOIN category ca ON ca.category_id=fc.category_id
WHERE ca.name='Family';

--3.5
SELECT fi.title, COUNT (rn.rental_date)
FROM film fi
INNER JOIN inventory inv ON inv.film_id=fi.film_id
INNER JOIN rental rn ON rn.inventory_id=inv.inventory_id
GROUP BY fi.title
ORDER BY COUNT (rn.rental_date) DESC;

--3.6
SELECT st.store_id, FORMAT("$%.2f",(SUM(py.amount))) AS 'Total Store Amount' 
FROM staff st
INNER JOIN payment py ON py.staff_id=st.staff_id
GROUP BY st.store_id;

--3.7
SELECT cu.store_id, ci.city, co.country
FROM customer cu 
INNER JOIN address ad ON ad.address_id=cu.address_id
INNER JOIN city ci ON ci.city_id=ad.city_id
INNER JOIN country co ON co.country_id=ci.country_id
GROUP BY cu.store_id

--3.8
SELECT ca.name, FORMAT("$%.2f", SUM(py.amount)) AS 'Ingresos Brutos'
FROM category ca
INNER JOIN film_category fc ON fc.category_id=ca.category_id
INNER JOIN film fi ON fi.film_id=fc.film_id
INNER JOIN inventory inv ON inv.film_id=fi.film_id
INNER JOIN rental re ON re.inventory_id=inv.inventory_id
INNER JOIN payment py ON py.rental_id=re.rental_id
GROUP BY ca.name
ORDER BY SUM(py.amount) DESC
LIMIT 5;
