var altura = 0;
var largura = 0;
var vidas = 1;
var tempo = 15;
var pontos = 0;
var isPaused = false;
var gameInterval;
var timerInterval;

var criaMosquitoTempo = 1500;

var nivel = window.location.search;
nivel = nivel.replace('?', '');

if(nivel === 'facil') {
    criaMosquitoTempo = 1500;
} else if(nivel === 'medio') {
    criaMosquitoTempo = 1000;
} else if(nivel === 'dificil') {
    criaMosquitoTempo = 750;
}

function ajustaTamanhoPalcoJogo() {
    altura = window.innerHeight;
    largura = window.innerWidth;
    console.log(largura, altura);
}

ajustaTamanhoPalcoJogo();

// Countdown Logic
function iniciarContagemRegressiva() {
    var count = 3;
    var overlay = document.getElementById('countdown-overlay');
    
    var countInterval = setInterval(function() {
        overlay.innerHTML = count;
        count--;
        
        if(count < 0) {
            clearInterval(countInterval);
            overlay.innerHTML = "GO!";
            setTimeout(function() {
                overlay.style.display = 'none';
                startGame();
            }, 500);
        }
    }, 1000);
}

function startGame() {
    document.getElementById('cronometro').innerHTML = tempo;
    
    timerInterval = setInterval(function() {
        if(!isPaused) {
            tempo -= 1;
            if (tempo < 0) {
                endGame('vitoria');
            } else {
                document.getElementById("cronometro").innerHTML = tempo;
            }
        }
    }, 1000);

    gameInterval = setInterval(function() {
        if(!isPaused) {
            posicaoRandomica();
        }
    }, criaMosquitoTempo);
}

function togglePause() {
    isPaused = !isPaused;
    var btn = document.getElementById('btn-pause');
    if(isPaused) {
        btn.innerHTML = "RESUME (P)";
        btn.style.background = "#28a745";
        btn.style.color = "white";
    } else {
        btn.innerHTML = "PAUSE (P)";
        btn.style.background = "#ffc107";
        btn.style.color = "black";
    }
}

// Keyboard shortcut for pause
document.addEventListener('keydown', function(event) {
    if(event.key === 'p' || event.key === 'P') {
        togglePause();
    }
});

function endGame(type) {
    clearInterval(timerInterval);
    clearInterval(gameInterval);
    
    // Save High Score
    var currentHighScore = localStorage.getItem('highscore_' + nivel) || 0;
    if(pontos > currentHighScore) {
        localStorage.setItem('highscore_' + nivel, pontos);
    }
    
    if(type === 'vitoria') {
        window.location.href = "vitoria.html?score=" + pontos;
    } else {
        window.location.href = "fim_de_jogo.html?score=" + pontos;
    }
}

function posicaoRandomica() {
    // Remove previous mosquito
    if (document.getElementById("mosquito")) {
        document.getElementById("mosquito").remove();

        if (vidas > 3) {
            endGame('gameover');
        } else {
            document.getElementById("v" + vidas).src = "imagens/coracao_vazio.png";
            vidas++;
        }
    }

    var posicaoX = Math.floor(Math.random() * largura) - 90;
    
    // Ajuste para não aparecer atrás do painel (aprox 100px de altura)
    var minY = 110;
    var maxY = altura - 90;
    if (maxY < minY) maxY = minY; // Proteção para telas muito pequenas
    
    var posicaoY = Math.floor(Math.random() * (maxY - minY)) + minY;

    posicaoX = posicaoX < 0 ? 0 : posicaoX;
    // posicaoY já está calculado com o offset mínimo

    // Create HTML element
    var mosquito = document.createElement("img");
    
    // Golden Mosquito Logic (10% chance)
    var isGolden = Math.random() < 0.1;
    
    mosquito.src = "imagens/mosquito.png";
    mosquito.className = tamanhoAleatorio() + " " + ladoAleatorio() + " animate-pop";
    
    if(isGolden) {
        mosquito.classList.add('mosquito-golden');
        mosquito.dataset.points = 3;
    } else {
        mosquito.dataset.points = 1;
    }
    
    mosquito.style.left = posicaoX + "px";
    mosquito.style.top = posicaoY + "px";
    mosquito.style.position = "absolute";
    mosquito.id = "mosquito";
    
    mosquito.onclick = function (e) {
        clickMosquito(this, e);
    }

    document.body.appendChild(mosquito);
}

function clickMosquito(element, event) {
    if(isPaused) return;
    
    var pointsToAdd = parseInt(element.dataset.points);
    pontos += pointsToAdd;
    document.getElementById('score').innerHTML = pontos;
    
    // Play funny sound
    var audio = new Audio('sons/slap.mp3');
    audio.play().catch(function(error) {
        console.log("Adicione um arquivo 'slap.mp3' na pasta 'sons' para ouvir o som!");
    });

    spawnHitEffect(event.clientX, event.clientY, pointsToAdd);
    
    element.remove();
}

function spawnHitEffect(x, y, points) {
    var hit = document.createElement("div");
    hit.className = "hit-effect";
    hit.innerHTML = points > 1 ? "TRIPLE!" : "POW!";
    hit.style.left = x + "px";
    hit.style.top = y + "px";
    document.body.appendChild(hit);
    
    setTimeout(function() {
        hit.remove();
    }, 500);
}

function tamanhoAleatorio() { 
    var classe = Math.floor(Math.random() * 3);

    switch(classe) {
        case 0:
            return "mosquito1";
        case 1:
            return "mosquito2";
        case 2:
            return "mosquito3";
    }
}

function ladoAleatorio() {
    var classe = Math.floor(Math.random() * 2);
    switch(classe) {
        case 0:
            return "ladoA";
        case 1:
            return "ladoB";
    }
}





