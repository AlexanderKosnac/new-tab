import { writable } from 'svelte/store';
import { browser } from '$app/environment';

export function localStorageStore(key, initialValue) {
  if (!browser) return initialValue;

  let serialize = JSON.stringify;
  let deserialize = JSON.parse;

  let storedValue = deserialize(localStorage.getItem(key));

  let store = writable(storedValue ? storedValue : initialValue);
  store.subscribe((value) => localStorage.setItem(key, serialize(value)));

  return store;
}