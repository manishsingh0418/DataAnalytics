select * from classicmodels.products;
select productline,count(productCode) from classicmodels.products group by productline order by count(productcode) desc;