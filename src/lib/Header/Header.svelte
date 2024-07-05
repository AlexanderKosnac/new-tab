<script>
    import { newTabData } from "$lib/storage.js";

    export let idx;
    export let editable;
</script>

{#if editable}
<div class="header" bind:textContent={data.text} contenteditable>{data.text}</div>
{:else}
<div class="header">{$newTabData["data"][idx].text}</div>
{/if}

<style>
.header {
  font-size: 24px;
  font-weight: bold;
  min-width: 50px;
}
</style>