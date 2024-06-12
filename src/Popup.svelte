<script>
  import data from "./lib/data.json";

  let ntdata;

  let elementTypes = [
    {
      display: "Favorite",
      default: {
        "type": "favorite",
        "url": "",
        "label": "",
        "shortcut": ""
      }
    }, {
      display: "Header",
      default: {
        "type": "header",
        "text": ""
      }
    },
  ];
  let selectedElementType = elementTypes[0];

  function save() {
    browser.storage.local.set({ "new-tab-data": ntdata });
  }

  function restoreDefault() {
    browser.storage.local.set({ "new-tab-data": data });
  }

  function clear() {
    browser.storage.local.remove("new-tab-data");
  }

  function exportData() {
    const date = new Date();
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, "0");
    const day = String(date.getDate()).padStart(2, "0");
    const hours = String(date.getHours()).padStart(2, "0");
    const minutes = String(date.getMinutes()).padStart(2, "0");
    const seconds = String(date.getSeconds()).padStart(2, "0");

    let filename = `new-tab-data-${year}-${month}-${day}-${hours}-${minutes}-${seconds}.json`;

    const text = JSON.stringify(ntdata, null, 2);
    let element = document.createElement("a");
    element.setAttribute("href", "data:text/plain;charset=utf-8," + encodeURIComponent(text));
    element.setAttribute("download", filename);
    element.style.display = "none";
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
  }

  function importData() {
    let data = window.prompt("Insert JSON data to import:", "");
    if (data == null) return;
    ntdata = JSON.parse(data);
    save();
  }

  function moveUp(idx) {
    if (idx == 0) return;
    let tmp = ntdata["data"][idx-1];
    ntdata["data"][idx-1] = ntdata["data"][idx];
    ntdata["data"][idx] = tmp;
  }

  function moveDown(idx) {
    if (idx == ntdata["data"].length) return;
    let tmp = ntdata["data"][idx+1];
    ntdata["data"][idx+1] = ntdata["data"][idx];
    ntdata["data"][idx] = tmp;
  }

  function deleteEntry(idx) {
    ntdata["data"].splice(idx, 1);
    ntdata["data"] = ntdata["data"];
  }

  function newEntry() {
    ntdata["data"].push(selectedElementType.default);
    ntdata["data"] = ntdata["data"];
  }

  let dataPromise = browser.storage.local.get("new-tab-data");
  dataPromise.then(it => { ntdata = it["new-tab-data"] }, () => {});
</script>

<div class="popup-container">
{#await dataPromise}
  <p>Loading new-tab data from storage.</p>
{:then _}
  <div class="d-flex flex-column gap-3">
    <div class="d-flex flex-row gap-1">
      <button class="ntinput green" on:click={save}>Save</button>
      <div style="flex-grow: 1"></div>
      <button class="ntinput" on:click={exportData}>Export</button>
      <button class="ntinput" on:click={importData}>Import</button>
      <div style="flex-grow: 1"></div>
      <button class="ntinput" on:click={restoreDefault}>Default</button>
      <button class="ntinput red" on:click={clear}>Clear</button>
    </div>

    <label>
      Title:
      <input type="text" class="ntinput" bind:value={ntdata["title"]}/>
    </label>

    {#each ntdata["data"] ?? [] as entry, idx}
    <div class="d-flex flex-row gap-3 align-items-center p-1 data-entry">
      <div class="d-flex flex-column gap-1">
        <button class="up-down-arrow" on:click={() => { moveUp(idx) }}>
          <img src="./icons/arrow.svg" alt="Move up"/>
        </button>
        <button class="up-down-arrow" on:click={() => { moveDown(idx) }}>
          <img src="./icons/arrow.svg" style="transform: rotate(180deg)" alt="Move down"/>
        </button>
      </div>
      {#if entry.type == "header"}
        <div><input type="text" class="ntinput" size="45" bind:value={entry["text"]}/></div>
      {/if}
      {#if entry.type == "favorite"}
        <div>
          <label>
            Label:<br>
            <input type="text" class="ntinput" size="15" bind:value={entry["label"]}/>
          </label>
        </div>
        <div>
          <label>
            URL:<br>
            <input type="text" class="ntinput" size="25" bind:value={entry["url"]}/>
          </label>
        </div>
        <!--div><input type="text" bind:value={entry["icon"]}/></div-->
        <div>
          <label>
            Shortcut:<br>
            <input type="text" class="ntinput" maxlength="1" size="5" bind:value={entry["shortcut"]}/>
          </label>
        </div>
      {/if}
      <div style="flex-grow: 1"></div>
      <div><button class="ntinput red" on:click={() => { deleteEntry(idx) }}>Delete</button></div>
    </div>
    {/each}

    <div>
      <select class="ntinput" bind:value={selectedElementType}>
        {#each elementTypes as type}
        <option value={type}>{type.display}</option>
        {/each}
      </select>
      <button class="ntinput" on:click={newEntry}>Create Element</button>
    </div>
  </div>
{:catch error}
  <p style="color: red">Could not load new-tab data from storage.</p>
  <code>{error}</code>
{/await}
</div>

<style>
  .popup-container {
    padding: 5px;
    width: 700px;
  }
  .data-entry {
    border-left: 6px solid var(--dark-background);
    background-color: var(--light-background);
  }
  .up-down-arrow {
    background: none;
    color: inherit;
    border: none;
    padding: 0;
    font: inherit;
    cursor: pointer;
    outline: inherit;
    line-height: 0;
  }
  .up-down-arrow > img {
    width: 24px;
    height: 24px;
  }
</style>