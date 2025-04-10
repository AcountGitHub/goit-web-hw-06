SELECT s.fullname AS student_name,
    g.name AS group_name,
    sub.name AS subject_name,
    gr.grade, gr.grade_date
FROM grades gr
INNER JOIN students s ON gr.student_id = s.id
INNER JOIN groups g ON s.group_id = g.id
INNER JOIN subjects sub ON gr.subject_id = sub.id
WHERE g.id = 1 AND sub.id = 3
ORDER BY s.fullname, gr.grade_date;