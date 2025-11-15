const fs = require('fs');

function countStudents(path) {
  try {
    const content = fs.readFileSync(path, 'utf8');
    const lines = content.split('\n').filter((line) => line.trim() !== '');

    if (lines.length === 0) {
      console.log('Number of students: 0');
      return;
    }

    const students = lines.slice(1);

    const filtered = students.filter((row) => row.trim() !== '');

    const fields = {};
    let total = 0;

    filtered.forEach((row) => {
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

    console.log(`Number of students: ${total}`);
    
     for (const field in fields) {
  if (Object.prototype.hasOwnProperty.call(fields, field)) {
    const list = fields[field].join(', ');
    console.log(`Number of students in ${field}: ${fields[field].length}. List: ${list}`);
  }
}

  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
