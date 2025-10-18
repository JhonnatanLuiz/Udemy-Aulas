# 📋 Folha de Referência Rápida - JavaScript

## 🔤 Tipos de Dados

```javascript
// String (texto)
let texto = "Olá";
let texto2 = 'Mundo';
let template = `Olá ${texto}`;  // Template literal (com variáveis)

// Number (número)
let inteiro = 42;
let decimal = 3.14;
let negativo = -10;

// Boolean (verdadeiro/falso)
let verdadeiro = true;
let falso = false;

// Array (lista)
let array = [1, 2, 3];

// Object (objeto)
let objeto = { nome: "João", idade: 25 };

// null e undefined
let nulo = null;        // intencionalmente vazio
let indefinido = undefined;  // não atribuído
```

---

## 🔢 Operadores

### Aritméticos
```javascript
5 + 3    // 8 (soma)
5 - 3    // 2 (subtração)
5 * 3    // 15 (multiplicação)
5 / 3    // 1.666... (divisão)
5 % 3    // 2 (resto/módulo)
5 ** 3   // 125 (potência)
++5      // incremento
--5      // decremento
```

### Comparação
```javascript
5 == 5       // true (igual valor)
5 === 5      // true (igual valor E tipo)
"5" == 5     // true (conversão automática)
"5" === 5    // false (tipos diferentes)
5 !== 3      // true (diferente)
5 > 3        // true (maior)
5 < 3        // false (menor)
5 >= 3       // true (maior ou igual)
```

### Lógicos
```javascript
true && true   // true (E)
true || false  // true (OU)
!true          // false (NÃO)
```

### Atribuição
```javascript
x = 5        // atribui 5
x += 3       // x = x + 3 (x = 8)
x -= 2       // x = x - 2
x *= 2       // x = x * 2
x /= 2       // x = x / 2
```

---

## 📝 Strings

```javascript
let texto = "Olá Mundo";

// Propriedades
texto.length           // 9 (comprimento)

// Métodos
texto.toUpperCase()    // "OLÁ MUNDO"
texto.toLowerCase()    // "olá mundo"
texto.indexOf("Mundo")  // 4 (posição)
texto.substring(0, 3)  // "Olá"
texto.slice(0, 3)      // "Olá"
texto.split(" ")       // ["Olá", "Mundo"]
texto.replace("Mundo", "Pessoal")  // "Olá Pessoal"
texto.trim()           // Remove espaços
texto.includes("Mundo")  // true
texto.startsWith("Olá")  // true
texto.endsWith("Mundo")  // true
```

---

## 📊 Arrays

```javascript
let arr = [1, 2, 3, 4, 5];

// Propriedades
arr.length             // 5

// Métodos de modificação
arr.push(6)            // Adiciona no final: [1,2,3,4,5,6]
arr.pop()              // Remove último: [1,2,3,4,5]
arr.unshift(0)         // Adiciona no início: [0,1,2,3,4,5]
arr.shift()            // Remove primeiro: [1,2,3,4,5]
arr.splice(1, 2)       // Remove 2 elementos a partir do índice 1
arr.reverse()          // Inverte: [5,4,3,2,1]
arr.sort()             // Ordena
arr.fill(0)            // Preenche com valor

// Métodos de busca
arr.indexOf(3)         // 2 (índice do elemento)
arr.includes(3)        // true (elemento existe?)
arr.find(x => x > 3)   // 4 (primeiro que atende a condição)
arr.findIndex(x => x > 3)  // 3 (índice)

// Métodos de transformação
arr.map(x => x * 2)    // [2,4,6,8,10] (transforma cada um)
arr.filter(x => x > 2) // [3,4,5] (filtra)
arr.reduce((a, b) => a + b)  // 15 (soma todos)
arr.join("-")          // "1-2-3-4-5" (transforma em string)
```

---

## 🎯 Condicionais

