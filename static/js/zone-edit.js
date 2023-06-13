var token = localStorage.getItem('token');
var editModal = document.getElementById("edit-modal");
var saveButton = document.getElementById("save-button");
var cancelButton = document.getElementById("cancel-button");
var zoneId = window.location.pathname.split('/').pop();

function getZoneInfo() {
  fetch(`/api/zone/${zoneId}`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Token ' + token
    }
  })
  .then(response => response.json())
  .then(data => {
    document.getElementById("name-input").value = data.name;
    document.getElementById("description-input").value = data.description;
  })
  .catch(error => {
    console.error('Error:', error);
  });
}

document.getElementById('edit-zone-form').addEventListener('submit', function(event) {
  event.preventDefault();

  var nameInput = document.getElementById("name-input").value;
  var descriptionInput = document.getElementById("description-input").value;

  var zoneData = {
    name: nameInput,
    description: descriptionInput
  };

  fetch("/api/zone/" + zoneId, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
      "Authorization": "Token " + token
    },
    body: JSON.stringify(zoneData)
  })
  .then(response => {
    window.location.href = "/zones/";
    if (response.ok) {
        console.log(response);
      //if (response.status === 200) {
        window.location.href = "/zones/";
      //} else {
      //  return response.json();
      //}
    } else {
      throw new Error('Failed to fetch zone');
    }
  })
  .catch(error => {
    console.error("Error:", error);
  });
})

cancelButton.addEventListener("click", function() {
  window.location.href = "/zones/";
});

getZoneInfo();