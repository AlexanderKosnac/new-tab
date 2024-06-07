<script>
    export let url;
    export let label;
    export let icon = "placeholder.svg";
    export let shortcut;

    import { base } from "$app/paths"

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

<div class="fav-element" bind:this={favEl}>
    <a href="{url}" class="link-element" bind:this={linkEl} draggable="false">
        {#if shortcut}
        <div class="shortcut">{shortcut}</div>
        {/if}
        <div class="link-icon" bind:this={iconEl}>
            <img class="icon" alt="Icon" src="{base}/icons/{icon}">
        </div>
    </a>
    <span class="link-label">{label}</span>
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
    border: 1px solid darkgrey;

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
    max-width: 60px;
}
</style>