/* Завдання на SQL до лекції 02. */


/*
1.
Вивести кількість фільмів в кожній категорії.
Результат відсортувати за спаданням
*/

SELECT category.name, COUNT(film.film_id)
FROM postgres.public.film
         LEFT JOIN film_category ON film.film_id = film_category.film_id
         LEFT JOIN category ON film_category.category_id = category.category_id

GROUP BY category.name
ORDER BY 2 DESC;


/*
2.
Вивести 10 акторів, чиї фільми брали на прокат найбільше.
Результат відсортувати за спаданням.
*/

SELECT CONCAT(actor.first_name, ' ', actor.last_name), COUNT(DISTINCT rental_id) AS films_rental_num
FROM rental
         JOIN inventory ON rental.inventory_id = inventory.inventory_id
         JOIN film ON inventory.film_id = film.film_id

         JOIN film_actor ON film.film_id = film_actor.film_id
         JOIN actor ON film_actor.actor_id = actor.actor_id

GROUP BY CONCAT(actor.first_name, ' ', actor.last_name)
ORDER BY 2 DESC
LIMIT 10;


/*
3.
Вивести категорія фільмів, на яку було витрачено найбільше грошей
в прокаті
*/

SELECT category.name, SUM(payment.amount) AS films_rental_sum
FROM rental
         JOIN inventory ON rental.inventory_id = inventory.inventory_id
         JOIN film ON inventory.film_id = film.film_id

         JOIN film_category ON film.film_id = film_category.film_id
         JOIN category ON category.category_id = film_category.category_id

         JOIN payment ON rental.rental_id = payment.rental_id

GROUP BY category.name
ORDER BY SUM(payment.amount) DESC
LIMIT 1;


/*
4.
Вивести назви фільмів, яких не має в inventory.
Запит має бути без оператора IN
*/

SELECT title
FROM film
         LEFT JOIN inventory ON film.film_id = inventory.film_id

WHERE inventory.film_id IS NULL;



/*
5.
Вивести топ 3 актори, які найбільше зʼявлялись в категорії фільмів “Children”.
*/

SELECT CONCAT(actor.first_name, ' ', actor.last_name), COUNT(film.film_id) as films_num_in_category

FROM film
         JOIN film_actor ON film.film_id = film_actor.film_id
         JOIN film_category ON film.film_id = film_category.film_id

         JOIN category ON film_category.category_id = category.category_id
         JOIN actor ON film_actor.actor_id = actor.actor_id

WHERE category.name = 'Children'

GROUP BY 1
ORDER BY COUNT(film.film_id) DESC
LIMIT 3;


/*
6.
Вивести міста з кількістю активних та неактивних клієнтів (в активних customer.active = 1).
Результат відсортувати за кількістю неактивних клієнтів за спаданням.
*/

SELECT city.city,
       COUNT(case when customer.active = 1 THEN customer_id END) AS active_customer_num,
       COUNT(case when customer.active = 0 THEN customer_id END) AS non_active_customer_num

FROM customer
         JOIN address ON customer.address_id = address.address_id
         JOIN city ON address.city_id = city.city_id

GROUP BY 1
ORDER BY 3 DESC;
