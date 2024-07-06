<script>
    import { newTabData, state } from "$lib/storage.js";

    export let idx;

    function deleteThis() {
        $newTabData["data"].splice(idx, 1);
        $newTabData = $newTabData;
    }
</script>

{#if $state.editable}
<div class="d-flex align-items-center">
    <div class="header" bind:textContent={$newTabData["data"][idx].text} contenteditable>{$newTabData["data"][idx].text}</div>
    <svg xmlns="http://www.w3.org/2000/svg" class="btn-delete" width="16" height="16" fill="#C80036" viewBox="0 0 16 16" on:click={deleteThis}>
        <circle cx="50%" cy="50%" r="7" fill="white"/>
        <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0M5.354 4.646a.5.5 0 1 0-.708.708L7.293 8l-2.647 2.646a.5.5 0 0 0 .708.708L8 8.707l2.646 2.647a.5.5 0 0 0 .708-.708L8.707 8l2.647-2.646a.5.5 0 0 0-.708-.708L8 7.293z"/>
    </svg>
</div>
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