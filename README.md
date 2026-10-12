# CipherMedia — Secure Media Encryption & Decryption

**CipherMedia** is a Python-based web application that allows users to encrypt and decrypt media files, including images, videos, and audio, using a password. The project provides a simple, modern web interface for protecting media files through cryptographic operations.

Developed as a **BCA Mini Project** to demonstrate file handling, cryptography, backend development, and frontend integration.

## Features

- **Media Encryption:** Encrypt supported media files using a password.
- **Media Decryption:** Decrypt previously encrypted files using the correct password.
- **Multiple Media Formats:** Designed for image, video, and audio files.
- **Password Protection:** Requires a password to encrypt and decrypt files.
- **Modern Web Interface:** Dark-themed, responsive interface with a cybersecurity-inspired design.
- **File Upload Support:** Upload files directly through the browser.
- **Simple Workflow:** Easy-to-use interface for encryption and decryption.
- **Python Backend:** Built using Flask.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend logic and file processing |
| Flask | Web application framework |
| HTML5 | Page structure |
| CSS3 | Styling and responsive design |
| JavaScript | Interactive user interface |
| Cryptography library | Cryptographic operations, as implemented in the backend |

## Project Structure

```text
CipherMedia/
├── app.py
├── requirements.txt
├── README.md
├── PROJECT_REPORT.md
├── TESTING_CHECKLIST.md
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── app.js
```

## Getting Started

Follow these steps to run CipherMedia on your local computer.

### Prerequisites

- Python 3.9 or later
- pip (Python package installer)
- Git (optional, for cloning the repository)

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/CipherMedia.git
```

Navigate into the project directory:

```bash
cd CipherMedia
```

Replace `YOUR-USERNAME` with your GitHub username and `CipherMedia` with your repository name if different.

### 2. Create a Virtual Environment

Creating a virtual environment is recommended.

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

### 5. Open the Website

Open your browser and visit:

http://127.0.0.1:5000

The CipherMedia application should now be accessible on your local machine.

## How to Use

### Encrypt a Media File

1. Open CipherMedia in your browser.
2. Select the Encrypt option.
3. Upload the media file you want to protect.
4. Enter a strong password.
5. Submit the form to encrypt the file.
6. Save the resulting encrypted file.

### Decrypt a Media File

1. Select the Decrypt option.
2. Upload a file previously encrypted by CipherMedia.
3. Enter the correct password used during encryption.
4. Submit the form to decrypt the file.
5. Save the recovered file.

**Important:** Decryption requires the correct password and a file compatible with the application's encryption format.

## Security Notes

- Use a strong, unique password.
- Keep your password safe. If the encryption design does not provide password recovery, a forgotten password may make the file unrecoverable.
- Do not upload confidential files to a publicly accessible deployment unless appropriate security controls are in place.
- Use HTTPS, appropriate upload limits, file validation, and temporary-file cleanup before deploying the application publicly.
- Security depends on the cryptographic algorithm, key derivation, and implementation used in the backend.

## Testing

Use the included `TESTING_CHECKLIST.md` to help verify the application.

Recommended test cases:

- Encrypt a supported media file.
- Decrypt it using the correct password.
- Attempt decryption with an incorrect password.
- Try unsupported or invalid files.
- Test empty passwords and missing uploads.
- Confirm the decrypted file opens correctly.

## Project Objectives

- Understand client-server architecture using Flask.
- Implement file upload and download workflows.
- Explore password-based encryption and decryption.
- Integrate HTML, CSS, and JavaScript with a Python backend.
- Develop a practical web application with a user-friendly interface.

## Future Enhancements

- Support for additional file formats.
- Improved file validation and error handling.
- Encryption progress indicators for large files.
- Improved temporary-file cleanup.
- Optional user authentication and encrypted file storage.
- Deployment with production-grade security settings.

## Project Information

**Project Name:** CipherMedia  
**Project Type:** BCA Mini Project  
**Domain:** Cybersecurity and Web Development  
**Backend:** Python and Flask  
**Frontend:** HTML, CSS, and JavaScript

## License

This project is intended for educational and learning purposes. If you plan to distribute or reuse it, add a license such as the MIT License and ensure that third-party dependencies comply with their respective licenses.

If you find this project useful, consider giving the repository a star.

**Disclaimer:** CipherMedia is an educational project. Review and test the actual encryption implementation before using it to protect sensitive or valuable data.
