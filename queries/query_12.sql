SELECT s.fullname AS student_name,
    g.name AS group_name,
    sub.name AS subject_name,
    gr.grade,
    gr.grade_date
FROM grades gr
INNER JOIN students s ON gr.student_id = s.id
INNER JOIN groups g ON s.group_id = g.id
INNER JOIN subjects sub ON gr.subject_id = sub.id
WHERE g.id = 1 AND sub.id = 3 AND
    gr.grade_date = (
        SELECT MAX(gr2.grade_date)
        FROM grades gr2
        INNER JOIN students s2 ON gr2.student_id = s2.id
        WHERE  gr2.subject_id = 3 AND s2.group_id = 1
    )
ORDER BY s.fullname;