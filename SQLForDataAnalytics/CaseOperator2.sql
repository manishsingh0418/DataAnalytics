SELECT * FROM classsicmodels.orderdetails;
select orderNumber , quantityOrdered,
case
    when quantityOrdered <=30 then "min order"
    when quantityOrdered >=40 then "max order"
    else  "avg order"
end as order_type
from classicmodels.orderdetails;