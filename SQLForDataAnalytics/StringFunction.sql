SELECT * FROM sakila.city;
select concat(city_id," - ",city) as city_name from sakila.city;
select concat_ws(" - ",city_id,city) as city_data from sakila.city;
select length(city_id) from sakila.city;
select upper(city) from sakila.city;
select lower(city) from sakila.city;
select left(city,4) as username from sakila.city;
select right(city,4) as username from sakila.city;
select mid(city,2,5) as midname from sakila.city;