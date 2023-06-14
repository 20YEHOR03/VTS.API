const form = document.getElementById('statisticsForm');
var token = localStorage.getItem('token');
const chartCanvas = document.getElementById('chart').getContext('2d');
const currentDate = new Date().toISOString().split('T')[0];
document.getElementById('start_date').value = currentDate;
document.getElementById('end_date').value = currentDate;
  // При відправці форми
  form.addEventListener('submit', function (event) {
    event.preventDefault();

    // Отримання значень з форми
    const startDate = document.getElementById('start_date').value;
    const endDate = document.getElementById('end_date').value;
    const statisticsType = document.getElementById('statisticsType').value;

    fetch(`/api/interaction/${statisticsType}?start_date=${startDate}&end_date=${endDate}`,{
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          //'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
          "Authorization": "Token " + token
        }
    })
    .then(response => response.json())
    .then(response => {
        const labels = response.labels; // мітки для осі X (назви зон або сервісів)
        const data = response.data; // дані для осі Y (кількість взаємодій)

        const chartCanvas = document.getElementById('chart');

// Check if a chart already exists
        const existingChart = Chart.getChart(chartCanvas);
        if (existingChart) {
        existingChart.destroy(); // Destroy the existing chart
        }

        // Create the new chart
        new Chart(chartCanvas, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
            label: 'Interactions',
            data: data,
            backgroundColor: 'rgba(75, 192, 192, 0.2)', // колір стовпчиків
            borderColor: 'rgba(75, 192, 192, 1)', // колір меж
            borderWidth: 1
            }]
        },
        options: {
            scales: {
            y: {
                beginAtZero: true
            }
            }
        }
        });
    })
    .catch(error => {
        console.error('Error:', error);
    });
    // Відправка AJAX-запиту на сервер з використанням отриманих значень
    // const xhr = new XMLHttpRequest();
    // xhr.open('GET', `/api/interaction/${statisticsType}?start_date=${startDate}&end_date=${endDate}`, true);
    // xhr.onreadystatechange = function () {
    //   if (xhr.readyState === 4 && xhr.status === 200) {
    //     // Отримання даних з сервера
    //     const response = JSON.parse(xhr.responseText);

    //     // Підготовка даних для графіку
    //     const labels = response.labels; // мітки для осі X (назви зон або сервісів)
    //     const data = response.data; // дані для осі Y (кількість взаємодій)

    //     // Створення гістограми
    //     new Chart(chartCanvas, {
    //       type: 'bar',
    //       data: {
    //         labels: labels,
    //         datasets: [{
    //           label: 'Interactions',
    //           data: data,
    //           backgroundColor: 'rgba(75, 192, 192, 0.2)', // колір стовпчиків
    //           borderColor: 'rgba(75, 192, 192, 1)', // колір меж
    //           borderWidth: 1
    //         }]
    //       },
    //       options: {
    //         scales: {
    //           y: {
    //             beginAtZero: true
    //           }
    //         }
    //       }
    //     });
    //   }
    // };
    // xhr.send();
  });