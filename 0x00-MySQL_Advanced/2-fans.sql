-- File country origins of bands, sorte by the number of (non-unique) fans.
-- Graham S. Paul - 2-fans.sql
SELECT origin, SUM(fans) AS nb_fans
    FROM metal_bands
    GROUP BY origin
    ORDER BY nb_fans DESC;
