var token = localStorage.getItem('token');
var servicesContainer = document.getElementById("services-container");
var addButton = document.getElementById("add-button");
var messageContainer = document.getElementById("message-container");

function displayMessage(message) {
    messageContainer.textContent = message;
    messageContainer.style.display = "block";
}

function hideMessage() {
    messageContainer.style.display = "none";
}

function fetchServices() {
    fetch("/api/service/", {
    method: "GET",
    headers: {
        "Content-Type": "application/json",
        "Authorization": "Token " + token
    }
    })
    .then(response => {
        if (response.ok) {
            if (response.description === 204) {
                // No services available
                // Update the UI accordingly or display a message
            } else {
                // services available, parse the JSON response
                return response.json();
            }
        } else {
        throw new Error("Failed to fetch services");
        }
    })
    .then(data => {
        hideMessage();

        if (!data) {
            displayMessage("У системі немає браслетів");
        } else {
            servicesContainer.innerHTML = "";
            data.forEach(service => createServiceCard(service));
        }
    })
    .catch(error => {
        console.error("Error:", error);
    });
}

function getZoneInfo(zoneId){
    var name = "";
    fetch(`/api/zone/${zoneId}`, {
        method: 'GET',
        headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Token ' + token
        }
    })
    .then(response => response.json())
    .then(data => {
        return data.name;
    })
    .catch(error => {
        console.error('Error:', error);
    });
    return name;
}

function createServiceCard(service) {
    var serviceCard = document.createElement("div");
    serviceCard.className = "item-card";
    serviceCard.dataset.serviceId = service.id;

    var name = document.createElement("h3");
    name.textContent = "Name: " + service.name;

    var description = document.createElement("p");
    description.textContent = "Description: " + service.description;

    var minAge = document.createElement("p");
    minAge.textContent = "Minimum age: " + service.minimum_age;

    var zone = document.createElement("p");
    if (service.zone_id !== null){
        fetch(`/api/zone/${service.zone_id}`, {
            method: 'GET',
            headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + token
            }
        })
        .then(response => response.json())
        .then(data => {
            zone.textContent = "Zone: " + data.name;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
    else{
        zone.textContent = `Zone: no zone`;
    }
    

    var buttonContainer = document.createElement("div");
    buttonContainer.className = "button-container";

    var editButton = document.createElement("button");
    editButton.textContent = "Edit";
    editButton.addEventListener("click", function() {
        window.location.href = "/service/edit/" + service.id;
    });

    var deleteButton = document.createElement("button");
    deleteButton.textContent = "Delete";
    deleteButton.addEventListener("click", function() {
        deleteService(service);
    });

    buttonContainer.appendChild(editButton);
    buttonContainer.appendChild(deleteButton);

    serviceCard.appendChild(name);
    serviceCard.appendChild(description);
    serviceCard.appendChild(minAge);
    serviceCard.appendChild(zone);
    serviceCard.appendChild(buttonContainer);
    servicesContainer.appendChild(serviceCard);
}

function deleteService(service) {
    fetch("/api/service/" + service.id, {
    method: "DELETE",
    headers: {
        "Content-Type": "application/json",
        "Authorization": "Token " + token
    }
    })
    .then(response => {
        if (response.ok) {
            fetchServices();
        } else {
            throw new Error("Failed to delete service");
        }
    })
    .catch(error => {
        console.error("Error:", error);
    });
}

addButton.addEventListener("click", function() {
    window.location.href = "/service/add";
});

fetchServices();