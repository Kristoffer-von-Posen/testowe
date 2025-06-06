

document.addEventListener("DOMContentLoaded", function() {

  var counter = 100;
  function hello() {
    counter = counter + 1;
    document.querySelector('#licznik').innerHTML = counter;
    document.querySelector('#dioda').style.backgroundColor = `rgb(${counter}, 0, 0)`;
  }

  document.querySelector('button').onclick = hello;

});