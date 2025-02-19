function changeBar(prev, cur) {
    const duration = 1000;
    for(let i = 0; i < 50; i++) {
        setTimeout(() =>{
            document.getElementById('progressBar').style.width = prev + (cur - prev) / 49 * i + '%';
        }, duration / 50);
    }
}

function applyChange(value) {
    let nextVal = 100, prev = parseFloat(document.getElementById('progressBar').style.width);
    if(value != -1) 
        nextVal = (value - 1) / 4 * 100;
    changeBar(prev, nextVal);
    if(value === -1) {
        document.getElementById('progressBar').innerHTML = 'Enter something';
    } else {
        document.getElementById('progressBar').innerHTML = value;
    }
    if(nextVal < 25) {
        document.getElementById('progressBar').style.backgroundColor = 'red';
    } else if(nextVal < 50) {
        document.getElementById('progressBar').style.backgroundColor = 'orange';
    } else if(nextVal < 75) {
        document.getElementById('progressBar').style.backgroundColor = 'yellow';
    } else {
        document.getElementById('progressBar').style.backgroundColor = '#B0FC38';
    }
}

function success() {
    if(document.querySelector('textarea').value === "") {
        document.querySelector('button').disabled = true;
    } else {
        document.querySelector('button').disabled = false;
    }
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').onsubmit = function(event) {
        event.preventDefault();
        const formData = new FormData(document.querySelector('form'));
        fetch('/predict', {
            'method': 'POST',
            'body': formData
        })
        .then(response => response.json())
        .then(data => {
            applyChange(data.prediction);
        });
    };
});
