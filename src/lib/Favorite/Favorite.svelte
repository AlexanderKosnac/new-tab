<script>
    export let url;
    export let label;
    export let icon = "placeholder.svg";

    import { base } from '$app/paths'
</script>

<div class="fav-element">
    <a href="{url}" class="link-element" draggable="false">
        <div class="link-icon">
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
}
</style>