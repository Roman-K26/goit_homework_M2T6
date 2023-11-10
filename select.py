import logging

import psycopg2
from psycopg2 import DatabaseError



# Підключення до бази даних
conn = psycopg2.connect(host="localhost", database="M2T6", user="postgres", password="567234")
cur = conn.cursor()

if __name__ == '__main__':
    sql_expression_01 = """
        SELECT students.id, students.fullname, AVG(grades.grade) AS avg_grade
        FROM students
        JOIN grades ON students.id = grades.student_id
        GROUP BY students.id, students.fullname
        ORDER BY avg_grade DESC
        LIMIT 5;
        """
    sql_expression_02 = """
        SELECT students.id, students.fullname, AVG(grades.grade) AS avg_grade
        FROM students
        JOIN grades ON students.id = grades.student_id
        JOIN subjects ON grades.subject_id = subjects.id
        WHERE subjects.name = 'idea'
        GROUP BY students.id, students.fullname
        ORDER BY avg_grade DESC
        LIMIT 1;
        """
    sql_expression_03 = """
        SELECT groups.name, AVG(grades.grade) AS avg_grade
        FROM groups
        JOIN students ON groups.id = students.group_id
        JOIN grades ON students.id = grades.student_id
        JOIN subjects ON grades.subject_id = subjects.id
        WHERE subjects.name = 'idea'
        GROUP BY groups.name;
        """
    sql_expression_04 = """
        SELECT AVG(grade) AS avg_grade FROM grades;
        """

    sql_expression_05 = """
        SELECT subjects.name
        FROM subjects
        JOIN teachers ON subjects.teacher_id = teachers.id
        WHERE teachers.fullname = 'Eric Todd';
        """

    sql_expression_06 = """
        SELECT * FROM students WHERE group_id = '3';
        """

    sql_expression_07 = """
        SELECT students.fullname, grades.grade
        FROM students
        JOIN grades ON students.id = grades.student_id
        JOIN subjects ON grades.subject_id = subjects.id
        WHERE students.group_id = '1' AND subjects.name = 'idea';
        """

    sql_expression_08 = """
        SELECT teachers.fullname, AVG(grades.grade) AS avg_grade
        FROM teachers
        JOIN subjects ON teachers.id = subjects.teacher_id
        JOIN grades ON subjects.id = grades.subject_id
        GROUP BY teachers.fullname;
        """
    sql_expression_09 = """
        SELECT subjects.name
        FROM subjects
        JOIN grades ON subjects.id = grades.subject_id
        JOIN students ON grades.student_id = students.id
        WHERE students.fullname = 'Christopher Combs IV';
        """
    sql_expression_10 = """
        SELECT subjects.name
        FROM subjects
        JOIN teachers ON subjects.teacher_id = teachers.id
        JOIN grades ON subjects.id = grades.subject_id
        JOIN students ON grades.student_id = students.id
        WHERE students.fullname = 'William Wood' AND teachers.fullname = 'Barbara Blackwell';
        """
    try:
        if conn is not None:
            c = conn.cursor()
            try:
                c.execute(sql_expression_01)
                result = c.fetchall()
                print(result)
                c.execute(sql_expression_02)
                result = c.fetchall()
                print(result)
                c.execute(sql_expression_03)
                result = c.fetchall()
                print(result)
                c.execute(sql_expression_04)
                result = c.fetchall()
                print(result)
                c.execute(sql_expression_05)
                result = c.fetchall()
                print(result)
                c.execute(sql_expression_06)
                result = c.fetchall()
                print(result)
                c.execute(sql_expression_07)
                result = c.fetchall()
                print(result)
                c.execute(sql_expression_08)
                result = c.fetchall()
                print(result)
                c.execute(sql_expression_09)
                result = c.fetchall()
                print(result)
                c.execute(sql_expression_10)
                result = c.fetchall()
                print(result)

            except DatabaseError as e:
                logging.error(e)
            finally:
                c.close()
        else:
            print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)