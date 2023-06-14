var token = localStorage.getItem('token');
var addModal = document.getElementById("add-modal");
var saveButton = document.getElementById("save-button");
var cancelButton = document.getElementById("cancel-button");
const date = new Date().toLocaleDateString();
document.getElementById("activation-date-input").value = date;
document.getElementById("deactivation-date-input").value = date;

document.getElementById('add-bracelet-form').addEventListener('submit', function(event) {
  event.preventDefault();
  var rfidInput = document.getElementById("rfid-input").value;
  var statusSelect = document.getElementById("status-select").value;
  var activationDateInput = document.getElementById("activation-date-input").value;
  var deactivationDateInput = document.getElementById("deactivation-date-input").value;

  var braceletData = {
    rfid: rfidInput,
    status: statusSelect,
    activation_date: activationDateInput,
    deactivation_date: deactivationDateInput
  };

  fetch("/api/bracelet/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
      "Authorization": "Token " + token
    },
    body: JSON.stringify(braceletData)
  })
  .then(response => {
    if (response.ok) {
      if (response.status === 201) {
        window.location.href = "/bracelets/";
      } else {
        return response.json();
      }
    } else {
      throw new Error('Failed to fetch bracelet');
    }
  })
  .catch(error => {
    console.error("Error:", error);
    return;
  });
})

cancelButton.addEventListener("click", function() {
    window.location.href = "/bracelets/";
});