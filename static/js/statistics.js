const form = document.getElementById('statisticsForm');
var token = localStorage.getItem('token');
const chartCanvas = document.getElementById('chart').getContext('2d');
const currentDate = new Date().toISOString().split('T')[0];
document.getElementById('start_date').value = currentDate;
document.getElementById('end_date').value = currentDate;

function getChart(){
    const startDate = document.getElementById('start_date').value;
    const endDate = document.getElementById('end_date').value;
    const statisticsType = document.getElementById('statisticsType').value;

    fetch(`/api/interaction/${statisticsType}?start_date=${startDate}&end_date=${endDate}`,{
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          "Authorization": "Token " + token
        }
    })
    .then(response => response.json())
    .then(response => {
        const labels = response.labels;
        const data = response.data;

        const chartCanvas = document.getElementById('chart');

        const existingChart = Chart.getChart(chartCanvas);
        if (existingChart) {
            existingChart.destroy();
        }

        new Chart(chartCanvas, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
            label: 'Interactions',
            data: data,
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
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
}

form.addEventListener('submit', function (event) {
    event.preventDefault();
    getChart()
  });
  
getChart()