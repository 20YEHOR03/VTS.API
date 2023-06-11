let token = localStorage.getItem('token');
let userName; // Приклад: ім'я користувача змінною
let nameElement = document.getElementById("name");

fetch("api/customuser/get-info/", {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Token ' + token
    }
    })
    .then(response => response.json())
    .then(data => {
        userName = data.first_name;
        nameElement.textContent += userName;
    })
  .catch(error => {
    console.error('Error:', error);
});