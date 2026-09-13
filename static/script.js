async function login() {

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const message = document.getElementById("message");

    const response = await fetch("/login", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            username: username,
            password: password
        })

    });

    const result = await response.json();

    if (result.success) {

        window.location.href = "/dashboard";

    }
    else {

        message.innerText = result.message;
        message.style.color = "red";

    }

}