<script>
    import Favorite from "$lib/Favorite/Favorite.svelte";
    import Header from "$lib/Header/Header.svelte";

    import data from '$lib/data.json';
</script>

{#if data}
<div class="title">{data["title"] ?? "New Tab"}</div>
<div class="content">
{#each data["data"] ?? [] as entry}
    {#if entry.type == "header"}
        <Header text={entry.text}/>
    {/if}
    {#if entry.type == "favorite"}
        <Favorite url={entry.url} label={entry.label} icon={entry.icon}/>
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