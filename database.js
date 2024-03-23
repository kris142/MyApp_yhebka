const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('./rentalService.db');

db.serialize(function() {
  db.run(`CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    car TEXT,
    date TEXT
  )`);
});

module.exports = db;
