[]

document.addEventListener("DOMContentLoaded", () => {



  /// local storage

  if (!localStorage.getItem('counter')) {
    localStorage.setItem('counter', 0);
  }

  // blokowanie przycisku submit gdy pole jest puste

  document.querySelector('#submit-fix').disabled = true;

  document.querySelector('#zadanie').onkeyup = () => {
    document.querySelector('#submit-fix').disabled = document.querySelector('#zadanie').value.length < 1
  }

  // dodawanie zadania do listy

  document.querySelector('form').onsubmit = () => {
    const zadanie = document.querySelector('#zadanie').value;
    const listowy = document.createElement('li');
    listowy.innerHTML = zadanie;
    document.querySelector('#zadania').append(listowy);
    document.querySelector('#zadanie').value = '';

    return false;
  }


  // zmiana koloru paska po wybraniu opcji z listy

  document.querySelector('select').onchange = function() {
    document.querySelector('select').style.backgroundColor = this.value;
  }

  // zmiana koloru diody i licznika po kliknieciu na przycisk


  document.querySelectorAll('#licznik').innerHTML = Number(localStorage.getItem('counter'));

  const buttons = document.querySelectorAll('button');
  var counter = Number(localStorage.getItem('counter'));

  function hello() {
    counter = counter + 1;
    localStorage.setItem('counter', counter);
    document.querySelector('#licznik').innerHTML = counter;
    document.querySelector('#dioda').style.backgroundColor = `rgb(${counter}, 0, 0)`;
    document.querySelector('#dioda').innerHTML = this.dataset.color;

  }

  buttons.forEach(i => {
    i.addEventListener('click', hello);
  });



});