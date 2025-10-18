# 💡 Exemplos Práticos - Conceitos JavaScript

## 📍 Exemplos Interativos que Você Pode Testar

Copie e cole qualquer um desses exemplos em um arquivo `.html` e abra no navegador!

---

## Exemplo 1: Entendendo `var` vs `let` vs `const`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Variáveis em JavaScript</title>
</head>
<body>
    <h1>Abra o Console (F12) para ver os resultados</h1>

    <script>
        // VAR: Escopo global/função (não recomendado em código moderno)
        var numero1 = 5;
        console.log("VAR numero1: " + numero1);

        // LET: Escopo de bloco (recomendado)
        let numero2 = 10;
        console.log("LET numero2: " + numero2);

        // CONST: Constante, não pode ser mudado
        const numero3 = 15;
        console.log("CONST numero3: " + numero3);

        // Teste: Tentar mudar const gera erro
        // numero3 = 20;  // ERRO!

        // Escopo de bloco (mostra diferença entre var e let)
        if (true) {
            var x = 1;      // x fica global
            let y = 2;      // y fica local ao if
            const z = 3;    // z fica local ao if
        }

        console.log("x fora do if: " + x);      // 1 (vazou!)
        console.log("y fora do if: " + y);      // ERRO! y não existe
    </script>
</body>
</html>
```

---

## Exemplo 2: Strings vs Números

```html
<!DOCTYPE html>
<html>
<body>
    <h1>Strings vs Números</h1>
    <p id="resultado"></p>

    <script>
        // NÚMERO
        let num1 = 5;
        let num2 = 3;
        console.log(num1 + num2);  // 8 (ADIÇÃO)

        // STRING (texto com aspas)
        let str1 = "5";
        let str2 = "3";
        console.log(str1 + str2);  // "53" (CONCATENAÇÃO!)

        // MISTURA: conversão automática (cuidado!)
        let resultado1 = 5 + "3";
        console.log(resultado1);   // "53" (virou string!)

        let resultado2 = "5" + 3;
        console.log(resultado2);   // "53" (ainda string!)

        // SOLUÇÃO: Converter explicitamente
        let resultado3 = Number("5") + 3;
        console.log(resultado3);   // 8 (soma corretamente)

        // Exibir no HTML
        document.getElementById('resultado').innerHTML = 
            "5 + 3 = " + (5 + 3) + "<br>" +
            "'5' + '3' = " + ("5" + "3");
    </script>
</body>
</html>
```

---

## Exemplo 3: Condicionais (if/else if/else)

```html
<!DOCTYPE html>
<html>
<body>
    <h1>Sistema de Notas</h1>
    <input type="number" id="nota" placeholder="Digite uma nota (0-100)" />
    <button onclick="verificarNota()">Verificar Nota</button>
    <p id="resultado"></p>

    <script>
        function verificarNota() {
            // Pegar valor do input e converter para número
            let nota = Number(document.getElementById('nota').value);
            let resultado;

            // CONDICIONAL: verifica a nota
            if (nota >= 90) {
                resultado = "A - Excelente! 🌟";
            } else if (nota >= 80) {
                resultado = "B - Muito bom! 👍";
            } else if (nota >= 70) {
                resultado = "C - Bom! ✓";
            } else if (nota >= 60) {
                resultado = "D - Satisfatório";
            } else if (nota >= 0) {
                resultado = "F - Reprovado ✗";
            } else {
                resultado = "Nota inválida!";
            }

            document.getElementById('resultado').innerHTML = resultado;
        }
    </script>
</body>
</html>
```

---

## Exemplo 4: Operadores Lógicos (&&, ||, !)

```html
<!DOCTYPE html>
<html>
<body>
    <h1>Operadores Lógicos</h1>
    <p id="resultado"></p>

    <script>
        let idade = 25;
        let temCarteira = true;

        // OPERADOR &&: AND (E)
        // Ambas precisam ser verdadeiras
        if (idade >= 18 && temCarteira) {
            console.log("Pode dirigir ✓");
        }

        // OPERADOR ||: OR (OU)
        // Pelo menos uma precisa ser verdadeira
        let temCarteira2 = false;
        let temAutorizacaoPais = true;

        if (temCarteira2 || temAutorizacaoPais) {
            console.log("Tem permissão para algo ✓");
        }

        // OPERADOR !: NOT (NÃO)
        // Inverte o valor booleano
        if (!temCarteira2) {
            console.log("Não tem carteira");
        }

        // EXEMPLO COMPLEXO
        let ehFimDeSemana = true;
        let temDinheiro = true;
        let temTempo = false;

        if ((ehFimDeSemana || temDinheiro) && temTempo) {
            console.log("Pode sair!");
        } else {
            console.log("Não pode sair");
        }

        // Exibir resultado
        document.getElementById('resultado').innerHTML =
            "<b>Operadores Lógicos:</b><br>" +
            "idade >= 18 && temCarteira = " + (idade >= 18 && temCarteira) + "<br>" +
            "!temCarteira2 = " + (!temCarteira2) + "<br>" +
            "Resultado final = " + ((ehFimDeSemana || temDinheiro) && temTempo);
    </script>
