SELECT t.fullname AS teacher_name,
    ROUND(AVG(g.grade), 2) AS average_grade
FROM teachers t
INNER JOIN subjects s ON t.id = s.teacher_id
INNER JOIN grades g ON s.id = g.subject_id
WHERE t.id = 2
GROUP BY t.fullname;