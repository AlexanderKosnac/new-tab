# New Tab

A plugin that replaces the default "New Tab" page in the browser with a more useful alternative.

The plugin is published on the [Mozilla add-ons site](https://addons.mozilla.org/en-US/firefox/addon/new-tab-droplet/).


## Build

To build the plugin, install the dependencies:

```bash
npm install
```

After that, the plugin can be build with:

```bash
npm run build
```

The built plugin is found in the `build` directory.


## Development

For development, `web-ext` can be useful. Install it via npm:

```bash
npm install --global web-ext
```

Switch into the `build` directory and check for errors and warnings with `web-ext lint` command.
Use `web-ext run` to run a separate, special browser instance that automatically reloads the changes in the `build` directory.
Note that you still have to run `npm run build`, to compile the changes into the `build` directory.
