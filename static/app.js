// UI interactions only. Encryption and decryption remain handled by the Flask backend.
document.querySelectorAll(".tab").forEach((tab) => {
  tab.addEventListener("click", () => {
    document.querySelectorAll(".tab").forEach((item) => {
      item.classList.remove("active");
      item.setAttribute("aria-selected", "false");
    });
    document.querySelectorAll(".panel").forEach((panel) => {
      panel.classList.remove("active-panel");
      panel.hidden = true;
    });
    tab.classList.add("active");
    tab.setAttribute("aria-selected", "true");
    const panel = document.getElementById(tab.dataset.panel);
    panel.hidden = false;
    panel.classList.add("active-panel");
  });
});

document.querySelectorAll(".toggle-password").forEach((button) => {
  button.addEventListener("click", () => {
    const input = document.getElementById(button.dataset.target);
    const reveal = input.type === "password";
    input.type = reveal ? "text" : "password";
    button.textContent = reveal ? "Hide" : "Show";
    button.setAttribute("aria-label", `${reveal ? "Hide" : "Show"} password`);
  });
});

[
  { input: "encrypt-file", title: "encrypt-file-title", subtitle: "encrypt-file-subtitle", zone: "encrypt-dropzone" },
  { input: "decrypt-file", title: "decrypt-file-title", subtitle: "decrypt-file-subtitle", zone: "decrypt-dropzone" }
].forEach((config) => {
  const input = document.getElementById(config.input);
  const zone = document.getElementById(config.zone);
  const title = document.getElementById(config.title);
  const subtitle = document.getElementById(config.subtitle);

  const showFile = (file) => {
    if (!file) return;
    title.textContent = file.name;
    subtitle.textContent = `${(file.size / (1024 * 1024)).toFixed(2)} MB · Ready to process`;
  };
  input.addEventListener("change", () => showFile(input.files[0]));

  ["dragenter", "dragover"].forEach((eventName) => zone.addEventListener(eventName, (event) => {
    event.preventDefault();
    zone.classList.add("dragover");
  }));
  ["dragleave", "drop"].forEach((eventName) => zone.addEventListener(eventName, (event) => {
    event.preventDefault();
    zone.classList.remove("dragover");
  }));
  zone.addEventListener("drop", (event) => {
    const files = event.dataTransfer.files;
    if (files.length) {
      try {
        input.files = files;
        showFile(files[0]);
      } catch (_error) {
        // The native file chooser remains available if a browser disallows assignment.
      }
    }
  });
});
