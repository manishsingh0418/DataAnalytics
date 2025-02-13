SELECT * FROM classicmodels.products;
select productName, quqntityInStock,
case
    when quantityInStock <1000 then "urgent need of more stock"
    else "not required as of now"
end as production_details
from classicmodels.products;
