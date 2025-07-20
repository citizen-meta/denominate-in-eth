require('dotenv').config();

const express = require('express');
const app = express();

const PORT = process.env.PORT || 3000;

// Middleware
app.use(express.json());

// Root Route
app.get('/', (req, res) => {
  res.send('Backend is running!');
});

// Example API Route
app.get('/api/example', (req, res) => {
  res.status(200).json({ message: 'API example route is working!' });
});

// Start the Server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
