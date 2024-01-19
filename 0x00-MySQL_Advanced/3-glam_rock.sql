-- SQL script that lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, (IFNULL(split, 2022) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%' AND formed <= 2022 AND (split IS NULL OR split <= 2022)
ORDER BY lifespan DESC;
