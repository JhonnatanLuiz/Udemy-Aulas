# 📚 Guia de Aprendizado - Calculadora JavaScript

## 🎯 O que você vai aprender neste projeto

Este projeto de calculadora demonstra os **conceitos fundamentais de JavaScript**:

---

## 1️⃣ **HTML & Estrutura**

### Meta Tags (Head)
```html
<meta charset="utf-8" />
```
- **charset**: Define o tipo de caractere que o navegador deve usar
- **utf-8**: Suporta acentuação e caracteres especiais (ç, ã, é, etc)

### Viewport (Responsividade)
```html
<meta name="viewport" content="width=device-width, initial-scale=1" />
```
- **width=device-width**: A página adapta-se à largura da tela do dispositivo
- **initial-scale=1**: Zoom inicial é 100%

### CDN (Content Delivery Network)
```html
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" />
```
- **CDN**: Carrega bibliotecas de um servidor remoto
- **Bootstrap**: Framework CSS que fornece componentes prontos (botões, grid, etc)
- **integrity**: Valida se o arquivo não foi alterado

---

## 2️⃣ **CSS - Selecionando Elementos**

### Classes CSS
```css
.calculadora {
  margin-top: 40px;        /* Espaçamento acima */
  border: solid 1px #000;  /* Borda sólida, preta, 1 pixel */
  padding: 20px;           /* Espaçamento interno */
  background-color: #2E2E2E; /* Cor de fundo (hexadecimal) */
  border-radius: 10px;     /* Cantos arredondados */
  box-shadow: 1px 1px 5px #000; /* Sombra: x, y, desfoque, cor */
}
```

### Especificidade CSS
- **Inline** (style=""): Alta prioridade
- **<style>**: Média prioridade
- **<link> externo**: Baixa prioridade

---

## 3️⃣ **Bootstrap Grid System**

```html
<div class="container">      <!-- Container responsivo -->
  <div class="row">          <!-- Linha com 12 colunas -->
    <div class="col">        <!-- Coluna (divide em partes iguais) -->
      <!-- Conteúdo -->
    </div>
  </div>
</div>
```

### Classes Úteis do Bootstrap
| Classe | O que faz |
|--------|----------|
| `.container` | Container responsivo com max-width |
| `.row` | Linha (usa Flexbox) |
| `.col` | Coluna que divide espaço |
| `.d-flex` | Display: flex |
| `.justify-content-center` | Alinha ao centro (eixo X) |
| `.btn` | Estilo básico de botão |
| `.btn-dark` | Botão com fundo preto |
| `.btn-lg` | Botão grande |

---

## 4️⃣ **HTML - Atributos Importantes**

### Input (Campo de texto)
```html
<input 
  id="resultado"           <!-- Identificador único (usado no JS) -->
  type="text"              <!-- Tipo: texto -->
  class="form-control"     <!-- Classe Bootstrap -->
  placeholder="0"          <!-- Texto quando vazio -->
  readonly                 <!-- Não permite edição direta -->
/>
```

### Button (Botão)
```html
<button 
  onclick="calcular('valor', '5')"  <!-- Função chamada ao clicar -->
  type="button"                      <!-- Tipo: botão (não submete) -->
  class="btn btn-dark btn-lg"        <!-- Classes de estilo -->
>
  5                                  <!-- Texto do botão -->
</button>
```

---

## 5️⃣ **JavaScript - Conceitos Principais**

### 🔹 Variáveis
```javascript
var resultado = 5;        // var = escopo global/função
let resultado = 5;        // let = escopo bloco (ES6)
const RESULTADO = 5;      // const = constante (não muda)
```

### 🔹 String (Texto)
```javascript
"5" + "3"  // = "53" (concatenação, não adição!)
5 + 3      // = 8 (adição matemática)
```

### 🔹 Operadores Lógicos
```javascript
valor === 'C'    // === igual (RIGOROSO - verifica tipo também)
valor == 'C'     // == igual (FLEXÍVEL - pode converter tipo)
valor !== 'C'    // !== diferente
valor > 5        // maior que
valor < 5        // menor que
valor && valor2  // AND (E) - ambas verdadeiras?
valor || valor2  // OR (OU) - uma delas verdadeira?
```

### 🔹 Condicionais
```javascript
// IF (Se)
if (tipo === 'acao') {
  // código executado se verdadeiro
}

// IF-ELSE (Se-Senão)
if (tipo === 'acao') {
  // código se verdadeiro
} else {
  // código se falso
}

// IF-ELSE IF (Se-Senão Se)
if (tipo === 'acao') {
  // ...
} else if (tipo === 'valor') {
  // ...
} else {
  // ...
}
```

