import { writable } from "svelte/store";

export const newTabData = writable({});

export const state = writable({
    editMenu: {
        open: false,
        idx: 0,
        x: 0,
        y: 0,
    }
});
