SELECT ROUND(AVG(g.grade), 2) AS average_grade,
    s.fullname AS student_name,
    t.fullname AS teacher_name
FROM grades g
INNER JOIN subjects sub ON g.subject_id = sub.id
INNER JOIN students s ON g.student_id = s.id
INNER JOIN teachers t ON sub.teacher_id = t.id
WHERE s.id = 20 AND t.id = 3
GROUP BY s.fullname, t.fullname;