"use strict"

let logo = document.querySelector('.logotype');
let rotateClass = 'rotate';
let changer = 1;

let progress = null;

logo.addEventListener('mouseout', function () {

    if (logo.style.transform != `rotate(0deg)`) {
        logo.classList.remove('rotate');
        clearInterval(progress);
    }
});

logo.addEventListener('mouseenter', function (event) {
    logo.classList.add(rotateClass);
    console.log(event);

    progress = setInterval(changeDegree, 1);

});

function changeDegree() {
    logo.style.transform = `rotate(${changer + 1}deg)`;
    changer += 1;

}



let menu = document.querySelector('.menu-burger')
let menuBar = document.querySelector('.menu-bar');
let menuText = document.querySelector('.menu-text');
let menuItem = document.querySelector('.menu-item');


menuBar.addEventListener('click', function () {
    menuBar.classList.toggle('change');
    menuText.classList.toggle('change');
    menuItem.classList.toggle('change');

});

