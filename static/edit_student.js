async function loadStudent() {

    const response = await fetch(`/students/${studentId}`);

    const student = await response.json();

    document.getElementById("name").value = student.name;
    document.getElementById("age").value = student.age;
    document.getElementById("department").value = student.department;

}

loadStudent();


async function updateStudent() {

    const name = document.getElementById("name").value;
    const age = document.getElementById("age").value;
    const department = document.getElementById("department").value;

    const response = await fetch(`/students/${studentId}`, {

        method: "PUT",

        headers: {

            "Content-Type": "application/json"

        },

        body: JSON.stringify({

            name: name,
            age: age,
            department: department

        })

    });

    const result = await response.json();

    alert(result.message);

    window.location.href = "/students-page";

}