var token = localStorage.getItem('token');
var braceletsTable = document.getElementById("bracelets-table").getElementsByTagName('tbody')[0];

fetch("api/bracelet/", {
    method: 'GET',
    headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Token ' + token
    }
})
.then(response => response.json())
.then(data => {
    data.forEach(bracelet => {
    var row = document.createElement("tr");
    var rfidCell = document.createElement("td");
    var statusCell = document.createElement("td");
    var activationDateCell = document.createElement("td");
    var deactivationDateCell = document.createElement("td");

    rfidCell.textContent = bracelet.rfid;
    statusCell.textContent = bracelet.status ? "Активний" : "Неактивний";
    activationDateCell.textContent = bracelet.activation_date;
    deactivationDateCell.textContent = bracelet.deactivation_date;

    row.appendChild(rfidCell);
    row.appendChild(statusCell);
    row.appendChild(activationDateCell);
    row.appendChild(deactivationDateCell);

    braceletsTable.appendChild(row);
    });
})
.catch(error => {
    console.error('Error:', error);
});