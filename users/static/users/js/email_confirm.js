const boxes = document.querySelectorAll(".code-box");
const realCodeInput = document.getElementById("real-code");

boxes[0].focus();

boxes.forEach((box, index) => {
    box.addEventListener("input", () => {
        box.value = box.value.replace(/\D/g, "");

        if (box.value && index < 5) {
            boxes[index + 1].focus();
        }

        updateCode();
    });

    box.addEventListener("keydown", (e) => {
        if (e.key === "Backspace" && !box.value && index > 0) {
            boxes[index - 1].focus();
        }
    });
});

function updateCode() {
    let code = "";
    boxes.forEach(b => code += b.value);
    realCodeInput.value = code;
}

let resendBtn = document.getElementById("resend-btn");
let timerEl = document.getElementById("timer");
let seconds = 30;

function startTimer() {
    resendBtn.disabled = true;
    timerEl.textContent = `Можно отправить через ${seconds} сек.`;

    const interval = setInterval(() => {
        seconds--;
        timerEl.textContent = `Можно отправить через ${seconds} сек.`;

        if (seconds <= 0) {
            clearInterval(interval);
            resendBtn.disabled = false;
            timerEl.textContent = "";
        }
    }, 1000);
}

startTimer();

resendBtn.addEventListener("click", () => {
    alert("Код отправлен повторно (заглушка).");
    seconds = 30;
    startTimer();
});
