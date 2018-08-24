COPY (SELECT
o1.kod AS kod_obce,
o1.nazev AS obec,
o3.nazev AS orp,
o4.nazev AS okres,
o5.nazev AS kraj,
st_astext(st_extent(o1.originalnihranice)) AS bbox
FROM obce AS o1
JOIN pou AS o2 ON o1.poukod = o2.kod
JOIN orp AS o3 ON o2.orpkod = o3.kod
JOIN okresy AS o4 ON o1.okreskod = o4.kod
JOIN vusc AS o5 ON o4.vusckod = o5.kod
GROUP BY o1.kod,o1.nazev,o3.nazev,o4.nazev,o5.nazev
ORDER BY o1.nazev,o3.nazev,o4.nazev,o5.nazev)
TO '/tmp/obce_cr.csv' WITH CSV DELIMITER ',';
