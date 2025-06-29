

document.addEventListener("DOMContentLoaded", () => {




  /// pozycja gracza

  x = 0;
  y = 0;
  speedx = 10;
  speedy = 10;



  /// dodanie strzalek robiacych rzeczy

  document.addEventListener('keydown', function(e) {
    switch (e.key.toLowerCase()) {
      case 'w':
        console.log('Up');
        y = y - 10;
        break;
      case 'a':
        console.log('Left');
        x = x - 10;
        break;
      case 's':
        console.log('Down');
        y = y + 10;
        break;
      case 'd':
        console.log('Right');
        x = x + 10;
        break;
    }
    document.querySelector('#player').style.left = x + 'px';
    document.querySelector('#player').style.top = y + 'px';
    document.querySelector('#stats').innerHTML = 'Start game' + ' x = ' + x + ' y = ' + y;

  });


});