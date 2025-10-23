# Piano di lavoro per funzionalità To-Do

## Contesto
- **Tecnologie:** Django 5, Python 3, SQLite, Bootstrap.
- **Obiettivo finale:** applicazione con elenco attività, registrazione/login, form di creazione task, pagina elenco utenti.
- **Profilo sviluppatore:** livello junior (≈1 settimana di esperienza Django); i passi includono riferimenti a comandi e file specifici.

## Prerequisiti
1. Assicurati di avere un virtualenv attivo (`python -m venv venv && source venv/bin/activate` se non già fatto).
2. Installa dipendenze indicate nel progetto (`pip install -r requirements.txt` se presente; altrimenti `pip install django Faker django-bootstrap5 pillow`).
3. Applica le migrazioni esistenti: `python manage.py migrate`.
4. Crea un superuser di test (facoltativo ma consigliato): `python manage.py createsuperuser`.

## Task dettagliati

### 1. Pulizia iniziale (≈0.25h)
1. Elimina gli script di autopopolamento non più necessari:
   - `populate_todo.py`
   - `populate_users.py`
2. Controlla che nessun file faccia import di questi script (usa `rg "populate_"`).

### 2. Revisione template base e navigazione (≈0.5h)
1. Apri `templates/todo_list/base.html`.
2. Aggiungi nella navbar link alle pagine principali:
   - Lista todo (`{% url 'todo_list:index' %}`).
   - Nuovo task.
   - Lista utenti.
   - Login/Logout con visibilità condizionata (`{% if user.is_authenticated %}`).
3. Verifica che il titolo della pagina (`<title>`) venga popolato tramite blocco template (`{% block title %}`) se utile.

### 3. Home: lista dei task (≈0.5h)
1. File coinvolti: `todo_list/views.py`, `templates/todo_list/index.html`, `static/todo_list/styles.css`.
2. Nella view `index` assicurati che `todos_list` venga passato al contesto (già presente, controllare).
3. Nel template:
   - Decommenta la sezione con tabella e rimuovi markup duplicato `<html>`.
   - Estendi `base.html` e inserisci il contenuto nel blocco `body_block`.
   - Richiama `{% load static %}` se necessario per applicare il CSS.
4. Aggiorna il file CSS solo se servono piccoli aggiustamenti (margini, spinner, ecc.).

### 4. Routing coerente per la home (≈0.25h)
1. In `first_project/urls.py` verifica che la root (`""`) punti alla view `index`.
2. Se necessario, aggiungi un redirect dalla root a `/todos/` o sposta la view in `path("", ...)`.
3. Controlla che la navbar usi sempre i nomi `url` per evitare percorsi hardcoded.

### 5. Vista e form di creazione task (≈0.5h)
1. File: `todo_list/views.py`, `templates/todo_list/new_task.html`, `todo_list/forms.py`.
2. View `new_task`:
   - Applica `@login_required`.
   - Dopo `form.save()` esegui `return redirect('todo_list:index')`.
   - Gestisci messaggi d’errore (`messages.error`) oppure visualizza gli errori nel template.
3. Template:
   - Estendi `base.html`.
   - Usa `{{ form.as_p }}` all’interno di un form Bootstrap (div con classi).
   - Visualizza `form.errors` se presenti.
4. Verifica che il form `FormTask` includa solo i campi necessari (considera `fields = ('title', 'description', 'status')` per mantenere ordine).

### 6. Registrazione utente (≈0.75h)
1. File: `todo_list/forms.py`, `todo_list/views.py`, `templates/todo_list/register.html`.
2. Rinomina `UserFrom` in `UserForm` (aggiorna import ovunque).
3. Aggiungi validazione password (es. `clean_password` se vuoi forzare requisiti extra).
4. Nella view:
   - Mostra messaggi di errore form (non solo `print`).
   - Dopo registrazione, effettua redirect al login o login automatico (scegli e commenta la decisione).
5. Template:
   - Mostra errori accanto ai campi (`{{ form.field.errors }}`).
   - Mantieni il feedback di successo già presente.

### 7. Login e logout (≈0.5h)
1. File: `todo_list/views.py`, `templates/todo_list/login.html`.
2. Correggi l’uso del POST: `request.POST.get("username")`.
3. Gestisci strade alternative:
   - Se credenziali errate, mostra messaggio nel template.
   - Se l’utente è già loggato, reindirizza alla home.
4. Dopo login riuscito, usa `return redirect('todo_list:index')`.
5. Aggiorna la navbar per mostrare `Login` solo quando l’utente è anonimo e `Logout` + nome quando autenticato.

### 8. Pagina elenco utenti (≈0.5h)
1. File: `todo_list/views.py`, `todo_list/urls.py`, `templates/todo_list/users.html`.
2. Sblocca la view `users` (rimuovi commenti) e import `User`.
3. Applica `@login_required`.
4. Passa al template `users_list = User.objects.all().order_by('username')`.
5. Aggiorna il template per estendere `base.html` e usare bootstrap.
6. Inserisci link alla navbar.

### 9. Protezione viste e redirect (≈0.25h)
1. Controlla che `special`, `new_task`, `users` abbiano `@login_required`.
2. Verifica la costante `LOGIN_URL` in `first_project/settings.py` (usa path con namespace `/login/`).
3. Testa manualmente: visita pagina protetta da utente anonimo e verifica redirect.

### 10. Miglioramenti qualità codice (≈0.5h)
1. In `todo_list/models.py` aggiungi `def __str__(self):` per `Todo`.
2. Aggiungi docstring/commenti brevi nelle view per chiarire i passaggi più complessi.
3. Rimuovi codice commentato non più utile.
4. Esegui `python manage.py makemigrations` (dovrebbe non generare modifiche per confermare che i modelli sono coerenti).

### 11. Verifica manuale end-to-end (≈0.75h)
1. Avvia server: `python manage.py runserver`.
2. Flusso consigliato:
   - Registra nuovo utente (verifica caricamento immagine opzionale).
   - Esegui login con l’utente appena creato.
   - Crea un paio di task, verifica visualizzazione nella lista.
   - Controlla pagina utenti.
   - Esegui logout.
   - Replica il login con credenziali errate per vedere messaggio.
3. Annota eventuali bug UX (ad es. mancanza di redirect) e correggi.
4. Se tutto ok, ferma il server (`Ctrl+C`).

### 12. Wrap-up (≈0.25h)
1. Usa `git status` per verificare file cambiati.
2. Opzionale: crea commit con messaggio coerente.
3. Aggiorna documentazione se necessario (es. README).

## Suggerimenti per avanzamento
- Procedi sezione per sezione, testando ogni modifica prima di passare alla successiva.
- In caso di problemi, controlla sempre i log di Django nella console.
- Mantieni la console aperta durante lo sviluppo per vedere errori runtime.

Buon lavoro!
