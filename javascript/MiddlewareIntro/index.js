const express = require('express');
const app = express();
const morgan = require('morgan');

app.use(morgan('common'));
app.use((req, res, next) => {
    console.log(req.method)
})

app.get('/', (req, res) =>{
    res.send('home page')
})

app.get('/dogs', (req, res) => {
    res.send('woof woof')
})

app.listen(3000, ()=> {
    console.log('App is running on localhost:3000')
})