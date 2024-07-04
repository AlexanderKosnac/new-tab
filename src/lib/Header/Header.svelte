<script>
    export let data;
    export let editable;
</script>

{#if editable}
<div class="header" bind:textContent={data.text} contenteditable>{data.text}</div>
{:else}
<div class="header">{data.text}</div>
{/if}

<style>
.header {
  font-size: 24px;
  font-weight: bold;
  min-width: 50px;
}
</style>