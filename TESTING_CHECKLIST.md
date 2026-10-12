# CipherMedia Test Checklist

- [ ] Start the Flask server and open `http://127.0.0.1:5000`.
- [ ] Encrypt a small JPG or PNG using a memorable test password.
- [ ] Confirm the browser downloads a `.cmenc` file.
- [ ] Decrypt it with the same password.
- [ ] Open the recovered file and compare it with the original.
- [ ] Attempt decryption with a wrong password; confirm an error appears.
- [ ] Try an encrypted file whose bytes have been modified; confirm rejection.
- [ ] Try an unsupported file type; confirm rejection.
- [ ] Try a zero-byte file; confirm rejection.
- [ ] Test both desktop and mobile-width browser layouts.
- [ ] Take screenshots of the home page, encrypted download, successful recovery and wrong-password error for the project report.
