const express = require('express');
const path = require('path');
const axios = require('axios');

const app = express();
const port = 3000;

// Set view engine
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Routes
app.get('/', async (req, res) => {
    try {
        const response = await axios.get('http://backend:5000/api');
        res.render('form', { data: response.data });
    } catch (error) {
        res.render('form', { error: 'Error fetching data from backend' });
    }
});

app.listen(port, () => {
    console.log(`Frontend server running at http://localhost:${port}`);
}); 