<script>
  import Favorite from "$lib/Favorite/Favorite.svelte";
  import Header from "$lib/Header/Header.svelte";

  import data from "$lib/data.json";

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
    <span class="title">{d["title"] ?? "New Tab"}</span>
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
</style>