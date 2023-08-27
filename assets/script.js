// Cookie handling
function getCookie(name) {
    cookies = document.cookie.split(";")
    for (i = 0; i < cookies.length; i++) {
        cookie = cookies[i];
        if (cookie.startsWith(name)) {
            return cookie.split("=", 2)[1];
        }
    }
    return null;
}

function getCookieAsArray(name) {
    return (getCookie(name) || "").split(",")
}

function setCookie(name, value) {
    document.cookie = name + "=" + value;
}

function setCookieAsArray(name, values) {
    setCookie(name, values.join(","));
}

// Visibility
COOKIE_STARTPAGE_VISIBILITY = "startpage-visibility";
VISIBILITY_STATE = []

const objIdMapping = new Map();


function readVisibilityState() {
    VISIBILITY_STATE = getCookieAsArray(COOKIE_STARTPAGE_VISIBILITY);
}

function writeVisibilityState() {
    setCookieAsArray(COOKIE_STARTPAGE_VISIBILITY, VISIBILITY_STATE);
}

function isLineVisibile(line) {
    return line.getAttribute("state") === "open";
}

function setLineVisible(line, bool) {
    line.setAttribute("state", bool ? "open" : "closed");
    VISIBILITY_STATE[objIdMapping.get(line)] = bool ? "1" : "0";
    console.log(VISIBILITY_STATE)
    writeVisibilityState();
}

function toggleLine(it) {
    setLineVisible(it, !isLineVisibile(it));
}

function setAllLinesBasedOnCookies() {
    let lines = document.querySelectorAll("h2");
    for (let i=0; i<lines.length; i++) {
        setLineVisible(lines[i], VISIBILITY_STATE[i] !== "0");
    }
}

function onload_hook() {
    let i = 0;
    document.querySelectorAll("h2").forEach(it => objIdMapping.set(it, i++));

    readVisibilityState();
    setAllLinesBasedOnCookies();
}
