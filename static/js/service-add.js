var token = localStorage.getItem('token');
var addModal = document.getElementById("add-modal");
var saveButton = document.getElementById("save-button");
var cancelButton = document.getElementById("cancel-button");
var selectZone = document.getElementById('zone-select');

var nameInput = document.getElementById("name-input");
var descriptionInput = document.getElementById("description-input");
var minAgeInput = document.getElementById("min-age-input");
var gender1Checkbox = document.getElementById("gender_1");
var gender2Checkbox = document.getElementById("gender_2");
var role1Checkbox = document.getElementById("role_1");
var role2Checkbox = document.getElementById("role_2");

fetch('/api/zone/', {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Token ' + token
  }
})
  .then(response => response.json())
  .then(data => {
    data.forEach(zone => {
      var option = document.createElement('option');
      option.value = zone.id;
      option.textContent = zone.name;
      selectZone.appendChild(option);
    });
  })
  .catch(error => {
    console.error('Error:', error);
  });

document.getElementById('add-service-form').addEventListener('submit', function(event) {
  event.preventDefault();
  var nameInputValue = nameInput.value;
  var descriptionInputValue = descriptionInput.value;
  var minAgeInputValue = minAgeInput.value;
  var zoneSelectValue = document.querySelector('#zone-select').value;
  var allowedGendersValue = [];
  var allowedRolesValue = [];

  if (gender1Checkbox.checked)
    allowedGendersValue.push(1);

  if (gender2Checkbox.checked)
    allowedGendersValue.push(2);

  if (role1Checkbox.checked)
    allowedRolesValue.push(1);

  if (role2Checkbox.checked)
    allowedRolesValue.push(2);


  var serviceData = {
    name: nameInputValue,
    description: descriptionInputValue,
    minimum_age: minAgeInputValue,
    zone_id: zoneSelectValue,
    allowed_genders: allowedGendersValue,
    allowed_roles: allowedRolesValue
  };
  fetch("/api/service/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
      "Authorization": "Token " + token
    },
    body: JSON.stringify(serviceData)
  })
  .then(response => {
    if (response.ok) {
        console.log(response);
      if (response.status === 201) {
        window.location.href = "/services/";
      } else {
        return response.json();
      }
    } else {
      throw new Error('Failed to fetch service');
    }
  })
  .catch(error => {
    console.error("Error:", error);
    return;
  });
})

cancelButton.addEventListener("click", function() {
    window.location.href = "/services/";
});