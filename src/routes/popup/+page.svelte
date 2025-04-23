<script>
    import { onMount } from "svelte"

    import data from "$lib/data.json"
    import { newTabData } from "$lib/storage.js"

    function save() {
        chrome.storage.local.set({ "new-tab-data": $newTabData })
    }

    function exportData() {
        const date = new Date()
        const year = date.getFullYear()
        const month = String(date.getMonth() + 1).padStart(2, "0")
        const day = String(date.getDate()).padStart(2, "0")
        const hours = String(date.getHours()).padStart(2, "0")
        const minutes = String(date.getMinutes()).padStart(2, "0")
        const seconds = String(date.getSeconds()).padStart(2, "0")

        let filename = `new-tab-data-${year}-${month}-${day}-${hours}-${minutes}-${seconds}.json`

        const text = JSON.stringify($newTabData, null, 2)
        let element = document.createElement("a")
        element.setAttribute("href", "data:text/plain;charset=utf-8," + encodeURIComponent(text))
        element.setAttribute("download", filename)
        element.style.display = "none"
        document.body.appendChild(element)
        element.click()
        document.body.removeChild(element)
    }

    function importData() {
        let data = window.prompt("Insert JSON data to import:", "")
        if (data == null) return
        newTabData.set(JSON.parse(data))
        save()
    }

    function resetData() {
        if (confirm("You are about to reset the data to the default. Do you really want to do this?")) {
            newTabData.set(data)
            save()
        }
    }

    let dataPromise
    onMount(() => {
        dataPromise = chrome.storage.local.get("new-tab-data").then((it) => {
            newTabData.set(it["new-tab-data"] ?? data)
        })
    })
</script>

<div class="popup-container">
    <h1>New-Tab Settings</h1>
    <p>
        <tt>new-tab</tt> is a plugin that replaces the default "New Tab" page in the browser with a more useful alternative. The project can be found on
        <a href="https://github.com/AlexanderKosnac/new-tab">GitHub</a>.
    </p>

    <p>You can edit the layout by switchting to edit mode via the gear icon in the top right of the newtab page. Text can be edited by simply clicking on it and editing it. Edit hidden values, move and delete elements by right-clicking on the respective element. Save the results via the button to the left of the gear icon, otherwise changes will be discarded.</p>

    <h2>Data</h2>
    <div class="d-flex flex-column gap-3">
        <div>
            <button class="ntinput btn-settings" on:click="{exportData}">Export</button>
            Download the stored data as a JSON.
        </div>
        <div>
            <button class="ntinput btn-settings" on:click="{importData}">Import</button>
            Import a JSON to overwrite the stored data.
        </div>
        <div>
            <button class="ntinput btn-settings" on:click="{resetData}">Reset</button>
            Reset the stored data to the default.
        </div>
    </div>
</div>

<style>
    a {
        color: var(--font-color);
        font-weight: 900;
        text-decoration: underline;
    }
    .popup-container {
        padding: 0px 5px 0px 5px;
        width: 700px;
        min-height: 400px;
    }
    .btn-settings {
        width: 60px;
    }
</style>
