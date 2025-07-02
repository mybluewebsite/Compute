// static/js/main.js
document.addEventListener('DOMContentLoaded', () => {
    const myButton = document.getElementById('myButton');

    if (myButton) {
        myButton.addEventListener('click', () => {
            alert('Button clicked from main.js!');
            console.log('Button was clicked!');
        });
    }

    // Example of a simple function
    function greet(name) {
        console.log(`Hello, ${name}!`);
    }

    greet('World');
});