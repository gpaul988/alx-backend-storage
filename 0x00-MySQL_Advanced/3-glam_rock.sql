-- File all bands with Glam rock as their style,
-- Filed by longevity
-- Graham . Paul - 3-glem_rock.sql
-- Column names must be: band_name & lifespan

SELECT band_name, ifnull(split, 2020)-ifnull(formed, 0) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC
