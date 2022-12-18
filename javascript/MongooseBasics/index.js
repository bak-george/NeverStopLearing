const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost:27017/movieApp')
    .then(() => {
        console.log("Connection Open")
    })
    .catch(err => {
        console.log("oh no error!!!")
        console.log(err)
    })

const movieSchema = new mongoose.Schema({
    title: String, 
    year: Number,
    score: Number, 
    rating: String
}); 

const Movie = mongoose.model('Movie', movieSchema)
/* 
Movie.insertMany([
    {title: 'Amelie', year: 2001, score: 8.3, rating: 'R'},
    {title: 'Alien', year: 1979, score: 8.1, rating: 'R'},
    {title: 'The Iron Giant', year: 1999, score: 7.5, rating: 'PG'}
])
    .then(data => {
        console.log('IT WORKED!')
        console.log(data);
    })
 */