<script>
    import { newTabData, state } from "$lib/storage.js";

    export let idx;

    $: icon = $newTabData["data"][idx].icon ?? "placeholder.svg";

    let linkEl;
    let iconEl;

    export function open() {
        iconEl.animate(
            [{ background: "#A0A0A0" }],
			{ duration: 100, direction: "alternate", iterations: 2 },
        );
        linkEl.click();
    }

    function deleteThis() {
        $newTabData["data"].splice(idx, 1);
        $newTabData = $newTabData;
    }

    function openIconSelection(e) {
        if (!$state.editable) return;

        $state.editMenu.open = !($state.editMenu.open && $state.editMenu.idx == idx);

        $state.editMenu.idx = idx;
        $state.editMenu.x = e.clientX + window.scrollX;
        $state.editMenu.y = e.clientY + window.scrollY;
    }
</script>

<div class="fav-element">
    {#if $state.editable}
    <svg xmlns="http://www.w3.org/2000/svg" class="btn-delete" width="16" height="16" fill="#C80036" viewBox="0 0 16 16" on:click={deleteThis}>
        <circle cx="50%" cy="50%" r="7" fill="white"/>
        <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0M5.354 4.646a.5.5 0 1 0-.708.708L7.293 8l-2.647 2.646a.5.5 0 0 0 .708.708L8 8.707l2.646 2.647a.5.5 0 0 0 .708-.708L8.707 8l2.647-2.646a.5.5 0 0 0-.708-.708L8 7.293z"/>
    </svg>
    {/if}
  
    <a href="{$state.editable ? "javascript: void(0)" : $newTabData["data"][idx].url}" class="link-element" bind:this={linkEl}>
        {#if $state.editable}
            <div class="shortcut" class:transient={!$newTabData["data"][idx].shortcut} bind:textContent={$newTabData["data"][idx].shortcut} contenteditable>{$newTabData["data"][idx].shortcut ?? ""}</div>
        {:else}
            {#if $newTabData["data"][idx].shortcut}
            <div class="shortcut">{$newTabData["data"][idx].shortcut}</div>
            {/if}
        {/if}
    
        <div class="link-icon" bind:this={iconEl}>
            <img class="icon" alt="Icon" src="{$newTabData["icons"][icon] ?? "./icons/placeholder.svg"}" draggable="false" on:click={openIconSelection}/>
        </div>
    </a>
    {#if $state.editable}
    <span class="link-label" bind:textContent={$newTabData["data"][idx].label} contenteditable>{$newTabData["data"][idx].label}</span>
    {:else}
    <span class="link-label">{$newTabData["data"][idx].label}</span>
    {/if}
</div>

<style>
.fav-element {
    display: inline-flex;
    flex-direction: column;
    align-items: center;
    border-radius: 7px;
    text-align: center;
    padding: 15px;
}

.link-element {
    position: relative;
}

.shortcut {
    position: absolute;
    transform: translate(-50%,-50%);
    top: 0;
    left: 100%;

    color: black;
    background-color: white;

    box-sizing: border-box;
    border-width: 1px;
    border-style: solid;
    border-color: darkgrey;
    border-radius: 50px;

    text-transform: capitalize;

    text-align: center;
    vertical-align: middle;

    --sc-size: 21px;
    width: var(--sc-size);
    height: var(--sc-size);
    line-height: var(--sc-size);
    font-weight: 900;
    font-size: 0.9em;
    white-space: nowrap;
}

.shortcut.transient {
    border-style: dashed;
    opacity: .5;
}

.fav-element:hover {
    background-color: var(--lighter-background);
}

.link-icon {
    background-color: var(--light-background);
    padding: 10px;

    box-shadow: 0 0 10px black;
    margin-bottom: 5px;
}

.link-icon, .icon {
    border-radius: 7px;
    min-width:  40px;
    max-width:  40px;
    min-height: 40px;
    max-height: 40px;
}

.link-label {
    font-size: small;
    min-width: 40px;
    max-width: 60px;
}
.btn-delete {
    position: relative;
    top: 4px;
    margin-top: -16px;

    z-index: 1;
}
</style>