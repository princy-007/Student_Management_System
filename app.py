from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)
def get_db_connection():
    connection = sqlite3.connect("student_management.db")
    connection.row_factory = sqlite3.Row
    return connection
def create_students_table():

    connection = get_db_connection()

    connection.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        department TEXT NOT NULL
        
    );
    """)

    connection.commit()

    connection.close()
create_students_table()

USERNAME = "admin"
PASSWORD = "admin123"

students = [
    {
        "id": 1,
        "name": "Anu",
        "age": 20,
        "department": "CS"
    },
    {
        "id": 2,
        "name": "Rahul",
        "age": 21,
        "department": "IT"
    }
]

@app.route("/")
def home():
    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/students-page")
def students_page():
    return render_template("students.html")


@app.route("/add-student")
def add_student_page():
    return render_template("add_student.html")


# NEW ROUTE
@app.route("/edit-student/<int:id>")
def edit_student_page(id):
    return render_template("edit_student.html", student_id=id)


@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if username == USERNAME and password == PASSWORD:

        return jsonify({
            "success": True,
            "message": "Login Successful"
        })

    return jsonify({
        "success": False,
        "message": "Invalid Credentials"
    })




@app.route("/students", methods=["GET"])
def get_students():

    connection = get_db_connection()

    students = connection.execute(
        "SELECT * FROM students"
    ).fetchall()

    connection.close()

    students_list = []

    for student in students:
        students_list.append({
            "id": student["id"],
            "name": student["name"],
            "age": student["age"],
            "department": student["department"]
        })

    return jsonify(students_list)

@app.route("/students", methods=["POST"])
def add_student():

    data = request.get_json()

    connection = get_db_connection()

    connection.execute(
        """
        INSERT INTO students (name, age, department)
        VALUES (?, ?, ?)
        """,
        (
            data["name"],
            data["age"],
            data["department"]
            
        )
    )

    connection.commit()
    connection.close()

    return jsonify({
        "message": "Student Added Successfully"
    }), 201


@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):

    data = request.get_json()

    connection = get_db_connection()

    cursor = connection.execute(
        """
        UPDATE students
        SET name = ?, age = ?, department = ?
        WHERE id = ?
        """,
        (
            data["name"],
            data["age"],
            data["department"],
            id
        )
    )

    connection.commit()

    if cursor.rowcount == 0:
        connection.close()
        return jsonify({
            "message": "Student not found"
        }), 404

    connection.close()

    return jsonify({
        "message": "Student Updated Successfully"
    })


@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):

    connection = get_db_connection()

    cursor = connection.execute(
        "DELETE FROM students WHERE id = ?",
        (id,)
    )

    connection.commit()

    if cursor.rowcount == 0:
        connection.close()
        return jsonify({
            "message": "Student not found"
        }), 404

    connection.close()

    return jsonify({
        "message": "Student Deleted Successfully"
    })

if __name__ == "__main__":
    app.run(debug=True)