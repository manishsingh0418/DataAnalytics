select * from sakila.payment;
-- select sum(amount) as total_amount from sakila.payment;
select count(customer_id) as total_customer from sakila.payment;
select avg(amount) as average_amount from sakila.payment;
select min(amount) as min_amount from sakila.payment;
select max(amount) as max_amount from sakila.payment;
select truncate(amount,0) as amount from sakila.payment;  -- this will print number without decimal value
select truncate(amount,1) as amount from sakila.payment;  -- this will print number with one decimal point value
select ceil(amount) as higher_amount from sakila.payment;    -- this will give upper decimal value
select floor(amount) as lower_amount from sakila.payment;    -- this will give lower decimal value