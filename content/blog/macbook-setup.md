---
title: "Macbook Setup"
date: 2017-07-19T18:57:02-07:00
draft: true
---

When I got my new computer for work, I realized I had to reinstall and set up
everything that had taken me years to curate on my old computer. And ... turns
out I have a really custom setup. Here are the steps I took to install
everything I need to get started.

## Personal web and input preferences

- [Google Chrome Browser](https://www.google.com/chrome/browser/desktop/index.html)
- ~Quicksilver~ - deprecated in favor of Spotlight Search
- Add Russian language for input sources
- Remove all Apple software from doc except preferences

## Development environment

- Git/XCode (type `git` at the Terminal and mac OS Sierra knows you're a coder
  and installs tools for you)

### Integrated development environment (IDE)

[PyCharm](https://www.jetbrains.com/pycharm/) is a fantastic IDE for Python
developers. It's excellent in part because it leverages the entire JetBrains
ecosystem, which has great plugins e.g. for Markdown and `.gitignore` files.

- Set margin columns to 79
- Enable soft wrapping
- `.ignore` plugin
- Solarized theme: https://github.com/jkaving/intellij-colors-solarized

Plugins:
- [Markdown Navigator](https://vladsch.com/product/markdown-navigator)
- [`.ignore`](https://plugins.jetbrains.com/plugin/7495--ignore)


### Terminal preferences

- oh my zsh: https://github.com/robbyrussell/oh-my-zsh
  - Add a few plugins: `plugins=(git osx python)`
  - Uncomment a few lines:
```zsh
# Uncomment the following line to enable command auto-correction.
ENABLE_CORRECTION="true"

... more options ...

# Preferred editor for local and remote sessions
# Changed to `emacs`
if [[ -n $SSH_CONNECTION ]]; then
  export EDITOR='vim'
else
  export EDITOR='mvim'
fi

... more options ...

# ssh
export SSH_KEY_PATH="~/.ssh/rsa_id" 
```

Add alias for Triton Supercomputing Cluster (TSCC):

```zsh
# Alias to Triton Supercomputing Cluster (TSCC)
alias tscc="ssh obotvinnik@tscc-login2.sdsc.edu"
```

Never use `vi`/`vim`:

```zsh
# >:)
alias vim=emacs
alias vi=emacs
```

- `ssh` keys
  - [Create a new `ssh` key](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)
  - [Add `ssh` key to GitHub](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/)
  - Log on to TSCC and add ssh key to accepted keys with
    [one line](http://www.linuxproblem.org/art_9.html]:

```bash
cat .ssh/id_rsa.pub | ssh obotvinnik@tscc.sdsc.edu 'cat >> .ssh/authorized_keys'
```


- Terminal settings
  - Mac OS Sierra's high contrast I-beam is on point. I've lost that cursor so many times in El Capitan
  - [Solarized scheme](https://github.com/tomislav/osx-terminal.app-colors-solarized)
  - [Inconsolata font, 14 point](https://fonts.google.com/specimen/Inconsolata)
  - [Set `option` as the `Meta` key for `emacs`](https://www.emacswiki.org/emacs/EmacsForMacOS#toc21): Preferences > Settings > Keyboard > Use option as meta key
- Anaconda Python
  - Make sure to copy the lines added to `~/.bash_profile` to `~/.zshrc` since Anaconda doesn't know you use `oh-my-zsh`
  - Make separate environments for each github repo
    - [Add kernels to Jupyter notebooks](https://ipython.readthedocs.io/en/latest/install/kernel_install.html)
    - For each environment, need to do:
```bash
source activate kvector-env
conda install ipykernel
python -m ipykernel install --user --name myenv --display-name "Python 3.6 (kvector-env)"
```
- Homebrew
  - `hub`
    - `brew install hub`: https://github.com/github/hub/issues/978
    - Add token for command line access so you can do `git pull-request` on the
      command line: https://github.com/github/hub/issues/978
    - `brew install git-lfs` for git large file storage
  - `tree` to view directory trees from the command line
  - `watch` to rerun commands forever


## Folder organization

I decided to keep all my github repositories in my home directory, under `~/code`.

  - Downloaded GitHub repos from grad school that I'm still working on

## Other software
Here are some other software packages that I find very useful to use on my Mac.

- [Caffeine](http://lightheadsw.com/caffeine/) - Turn off the screen dimming on
  your mac - keep it "awake" :)
- [Toggl](https://www.toggl.com) for time tracking so I know how long I spend on projects. This was especially useful for seeing how long formatting my dissertation took
- [VLC](http://www.videolan.org/vlc/index.html) - Watch videos in something
  other than .mov or .mp4 format
- [Flux](https://justgetflux.com/) - Dim the blue light in your screen at night
  so you sleep better