# Spotify Clone (Projeto de Estudo)

Interface inspirada no Spotify desenvolvida para fins educacionais (curso Front-end). Inclui melhorias de acessibilidade, performance, SEO e experiência.

## Funcionalidades
- Layout responsivo (Bootstrap 4)
- Carrossel inicial
- Seções de serviços e recursos
- Footer organizado em navegações semânticas
- Tema claro/escuro com persistência (localStorage) e respeito a `prefers-color-scheme`
- Suporte a `prefers-reduced-motion` (pausa carrossel)
- Skip link para acessibilidade
- Foco visível somente via teclado (`:focus-visible`)
- PWA básico (manifest + service worker, cache estático, fallback offline, página 404)
- Animações de entrada (IntersectionObserver)
- Barra de progresso de scroll
- Botão "Voltar ao topo"
- Contador animado de músicas
- Toast de atualização de versão (Service Worker update)
- Open Graph / Twitter Card / theme-color

## Arquitetura / Técnicas
- Variáveis CSS para cores e tokens
- Estratégia de cache-first dinâmica simples no Service Worker
- Preconnect e preload para recursos críticos
- Lazy loading em imagens não críticas

## Próximos Passos Sugeridos
- Converter imagens para WebP/AVIF e usar `<picture>`
- Otimizar e minificar CSS/JS (ex: build com PostCSS ou outro)
- Adicionar testes de acessibilidade (axe, Lighthouse)
- Melhorar contraste de alguns tons no tema claro se necessário
- Otimizar offline: versão de atualização com estratégia stale-while-revalidate
- Página 404 personalizada

## Desenvolvimento Local
Basta abrir `index.html` em um navegador moderno. Para testar Service Worker/localStorage em condições ideais, sirva via HTTP:

Powershell (exemplo com servidor simples Python):
```powershell
python -m http.server 8000
```
Abra: http://localhost:8000/

## Licença
Uso educacional. Marcas e logotipos pertencem aos seus respectivos proprietários.
