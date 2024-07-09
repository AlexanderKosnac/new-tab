<script>
    import { newTabData, state } from "$lib/storage.js";

    export let idx;

    function openEditMenu(e) {
        if (!$state.editable) return;

        $state.editMenu.type = "header";
        $state.editMenu.open = !($state.editMenu.open && $state.editMenu.idx == idx);

        $state.editMenu.idx = idx;
        $state.editMenu.x = e.clientX + window.scrollX;
        $state.editMenu.y = e.clientY + window.scrollY;
    }
</script>

{#if $state.editable}
<div class="header" bind:textContent={$newTabData["data"][idx].text} contenteditable on:contextmenu|preventDefault={openEditMenu}>{$newTabData["data"][idx].text}</div>
{:else}
<div class="header">{$newTabData["data"][idx].text}</div>
{/if}

<style>
.header {
    font-size: 24px;
    font-weight: bold;
    min-width: 50px;
    margin-right: 10px;
    min-height: 1em;
}
</style>