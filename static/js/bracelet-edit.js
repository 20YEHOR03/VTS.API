var token = localStorage.getItem('token');
var editModal = document.getElementById("edit-modal");
var saveButton = document.getElementById("save-button");
var cancelButton = document.getElementById("cancel-button");
var braceletId = window.location.pathname.split('/').pop();
var selectCustomuser = document.getElementById('customuser-select');

function getVisitorsInfo() {
  fetch('/api/customuser/get-visitors/', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Token ' + token
    }
  })
    .then(response => response.json())
    .then(data => {
      data.forEach(visitor => {
        var option = document.createElement('option');
        option.value = visitor.id;
        option.textContent = visitor.first_name + " " + visitor.last_name + " " + visitor.age;
        selectCustomuser.appendChild(option);
      });
    })
    .catch(error => {
      console.error('Error:', error);
    });
}

function getBraceletInfo() {
  fetch(`/api/bracelet/${braceletId}`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Token ' + token
    }
  })
  .then(response => response.json())
  .then(data => {
    document.getElementById("rfid-input").value = data.rfid;
    document.querySelector('#status-select').value = data.status;
    document.getElementById("activation-date-input").value = data.activation_date;
    document.getElementById("deactivation-date-input").value = data.deactivation_date;
    document.querySelector('#customuser-select').value = data.customuser_id;
  })
  .catch(error => {
    console.error('Error:', error);
  });
}

document.getElementById('edit-bracelet-form').addEventListener('submit', function(event) {
  event.preventDefault();

  var rfidInput = document.getElementById("rfid-input").value;
  var statusSelect = document.getElementById("status-select").value;
  var activationDateInput = document.getElementById("activation-date-input").value;
  var deactivationDateInput = document.getElementById("deactivation-date-input").value;
  var customuserSelect = document.getElementById("customuser-select").value;
  
  var braceletData = {
    rfid: rfidInput,
    status: statusSelect,
    activation_date: activationDateInput,
    deactivation_date: deactivationDateInput, 
    customuser_id: customuserSelect
  };

  console.log(braceletData);
  fetch("/api/bracelet/" + braceletId, {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
      'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
      "Authorization": "Token " + token
    },
    body: JSON.stringify(braceletData)
  })
  .then(response => {
    if (response.ok) {
        console.log(response);
      if (response.status === 204) {
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
  });
})

cancelButton.addEventListener("click", function() {
  window.location.href = "/bracelets/";
});

getBraceletInfo();
getVisitorsInfo();