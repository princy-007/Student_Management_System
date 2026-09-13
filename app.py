from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

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
    return jsonify(students)


@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):

    for student in students:

        if student["id"] == id:
            return jsonify(student)

    return jsonify({
        "message": "Student Not Found"
    }), 404


@app.route("/students", methods=["POST"])
def add_student():

    data = request.get_json()

    new_student = {
        "id": len(students) + 1,
        "name": data["name"],
        "age": data["age"],
        "department": data["department"]
    }

    students.append(new_student)

    return jsonify({
        "message": "Student Added Successfully",
        "student": new_student
    }), 201


@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):

    data = request.get_json()

    for student in students:

        if student["id"] == id:

            student["name"] = data["name"]
            student["age"] = data["age"]
            student["department"] = data["department"]

            return jsonify({
                "message": "Student Updated Successfully"
            })

    return jsonify({
        "message": "Student Not Found"
    }), 404


@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):

    for student in students:

        if student["id"] == id:

            students.remove(student)

            return jsonify({
                "message": "Student Deleted Successfully"
            })

    return jsonify({
        "message": "Student Not Found"
    }), 404


if __name__ == "__main__":
    app.run(debug=True)