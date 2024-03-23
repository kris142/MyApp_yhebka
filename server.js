const express = require('express');
const bodyParser = require('body-parser');
const db = require('./database');

const app = express();
const port = 3000;

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Роут для обработки данных аренды
app.post('/', (req, res) => {
  const { name, email, car, date } = req.body;

  const sql = `INSERT INTO users (name, email, car, date) VALUES (?, ?, ?, ?)`;
  
  db.run(sql, [name, email, car, date], function(err) {
    if (err) {
      return console.error(err.message);
    }
    res.send('Аренда успешно зарегистрирована!');
  });
});
const path = require('path');


app.listen(port, () => console.log(`Сервер запущен на порту ${port}`));