</body>
</html>
```

---

## Exemplo 5: Loops (for, while)

```html
<!DOCTYPE html>
<html>
<body>
    <h1>Loops em JavaScript</h1>
    <p id="resultado"></p>

    <script>
        let saida = "";

        // LOOP FOR: executa X vezes (conhecido)
        // for (início; condição; incremento)
        console.log("--- FOR LOOP ---");
        for (let i = 0; i < 5; i++) {
            console.log("Iteração " + i);
            saida += "i = " + i + "<br>";
        }

        // FOR tabuada
        console.log("--- TABUADA DO 5 ---");
        for (let i = 1; i <= 10; i++) {
            console.log("5 x " + i + " = " + (5 * i));
        }

        // WHILE LOOP: enquanto condição for verdadeira
        console.log("--- WHILE LOOP ---");
        let contador = 0;
        while (contador < 3) {
            console.log("Contador: " + contador);
            contador++;  // incrementar
        }

        // FOR com array (lista)
        console.log("--- FOR COM ARRAY ---");
        let frutas = ["maçã", "banana", "laranja"];
        for (let i = 0; i < frutas.length; i++) {
            console.log(frutas[i]);
            saida += "Fruta: " + frutas[i] + "<br>";
        }

        document.getElementById('resultado').innerHTML = saida;
    </script>
</body>
</html>
```

---

## Exemplo 6: Arrays (Listas)

```html
<!DOCTYPE html>
<html>
<body>
    <h1>Arrays em JavaScript</h1>
    <p id="resultado"></p>

    <script>
        // CRIAR ARRAY
        let numeros = [1, 2, 3, 4, 5];
        let nomes = ["João", "Maria", "Pedro"];
        let misto = [1, "texto", true, 3.14];

        // ACESSAR ELEMENTOS (começa em 0!)
        console.log(numeros[0]);    // 1
        console.log(nomes[1]);      // Maria
        console.log(numeros.length); // 5 (tamanho do array)

        // ADICIONAR ELEMENTO
        numeros.push(6);            // Adiciona no final
        console.log(numeros);       // [1, 2, 3, 4, 5, 6]

        // REMOVER ELEMENTO
        numeros.pop();              // Remove o último
        console.log(numeros);       // [1, 2, 3, 4, 5]

        // PROCURAR ELEMENTO
        let indice = nomes.indexOf("Maria");  // 1
        console.log("Índice de Maria: " + indice);

        // FILTRAR ARRAY
        let maioresQue2 = numeros.filter(function(num) {
            return num > 2;
        });
        console.log("Maiores que 2: " + maioresQue2);  // [3, 4, 5]

        // MAPEAR ARRAY (transformar cada elemento)
        let dobrados = numeros.map(function(num) {
            return num * 2;
        });
        console.log("Dobrados: " + dobrados);  // [2, 4, 6, 8, 10]

        // EXIBIR RESULTADO
        document.getElementById('resultado').innerHTML =
            "<b>Array Original:</b> " + numeros + "<br>" +
            "<b>Nomes:</b> " + nomes + "<br>" +
            "<b>Maiores que 2:</b> " + maioresQue2 + "<br>" +
            "<b>Dobrados:</b> " + dobrados;
    </script>
</body>
</html>
```

---

## Exemplo 7: Objetos

```html
<!DOCTYPE html>
<html>
<body>
    <h1>Objetos em JavaScript</h1>
    <p id="resultado"></p>

    <script>
        // CRIAR OBJETO
        let pessoa = {
            nome: "João",
            idade: 25,
            email: "joao@email.com",
            ativo: true
        };

        // ACESSAR PROPRIEDADES
        console.log(pessoa.nome);      // João
        console.log(pessoa["idade"]);  // 25

        // MODIFICAR PROPRIEDADES
        pessoa.idade = 26;
        console.log(pessoa.idade);     // 26

        // ADICIONAR PROPRIEDADE
        pessoa.telefone = "999999999";

        // REMOVER PROPRIEDADE
        delete pessoa.email;

        // OBJETO COM MÉTODO (função dentro do objeto)
        let calculadora = {
            nome: "Calc",
            somar: function(a, b) {
                return a + b;
            },
            subtrair: function(a, b) {
                return a - b;
            }
        };

        console.log(calculadora.somar(5, 3));      // 8
        console.log(calculadora.subtrair(5, 3));   // 2

        // ITERAR SOBRE OBJETO
        let saida = "<b>Dados da Pessoa:</b><br>";
        for (let chave in pessoa) {
            saida += chave + ": " + pessoa[chave] + "<br>";
        }

        document.getElementById('resultado').innerHTML = saida;
    </script>
