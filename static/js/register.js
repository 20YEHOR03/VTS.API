document.getElementById('registration-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Заборонити стандартну поведінку форми (автоматичну відправку)

    // Отримати значення полів форми
    const customuser_first_name = document.getElementById('customuser_first_name').value;
    const customuser_last_name = document.getElementById('customuser_last_name').value;
    const customuser_age = document.getElementById('customuser_age').value;
    const customuser_gender = document.getElementById('customuser_gender').value;
    const customuser_email = document.getElementById('customuser_email').value;
    const customuser_password = document.getElementById('customuser_password').value;
    const organization_name = document.getElementById('organization_name').value;
    const organization_address = document.getElementById('organization_address').value;
    const organization_email = document.getElementById('organization_email').value;
    const organization_phone = document.getElementById('organization_phone').value;

    // Відправити POST-запит на сервер для створення організації
    fetch("/api/organization/", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value
        },
        body: JSON.stringify(
        { 
            name: organization_name,
            address: organization_address,
            email: organization_email,
            phone_number: organization_phone
        })
    })
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        var organizationId = data.id; // Отримати ID організації з відповіді сервера

        // Відправити POST-запит на сервер для створення користувача з ID організації

        fetch("/api/customuser/register/", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value
            },
            body: JSON.stringify(
            { 
                email: customuser_email, 
                password: customuser_password,
                first_name: customuser_first_name,
                last_name: customuser_last_name,
                gender_id: customuser_gender,
                age: customuser_age,
                organization_id: organizationId
            })
        })
        .then(function(response) {
            // // Обробити відповідь сервера після створення користувача
            // if (response.ok) {
            //     window.location.href = "";
            //     console.log('Користувача створено успішно!');
            // } else {
            //     // Обробити помилку створення користувача
            //     console.error('Помилка при створенні користувача!');
            // }
            return response.json();
        })
        .catch(function(error) {
            // Обробити помилку запиту на сервер для створення користувача
            console.error('Помилка запиту на сервер для створення користувача: ' + error);
        });
    })
    .catch(function(error) {
        // Обробити помилку запиту на сервер для створення організації
        console.error('Помилка запиту на сервер для створення організації: ' + error);
    });
});