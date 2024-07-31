const express = require('express');
// const bodyParser = require('body-parser');
const CORS = require('cors');
const dotenv = require('dotenv').config();
const {errorHandler} = require('./middleware/errorMiddleware')

const app = express()
const PORT = process.env.PORT || 8000;

//Middleware
// app.use(bodyParser.json());
app.use(CORS());
app.use(express.json());
app.use(express.urlencoded({extended: false}));

app.use('/api/main', require('./api/main'))

app.use(errorHandler)
// const routes = require('./api/main');
// app.use('/', routes);

// const posts = require('./routes/api/posts');
// app.use('/api/posts', posts);

app.listen(PORT, ()=>{
    console.log(`API Listening on ${PORT}...`);
});