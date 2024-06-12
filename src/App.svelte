<script>
  import Favorite from "./lib/Favorite/Favorite.svelte";
  import Header from "./lib/Header/Header.svelte";

  import data from "./lib/data.json";

  let shortcuts = {};

  function openShortcut(e) {
      const el = shortcuts[e.key];
      if (e.ctrlKey) return;
      if (el) el.open();
  }

  let dataPromise = browser.storage.local.get("new-tab-data") ?? data;
</script>

<svelte:window on:keyup={openShortcut} />

{#await dataPromise}
  <p>Loading new-tab data from storage.</p>
{:then ntdata}
  {@const data = ntdata["new-tab-data"] ?? {}}
  <!--pre>{JSON.stringify(data, null, 2)}</pre-->

  <div class="d-flex align-items-center justify-content-space-around">
    <span class="title">{data["title"] ?? "New Tab"}</span>
  </div>
  <div class="content">
  {#each data["data"] ?? [] as entry}
    {#if entry.type == "header"}
      <Header text={entry.text}/>
    {/if}
    {#if entry.type == "favorite"}
      <Favorite url={entry.url} label={entry.label} icon={entry.icon} shortcut={entry.shortcut} bind:this={shortcuts[entry.shortcut?.toLowerCase()]}/>
    {/if}
  {/each}
  </div>
{:catch error}
  <p style="color: red">Could not load new-tab data from storage.</p>
  <code>{error}</code>
{/await}

<style>
.title {
  font-size: 32px;
  font-weight: bold;
}
</style>