</body>
</html>
```

---

## Exemplo 8: DOM Manipulation (Modificar HTML)

```html
<!DOCTYPE html>
<html>
<body>
    <h1>Manipulação do DOM</h1>
    <div id="container"></div>
    <button onclick="adicionar()">Adicionar Item</button>
    <button onclick="limpar()">Limpar</button>

    <script>
        // ACESSAR ELEMENTO
        let container = document.getElementById('container');

        // MODIFICAR TEXTO
        container.innerHTML = "<p>Olá, DOM!</p>";

        // MODIFICAR ATRIBUTO
        container.style.backgroundColor = "#f0f0f0";
        container.style.padding = "20px";
        container.style.borderRadius = "10px";

        // FUNÇÃO PARA ADICIONAR ITEM
        function adicionar() {
            // Criar novo elemento
            let novo = document.createElement('p');
            novo.innerHTML = "Item adicionado em " + new Date();
            novo.style.color = "blue";

            // Adicionar ao container
            container.appendChild(novo);
        }

        // FUNÇÃO PARA LIMPAR
        function limpar() {
            container.innerHTML = "";
        }

        // ADICIONAR CLASSE CSS
        container.classList.add("destaque");  // Adiciona classe
        container.classList.remove("destaque"); // Remove classe
        container.classList.toggle("destaque"); // Alterna classe

        // EVENTOS
        let botao = document.querySelector('button');
        botao.addEventListener('click', function() {
            console.log("Botão clicado!");
        });
    </script>
</body>
</html>
```

---

## Exemplo 9: Try/Catch (Tratamento de Erros)

```html
<!DOCTYPE html>
<html>
<body>
    <h1>Tratamento de Erros</h1>
    <p id="resultado"></p>

    <script>
        // TRY: tenta executar o código
        // CATCH: se houver erro, executa isto
        try {
            let resultado = eval("5 + 3");
            console.log("Resultado: " + resultado);

            // Isto gera erro
            let valor = funcaoQueNaoExiste();
        } catch (erro) {
            console.error("Erro capturado: " + erro.message);
        } finally {
            // FINALLY: executa sempre, com ou sem erro
            console.log("Fim do try/catch");
        }

        // VALIDAÇÃO COM TRY/CATCH
        function dividir(a, b) {
            try {
                if (b === 0) {
                    throw new Error("Não pode dividir por zero!");
                }
                return a / b;
            } catch (erro) {
                return "Erro: " + erro.message;
            }
        }

        console.log(dividir(10, 2));  // 5
        console.log(dividir(10, 0));  // Erro: Não pode dividir por zero!

        // Exibir resultado
        document.getElementById('resultado').innerHTML =
            "Veja o Console (F12) para ver os resultados do Try/Catch";
    </script>
</body>
</html>
```

---

## Exemplo 10: Callbacks e Funções como Parâmetros

```html
<!DOCTYPE html>
<html>
<body>
    <h1>Callbacks em JavaScript</h1>
    <p id="resultado"></p>

    <script>
        // FUNÇÃO QUE ACEITA UMA FUNÇÃO COMO PARÂMETRO (callback)
        function processar(numero, funcao) {
            console.log("Processando: " + numero);
            return funcao(numero);
        }

        // DEFINE FUNÇÕES
        function dobrar(x) {
            return x * 2;
        }

        function triplicar(x) {
            return x * 3;
        }

        // USA CALLBACKS
        let resultado1 = processar(5, dobrar);      // 10
        let resultado2 = processar(5, triplicar);   // 15

        console.log("Resultado 1: " + resultado1);
        console.log("Resultado 2: " + resultado2);

        // CALLBACK COM FUNÇÕES ANÔNIMAS (sem nome)
        let resultado3 = processar(5, function(x) {
            return x * x;  // quadrado
        });
        console.log("Quadrado: " + resultado3);  // 25

        // CASO PRÁTICO: Simulando uma operação assíncrona
        function buscarDados(id, callback) {
            console.log("Buscando dados do usuário " + id + "...");
            
            // Simular delay de 2 segundos
            setTimeout(function() {
                let usuario = { id: id, nome: "João", email: "joao@email.com" };
                callback(usuario);  // Chama a função de callback
            }, 2000);
        }

        buscarDados(1, function(usuario) {
            console.log("Dados recebidos: ", usuario);
        });

        document.getElementById('resultado').innerHTML =
            "Resultado 1: " + resultado1 + "<br>" +
            "Resultado 2: " + resultado2 + "<br>" +
            "Quadrado: " + resultado3;
    </script>
</body>
</html>
```

---

## 🎯 Como Usar Estes Exemplos

1. **Crie um arquivo** chamado `exemplo.html`
2. **Copie e cole** qualquer um dos códigos acima
3. **Abra no navegador** (duplo clique no arquivo)
4. **Abra o Console** pressionando `F12` → Aba "Console"
5. **Veja os resultados** do `console.log()`
6. **Modifique valores** e teste!

---

## ✨ Próximo Passo

Agora que entende estes conceitos:
- 🔄 Refatore a calculadora para usar **objetos** em vez de parâmetros
- 🎨 Adicione **validação** com try/catch
- 📱 Use **addEventListener** em vez de onclick inline
- 🚀 Crie um arquivo `.js` separado

---

**Bom aprendizado! Continue praticando!** 🚀
