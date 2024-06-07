<script>
    import Favorite from "$lib/Favorite/Favorite.svelte";
    import Header from "$lib/Header/Header.svelte";

    import data from '$lib/data.json';

    let shortcuts = {};

    function openShortcut(e) {
        const el = shortcuts[e.key];
        if (e.ctrlKey) return;
        if (el) el.open();
    }
</script>

<svelte:window on:keyup={openShortcut} />

{#if data}
<div class="title">{data["title"] ?? "New Tab"}</div>
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
{/if}

<style>
.title {
    font-size: 32px;
    font-weight: bold;
}
</style>