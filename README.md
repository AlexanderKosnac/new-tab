# New Tab Page

Build a static, dark themed "New Tab" page based on a simple json file.

It creates a simple static html file with sections and linked icons based on
the provided structure in the json input.

Take a look at `example.json`, which covers all available structures. It is
ready to build and can be built with the make target `build-example`.

Call the Python script like this:

```
python build.py <input_file> <profile> <assets_dir> <output_dir>
```

## Problems with Firefox

Firefox removed the ability to configure the "New Tab" Page some time ago
(for security reasons), so we need a workaround.

From the base directory of your Firefox installation, create the following two
files with the respective content:


`autoconfig.cfg`

Set the path to the html file in `PATH`

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
