SELECT DISTINCT s.name AS subject_name
FROM grades g
INNER JOIN subjects s ON s.id = g.subject_id
WHERE g.student_id = 10 AND s.teacher_id = 4