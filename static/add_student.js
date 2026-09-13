async function addStudent() {

    const name = document.getElementById("name").value;
    const age = document.getElementById("age").value;
    const department = document.getElementById("department").value;

    if(name=="" || age=="" || department==""){

        alert("Please fill all fields.");

        return;

    }

    const response = await fetch("/students",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({

            name:name,
            age:age,
            department:department

        })

    });

    const result = await response.json();

    alert(result.message);

    window.location.href="/students-page";

}