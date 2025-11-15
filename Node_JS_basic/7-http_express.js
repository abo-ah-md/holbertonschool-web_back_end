const express = require('express');
const fs = require('fs');

const DB_PATH = process.argv[2] || '';

function countStudentsAsync(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, content) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }
      const lines = content.split('\n').filter((line) => line.trim() !== '');
      if (lines.length === 0) {
        resolve('Number of students: 0');
        return;
      }
      const students = lines.slice(1).filter((row) => row.trim() !== '');
      const fields = {};
      let total = 0;
      students.forEach((row) => {
        const vals = row.split(',');
        if (vals.length >= 4) {
          const firstname = vals[0].trim();
          const field = vals[3].trim();
          if (!fields[field]) {
            fields[field] = [];
          }
          fields[field].push(firstname);
          total += 1;
        }
      });
      let result = `Number of students: ${total}`;
      for (const field in fields) {
        if (Object.prototype.hasOwnProperty.call(fields, field)) {
          result += `\nNumber of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`;
        }
      }
      resolve(result);
    });
  });
}

const app = express();

app.get('/', (req, res) => {
  res.type('text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.type('text/plain');
  res.write('This is the list of our students\n');
  await countStudentsAsync(DB_PATH)
    .then((msg) => {
      res.end(msg);
    })
    .catch((err) => {
      res.end(err.message);
    });
});

app.listen(1245);

module.exports = app;
