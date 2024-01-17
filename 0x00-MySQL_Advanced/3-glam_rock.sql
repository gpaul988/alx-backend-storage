-- Graham S. Paul - 3-glam_rock.sql
-- SQL script  that files all band with Glam Rock as their defgaul style
-- rated by longevity

SELECT band_name, (IFNULL(split, 2022) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam Rock%'
ORDER BY lifespan DESC;
