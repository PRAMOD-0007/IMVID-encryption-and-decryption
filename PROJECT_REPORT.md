# CipherMedia: Secure Image, Video and Audio Encryption & Decryption System

## 1. Abstract
CipherMedia is a web-based application that protects image, video and audio files using password-based authenticated encryption. A user selects a supported media file, enters a secret password and downloads an encrypted `.cmenc` file. The same password is used to recover the original file. The system uses PBKDF2-HMAC-SHA256 to derive a 256-bit key and AES-256-GCM to provide confidentiality and integrity.

## 2. Problem Statement
Digital media files may contain private or sensitive information. Files stored or transferred without encryption can be accessed by unauthorized people. CipherMedia demonstrates a simple workflow for encrypting media files and recovering them only with the correct secret password.

## 3. Objectives
- Design a simple website for media encryption and decryption.
- Support common image, video and audio file formats.
- Apply password-based key derivation and authenticated encryption.
- Detect incorrect passwords and ciphertext modification.
- Provide downloadable encrypted and recovered files.
- Demonstrate frontend/backend integration and cryptography concepts.

## 4. Scope
This academic prototype processes files locally through a Flask backend. It does not provide user accounts or cloud storage. It is intended for classroom demonstration and small test files, not as a production file-sharing service.

## 5. Technologies
- HTML5: structure
- CSS3: responsive visual design
- JavaScript: tabs, password visibility and file selection interactions
- Python: backend logic
- Flask: HTTP routes and file responses
- `cryptography`: PBKDF2-HMAC-SHA256 and AES-GCM

## 6. System Requirements
**Hardware:** A computer with 4 GB RAM or more and sufficient disk space.

**Software:** Python 3.10+, pip, VS Code or another editor, and a modern browser.

## 7. System Design
**Input:** Media file and secret password.

**Encryption process:** Validate upload → generate random salt and nonce → derive 256-bit key using PBKDF2 → encrypt with AES-GCM → package header, salt, nonce and ciphertext → return `.cmenc` download.

**Decryption process:** Upload `.cmenc` file → parse header, salt and nonce → derive the same key from password → authenticate and decrypt → return original bytes as a download. If authentication fails, display an error instead of returning corrupted output.

## 8. Algorithm
### Encryption
1. Read the uploaded file bytes.
2. Generate a cryptographically random 16-byte salt.
3. Generate a cryptographically random 12-byte nonce.
4. Derive a 32-byte key from the password using PBKDF2-HMAC-SHA256.
5. Encrypt with AES-256-GCM, authenticating the application header.
6. Combine the header, salt, nonce and ciphertext/tag.
7. Return the result as a `.cmenc` download.

### Decryption
1. Read the `.cmenc` file.
2. Validate the header and minimum length.
3. Extract the salt, nonce and ciphertext/tag.
4. Derive the key from the supplied password and stored salt.
5. Authenticate and decrypt using AES-GCM.
6. Return the recovered bytes only if authentication succeeds.

## 9. Modules
- User interface module
- File validation and upload module
- Password-based key derivation module
- Encryption module
- Decryption and integrity verification module
- Download and error-handling module

## 10. Testing
| Test | Expected result |
|---|---|
| Encrypt a PNG file | `.cmenc` file downloads |
| Decrypt with correct password | Original file bytes are recovered |
| Decrypt with wrong password | Authentication error is shown |
| Modify encrypted bytes | Decryption is rejected |
| Upload unsupported extension | Upload is rejected |
| Submit an empty file | Validation error is shown |
| Upload a file over 200 MB | Size-limit error is shown |

## 11. Advantages
- Supports multiple media types.
- Uses authenticated encryption rather than a homemade cipher.
- Password is not stored.
- Random salt and nonce are generated for each encryption.
- Simple browser interface and downloadable output.

## 12. Limitations
- Current version reads files into memory.
- No user accounts, database, or cloud storage.
- Password recovery is not possible.
- Development server is not intended for public deployment.
- Extension checks are a basic usability filter, not full file-content validation.

## 13. Future Enhancements
- Streaming encryption for large files.
- Optional account-based file history without storing passwords.
- File checksum display and progress indicators.
- Multi-file batch processing.
- Secure deployment with HTTPS, CSRF protection and rate limiting.

## 14. Conclusion
CipherMedia demonstrates how a web application can combine file handling, password-based key derivation and authenticated encryption to protect image, video and audio files. It provides a practical example of cryptographic concepts and client/server web development.

## 15. References
- Python documentation: https://docs.python.org/3/
- Flask documentation: https://flask.palletsprojects.com/
- Cryptography documentation: https://cryptography.io/
- NIST FIPS 197, Advanced Encryption Standard (AES): https://csrc.nist.gov/pubs/fips/197/final
- NIST SP 800-132, Password-Based Key Derivation: https://csrc.nist.gov/pubs/sp/800/132/final
