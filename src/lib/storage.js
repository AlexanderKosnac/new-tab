import { writable } from "svelte/store";

export const newTabData = writable({});

export const state = writable({
    editable: false,
    editMenu: {
        type: "",
        open: false,
        idx: NaN,
        x: 0,
        y: 0,
    }
});
