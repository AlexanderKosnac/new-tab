<script>
  import Favorite from "$lib/Favorite/Favorite.svelte";
  import Header from "$lib/Header/Header.svelte";

  import data from "$lib/data.json";

  let editable = false;

  const componentMapping = {
    "header": Header,
    "favorite": Favorite,
  };

  let shortcuts = {};

  function openShortcut(e) {
      const el = shortcuts[e.key];
      if (e.ctrlKey) return;
      if (el) el.open();
  }

  import { onMount } from 'svelte';
  let dataPromise;
  onMount(() => {
    dataPromise = chrome.storage.local.get("new-tab-data");
  });
</script>

<svelte:window on:keyup={openShortcut} />

{#await dataPromise}
  <p>Loading new-tab data from storage.</p>
{:then ntdata}
  {#if ntdata}
  {@const d = ntdata["new-tab-data"] ?? data}
  <!--pre>{JSON.stringify(data, null, 2)}</pre-->

  <div class="d-flex align-items-center justify-content-space-around">
    <div class="title">{d["title"] ?? "New Tab"}</div>
    <svg id="btnEdit" xmlns="http://www.w3.org/2000/svg" width="24" height="24" class:editable={editable} stroke="white" viewBox="0 0 16 16" on:click={() => { editable = !editable }}>
      <path transform="scale(0.9 0.9) translate(1 1)" d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z"/>
    </svg>
  </div>
  <div class="content">
  {#each d["data"] ?? [] as entry}
    <svelte:component this={componentMapping[entry.type]} data={entry} bind:this={shortcuts[entry.shortcut?.toLowerCase()]} />
  {/each}
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
</style>