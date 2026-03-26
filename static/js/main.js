console.log("HeartRate Pro UI loaded successfully");

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
            consoleBox.scrollTop = consoleBox.scrollHeight;
        }
    }

    if (startBtn) {
        startBtn.addEventListener("click", async function () {
            try {
                addConsoleMessage("Requesting webcam access...");

                videoStream = await navigator.mediaDevices.getUserMedia({
                    video: true,
                    audio: false
                });

                webcam.srcObject = videoStream;
                webcam.style.display = "block";
                placeholder.style.display = "none";

                addConsoleMessage("Webcam started successfully.");
                addConsoleMessage("Live monitoring session started.");
            } catch (error) {
                console.error("Camera access error:", error);
                addConsoleMessage("Failed to access webcam.");
                alert("Could not access webcam. Please allow camera permission.");
            }
        });
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
                addConsoleMessage("Monitoring stopped.");
            }
        });
    }
});
