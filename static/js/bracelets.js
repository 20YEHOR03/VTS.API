var token = localStorage.getItem('token');
var braceletsContainer = document.getElementById("bracelets-container");
var addButton = document.getElementById("add-button");
var messageContainer = document.getElementById("message-container");

function displayMessage(message) {
    messageContainer.textContent = message;
    messageContainer.style.display = "block";
}

function hideMessage() {
    messageContainer.style.display = "none";
}

function fetchBracelets() {
    fetch("/api/bracelet/", {
    method: "GET",
    headers: {
        "Content-Type": "application/json",
        "Authorization": "Token " + token
    }
    })
    .then(response => {
        if (response.ok) {
            if (response.status === 204) {
                // No bracelets available
                // Update the UI accordingly or display a message
            } else {
                // Bracelets available, parse the JSON response
                return response.json();
            }
        } else {
        throw new Error("Failed to fetch bracelets");
        }
    })
    .then(data => {
        hideMessage();

        if (!data) {
            displayMessage("У системі немає браслетів");
        } else {
            braceletsContainer.innerHTML = "";
            data.forEach(bracelet => createBraceletCard(bracelet));
        }
    })
    .catch(error => {
        console.error("Error:", error);
    });
}

function createBraceletCard(bracelet) {
    var braceletCard = document.createElement("div");
    braceletCard.className = "item-card";
    braceletCard.dataset.braceletId = bracelet.id;

    var rfid = document.createElement("h3");
    rfid.textContent = "RFID: " + bracelet.rfid;

    var status = document.createElement("p");
    status.textContent = "Status: " + (bracelet.status? "Active" : "Unactive");

    var activationDate = document.createElement("p");
    activationDate.textContent = "Activation date: " + bracelet.activation_date;

    var deactivationDate = document.createElement("p");
    deactivationDate.textContent = "Deactivation date: " + bracelet.deactivation_date;

    var user = document.createElement("p");
    if (bracelet.customuser_id !== null){
        fetch(`/api/customuser/get-info/${bracelet.customuser_id}`, {
            method: 'GET',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': 'Token ' + token
            }
          })
          .then(response => response.json())
          .then(data => {
            user.textContent = `User: ${data.first_name} ${data.last_name} ${data.age}`;
          })
          .catch(error => {
            console.error('Error:', error);
          });
    }
    else{
        user.textContent = `User: no user`;
    }

    var buttonContainer = document.createElement("div");
    buttonContainer.className = "button-container";

    var editButton = document.createElement("button");
    editButton.textContent = "Edit";
    editButton.addEventListener("click", function() {
        window.location.href = "/bracelet/edit/" + bracelet.id;
    });

    var deleteButton = document.createElement("button");
    deleteButton.textContent = "Delete";
    deleteButton.addEventListener("click", function() {
        deleteBracelet(bracelet);
    });

    buttonContainer.appendChild(editButton);
    buttonContainer.appendChild(deleteButton);

    braceletCard.appendChild(rfid);
    braceletCard.appendChild(status);
    braceletCard.appendChild(activationDate);
    braceletCard.appendChild(deactivationDate);
    braceletCard.appendChild(user);
    braceletCard.appendChild(buttonContainer);

    braceletsContainer.appendChild(braceletCard);
}

function deleteBracelet(bracelet) {
    fetch("/api/bracelet/" + bracelet.id, {
    method: "DELETE",
    headers: {
        "Content-Type": "application/json",
        "Authorization": "Token " + token
    }
    })
    .then(response => {
        if (response.ok) {
            fetchBracelets();
        } else {
            throw new Error("Failed to delete bracelet");
        }
    })
    .catch(error => {
        console.error("Error:", error);
    });
}

addButton.addEventListener("click", function() {
    window.location.href = "/bracelet/add";
});

fetchBracelets();