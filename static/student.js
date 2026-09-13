async function loadStudents() {

    const response = await fetch("/students");

    const students = await response.json();

    let rows = "";

    students.forEach(student => {

        rows += `
        <tr>

            <td>${student.id}</td>
            <td>${student.name}</td>
            <td>${student.age}</td>
            <td>${student.department}</td>

            <td>

                <button onclick="editStudent(${student.id})">
                    Edit
                </button>

                <button onclick="deleteStudent(${student.id})">
                    Delete
                </button>

            </td>

        </tr>
        `;

    });

    document.getElementById("studentTable").innerHTML = rows;

}

loadStudents();


function editStudent(id) {

    window.location.href = `/edit-student/${id}`;

}


async function deleteStudent(id) {

    const confirmDelete = confirm("Are you sure you want to delete this student?");

    if (!confirmDelete) {
        return;
    }

    const response = await fetch(`/students/${id}`, {

        method: "DELETE"

    });

    const result = await response.json();

    alert(result.message);

    loadStudents();

}