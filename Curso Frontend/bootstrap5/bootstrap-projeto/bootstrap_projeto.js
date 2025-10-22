document.addEventListener('DOMContentLoaded', () => {
    const htmlEl = document.documentElement;
    const themeToggleBtn = document.getElementById('themeToggle');
    const feedbackToastEl = document.getElementById('feedbackToast');
    const feedbackToastBody = document.getElementById('feedbackToastBody');
    const copyButtons = document.querySelectorAll('[data-copy-target]');
    const utilityHighlightBtn = document.querySelector('[data-highlight-utilities]');
    const utilityPills = document.querySelectorAll('.utility-pill');
    const gridControls = document.querySelectorAll('[data-grid-control]');
    const gridPreview = document.querySelector('[data-grid-preview] .row');
    const themePreview = document.querySelector('[data-theme-preview]');
    const themePreviewToggle = document.getElementById('toggleThemePreview');
    const form = document.querySelector('[data-live-form]');
    const resetFormBtn = document.querySelector('[data-reset-form]');
    const showToastBtn = document.querySelector('[data-show-toast]');
    const demoToastEl = document.getElementById('demoToast');
    const lastUpdatedEl = document.getElementById('lastUpdated');
    const backToTopBtn = document.getElementById('backToTop');
    const searchInput = document.getElementById('searchGuide');
    const clearSearchBtn = document.getElementById('clearSearch');
    const searchResults = document.getElementById('searchResults');
    const searchResultsList = document.getElementById('searchResultsList');
    const searchCount = document.getElementById('searchCount');
    const closeSearchResults = document.getElementById('closeSearchResults');
    const testBreakpointsBtn = document.getElementById('testBreakpoints');
    const currentBreakpoint = document.getElementById('currentBreakpoint');
    const breakpointValue = document.getElementById('breakpointValue');
    const widthValue = document.getElementById('widthValue');
    const showAlertBtn = document.getElementById('showAlert');
    const alertContainer = document.getElementById('alertContainer');
    const sectionCompleteButtons = document.querySelectorAll('[data-section-complete]');
    const progressBar = document.getElementById('progressBar');
    const progressText = document.getElementById('progressText');
    const resetProgressBtn = document.getElementById('resetProgress');
    const playgroundCode = document.getElementById('playgroundCode');
    const playgroundOutput = document.getElementById('playgroundOutput');
    const renderPlaygroundBtn = document.getElementById('renderPlayground');
    const clearPlaygroundBtn = document.getElementById('clearPlayground');
    const loadExampleBtn = document.getElementById('loadExample');
    const solutionButtons = document.querySelectorAll('[data-show-solution]');

    const toast = feedbackToastEl ? bootstrap.Toast.getOrCreateInstance(feedbackToastEl) : null;
    const demoToast = demoToastEl ? bootstrap.Toast.getOrCreateInstance(demoToastEl) : null;

    // Data e hora
    if (lastUpdatedEl) {
        const formatted = new Intl.DateTimeFormat('pt-BR', {
            dateStyle: 'long'
        }).format(new Date());
        lastUpdatedEl.textContent = formatted;
    }

    // Sistema de feedback
    function showFeedback(message) {
        if (!toast || !feedbackToastBody) return;
        feedbackToastBody.textContent = message;
        toast.show();
    }

    // Copiar para clipboard
    function copyToClipboard(text) {
        if (navigator.clipboard && window.isSecureContext) {
            return navigator.clipboard.writeText(text);
        }
        return new Promise((resolve, reject) => {
            try {
                const textarea = document.createElement('textarea');
                textarea.value = text;
                textarea.style.position = 'fixed';
                textarea.style.opacity = '0';
                document.body.appendChild(textarea);
                textarea.focus();
                textarea.select();
                const successful = document.execCommand('copy');
                document.body.removeChild(textarea);
                if (successful) {
                    resolve();
                } else {
                    reject(new Error('Copy command unsuccessful'));
                }
            } catch (err) {
                reject(err);
            }
        });
    }

    // Botões de copiar
    copyButtons.forEach((button) => {
        button.addEventListener('click', () => {
            const selector = button.getAttribute('data-copy-target');
            const target = document.querySelector(selector);
            if (!target) {
                showFeedback('Elemento não encontrado para copiar.');
                return;
            }
            copyToClipboard(target.innerText)
                .then(() => showFeedback('Snippet copiado para a área de transferência!'))
                .catch(() => showFeedback('Não foi possível copiar. Copie manualmente.'));
        });
    });

    // Toggle de tema
    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', () => {
            const isLight = htmlEl.getAttribute('data-bs-theme') !== 'dark';
            htmlEl.setAttribute('data-bs-theme', isLight ? 'dark' : 'light');
            themeToggleBtn.innerHTML = isLight
                ? '<i class="bi bi-moon-stars"></i><span class="ms-1">Escuro</span>'
                : '<i class="bi bi-brightness-high"></i><span class="ms-1">Claro</span>';
        });
    }

    // Destacar utilitários
    if (utilityHighlightBtn) {
        utilityHighlightBtn.addEventListener('click', () => {
            utilityHighlightBtn.disabled = true;
            utilityPills.forEach((pill, index) => {
                setTimeout(() => {
                    pill.classList.add('active');
                }, index * 120);
            });
            setTimeout(() => {
                utilityPills.forEach((pill) => pill.classList.remove('active'));
                utilityHighlightBtn.disabled = false;
            }, utilityPills.length * 120 + 1200);
        });
    }

    // Grid layouts
    const gridLayouts = {
        2: [
            { content: 'Coluna 1', classes: 'col-12 col-md-6' },
            { content: 'Coluna 2', classes: 'col-12 col-md-6' }
        ],
        3: [
            { content: 'Coluna 1', classes: 'col-12 col-md-4' },
            { content: 'Coluna 2', classes: 'col-12 col-md-4' },
            { content: 'Coluna 3', classes: 'col-12 col-md-4' }
        ],
        4: [
            { content: 'Coluna 1', classes: 'col-6 col-lg-3' },
            { content: 'Coluna 2', classes: 'col-6 col-lg-3' },
            { content: 'Coluna 3', classes: 'col-6 col-lg-3' },
            { content: 'Coluna 4', classes: 'col-6 col-lg-3' }
        ],
        responsive: [
            { content: '12 / 6 / 3', classes: 'col-12 col-md-6 col-xl-3' },
            { content: '12 / 6 / 3', classes: 'col-12 col-md-6 col-xl-3' },
            { content: '12 / 6 / 3', classes: 'col-12 col-md-6 col-xl-3' },
            { content: '12 / 6 / 3', classes: 'col-12 col-md-6 col-xl-3' }
        ]
    };

    function renderGrid(mode) {
        if (!gridPreview) return;
        const layout = gridLayouts[mode];
        if (!layout) return;
        gridPreview.innerHTML = layout
            .map((item) => `
                <div class="${item.classes}">
                    <div class="preview-box">${item.content}</div>
                </div>
            `)
            .join('');
    }

    gridControls.forEach((button) => {
        button.addEventListener('click', () => {
            const mode = button.getAttribute('data-grid-control');
            renderGrid(mode);
        });
    });

    // Theme preview
    if (themePreview && themePreviewToggle) {
        themePreviewToggle.addEventListener('click', () => {
            const isDark = themePreview.dataset.mode === 'dark';
            themePreview.dataset.mode = isDark ? 'light' : 'dark';
            themePreview.classList.toggle('bg-dark', !isDark);
            themePreview.classList.toggle('text-white', !isDark);
            themePreviewToggle.textContent = isDark ? 'Alternar tema de visualização' : 'Alternar para tema claro';
        });
    }

    // Validação de formulário
    if (form) {
        form.addEventListener('submit', (event) => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
                showFeedback('Verifique os campos destacados antes de enviar.');
            } else {
                event.preventDefault();
                showFeedback('Formulário validado! Pronto para integrar com o backend.');
            }
            form.classList.add('was-validated');
        });
    }

    if (resetFormBtn && form) {
        resetFormBtn.addEventListener('click', () => {
            form.reset();
            form.classList.remove('was-validated');
        });
    }

    // Demo toast
    if (showToastBtn && demoToast) {
        showToastBtn.addEventListener('click', () => {
            demoToast.show();
        });
    }

    // Botão voltar ao topo
    if (backToTopBtn) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 300) {
                backToTopBtn.style.display = 'block';
            } else {
                backToTopBtn.style.display = 'none';
            }
        });

        backToTopBtn.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Sistema de busca
    if (searchInput) {
        let searchTimeout;
        searchInput.addEventListener('input', (e) => {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {
                const query = e.target.value.trim().toLowerCase();
                if (query.length < 2) {
                    searchResults.classList.add('d-none');
                    return;
                }
                performSearch(query);
            }, 300);
        });
    }

    function performSearch(query) {
        const sections = document.querySelectorAll('.content-section');
        const results = [];

        sections.forEach(section => {
            const text = section.textContent.toLowerCase();
            const title = section.querySelector('h2, h3')?.textContent || 'Sem título';
            const id = section.id;

            if (text.includes(query)) {
                const index = text.indexOf(query);
                const context = text.substring(Math.max(0, index - 50), Math.min(text.length, index + 100));
                results.push({ title, id, context });
            }
        });

        displaySearchResults(results, query);
    }

    function displaySearchResults(results, query) {
        if (!searchResultsList || !searchResults || !searchCount) return;

        searchCount.textContent = results.length;

        if (results.length === 0) {
            searchResultsList.innerHTML = '<div class="text-muted p-3">Nenhum resultado encontrado.</div>';
        } else {
            searchResultsList.innerHTML = results.map(result => `
                <div class="search-result-item" data-goto="${result.id}">
                    <strong>${result.title}</strong>
                    <p class="small text-muted mb-0">${highlightQuery(result.context, query)}</p>
                </div>
            `).join('');

            // Adicionar eventos de clique
            searchResultsList.querySelectorAll('.search-result-item').forEach(item => {
                item.addEventListener('click', () => {
                    const targetId = item.getAttribute('data-goto');
                    const targetElement = document.getElementById(targetId);
                    if (targetElement) {
                        targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
                        searchResults.classList.add('d-none');
                        searchInput.value = '';
                    }
                });
            });
        }

        searchResults.classList.remove('d-none');
    }

    function highlightQuery(text, query) {
        const regex = new RegExp(`(${query})`, 'gi');
        return text.replace(regex, '<span class="search-highlight">$1</span>');
    }

    if (clearSearchBtn) {
        clearSearchBtn.addEventListener('click', () => {
            searchInput.value = '';
            searchResults.classList.add('d-none');
        });
    }

    if (closeSearchResults) {
        closeSearchResults.addEventListener('click', () => {
            searchResults.classList.add('d-none');
        });
    }

    // Teste de breakpoints
    if (testBreakpointsBtn) {
        testBreakpointsBtn.addEventListener('click', () => {
            const width = window.innerWidth;
            let bp = 'XS (< 576px)';
            
            if (width >= 1400) bp = 'XXL (≥ 1400px)';
            else if (width >= 1200) bp = 'XL (≥ 1200px)';
            else if (width >= 992) bp = 'LG (≥ 992px)';
            else if (width >= 768) bp = 'MD (≥ 768px)';
            else if (width >= 576) bp = 'SM (≥ 576px)';

            breakpointValue.textContent = bp;
            widthValue.textContent = width;
            currentBreakpoint.classList.remove('d-none');
        });
    }

    // Alert dinâmico
    if (showAlertBtn && alertContainer) {
        showAlertBtn.addEventListener('click', () => {
            const alertTypes = ['primary', 'success', 'danger', 'warning', 'info'];
            const randomType = alertTypes[Math.floor(Math.random() * alertTypes.length)];
            
            alertContainer.innerHTML = `
                <div class="alert alert-${randomType} alert-dismissible fade show" role="alert">
                    <strong>Alert ${randomType}!</strong> Este é um exemplo de alert dinâmico.
                    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                </div>
            `;
        });
    }

    // Sistema de progresso
    const totalSections = 9;
    let completedSections = new Set(JSON.parse(localStorage.getItem('completedSections') || '[]'));

    function updateProgress() {
        const percentage = (completedSections.size / totalSections) * 100;
        progressBar.style.width = percentage + '%';
        progressBar.textContent = Math.round(percentage) + '%';
        progressText.textContent = `${completedSections.size}/${totalSections}`;
        
        localStorage.setItem('completedSections', JSON.stringify([...completedSections]));
    }

    sectionCompleteButtons.forEach(button => {
        const sectionId = button.getAttribute('data-section-complete');
        const section = document.getElementById(sectionId);

        // Verificar estado inicial
        if (completedSections.has(sectionId)) {
            button.innerHTML = '<i class="bi bi-check-circle-fill"></i> Concluído';
            button.classList.replace('btn-success', 'btn-secondary');
            if (section) section.classList.add('completed');
        }

        button.addEventListener('click', () => {
            if (completedSections.has(sectionId)) {
                completedSections.delete(sectionId);
                button.innerHTML = '<i class="bi bi-check-circle"></i> Marcar como concluído';
                button.classList.replace('btn-secondary', 'btn-success');
                if (section) section.classList.remove('completed');
            } else {
                completedSections.add(sectionId);
                button.innerHTML = '<i class="bi bi-check-circle-fill"></i> Concluído';
                button.classList.replace('btn-success', 'btn-secondary');
                if (section) section.classList.add('completed');
                showFeedback('Seção marcada como concluída! 🎉');
            }
            updateProgress();
        });
    });

    if (resetProgressBtn) {
        resetProgressBtn.addEventListener('click', () => {
            if (confirm('Deseja realmente resetar todo o progresso?')) {
                completedSections.clear();
                localStorage.removeItem('completedSections');
                updateProgress();
                
                sectionCompleteButtons.forEach(button => {
                    const sectionId = button.getAttribute('data-section-complete');
                    const section = document.getElementById(sectionId);
                    button.innerHTML = '<i class="bi bi-check-circle"></i> Marcar como concluído';
                    button.classList.replace('btn-secondary', 'btn-success');
                    if (section) section.classList.remove('completed');
                });
                
                showFeedback('Progresso resetado!');
            }
        });
    }

    updateProgress();

    // Playground interativo
    if (renderPlaygroundBtn && playgroundCode && playgroundOutput) {
        renderPlaygroundBtn.addEventListener('click', () => {
            const code = playgroundCode.value;
            playgroundOutput.innerHTML = code;
            showFeedback('Código renderizado com sucesso!');
        });
    }

    if (clearPlaygroundBtn && playgroundCode && playgroundOutput) {
        clearPlaygroundBtn.addEventListener('click', () => {
            playgroundCode.value = '';
            playgroundOutput.innerHTML = '<div class="alert alert-info"><i class="bi bi-info-circle me-2"></i>Playground limpo.</div>';
        });
    }

    if (loadExampleBtn && playgroundCode) {
        loadExampleBtn.addEventListener('click', () => {
            const example = `<div class="card mb-3">
  <div class="card-header bg-primary text-white">
    <h5 class="mb-0">Card Exemplo</h5>
  </div>
  <div class="card-body">
    <p class="card-text">Este é um exemplo pré-carregado.</p>
    <div class="d-flex gap-2">
      <button class="btn btn-success btn-sm">Ação 1</button>
      <button class="btn btn-outline-secondary btn-sm">Ação 2</button>
    </div>
  </div>
  <div class="card-footer text-muted">
    Footer do card
  </div>
</div>

<div class="alert alert-warning alert-dismissible fade show" role="alert">
  <strong>Atenção!</strong> Você pode editar este exemplo.
  <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
</div>`;
            
            playgroundCode.value = example;
            showFeedback('Exemplo carregado! Clique em "Renderizar" para visualizar.');
        });
    }

    // Mostrar soluções dos exercícios
    solutionButtons.forEach(button => {
        button.addEventListener('click', () => {
            const solutionId = button.getAttribute('data-show-solution');
            const solutionDiv = document.querySelector(`[data-solution="${solutionId}"]`);
            
            if (solutionDiv) {
                solutionDiv.classList.toggle('d-none');
                button.innerHTML = solutionDiv.classList.contains('d-none')
                    ? '<i class="bi bi-lightbulb"></i> Ver solução'
                    : '<i class="bi bi-eye-slash"></i> Ocultar solução';
            }
        });
    });
});