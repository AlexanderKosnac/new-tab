<script>
  import data from "./lib/data.json";

  let ntdata;

  function save() {
    console.log(ntdata);
    browser.storage.local.set({ "new-tab-data": ntdata });
  }

  function clear() {
    browser.storage.local.remove("new-tab-data");
  }

  function restoreDefault() {
    browser.storage.local.set({ "new-tab-data": data });
  }

  let dataPromise = browser.storage.local.get("new-tab-data");
  dataPromise.then(it => { ntdata = it["new-tab-data"] }, () => {});
</script>

{#await dataPromise}
  <p>Loading new-tab data from storage.</p>
{:then _}
  <div style="display: flex; flex-direction: column; gap: 2px">
    <div style="display: flex; flex-direction: row; gap: 2px">
      <button type="button" on:click={save}>Save</button>
      <button type="button" on:click={restoreDefault}>Default</button>
      <button type="button" on:click={clear}>Clear</button>
    </div>
    <br>
    <label>
      Title:
      <input type="text" bind:value={ntdata["title"]}/>
    </label>
  </div>

  <pre>{JSON.stringify(ntdata, null, 2)}</pre>
{:catch error}
  <p style="color: red">Could not load new-tab data from storage.</p>
  <code>{error}</code>
{/await}

<style>
</style>