### 🔹 Objetos e DOM (Document Object Model)
```javascript
document                              // Objeto que representa a página
document.getElementById('resultado')  // Encontra elemento por ID
.value                                // Propriedade que armazena o valor
= ''                                  // Atribui valor vazio
+= valor                              // Concatena e atribui
```

### 🔹 Funções
```javascript
// Sintaxe:
function nomeFuncao(parametro1, parametro2) {
  // código
  return resultado;  // opcional
}

// Chamada:
nomeFuncao('acao', 'C');  // passa 'acao' para parametro1, 'C' para parametro2
```

### 🔹 Especial: eval()
```javascript
var expressao = "5+3";
var resultado = eval(expressao);  // eval calcula a string e retorna 8
console.log(resultado);            // exibe 8
```

⚠️ **Aviso**: `eval()` é perigoso em produção (risco de segurança), mas funciona para este exemplo educacional!

### 🔹 Console (Debugging)
```javascript
console.log("mensagem");      // Exibe mensagem
console.error("erro");        // Exibe erro em vermelho
console.warn("aviso");        // Exibe aviso em amarelo
console.table({a: 1, b: 2});  // Exibe dados em tabela
```

---

## 6️⃣ **Fluxo de Execução da Calculadora**

### Passo 1: Usuário clica no botão "5"
```html
<button onclick="calcular('valor', '5')">5</button>
```

### Passo 2: Função `calcular()` é chamada
```javascript
calcular('valor', '5')  // tipo = 'valor', valor = '5'
```

### Passo 3: Avalia as condições
```javascript
if (tipo === 'acao') {
  // Pula, pois tipo = 'valor'
} else if (tipo === 'valor') {
  // ENTRA AQUI!
  document.getElementById('resultado').value += '5';
  // Se tinha vazio, agora tem "5"
  // Se tinha "3", agora tem "35"
}
```

### Passo 4: Display atualiza
- O navegador renderiza o novo valor no input

---

## 7️⃣ **Casos de Uso Completos**

### Caso 1: Cálculo Simples
```
1. Clica "5" → Input: "5"
2. Clica "+" → Input: "5+"
3. Clica "3" → Input: "5+3"
4. Clica "=" → eval("5+3") = 8 → Input: "8"
```

### Caso 2: Limpar
```
1. Input tem "5+3"
2. Clica "C" → Input limpo (vazio)
```

### Caso 3: Decimal
```
1. Clica "3" → Input: "3"
2. Clica "." → Input: "3."
3. Clica "5" → Input: "3.5"
```

---

## 8️⃣ **Boas Práticas Aprendidas**

✅ **Use `id` para elementos únicos** que JavaScript precisa acessar
```html
<input id="resultado" />
```

✅ **Use `class` para estilos CSS reutilizáveis**
```html
<button class="btn btn-dark">Click</button>
```

✅ **Use `readonly` em inputs que não devem ser editados manualmente**
```html
<input readonly />
```

✅ **Use `console.log()` para debugar**
```javascript
console.log(valor_campo + ' = ' + resultado);
```

✅ **Use comentários para documentar código**
```javascript
// Esta é uma boa prática!
var resultado = 5;  // Explica por que 5, não 3
```

---

## 9️⃣ **Desafios para Praticar**

1. **Mudança de Cor**: Quando clica "=", mude a cor do input para verde
2. **Histórico**: Crie um elemento `<div>` que mostre histórico de cálculos
3. **Validação**: Impeça digitar "5++" (operadores inválidos)
4. **Teclado**: Adicione suporte para clicar números usando teclado físico
5. **Mais Operações**: Adicione raiz quadrada, potência, porcentagem

---

## 🔟 **Recursos Adicionais**

- 📖 [MDN JavaScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript)
- 📖 [Bootstrap Documentação](https://getbootstrap.com/docs/4.0/)
- 🎥 [Abra F12 para ver Console](https://www.google.com/search?q=como+abrir+console+navegador)

---

## ✨ Próximos Passos

Após dominar este projeto:
1. ✅ Refatore para usar `querySelector()` em vez de `getElementById()`
2. ✅ Use `addEventListener()` em vez de `onclick` inline
3. ✅ Crie arquivo `.js` separado (melhor organização)
4. ✅ Implemente classe `Calculator` (POO)
5. ✅ Publique no GitHub Pages

---

**Bom aprendizado! 🚀**
