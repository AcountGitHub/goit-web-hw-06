SELECT DISTINCT sub.name AS subject_name
FROM grades g
INNER JOIN subjects sub ON g.subject_id = sub.id
WHERE g.student_id = 5;