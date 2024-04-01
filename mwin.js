function openModal(carName) {
    document.getElementById('car').value = carName;
    document.getElementById('rentModal').style.display = 'block';
}

document.getElementById('rentForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const formData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        car: document.getElementById('car').value,
        date: new Date().toISOString(),
    };

    // Отправка данных на сервер
    fetch('/rent', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        })
        .then(response => response.text())
        .then(data => {
            alert(data);
            document.getElementById('rentModal').style.display = 'none';
        })
        .catch((error) => {
            console.error('Ошибка:', error);
        });
});