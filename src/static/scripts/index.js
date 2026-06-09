
let originalTitle = document.title;
let scrollText = originalTitle + " • ";
let index = 0;
let scrollInterval;
let isFocused = true;

function init() {
    startScrolling();
    removePanel();
}

function startScrolling() {
    stopScrolling();
    scrollInterval = setInterval(() => {
        document.title = scrollText.substring(index) + scrollText.substring(0, index);
        index = (index + 1) % scrollText.length;
    }, 300); // rychlost scrollování
}

function stopScrolling() {
    clearInterval(scrollInterval);
}

window.addEventListener("focus", () => {
    isFocused = true;
    startScrolling();
});

window.addEventListener("blur", () => {
    isFocused = false;
    stopScrolling();
    document.title = "Come back to me 😑";
});