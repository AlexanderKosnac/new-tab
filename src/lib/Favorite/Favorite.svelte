<script>
    export let data;
    export let editable;

    $: icon = data.icon ?? "placeholder.svg";

    let favEl;
    let linkEl;
    let iconEl;

    export function open() {
        iconEl.animate(
            [{ background: "#A0A0A0" }],
			{ duration: 100, direction: "alternate", iterations: 2 },
        );
        linkEl.click();
    }
</script>

<div class="fav-element" bind:this={favEl} draggable="false">
    <a href="{editable ? "javascript: void(0)" : data.url}" class="link-element" bind:this={linkEl} draggable="false">
        {#if editable}
            <div class="shortcut" class:transient={!data.shortcut} bind:textContent={data.shortcut} contenteditable>{data.shortcut ?? ""}</div>
        {:else}
            {#if data.shortcut}
            <div class="shortcut">{data.shortcut}</div>
            {/if}
        {/if}
    
        <div class="link-icon" bind:this={iconEl}>
            <img class="icon" alt="Icon" src="./icons/{icon}" draggable="false" />
        </div>
    </a>
    {#if editable}
    <span class="link-label" bind:textContent={data.label} contenteditable>{data.label}</span>
    {:else}
    <span class="link-label">{data.label}</span>
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
</style>