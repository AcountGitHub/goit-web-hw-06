-- Groups table
DROP TABLE IF EXISTS groups CASCADE;
CREATE TABLE groups (
  id SERIAL PRIMARY KEY NOT NULL,
  name VARCHAR(50) NOT NULL
);

-- Students table
DROP TABLE IF EXISTS students CASCADE;
CREATE TABLE students (
  id SERIAL PRIMARY KEY NOT NULL,
  fullname VARCHAR(100) NOT NULL,
  group_id INTEGER,
  FOREIGN KEY (group_id) REFERENCES groups(id)
  	ON DELETE CASCADE
  	ON UPDATE CASCADE
);

-- Teachers table
DROP TABLE IF EXISTS teachers CASCADE;
CREATE TABLE teachers (
  id SERIAL PRIMARY KEY NOT NULL,
  fullname VARCHAR(100) NOT NULL
);

-- Subjects table
DROP TABLE IF EXISTS subjects CASCADE;
CREATE TABLE subjects (
  id SERIAL PRIMARY KEY NOT NULL,
  name VARCHAR(150) NOT NULL,
  teacher_id INTEGER,
  FOREIGN KEY (teacher_id) REFERENCES teachers(id)
  	ON DELETE SET NULL
  	ON UPDATE CASCADE
);

-- Grades table
DROP TABLE IF EXISTS grades;
CREATE TABLE grades (
  id SERIAL PRIMARY KEY NOT NULL,
  student_id INTEGER,
  subject_id INTEGER,
  grade INTEGER CHECK (grade >= 0 AND grade <= 100),
  grade_date DATE NOT NULL,
  FOREIGN KEY (student_id) REFERENCES students(id)
  	ON DELETE CASCADE
  	ON UPDATE CASCADE,
  FOREIGN KEY (subject_id) REFERENCES subjects(id)
  	ON DELETE CASCADE
  	ON UPDATE CASCADE
);