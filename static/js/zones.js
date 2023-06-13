var token = localStorage.getItem('token');
var zonesContainer = document.getElementById("zones-container");
var addButton = document.getElementById("add-button");
var messageContainer = document.getElementById("message-container");

function displayMessage(message) {
    messageContainer.textContent = message;
    messageContainer.style.display = "block";
}

function hideMessage() {
    messageContainer.style.display = "none";
}

function fetchZones() {
    fetch("/api/zone/", {
    method: "GET",
    headers: {
        "Content-Type": "application/json",
        "Authorization": "Token " + token
    }
    })
    .then(response => {
        if (response.ok) {
            if (response.status === 204) {
                // No zones available
                // Update the UI accordingly or display a message
            } else {
                // zones available, parse the JSON response
                return response.json();
            }
        } else {
        throw new Error("Failed to fetch zones");
        }
    })
    .then(data => {
        hideMessage();

        if (!data) {
            displayMessage("There are no zones");
        } else {
            zonesContainer.innerHTML = "";
            data.forEach(zone => createZoneCard(zone));
        }
    })
    .catch(error => {
        console.error("Error:", error);
    });
}

function createZoneCard(zone) {
    var zoneCard = document.createElement("div");
    zoneCard.className = "item-card";
    zoneCard.dataset.zoneId = zone.id;

    var name = document.createElement("h3");
    name.textContent = "Name: " + zone.name;

    var description = document.createElement("p");
    description.textContent = "Description: " + zone.description;

    var buttonContainer = document.createElement("div");
    buttonContainer.className = "button-container";

    var editButton = document.createElement("button");
    editButton.textContent = "Edit";
    editButton.addEventListener("click", function() {
        window.location.href = "/zone/edit/" + zone.id;
    });

    var deleteButton = document.createElement("button");
    deleteButton.textContent = "Delete";
    deleteButton.addEventListener("click", function() {
        deleteZone(zone);
    });

    buttonContainer.appendChild(editButton);
    buttonContainer.appendChild(deleteButton);

    zoneCard.appendChild(name);
    zoneCard.appendChild(description);
    zoneCard.appendChild(buttonContainer);

    zonesContainer.appendChild(zoneCard);
}

function deleteZone(zone) {
    fetch("/api/zone/" + zone.id, {
    method: "DELETE",
    headers: {
        "Content-Type": "application/json",
        "Authorization": "Token " + token
    }
    })
    .then(response => {
        if (response.ok) {
            fetchZones();
        } else {
            throw new Error("Failed to delete zone");
        }
    })
    .catch(error => {
        console.error("Error:", error);
    });
}

addButton.addEventListener("click", function() {
    window.location.href = "/zone/add";
});

fetchZones();