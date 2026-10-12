import os
import secrets
from io import BytesIO
from flask import Flask, render_template, request, send_file, flash, redirect, url_for
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", secrets.token_hex(32))
app.config["MAX_CONTENT_LENGTH"] = 200 * 1024 * 1024  # 200 MB upload limit

MAGIC = b"CIPHERMEDIA1"
SALT_SIZE = 16
NONCE_SIZE = 12
KEY_SIZE = 32
ITERATIONS = 600_000
ALLOWED_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp", ".tiff",
    ".mp4", ".mov", ".mkv", ".avi", ".webm",
    ".mp3", ".wav", ".aac", ".m4a", ".ogg", ".flac"
}

def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_SIZE,
        salt=salt,
        iterations=ITERATIONS,
    )
    return kdf.derive(password.encode("utf-8"))

def encrypt_bytes(data: bytes, password: str) -> bytes:
    salt = os.urandom(SALT_SIZE)
    nonce = os.urandom(NONCE_SIZE)
    key = derive_key(password, salt)
    ciphertext = AESGCM(key).encrypt(nonce, data, MAGIC)
    return MAGIC + salt + nonce + ciphertext

def decrypt_bytes(blob: bytes, password: str) -> bytes:
    header_size = len(MAGIC) + SALT_SIZE + NONCE_SIZE
    if len(blob) < header_size + 16 or not blob.startswith(MAGIC):
        raise ValueError("This does not look like a valid CipherMedia encrypted file.")
    pos = len(MAGIC)
    salt = blob[pos:pos + SALT_SIZE]
    pos += SALT_SIZE
    nonce = blob[pos:pos + NONCE_SIZE]
    ciphertext = blob[pos + NONCE_SIZE:]
    key = derive_key(password, salt)
    try:
        return AESGCM(key).decrypt(nonce, ciphertext, MAGIC)
    except Exception as exc:
        raise ValueError("Decryption failed. Check the secret key or encrypted file integrity.") from exc

def safe_download_name(name: str) -> str:
    # Strip any path components supplied by a client.
    return os.path.basename(name.replace("\\", "/")) or "download.bin"

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/encrypt")
def encrypt_route():
    uploaded = request.files.get("file")
    password = request.form.get("password", "")
    if not uploaded or not uploaded.filename:
        flash("Choose a file first.", "error")
        return redirect(url_for("index"))
    if len(password) < 8:
        flash("Use a secret key of at least 8 characters.", "error")
        return redirect(url_for("index"))

    filename = safe_download_name(uploaded.filename)
    extension = os.path.splitext(filename)[1].lower()
    if extension not in ALLOWED_EXTENSIONS:
        flash("Unsupported file type. Choose an image, video, or audio file.", "error")
        return redirect(url_for("index"))

    data = uploaded.read()
    if not data:
        flash("The selected file is empty.", "error")
        return redirect(url_for("index"))
    encrypted = encrypt_bytes(data, password)
    output = filename + ".cmenc"
    return send_file(
        BytesIO(encrypted),
        as_attachment=True,
        download_name=output,
        mimetype="application/octet-stream",
    )

@app.post("/decrypt")
def decrypt_route():
    uploaded = request.files.get("file")
    password = request.form.get("password", "")
    if not uploaded or not uploaded.filename:
        flash("Choose an encrypted .cmenc file first.", "error")
        return redirect(url_for("index"))
    if not password:
        flash("Enter the secret key used during encryption.", "error")
        return redirect(url_for("index"))

    encrypted_name = safe_download_name(uploaded.filename)
    blob = uploaded.read()
    try:
        data = decrypt_bytes(blob, password)
    except ValueError as exc:
        flash(str(exc), "error")
        return redirect(url_for("index"))

    output = encrypted_name[:-6] if encrypted_name.lower().endswith(".cmenc") else "decrypted_file"
    output = safe_download_name(output)
    return send_file(
        BytesIO(data),
        as_attachment=True,
        download_name=output,
        mimetype="application/octet-stream",
    )

@app.errorhandler(413)
def too_large(_error):
    flash("File is too large. The maximum supported upload is 200 MB.", "error")
    return redirect(url_for("index"))

if __name__ == "__main__":
    # Local development only. Do not use Flask's development server in production.
    app.run(debug=True)
