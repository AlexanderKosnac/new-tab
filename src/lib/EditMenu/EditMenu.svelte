<script>
    import { newTabData, state } from "$lib/storage.js";

    function close() {
        $state.editMenu.open = false;
    }

    function setIcon(key) {
        $newTabData["data"][$state.editMenu.idx].icon = key;
    }

    function moveUp() {
        const idx = $state.editMenu.idx;
        if (idx == 0) return;
        let tmp = $newTabData["data"][idx-1];
        $state.editMenu.idx -= 1;
        $newTabData["data"][idx-1] = $newTabData["data"][idx];
        $newTabData["data"][idx] = tmp;
    }

    function moveDown() {
        const idx = $state.editMenu.idx;
        if (idx == $newTabData["data"].length) return;
        let tmp = $newTabData["data"][idx+1];
        $state.editMenu.idx += 1;
        $newTabData["data"][idx+1] = $newTabData["data"][idx];
        $newTabData["data"][idx] = tmp;
    }

    function deleteThis() {
        $newTabData["data"].splice($state.editMenu.idx, 1);
        $newTabData = $newTabData;
        close();
    }
</script>

<div class="menu" class:hidden={!$state.editMenu.open} style="left: {$state.editMenu.x}px; top: {$state.editMenu.y}px">
    <div class="d-flex flex-row justify-content-space-between">
        <div><strong>Edit Menu</strong></div>
        <div>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="white" viewBox="0 0 16 16" on:click={close}>
                <path d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8z"/>
            </svg>
        </div>
    </div>
    <div class="menu-content d-flex flex-column gap-3">
        <div>
            <input type="button" class="ntinput" value="Move up" on:click={moveUp}/>
            <input type="button" class="ntinput" value="Move down" on:click={moveDown}/>
        </div>
        {#if $state.editMenu.idx}
            <input type="text" class="ntinput" placeholder="URL" bind:value={$newTabData["data"][$state.editMenu.idx].url}/>
        {/if}
        <div>
            <input type="button" class="ntinput" value="Remove this Element" on:click={deleteThis}/>
        </div>
        <div class="d-flex flex-wrap icon-list">
            {#each Object.entries($newTabData["icons"] ?? {}) as [key, base64]}
            <img class="icon hover-highlight" src="{base64}" alt="icon" title="{key}" on:click={() => setIcon(key)}/>
            {/each}
        </div>
    </div>
</div>

<style>
.menu {
    position: absolute;

    z-index: 2;

    padding: 10px;

    background-color: var(--main-background);
    border-width: 1px;
    border-radius: 5px;
    box-shadow: 0 0 5px black;

    width: 300px;
}

.menu-content {
    max-height: 300px;
    overflow-y: scroll;
}

.icon {
    border-radius: 7px;
    min-width:  40px;
    max-width:  40px;
    min-height: 40px;
    max-height: 40px;
}

.icon.hover-highlight:hover {
    box-shadow: 0 0 10px white;
}

.icon-list {
    gap: 10px;
    row-gap: 10px;
}

.hidden {
    display: none;
}
</style>