select * from fact_ventas

ALTER TABLE fact_ventas
ADD COLUMN subtotalventa numeric(18,2);

ALTER TABLE fact_ventas
ADD COLUMN totalconimpuesto numeric(18,2);

UPDATE fact_ventas
SET subtotalventa = cantidadvendida * (preciounitario - descuentounitario);

UPDATE fact_ventas
SET totalconimpuesto = subtotalventa + taxamt;


SELECT cantidadvendida, preciounitario, descuentounitario, taxamt, 
       subtotalventa, totalconimpuesto
FROM fact_ventas
LIMIT 10;
select * from fact_ventas
select * from dim_tiempo
select * from dim_producto
select * from dim_tienda
select * from dim_empleado
select * from dim_cliente
/* 
Ventas mensuales por categoría de producto

Ventas anuales por territorio

Top 10 clientes con mayor facturación

Comparación de ventas por empleado

Margen estimado por producto (si incluye costo)
*/


/* Ventas mensuales pro categoria de producto*/
SELECT 
    dp.name,
    dt.anio,
    dt.nombre_mes,
    SUM(fv.totalconimpuesto) AS ventas_mensuales
FROM fact_ventas as fv
JOIN dim_producto dp ON fv.fk_product = dp.key_producto
JOIN dim_tiempo dt ON fv.fk_tiempo = dt.key_tiempo_dim
GROUP BY dp.name, dt.anio, dt.nombre_mes
ORDER BY dt.anio, dt.nombre_mes, dp.name

/* Ventas anuales por territorio*/

select 
      dt.anio,
	  dtd.name,
	  sum(ft.totalconimpuesto) as ventasAnuales
	  from fact_ventas as ft
	  Join dim_tiempo as dt on ft.fk_tiempo = dt.key_tiempo_dim
	  join dim_tienda as dtd on ft.fk_tienda = dtd.key_tienda_dim
	  GROUP BY dt.anio , dtd.name
	  order by dt.anio , dtd.name

	  
/* Top 10 clientes con mayor facturación */
select 
     c.firstname,
	 c.lastname,
	 sum(ft.totalconimpuesto) as totalFacturado
	 from fact_ventas as ft
	 Join dim_cliente as c on ft.fk_cliente = c.key_cliente
	 GROUP BY c.firstname , c.lastname
	 order by totalFacturado DESC
	 limit 10;

/* Comparación de ventas por empleado*/
SELECT 
    dt.firstname,
    sum(ft.totalconimpuesto) AS ventasEmpleado
FROM fact_ventas ft
JOIN dim_empleado dt ON ft.fk_empleado = dt.key_empleado
GROUP BY dt.firstname 
ORDER BY ventasEmpleado DESC;