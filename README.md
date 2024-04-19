# markdown file links

A way to link to other Markdown (and non-Markdown) files from your Markdown notes.

https://github.com/kevinfiol/sublime_markdown_file_links/assets/4752973/0c9350ca-7a41-4daa-95c0-e4356b9bd72a

## Installation

### Manually

1. Navigate to your `Packages` folder (easiest way to find it is from within Sublime Text, go to `Preferences > Browse Packages...`).
2. Download the latest release from the [releases page](https://github.com/kevinfiol/markdown_file_links/releases).
3. Unzip the downloaded archive. Copy the directory `markdown_file_links-x.x.x` into your `Packages` folder.

### With Git

Use `git clone` to clone this repository into your `Packages` folder.

```bash
# From within your `Packages` folder
git clone https://github.com/kevinfiol/markdown_file_links.git
```

## Usage

In your Markdown files, link to other files using the `[[file_path]]` notation:
```md
Go to [[todos]].
```
By default, the plugin will assume an extension of `.md`.

Relative paths from the current file can be used to link to nested files, or files in parent directories. This works as you'd expect.

```md
Go to [[nested/markdown/file.md]]

Go to [[../../todos]]

Go to [[./cat_picture.jpg]]
```

## Credits

Big thanks to [OdatNurd](https://github.com/OdatNurd) for always fielding Sublime Text plugin development questions.
