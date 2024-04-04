<?php

ini_set('display_errors', 1);
error_reporting(E_ALL);

// Проверяем наличие файла базы данных и права доступа
$dbPath = __DIR__ . '/database.sqlite';
if (!file_exists($dbPath) || !is_writable($dbPath)) {
    die("Ошибка: файл базы данных не существует или не доступен для записи.");
}

// Подключаемся к базе данных SQLite
$pdo = new PDO('sqlite:' . $dbPath);
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

// Проверяем, что все необходимые данные были отправлены
if (!empty($_POST['name']) && !empty($_POST['email']) && !empty($_POST['phone']) && !empty($_POST['message'])) {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    $message = $_POST['message'];

    // Подготавливаем SQL запрос для вставки данных
    $sql = "INSERT INTO feedback (name, email, phone, message) VALUES (?, ?, ?, ?)";
    $stmt = $pdo->prepare($sql);

    // Выполняем запрос
    try {
        $stmt->execute([$name, $email, $phone, $message]);
        echo "Ваша заявка успешно отправлена!";
    } catch (Exception $e) {
        echo "Ошибка при отправке заявки: " . $e->getMessage();
    }
} else {
    echo "Необходимо заполнить все поля формы.";
}