```javascript
// IF
if (condicao) {
    // código
}

// IF-ELSE
if (condicao) {
    // código 1
} else {
    // código 2
}

// IF-ELSE IF-ELSE
if (condicao1) {
    // código 1
} else if (condicao2) {
    // código 2
} else {
    // código 3
}

// SWITCH
switch (valor) {
    case 1:
        // se valor == 1
        break;
    case 2:
        // se valor == 2
        break;
    default:
        // se nenhum acima
}

// TERNÁRIO (if-else em uma linha)
let resultado = condicao ? valorSeTrue : valorSeFalse;
// Exemplo:
let status = idade >= 18 ? "Maior de idade" : "Menor de idade";
```

---

## 🔁 Loops

```javascript
// FOR (número de vezes conhecido)
for (let i = 0; i < 5; i++) {
    console.log(i);  // 0, 1, 2, 3, 4
}

// WHILE (enquanto condição for verdadeira)
let i = 0;
while (i < 5) {
    console.log(i);
    i++;
}

// DO-WHILE (executa uma vez, depois verifica)
let j = 0;
do {
    console.log(j);
    j++;
} while (j < 5);

// FOR-OF (para cada elemento do array)
let arr = [1, 2, 3];
for (let numero of arr) {
    console.log(numero);  // 1, 2, 3
}

// FOR-IN (para cada chave do objeto)
let obj = { a: 1, b: 2 };
for (let chave in obj) {
    console.log(chave, obj[chave]);  // a 1, b 2
}

// BREAK (para o loop)
for (let i = 0; i < 10; i++) {
    if (i === 5) break;  // sai do loop
}

// CONTINUE (pula para próxima iteração)
for (let i = 0; i < 10; i++) {
    if (i === 3) continue;  // pula este
    console.log(i);
}
```

---

## 🔧 Funções

```javascript
// Função básica
function saudar(nome) {
    return "Olá, " + nome;
}
saudar("João");

// Função com múltiplos parâmetros
function somar(a, b) {
    return a + b;
}
somar(5, 3);  // 8

// Função com parâmetro padrão
function multiplicar(a, b = 2) {
    return a * b;
}
multiplicar(5);      // 10
multiplicar(5, 3);   // 15

// Função anônima
let funcao = function(x) {
    return x * 2;
};
funcao(5);  // 10

// Arrow function (ES6)
let dobrar = (x) => x * 2;
let contar = (a, b) => {
    let soma = a + b;
    return soma * 2;
};
dobrar(5);      // 10
contar(2, 3);   // 10

// Função que retorna função
function criar_multiplicador(n) {
    return (x) => x * n;
}
let multiplicarPor3 = criar_multiplicador(3);
multiplicarPor3(5);  // 15
```

---

## 🏢 Objetos

```javascript
// Criar objeto
let pessoa = {
    nome: "João",
    idade: 25,
    ativo: true
};

// Acessar propriedades
pessoa.nome          // "João"
pessoa["idade"]      // 25

// Modificar
pessoa.nome = "Maria";

// Adicionar propriedade
pessoa.email = "joao@email.com";

// Remover
delete pessoa.email;

// Verificar se existe
"nome" in pessoa     // true

// Objeto com método (função)
let calculadora = {
    somar: function(a, b) {
        return a + b;
    },
    // Arrow function também funciona
    subtrair: (a, b) => a - b
};
calculadora.somar(5, 3);  // 8

// Iterar sobre objeto
for (let chave in pessoa) {
    console.log(chave + ": " + pessoa[chave]);
}

// Objetos em array
let pessoas = [
    { nome: "João", idade: 25 },
    { nome: "Maria", idade: 30 }
];
pessoas[0].nome;  // "João"
```

---

## 📦 DOM (Document Object Model)

