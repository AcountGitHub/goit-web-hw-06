SELECT g.name AS group_name,
    ROUND(AVG(gr.grade), 2) AS average_grade
FROM grades gr
INNER JOIN students s ON gr.student_id = s.id
INNER JOIN groups g ON s.group_id = g.id
WHERE gr.subject_id = 3
GROUP BY g.id, g.name
ORDER BY average_grade DESC;