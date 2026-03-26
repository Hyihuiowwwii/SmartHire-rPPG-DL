alert("main.js loaded");

let videoStream = null;

document.addEventListener("DOMContentLoaded", function () {
    const startBtn = document.getElementById("startBtn");
    const stopBtn = document.getElementById("stopBtn");
    const webcam = document.getElementById("webcam");
    const placeholder = document.getElementById("cameraPlaceholder");
    const consoleBox = document.getElementById("consoleBox");

    function addConsoleMessage(message) {
        if (consoleBox) {
            const p = document.createElement("p");
            p.textContent = ">>> " + message;
            consoleBox.appendChild(p);
        }
    }

    if (startBtn) {
        startBtn.addEventListener("click", async function () {
            alert("Start button clicked");

            try {
                videoStream = await navigator.mediaDevices.getUserMedia({
                    video: true,
                    audio: false
                });

                webcam.srcObject = videoStream;
                webcam.style.display = "block";
                placeholder.style.display = "none";

                addConsoleMessage("Webcam started successfully.");
            } catch (error) {
                console.error(error);
                alert("Camera access failed");
                addConsoleMessage("Failed to access webcam.");
            }
        });
    } else {
        alert("startBtn not found");
    }

    if (stopBtn) {
        stopBtn.addEventListener("click", function () {
            if (videoStream) {
                const tracks = videoStream.getTracks();
                tracks.forEach(track => track.stop());

                webcam.srcObject = null;
                webcam.style.display = "none";
                placeholder.style.display = "block";

                addConsoleMessage("Webcam stopped.");
            }
        });
    }
});
