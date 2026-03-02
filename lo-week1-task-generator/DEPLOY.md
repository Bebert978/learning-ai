# Déployer le Task Generator sur un VPS

## 1. Cloner le projet

```bash
git clone <url-du-repo> task-generator
cd task-generator
```

## 2. Créer l'environnement Python

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 3. Créer le fichier `.env` sur le VPS

**Ne jamais copier le `.env` depuis ton PC** — crée-le directement sur le serveur :

```bash
nano .env
```

Contenu :

```
OPENAI_API_KEY=sk-ta-cle-ici
```

Puis verrouiller les permissions (seul ton utilisateur peut le lire) :

```bash
chmod 600 .env
```

## 4. Lancer Streamlit

```bash
streamlit run app.py
```

L'app écoute sur `127.0.0.1:8501` (local uniquement, pas accessible depuis internet).

## 5. Configurer Nginx comme reverse proxy

Nginx sert de "porte d'entrée" — il reçoit les requêtes internet et les transmet à Streamlit en local.

Créer le fichier de config Nginx :

```bash
sudo nano /etc/nginx/sites-available/task-generator
```

Contenu :

```nginx
server {
    listen 80;
    server_name ton-domaine.com;

    location / {
        proxy_pass http://127.0.0.1:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Activer le site :

```bash
sudo ln -s /etc/nginx/sites-available/task-generator /etc/nginx/sites-enabled/
sudo nginx -t          # Vérifier la syntaxe
sudo systemctl reload nginx
```

## 6. Vérifier que le port 8501 n'est PAS ouvert au public

Depuis ton PC (pas le VPS), teste :

```bash
curl http://ip-du-vps:8501
```

Si tu reçois une **erreur de connexion** → c'est bon, le port est fermé.
Si tu reçois une **réponse HTML** → le port est ouvert, il faut le bloquer :

```bash
# Sur le VPS, bloquer l'accès externe au port 8501
sudo ufw deny 8501
sudo ufw enable
```

## Résumé sécurité

| Point | Status |
|-------|--------|
| `.env` jamais dans git | `.gitignore` le bloque |
| Clé API non affichée | Le code ne la print jamais |
| Streamlit écoute en local | `config.toml` → `127.0.0.1` |
| Accès contrôlé par Nginx | Reverse proxy devant l'app |
| Port 8501 fermé au public | Vérifier avec `ufw` ou `curl` |
