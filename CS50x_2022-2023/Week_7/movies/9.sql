SELECT name FROM people
JOIN stars ON person_id = people.id
JOIN movies ON movies.id = movie_id
WHERE movies.year = 2004
ORDER BY people.birth;