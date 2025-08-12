from flask import Flask, render_template, jsonify

app = Flask(__name__)

LEVELS = [
    {
        "id": 1,
        "name": "Words",
        "items": [
            {"id": "w1",  "text": "Device",     "type": "word",   "audio": "device.wav",     "image": "device.png"},
            {"id": "w2",  "text": "Software",   "type": "word",   "audio": "software.wav",   "image": "software.png"},
            {"id": "w3",  "text": "Hardware",   "type": "word",   "audio": "hardware.wav",   "image": "hardware.png"},
            {"id": "w4",  "text": "Network",    "type": "word",   "audio": "network.wav",    "image": "network.png"},
            {"id": "w5",  "text": "Upload",     "type": "word",   "audio": "upload.wav",     "image": "upload.png"},
            {"id": "w6",  "text": "Repository", "type": "word",   "audio": "repository.wav", "image": "repository.png"},
            {"id": "w7",  "text": "Browser",    "type": "word",   "audio": "browser.wav",    "image": "browser.png"},
            {"id": "w8",  "text": "Server",      "type": "word",  "audio": "server.wav",      "image": "cloud.png"},
            {"id": "w9",  "text": "Update",     "type": "word",   "audio": "update.wav",     "image": "update.png"},
            {"id": "w10", "text": "Password",   "type": "word",   "audio": "password.wav",   "image": "password.png"},
        ],
    },
    {
         "id": 2,
    "name": "Phrases",
    "items": [
        {"id": "p1",  "text": "Device driver.",                              "type": "phrase", "audio": "p1.wav",  "image": "p1.png"},
        {"id": "p2",  "text": "Software update.",                       "type": "phrase", "audio": "p2.wav",  "image": "p2.png"},
        {"id": "p3",  "text": "Hardware issue.",                           "type": "phrase", "audio": "p3.wav",  "image": "p3.png"},
        {"id": "p4",  "text": "Network speed.",              "type": "phrase", "audio": "p4.wav",  "image": "p4.png"},
        {"id": "p5",  "text": "Upload file.",                    "type": "phrase", "audio": "p5.wav",  "image": "p5.png"},
        {"id": "p6",  "text": "Repository access.",       "type": "phrase", "audio": "p6.wav",  "image": "p6.png"},
        {"id": "p7",  "text": "Browser window.",               "type": "phrase", "audio": "p7.wav",  "image": "p7.png"},
        {"id": "p8",  "text": "Server status.",               "type": "phrase", "audio": "p8.wav",  "image": "p8.png"},
        {"id": "p9",  "text": "Update settings.",               "type": "phrase", "audio": "p9.wav",  "image": "p9.png"},
        {"id": "p10", "text": "Password manager.",                      "type": "phrase", "audio": "p10.wav", "image": "p10.png"},
        ],
    },
    {
        "id": 3,
        "name": "Collocations",
        "items": [
            {"id": "c1",  "text": "Device control panel",        "type": "collocation", "audio": "device-control-panel.wav",       "image": "device-control-panel.png"},
            {"id": "c2",  "text": "Software license agreement",  "type": "collocation", "audio": "software-license-agreement.wav", "image": "software-license-agreement.png"},
            {"id": "c3",  "text": "Hardware compatibility check", "type": "collocation", "audio": "hardware-compatibility-check.wav","image": "hardware-compatibility-check.png"},
            {"id": "c4",  "text": "Network security audit",      "type": "collocation", "audio": "network-security-audit.wav",     "image": "network-security-audit.png"},
            {"id": "c5",  "text": "Upload progress bar",         "type": "collocation", "audio": "upload-progress-bar.wav",        "image": "upload-progress-bar.png"},
            {"id": "c6",  "text": "Repository branch merge",     "type": "collocation", "audio": "repository-branch-merge.wav",    "image": "repository-branch-merge.png"},
            {"id": "c7",  "text": "Browser cache settings",      "type": "collocation", "audio": "browser-cache-settings.wav",     "image": "browser-cache-settings.png"},
            {"id": "c8",  "text": "Server backup service",       "type": "collocation", "audio": "server-backup-service.wav",      "image": "server-backup-service.png"},
            {"id": "c9",  "text": "Update notification panel",   "type": "collocation", "audio": "update-notification-panel.wav",  "image": "update-notification-panel.png"},
            {"id": "c10", "text": "Password recovery tool",      "type": "collocation", "audio": "password-recovery-tool.wav",     "image": "password-recovery-tool.png"},
        ],
    },

    # ---- Nuevo Nivel 4 ----
    {
        "id": 4,
        "name": "Short Phrases",
        "items": [
            {"id": "sp1",  "text": "Update your device now",    "type": "phrase", "audio": "update-your-device-now.wav",    "image": "update-your-device-now.png"},
            {"id": "sp2",  "text": "I need a software license", "type": "phrase", "audio": "need-software-license.wav",      "image": "need-software-license.png"},
            {"id": "sp3",  "text": "Install the hardware",      "type": "phrase", "audio": "install-the-hardware.wav",       "image": "install-the-hardware.png"},
            {"id": "sp4",  "text": "The network is slow",       "type": "phrase", "audio": "network-is-slow.wav",            "image": "network-is-slow.png"},
            {"id": "sp5",  "text": "Please upload the file",    "type": "phrase", "audio": "upload-the-file.wav",            "image": "upload-the-file.png"},
            {"id": "sp6",  "text": "Access the repository",     "type": "phrase", "audio": "access-the-repository.wav",      "image": "access-the-repository.png"},
            {"id": "sp7",  "text": "Open a new browser tab",    "type": "phrase", "audio": "open-new-browser-tab.wav",       "image": "open-new-browser-tab.png"},
            {"id": "sp8",  "text": "Our server is secure",      "type": "phrase", "audio": "server-is-secure.wav",           "image": "server-is-secure.png"},
            {"id": "sp9",  "text": "Schedule an update",        "type": "phrase", "audio": "schedule-an-update.wav",         "image": "schedule-an-update.png"},
            {"id": "sp10", "text": "Check your password",       "type": "phrase", "audio": "check-your-password.wav",        "image": "check-your-password.png"},
        ],
    },

    # ---- Nuevo Nivel 5 ----
    {
        "id": 5,
        "name": "Sentences",
        "items": [
            {"id": "s1",  "text": "The software update fixed my device",           "type": "sentence", "audio": "update-fixed-my-device.wav",     "image": "update-fixed-my-device.png"},
            {"id": "s2",  "text": "I need a software license to continue",         "type": "sentence", "audio": "need-license-to-continue.wav",   "image": "need-license-to-continue.png"},
            {"id": "s3",  "text": "Install the hardware drivers today",            "type": "sentence", "audio": "install-hardware-drivers.wav",   "image": "install-hardware-drivers.png"},
            {"id": "s4",  "text": "Let's check the network speed",                 "type": "sentence", "audio": "check-network-speed.wav",        "image": "check-network-speed.png"},
            {"id": "s5",  "text": "Please upload the file to the repository",      "type": "sentence", "audio": "upload-file-to-repository.wav",  "image": "upload-file-to-repository.png"},
            {"id": "s6",  "text": "They accessed the repository online",           "type": "sentence", "audio": "accessed-repository-online.wav", "image": "accessed-repository-online.png"},
            {"id": "s7",  "text": "Open the browser and test the site",            "type": "sentence", "audio": "open-browser-test-site.wav",     "image": "open-browser-test-site.png"},
            {"id": "s8",  "text": "Our team uses the server for storage",          "type": "sentence", "audio": "server-for-storage.wav",         "image": "server-for-storage.png"},
            {"id": "s9",  "text": "He scheduled the update for tomorrow",          "type": "sentence", "audio": "scheduled-update-tomorrow.wav",  "image": "scheduled-update-tomorrow.png"},
            {"id": "s10", "text": "My password manager keeps it safe",             "type": "sentence", "audio": "password-manager-safe.wav",      "image": "password-manager-safe.png"},
        ],
    },
]

@app.route("/api/levels")
def api_levels():
    return jsonify(LEVELS)

# Lo dejamos por compatibilidad, aunque el front nuevo ya no lo usa
@app.route('/api/words')
def api_words():
    return jsonify([i["text"] for i in LEVELS[0]["items"]])

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)