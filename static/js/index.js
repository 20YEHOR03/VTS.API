let token = localStorage.getItem('token');
let userName; // Приклад: ім'я користувача змінною
let nameElement = document.getElementById("name");
let reportContent = document.getElementById("report-content");
let organizationId;

fetch("/api/customuser/get-info/", {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Token ' + token
    }
    })
    .then(response => response.json())
    .then(data => {
        userName = data.first_name;
        organizationId = data.organization_id;
        nameElement.textContent += userName;

        fetch('/api/organization/' + organizationId,{
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + token
          }
          })
          .then(response => response.json())
          .then(data => {
            const organizationInfo = document.createElement('div');
            organizationInfo.innerHTML = `
              <p id="name">Organization Name: ${data.name}</p>
              <p id="address">Address: ${data.address}</p>
              <p id="email">Email: ${data.email}</p>
              <p id="phoneNumber">Phone: ${data.phone_number}</p>
            `;
            reportContent.appendChild(organizationInfo);
          })
          .catch(error => {
            console.error('Error:', error);
          });
        
          fetch('/api/organization/statistics/' + organizationId, {
            method: 'GET',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': 'Token ' + token
            }
            })
          .then(response => response.json())
          .then(data => {
            const statisticsInfo = document.createElement('div');
            statisticsInfo.innerHTML = `
              <p id="currentVisitorsCount">Number of Current Visitors: ${data.currentVisitorsCount}</p>
              <p id="totalBracelets">Total Bracelets: ${data.totalBracelets}</p>
              <p id="totalZones">Total Zones: ${data.totalZones}</p>
              <p id="totalServices">Total Services: ${data.totalServices}</p>
              <p id="InteractionsToday">Total Interactions Today: ${data.totalInteractionsToday}</p>
            `;
            reportContent.appendChild(statisticsInfo);
          })
          .catch(error => {
            console.error('Error:', error);
          });
    })
  .catch(error => {
    console.error('Error:', error);
});

function generateReport() {
  fetch("/api/customuser/get-info/", {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Token ' + token
    }
    })
    .then(response => response.json())
    .then(data => {
        organizationId = data.organization_id;
        fetch('/api/organization/statistics/get-report/' + organizationId, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            "Authorization": "Token " + token
          },
          responseType: 'blob'
        })
        .then(response => {
          if (response.ok) {
            return response.blob();
          } else {
            throw new Error('Failed to generate report');
          }
        })
        .then(blob => {
          // Створення посилання для завантаження файлу звіту
          const downloadLink = document.createElement('a');
          downloadLink.href = URL.createObjectURL(blob);
          downloadLink.download = 'report.docx';
          downloadLink.click();
          URL.revokeObjectURL(downloadLink.href);
        })
        .catch(error => {
          console.error('Error:', error);
        });
    })
    .catch(error => {
    console.error('Error:', error);
});
  // Запит на сервер для отримання звіту у форматі Word

}