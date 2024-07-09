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

    function openIconSelection(e) {
        if (!$state.editable) return;

        $state.editMenu.open = !($state.editMenu.open && $state.editMenu.idx == idx);

        $state.editMenu.idx = idx;
        $state.editMenu.x = e.clientX + window.scrollX;
        $state.editMenu.y = e.clientY + window.scrollY;
    }
</script>

<div class="fav-element">
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