```javascript
// Selecionadores
document.getElementById('meuId')
document.querySelector('.classe')      // Primeiro com classe
document.querySelectorAll('.classe')   // Todos com classe
document.getElementsByClassName('classe')  // Todos com classe

// Modificar conteúdo
elemento.innerHTML = "<p>Novo conteúdo</p>";
elemento.textContent = "Apenas texto";
elemento.innerText = "Texto (visual)";

// Modificar atributos
elemento.id = "novo-id";
elemento.className = "nova-classe";
elemento.setAttribute('data-id', '123');
elemento.getAttribute('data-id');      // '123'
elemento.removeAttribute('data-id');

// Modificar estilos
elemento.style.backgroundColor = "red";
elemento.style.fontSize = "20px";
elemento.style.display = "none";

// Classes CSS
elemento.classList.add('ativa');       // Adiciona classe
elemento.classList.remove('ativa');    // Remove classe
elemento.classList.toggle('ativa');    // Alterna
elemento.classList.contains('ativa');  // Verifica

// Criar e adicionar elementos
let novo = document.createElement('div');
novo.textContent = "Novo elemento";
elemento.appendChild(novo);             // Adiciona como filho
elemento.insertBefore(novo, elemento.firstChild);  // Insere no início
elemento.removeChild(novo);             // Remove

// Eventos
elemento.onclick = function() { };
elemento.addEventListener('click', function() { });
elemento.removeEventListener('click', funcao);

// Propriedades úteis
elemento.parentElement              // Elemento pai
elemento.children                   // Filhos (elementos)
elemento.childNodes                 // Filhos (nós)
elemento.nextSibling               // Próximo elemento
elemento.previousSibling           // Elemento anterior
elemento.firstChild                // Primeiro filho
elemento.lastChild                 // Último filho
```

---

## ⏱️ Funções Especiais

```javascript
// setTimeout (executa após delay)
setTimeout(function() {
    console.log("Executado após 2 segundos");
}, 2000);

// setInterval (executa repetidamente)
let intervalo = setInterval(function() {
    console.log("A cada segundo");
}, 1000);
clearInterval(intervalo);  // Para

// console methods
console.log("Mensagem");
console.error("Erro");
console.warn("Aviso");
console.table({a: 1, b: 2});
console.time("timer");
// ... código ...
console.timeEnd("timer");

// Parse/Stringify JSON
let json = JSON.stringify({nome: "João", idade: 25});
let obj = JSON.parse('{"nome":"João","idade":25}');

// Eval (CUIDADO - perigoso!)
eval("5+3");  // 8

// isNaN, isFinite, parseInt, parseFloat
isNaN(5)              // false
isFinite(5)           // true
parseInt("5px")       // 5
parseFloat("3.14abc") // 3.14
Number("5")           // 5
String(5)             // "5"
Boolean(1)            // true
```

---

## 🚨 Tratamento de Erros

```javascript
try {
    // código que pode gerar erro
    riscar();
} catch (erro) {
    // executado se houver erro
    console.error(erro.message);
} finally {
    // executado sempre
    console.log("Fim");
}

// Lançar erro
throw new Error("Mensagem de erro");

// Tipos de erros
new Error()
new TypeError()
new ReferenceError()
new SyntaxError()
```

---

## 📱 Eventos Comuns

```javascript
// Mouse
'click'          // Clique
'dblclick'       // Duplo clique
'mouseenter'     // Mouse entra
'mouseleave'     // Mouse sai
'mousemove'      // Mouse se move
'mousedown'      // Botão pressionado
'mouseup'        // Botão solto

// Teclado
'keydown'        // Tecla pressionada
'keyup'          // Tecla solta
'keypress'       // Tecla pressionada e solta

// Formulário
'change'         // Valor mudou
'input'          // Valor digitado
'focus'          // Campo focado
'blur'           // Campo desfocado
'submit'         // Formulário enviado

// Janela
'load'           // Página carregou
'unload'         // Página vai descarregar
'scroll'         // Página rolada
'resize'         // Janela redimensionada
```

---

## 📚 Estrutura Típica de um Script

```javascript
// 1. Esperar página carregar
document.addEventListener('DOMContentLoaded', function() {
    
    // 2. Selecionar elementos
    let botao = document.getElementById('meuBotao');
    let resultado = document.getElementById('resultado');
    
    // 3. Definir funções
    function calcular() {
        let valor = 5 + 3;
        resultado.textContent = valor;
    }
    
    // 4. Adicionar listeners
    botao.addEventListener('click', calcular);
    
});
```

---

**Dica**: Salve esta folha de referência e consulte sempre que precisar! 📖
