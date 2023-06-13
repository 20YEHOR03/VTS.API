var token = localStorage.getItem('token');
var visitorsContainer = document.getElementById("visitors-container");
var addButton = document.getElementById("add-button");
var messageContainer = document.getElementById("message-container");

function displayMessage(message) {
    messageContainer.textContent = message;
    messageContainer.style.display = "block";
}

function hideMessage() {
    messageContainer.style.display = "none";
}

function fetchVisitors() {
    fetch("/api/customuser/get-visitors/", {
    method: "GET",
    headers: {
        "Content-Type": "application/json",
        "Authorization": "Token " + token
    }
    })
    .then(response => {
        if (response.ok) {
            if (response.status === 200) {
                return response.json();
            }
        } else {
            throw new Error("Failed to fetch visitors");
        }
    })
    .then(data => {
        hideMessage();
        if (!data) {
            displayMessage("There are no visitors");
        } else {
            visitorsContainer.innerHTML = "";
            data.forEach(visitor => createVisitorCard(visitor));
        }
    })
    .catch(error => {
        console.error("Error:", error);
    });
}

function createVisitorCard(visitor) {
    var visitorCard = document.createElement("div");
    visitorCard.className = "item-card";
    visitorCard.dataset.visitorId = visitor.id;

    var name = document.createElement("h3");
    name.textContent = visitor.first_name + " " + visitor.last_name;

    var age = document.createElement("p");
    age.textContent = "Age: " + visitor.age;

    var gender = document.createElement("p");
    gender.textContent = "Gender: " + (visitor.gender_id == 1 ? "Male" : "Female");

    var buttonContainer = document.createElement("div");
    buttonContainer.className = "button-container";

    var editButton = document.createElement("button");
    editButton.textContent = "Edit";
    editButton.addEventListener("click", function() {
        window.location.href = "/visitor/edit/" + visitor.id;
    });

    var deleteButton = document.createElement("button");
    deleteButton.textContent = "Deactivate";
    deleteButton.addEventListener("click", function() {
        deletevisitor(visitor);
    });

    buttonContainer.appendChild(editButton);
    buttonContainer.appendChild(deleteButton);

    visitorCard.appendChild(name);
    visitorCard.appendChild(age);
    visitorCard.appendChild(gender);
    visitorCard.appendChild(buttonContainer);

    visitorsContainer.appendChild(visitorCard);
}

function deletevisitor(visitor) {
    var visitorData = {};
    fetch("/api/customuser/deactivate-info/" + visitor.id, {
    method: "PATCH",
    headers: {
        "Content-Type": "application/json",
        "Authorization": "Token " + token
    },
    body: JSON.stringify(visitorData)
    })
    .then(response => {
        if (response.ok) {
            fetchVisitors();
        } else {
            throw new Error("Failed to deactivate visitor");
        }
    })
    .catch(error => {
        console.error("Error:", error);
    });
}

addButton.addEventListener("click", function() {
    window.location.href = "/visitor/add";
});

fetchVisitors();