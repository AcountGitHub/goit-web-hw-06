SELECT s.fullname AS student_name,
    ROUND(AVG(g.grade), 2) AS average_grade
FROM students s
INNER JOIN grades g ON s.id = g.student_id
WHERE g.subject_id = 3
GROUP BY s.id, s.fullname
ORDER BY average_grade DESC
LIMIT 1;