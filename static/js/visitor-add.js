var token = localStorage.getItem('token');
var addModal = document.getElementById("add-modal");
var saveButton = document.getElementById("save-button");
var cancelButton = document.getElementById("cancel-button");

var firstNameInput = document.getElementById("first-name-input");
var lastNameInput = document.getElementById("last-name-input");
var ageInput = document.getElementById("age-input");
var emailInput = document.getElementById("email-input");
var passwordInput = document.getElementById("password-input");

document.getElementById('add-visitor-form').addEventListener('submit', function(event) {
  event.preventDefault();
  var firstNameInputValue = firstNameInput.value;
  var lastNameInputValue = lastNameInput.value;
  var ageInputValue = ageInput.value;
  var emailInputValue = emailInput.value;
  var passwordInputValue = passwordInput.value;
  var genderSelectValue = document.querySelector('#gender-select').value;

  var serviceData = {
    email: emailInputValue,
    password: passwordInputValue,
    first_name: firstNameInputValue,
    last_name: lastNameInputValue,
    gender_id: genderSelectValue,
    age: ageInputValue
  };

  fetch("/api/customuser/create-visitor/", {
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
        window.location.href = "/visitors/";
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
    window.location.href = "/visitors/";
});