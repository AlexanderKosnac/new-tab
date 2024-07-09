<script>
  import { onMount } from "svelte";

  import Favorite from "$lib/Favorite/Favorite.svelte";
  import Header from "$lib/Header/Header.svelte";
  import EditMenu from "$lib/EditMenu/EditMenu.svelte";

  import data from "$lib/data.json";
  import { newTabData, state } from "$lib/storage.js";

  let saveStatus;
  let iconInput;

  const componentMapping = {
    "header": {
      clazz: Header,
      display: "Header",
      default: {
          "type": "header",
          "text": ""
      }
    },
    "favorite": {
      clazz: Favorite,
      display: "Favorite",
      default: {
        "type": "favorite",
        "url": "",
        "label": "",
        "shortcut": ""
      }
    }
  };

  let shortcuts = {};

  function openShortcut(e) {
      const el = shortcuts[e.key];
      if (e.ctrlKey || $state.editable) return;
      if (el) el.open();
  }

  function save() {
    chrome.storage.local.set({ "new-tab-data": $newTabData }).then(
      () => {
        saveStatus.innerText = "Save succeeded!";
        saveStatus.classList.add("font-success");
      },
      () => {
        saveStatus.innerText = "Save failed!";
        saveStatus.classList.add("font-error");
      }
    ).then(() => {
      saveStatus.classList.remove("hidden");
      setTimeout(() => { saveStatus.classList.add("hidden") }, 1000)
    });
  }

  function newEntry(e) {
    const type = e.originalTarget.getAttribute("etype");
    const data = structuredClone(componentMapping[type].default);
    $newTabData["data"].push(data);
    $newTabData = $newTabData;
  }

  function loadIcons() {
    $newTabData["icons"] ??= {};
    for (let i=0; i<iconInput.files.length; i++) {
      const file = iconInput.files.item(i);

      const reader = new FileReader();
      reader.onload = e => {
        $newTabData["icons"][file.name] = e.target.result;
      };

      reader.readAsDataURL(file);
    }
  }

  function deleteIcon(key) {
    delete $newTabData["icons"][key];
    $newTabData = $newTabData;
  }

  let dataPromise;
  onMount(() => {
    dataPromise = chrome.storage.local.get("new-tab-data").then(it => {
      newTabData.set(it["new-tab-data"] ?? data);
    });
  });
</script>

<svelte:window on:keyup={openShortcut} />

{#await dataPromise}
  <p>Loading new-tab data from storage.</p>
{:then _}
  <!--pre>{JSON.stringify(data, null, 2)}</pre-->

  <div class="d-flex align-items-center justify-content-space-between gap-2">
    <div class="title" style="flex-grow: 1">{$newTabData["title"] ?? "New Tab"}</div>
    {#if $state.editable}
      <div bind:this={saveStatus} class="save-status flash-and-hide hidden"></div>
      <button class="ntinput green" on:click={save}>Save</button>
    {/if}
    <svg id="btnEdit" xmlns="http://www.w3.org/2000/svg" width="24" height="24" class:editable={$state.editable} stroke="white" viewBox="0 0 16 16" on:click={() => { $state.editable = !$state.editable }}>
      <path transform="scale(0.9 0.9) translate(1 1)" d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z"/>
    </svg>
  </div>
  <div class="content">
  {#each $newTabData["data"] ?? [] as entry, idx}
    <svelte:component this={componentMapping[entry.type].clazz} {idx} bind:this={shortcuts[entry.shortcut?.toLowerCase()]} />
  {/each}
  </div>
  {#if $state.editable}
  <hr>
  <div class="d-flex flex-column gap-1">
    <h4>Insert new Element:</h4>
    <div>
      <input type="button" class="ntinput" on:click={newEntry} etype="header" value="Header"/>
      <input type="button" class="ntinput" on:click={newEntry} etype="favorite" value="Favorite"/>
    </div>

    <h4>Load Icons:</h4>
    <div>
      <input type="file" class="ntinput" multiple="multiple" accept="image/*" bind:this={iconInput} />
      <input type="button" class="ntinput" on:click={loadIcons} value="Load"/>
    </div>

    <h4>Stored Icons:</h4>
    <div class="d-flex flex-wrap icon-display" style="max-width: 800px">
      {#each Object.entries($newTabData["icons"] ?? {}) as [key, base64]}
      <img class="icon" src="{base64}" alt="icon" title="{key}"/>
      <svg xmlns="http://www.w3.org/2000/svg" class="btn-delete" width="16" height="16" fill="#C80036" viewBox="0 0 16 16" on:click={() => deleteIcon(key)}>
        <circle cx="50%" cy="50%" r="7" fill="white"/>
        <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0M5.354 4.646a.5.5 0 1 0-.708.708L7.293 8l-2.647 2.646a.5.5 0 0 0 .708.708L8 8.707l2.646 2.647a.5.5 0 0 0 .708-.708L8.707 8l2.647-2.646a.5.5 0 0 0-.708-.708L8 7.293z"/>
      </svg>
      {/each}
    </div>
  </div>
  {/if}
{:catch error}
  <div class="font-error">
    <p>Failed to load new-tab data from storage.</p>
    <code>{error}</code>
  </div>
{/await}

<EditMenu/>

<style>
.title {
  font-size: 32px;
  font-weight: bold;
}
#btnEdit {
  width: 24px;
  height: 24px;
  background-color: transparent;
}
svg#btnEdit {
  transition: transform .5s, fill .5s;
  transform: rotate(0deg);
  fill: transparent;
}
svg#btnEdit.editable {
  transform: rotate(45deg);
  fill: white;
}
.save-status {
  font-weight: 600;
  font-size: 0.8em;
}
.flash-and-hide {
  opacity: 1;
  transition: none;
}
.flash-and-hide.hidden {
  opacity: 0;
  transition: opacity 0.5s linear;
}
.icon {
  border-radius: 7px;
  min-width:  40px;
  max-width:  40px;
  min-height: 40px;
  max-height: 40px;
}
.btn-delete {
  position: relative;
  left: -8px;
  top: -8px;
  margin-right: 10px;

  z-index: 1;
}
.icon-display {
  row-gap: 10px;
}
</style>