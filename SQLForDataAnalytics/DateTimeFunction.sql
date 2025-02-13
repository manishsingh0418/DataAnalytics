select * from sakila.payment;
select date(payment_date) as dates from sakila.payment;
select time(payment_date) as dates from sakila.payment;
select time(payment_date) as dates from sakila.payment;

-- for differrent table
select * from classicalmodels.order;
select datediff(shippedDate,OrderDate) as dates  from classicalmodels.order;
select day(payment_date) as day from sakila.payment;
select dayname(payment_date) as dayname from sakila.payment;
select month(payment_date) as month from sakila.payment;
select monthname(payment_date) as monthname from sakila.payment;
select year(payment_date) as year from sakila.payment;
select minute(payment_date) as minute from sakila.payment;