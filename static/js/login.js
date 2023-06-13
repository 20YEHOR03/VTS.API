document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    fetch("/api/customuser/login/", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value
      },
      body: JSON.stringify({ username: email, password: password })
    })
    .then(response => response.json())
    .then(data => {
        const token  = data.token;
        localStorage.setItem('token', token);
        window.location.href = "/index/";
    })
    .catch(error => {
      console.error('Error:', error);
    });
  });