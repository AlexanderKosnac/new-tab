# New Tab Page

Build a generic "New Tab" page. You can find an example deployed on [GitHub pages](https://alexanderkosnac.github.io/new-tab/).


## Build

To compile the page, run the following:

```bash
npm run build
```

The result is found in the `build` directory.


## Problems with Firefox

Firefox removed the ability to configure the "New Tab" Page some time ago
(for security reasons), so we need a workaround.

From the base directory of your Firefox installation, create the following two
files with the respective content:


`autoconfig.cfg`

Set the path to the HTML file in `PATH`

```javascript
// comment required
var {classes:Cc,interfaces:Ci,utils:Cu} = Components;

try {
    Cu.import("resource:///modules/AboutNewTab.jsm");
    AboutNewTab.newTabURL = "<PATH>";
} catch(e){
    Cu.reportError(e);
}
```


`defaults/pref/autoconfig.js`

```javascript
// comment required
pref("general.config.filename", "autoconfig.cfg");
pref("general.config.obscure_value", 0);
pref("general.config.sandbox_enabled", false);
```
