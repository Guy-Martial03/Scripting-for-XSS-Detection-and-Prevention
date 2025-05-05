from flask import Flask, request, render_template_string, session, redirect, url_for
import sqlite3, secrets, os

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
DB_PATH = "comments.db"

def init_db():
    if not os.path.exists(DB_PATH):
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute('''
                CREATE TABLE commentaires (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    contenu TEXT NOT NULL,
                    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    error = ""
    success = ""

    if "csrf_token" not in session:
        session["csrf_token"] = secrets.token_hex(32)

    if "show_raw" not in session:
        session["show_raw"] = False

    if request.method == "POST":
        token = request.form.get("csrf_token")
        comment = request.form.get("comment", "").strip()

        if not token or token != session["csrf_token"]:
            error = "⚠️ CSRF invalide"
        elif not comment:
            error = "Le commentaire est vide."
        else:
            with sqlite3.connect(DB_PATH) as conn:
                conn.execute("INSERT INTO commentaires (contenu) VALUES (?)", (comment,))
            success = "✅ Commentaire enregistré."

    with sqlite3.connect(DB_PATH) as conn:
        comments = conn.execute("SELECT contenu FROM commentaires ORDER BY id DESC LIMIT 10").fetchall()

    return render_template_string("""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Test XSS sécurisé</title>
    </head>
    <body>
        <h2>Tester les protections XSS</h2>

        {% if error %}<p style="color:red;">{{ error }}</p>{% endif %}
        {% if success %}<p style="color:green;">{{ success }}</p>{% endif %}

        <form method="post">
            <textarea name="comment" rows="4" cols="50" placeholder='Your comments' required></textarea><br>
            <input type="hidden" name="csrf_token" value="{{ session.csrf_token }}">
            <button type="submit">Envoyer</button>
        </form>

        <form action="{{ url_for('toggle_mode') }}" method="post" style="margin-top:1em;">
            <button type="submit">
                {% if session.show_raw %}🔒 Revenir à l'affichage protégé{% else %}⚠️ Voir affichage brut (non sécurisé){% endif %}
            </button>
        </form>

        <form action="{{ url_for('clear_comments') }}" method="post" style="margin-top:1em;">
            <button type="submit" style="color:red;">🗑️ Vider tous les commentaires</button>
        </form>

        <h3>Commentaires :</h3>
        {% for c in comments %}
            <div style="background:#f0f0f0; padding:6px; margin:4px 0;">
                {% if session.show_raw %}
                    <strong>Raw :</strong> {{ c[0] | safe }}
                {% else %}
                    <strong>Sanitized :</strong> {{ c[0] | e }}
                {% endif %}
            </div>
        {% endfor %}
    </body>
    </html>
    """, error=error, success=success, comments=comments)

# Route pour basculer l'affichage protégé / brut
@app.route("/toggle", methods=["POST"])
def toggle_mode():
    session["show_raw"] = not session.get("show_raw", False)
    return redirect(url_for("index"))

# Route pour effacer tous les commentaires
@app.route("/clear", methods=["POST"])
def clear_comments():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("DELETE FROM commentaires")
    return redirect(url_for("index"))

# Route pour afficher tous les commentaires dans le terminal
@app.route("/view_comments", methods=["GET"])
def view_comments():
    with sqlite3.connect(DB_PATH) as conn:
        comments = conn.execute("SELECT * FROM commentaires").fetchall()
        print("\n=== Liste des commentaires ===")
        for comment in comments:
            print(f"ID: {comment[0]}, Contenu: {comment[1]}, Date: {comment[2]}")
        print("===============================")
    return "Commentaires affichés dans le terminal. Vérifiez votre console."

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
