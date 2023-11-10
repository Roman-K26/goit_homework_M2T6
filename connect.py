import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def create_tables():
    connection = psycopg2.connect(
        dbname="M2T6",
        user="postgres",
        password="567234",
        host="localhost",
        port="5432"
    )

    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cursor = connection.cursor()

    try:
        # SQL-запит для створення таблиць
        create_tables_sql = """
        -- Таблиця груп
        CREATE TABLE IF NOT EXISTS groups (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL
        );

        -- Таблиця студентів
        CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            fullname VARCHAR(150) NOT NULL,
            group_id INTEGER REFERENCES groups(id) ON DELETE CASCADE
        );

        -- Таблиця викладачів
        CREATE TABLE IF NOT EXISTS teachers (
            id SERIAL PRIMARY KEY,
            fullname VARCHAR(150) NOT NULL
        );

        -- Таблиця предметів
        CREATE TABLE IF NOT EXISTS subjects (
            id SERIAL PRIMARY KEY,
            name VARCHAR(175) NOT NULL,
            teacher_id INTEGER REFERENCES teachers(id) ON DELETE CASCADE
        );

        -- Таблиця оцінок
        CREATE TABLE IF NOT EXISTS grades (
            id SERIAL PRIMARY KEY,
            student_id INTEGER REFERENCES students(id) ON DELETE CASCADE,
            subject_id INTEGER REFERENCES subjects(id) ON DELETE CASCADE,
            grade INTEGER CHECK (grade >= 0 AND grade <= 100),
            grade_date DATE NOT NULL
        );
        """

        cursor.execute(create_tables_sql)
        print("Таблиці успішно створені.")

    except Exception as e:
        print(f"Помилка при створенні таблиць: {e}")

    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    create_tables()