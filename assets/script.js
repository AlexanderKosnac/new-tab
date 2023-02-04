/*
 * COOKIE HANDLING
 */
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

/*
 * LINE VISIBILITY
 */
COOKIE_STARTPAGE_VISIBILITY = "startpage-visibility";
VISIBILITY_STATE = []

function readVisibilityState() {
    VISIBILITY_STATE = getCookieAsArray(COOKIE_STARTPAGE_VISIBILITY);
}

function writeVisibilityState() {
    setCookieAsArray(COOKIE_STARTPAGE_VISIBILITY, VISIBILITY_STATE);
}

function getLine(lineNo) {
    return document.getElementById("line-" + lineNo);
}

function isLineVisibile(line) {
    return !(line.style.display == "none");
}

function setLineVisible(line, bool) {
    line.style.display = bool ? "flex" : "none";

    lineNo = line.id.split("-")[1];
    VISIBILITY_STATE[lineNo] = bool ? "1" : "0";
    writeVisibilityState();
}

function toggleLine(lineNo) {
    line = getLine(lineNo);
    b = !isLineVisibile(line);
    setLineVisible(line, b);
}

function setLineVisibilityBasedOnCookie(lineNo) {
    line = getLine(lineNo);
    visible = VISIBILITY_STATE[lineNo] == "0" ? false : true;
    setLineVisible(line, visible);
}

function setAllLinesBasedOnCookies() {
    lines = document.getElementsByClassName("line");
    for (i = 0; i < lines.length; i++) {
        setLineVisibilityBasedOnCookie(i);
    }
}

function onload_hook() {
    readVisibilityState();
    setAllLinesBasedOnCookies();
}
