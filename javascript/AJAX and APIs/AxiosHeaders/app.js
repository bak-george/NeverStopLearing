const jokes = document.querySelector('#jokes');

const getDadJoke = async() => {
    const config = {headers: {Accept: 'application/json'}}
    const res = await axios.get('https://icanhazdadjoke.com', config); 
    console.log(res.data.joke);
    const newLI = document.createElement('LI');
    newLI.append(res.data.joke);
    jokes.append(newLI)
}
