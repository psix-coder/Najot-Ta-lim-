document.addEventListener('DOMContentLoaded', function() {
    const changeColorButton = document.getElementById('changeColorButton');
    
    changeColorButton.addEventListener('click', function() {
        document.body.style.backgroundColor = document.body.style.backgroundColor === 'lightblue' ? '#f4f4f4' : 'lightblue';
    });
});
