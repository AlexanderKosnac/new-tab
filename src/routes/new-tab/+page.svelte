<script>
  import { onMount } from "svelte";

  import Favorite from "$lib/Favorite/Favorite.svelte";
  import Header from "$lib/Header/Header.svelte";

  import data from "$lib/data.json";
  import { newTabData } from "$lib/storage.js";

  let editable = false;
  let saveStatus;

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
  let selectedElementKey = "favorite";

  let shortcuts = {};

  function openShortcut(e) {
      const el = shortcuts[e.key];
      if (e.ctrlKey || editable) return;
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

  function newEntry() {
    newTabData["data"].push(structuredClone(componentMapping[selectedElementKey].default));
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

  <div class="d-flex align-items-center justify-content-space-around gap-2">
    <div class="title" style="flex-grow: 1">{$newTabData["title"] ?? "New Tab"}</div>
    {#if editable}
      <div bind:this={saveStatus} class="save-status flash-and-hide hidden"></div>
      <button class="ntinput green" on:click={save}>Save</button>
    {/if}
    <svg id="btnEdit" xmlns="http://www.w3.org/2000/svg" width="24" height="24" class:editable={editable} stroke="white" viewBox="0 0 16 16" on:click={() => { editable = !editable }}>
      <path transform="scale(0.9 0.9) translate(1 1)" d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z"/>
    </svg>
  </div>
  <div class="content">
  {#each $newTabData["data"] ?? [] as entry, idx}
    <svelte:component this={componentMapping[entry.type].clazz} {idx} {editable} bind:this={shortcuts[entry.shortcut?.toLowerCase()]} />
  {/each}
  </div>
  {#if editable}
  <div>
    <select class="ntinput" bind:value={selectedElementKey}>
      {#each Object.entries(componentMapping) as [key, data]}
      <option value={key}>{data.display}</option>
      {/each}
    </select>

    <button class="ntinput" on:click={newEntry}>Create Element</button>
  </div>
  {/if}
{:catch error}
  <div class="font-error">
    <p>Failed to load new-tab data from storage.</p>
    <code>{error}</code>
  </div>
{/await}

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
</style>