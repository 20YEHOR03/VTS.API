var token = localStorage.getItem('token');
var editModal = document.getElementById("edit-modal");
var saveButton = document.getElementById("save-button");
var cancelButton = document.getElementById("cancel-button");
var customuserId = window.location.pathname.split('/').pop();

var firstNameInput = document.getElementById("first-name-input");
var lastNameInput = document.getElementById("last-name-input");
var ageInput = document.getElementById("age-input");
var passwordInput = document.getElementById("password-input");

function getVisitorInfo() {
  fetch(`/api/customuser/get-info/${customuserId}`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Token ' + token
    }
  })
  .then(response => response.json())
  .then(data => {
    firstNameInput.value = data.first_name;
    lastNameInput.value = data.last_name;
    ageInput.value = data.age;
    document.querySelector('#gender-select').value = data.gender_id;
  })
  .catch(error => {
    console.error('Error:', error);
  });
}

document.getElementById('edit-visitor-form').addEventListener('submit', function(event) {
  event.preventDefault();

  var firstNameInputValue = firstNameInput.value;
  var lastNameInputValue = lastNameInput.value;
  var ageInputValue = ageInput.value;
  var genderSelectValue = document.querySelector('#gender-select').value;
    
  var visitorData = {
    first_name: firstNameInputValue,
    last_name: lastNameInputValue,
    gender_id: genderSelectValue,
    age: ageInputValue
  };

  fetch(`/api/customuser/update-info/${customuserId}`, {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
      'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
      "Authorization": "Token " + token
    },
    body: JSON.stringify(visitorData)
  })
  .then(response => {
    if (response.ok) {
        console.log(response);
      if (response.status === 204) {
        window.location.href = "/visitors/";
      } else {
        return response.json();
      }
    } else {
      throw new Error('Failed to fetch visitor');
    }
  })
  .catch(error => {
    console.error("Error:", error);
  });
})

cancelButton.addEventListener("click", function() {
  window.location.href = "/visitors/";
});

getVisitorInfo();