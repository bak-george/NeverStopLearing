const btn = document.querySelector('#v2')

btn.onclick = function() {
    console.log("You clicked me")
    console.log("I hope it works")
}

function scream() {
    console.log("Hey screaming")
}

btn.onmouseenter = scream;

document.querySelector('h1').onclick = function() {
    alert('you clicked the h1!')
}

const btn3 = document.querySelector('#v3');

btn3.addEventListener('click', function() {
    alert("CLICKED");
})

function twist() {
    console.log('twist');
}

function shout() {
    console.log('shout');
}

const tasButton = document.querySelector('#tas');

tasButton.addEventListener('click', twist, {once: true})
tasButton.addEventListener('click', shout)

