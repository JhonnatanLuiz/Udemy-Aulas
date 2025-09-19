# Renomeação de Repositório | Repository Renaming

Este documento explica o que acontece quando você renomeia um repositório no GitHub e como gerenciar as mudanças localmente.

This document explains what happens when you rename a repository on GitHub and how to manage the changes locally.

---

## Português

### Pergunta: Se eu renomear este projeto aqui, automaticamente será renomeada a pasta no meu computador?

**Resposta Rápida:** **NÃO**, renomear o repositório no GitHub **não renomeia automaticamente** a pasta local no seu computador.

### O que acontece quando você renomeia um repositório no GitHub:

1. **URL do repositório muda**: De `github.com/usuario/nome-antigo` para `github.com/usuario/nome-novo`
2. **Redirecionamento automático**: GitHub cria redirecionamentos temporários do nome antigo para o novo
3. **Pasta local permanece igual**: Sua pasta local mantém o nome original
4. **Git remote continua funcionando**: Devido aos redirecionamentos, `git push` e `git pull` continuam funcionando temporariamente

### Como atualizar sua configuração local após renomear:

#### Opção 1: Atualizar apenas o remote URL (Recomendado)
```bash
# Verificar o remote atual
git remote -v

# Atualizar para o novo nome do repositório
git remote set-url origin https://github.com/SeuUsuario/NovoNome.git

# Verificar se foi alterado
git remote -v
```

#### Opção 2: Renomear a pasta local também
```bash
# Navegar para o diretório pai
cd ..

# Renomear a pasta local
mv pasta-antiga pasta-nova

# Entrar na pasta renomeada
cd pasta-nova

# Atualizar o remote URL
git remote set-url origin https://github.com/SeuUsuario/NovoNome.git
```

#### Opção 3: Clonar novamente (Menos eficiente)
```bash
# Fazer backup de mudanças não commitadas se necessário
git stash

# Clonar o repositório com o novo nome
git clone https://github.com/SeuUsuario/NovoNome.git

# Copiar mudanças locais se houver
```

### Dicas importantes:

- ✅ **Atualize o remote URL imediatamente** para evitar confusão
- ✅ **Atualize bookmarks e links** que apontam para o repositório
- ✅ **Notifique colaboradores** sobre a mudança de nome
- ⚠️ **Redirecionamentos são temporários** - não dependa deles permanentemente
- ⚠️ **Atualize documentação** que menciona o nome antigo do repositório

---

## English

### Question: If I rename this project here, will the folder on my computer be automatically renamed?

**Quick Answer:** **NO**, renaming a repository on GitHub does **not automatically rename** the local folder on your computer.

### What happens when you rename a repository on GitHub:

1. **Repository URL changes**: From `github.com/username/old-name` to `github.com/username/new-name`
2. **Automatic redirects**: GitHub creates temporary redirects from the old name to the new one
3. **Local folder stays the same**: Your local folder keeps its original name
4. **Git remote keeps working**: Due to redirects, `git push` and `git pull` continue working temporarily

### How to update your local setup after renaming:

#### Option 1: Update only the remote URL (Recommended)
```bash
# Check current remote
git remote -v

# Update to the new repository name
git remote set-url origin https://github.com/YourUsername/NewName.git

# Verify the change
git remote -v
```

#### Option 2: Rename the local folder too
```bash
# Navigate to the parent directory
cd ..

# Rename the local folder
mv old-folder new-folder

# Enter the renamed folder
cd new-folder

# Update the remote URL
git remote set-url origin https://github.com/YourUsername/NewName.git
```

#### Option 3: Clone again (Less efficient)
```bash
# Backup uncommitted changes if needed
git stash

# Clone the repository with the new name
git clone https://github.com/YourUsername/NewName.git

# Copy local changes if any
```

### Important tips:

- ✅ **Update the remote URL immediately** to avoid confusion
- ✅ **Update bookmarks and links** pointing to the repository
- ✅ **Notify collaborators** about the name change
- ⚠️ **Redirects are temporary** - don't rely on them permanently
- ⚠️ **Update documentation** that mentions the old repository name

---

## Comandos Úteis | Useful Commands

### Verificar configuração atual | Check current configuration
```bash
# Ver informações do repositório
git remote -v
git status
git branch -vv

# Ver configuração do Git
git config --list --local
```

### Validar após mudanças | Validate after changes
```bash
# Testar conexão com o repositório
git ls-remote origin

# Fazer um push de teste
git push origin nome-do-branch

# Fazer um pull de teste
git pull origin nome-do-branch
```

### Exemplo prático | Practical example
```bash
# Situação: Repositório "MeuProjeto" foi renomeado para "ProjetoUdemy"

# 1. Verificar estado atual
git remote -v
# origin  https://github.com/usuario/MeuProjeto.git (fetch)
# origin  https://github.com/usuario/MeuProjeto.git (push)

# 2. Atualizar remote
git remote set-url origin https://github.com/usuario/ProjetoUdemy.git

# 3. Verificar mudança
git remote -v
# origin  https://github.com/usuario/ProjetoUdemy.git (fetch)
# origin  https://github.com/usuario/ProjetoUdemy.git (push)

# 4. Testar conexão
git push origin main
```

---

## Resolução de Problemas | Troubleshooting

### Erro: repository not found
```bash
# Verificar se o nome do repositório está correto
git remote -v

# Atualizar com o nome correto
git remote set-url origin https://github.com/usuario/nome-correto.git
```

### Erro: authentication failed
```bash
# Verificar credenciais salvas
git config --list | grep user

# Pode precisar atualizar credenciais no sistema
# Windows: Gerenciador de Credenciais
# macOS: Keychain Access
# Linux: gnome-keyring ou similar
```

### Múltiplos remotes
```bash
# Se você tem múltiplos remotes
git remote -v

# Atualizar específico
git remote set-url upstream https://github.com/usuario/novo-nome.git
```