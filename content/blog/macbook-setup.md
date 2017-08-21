---
title: "Macbook Setup"
date: 2017-08-17T16:57:02-07:00
draft: False
---

When I got my new computer for work, I realized I had to reinstall and set up
everything that had taken me years to curate on my old computer. And ... turns
out I have a really custom setup. Here are the steps I took to install
everything I need to get started.

## Personal web and input preferences

- [Google Chrome Browser](https://www.google.com/chrome/browser/desktop/index.html)
- ~Quicksilver~ - deprecated in favor of Spotlight Search
- Add Russian language for input sources
- Remove all Apple software from dock except "System Preferences"

## Development environment

- Git/XCode (type `git` at the Terminal and mac OS Sierra knows you're a coder
  and installs tools for you)

### (Interactive) Python Debugger Settings

When I can, I prefer to use the interactive Python debugger (`ipdb`) over the
built-in `pdb`. For example, when debugging
[dobby](https://github.com/czbiohub/dobby) instead of running `python -m pdb
dobby/cli.py`, I'll run `python -m ipdb dobby.cli.py`. To make `pdb` especially
useful, I really like using these aliases which are super helpful to navigate
the stack trace and print the variables you have around.

```bash
# Ned's .pdbrc from https://stackoverflow.com/questions/1623039/python-debugging-tips

# Print a dictionary, sorted. %1 is the dict, %2 is the prefix for the names.
alias p_ for k in sorted(%1.keys()): print "%s%-15s= %-80.80s" % ("%2",k,repr(%1[k]))

# Print the instance variables of a thing.
alias pi p_ %1.__dict__ %1.

# Print the instance variables of self.
alias ps pi self

# Print the locals.
alias pl p_ locals() local:

# Next and list, and step and list.
alias nl n;;l
alias sl s;;l

# Short cuts for walking up and down the stack
alias uu u;;u
alias uuu u;;u;;u
alias uuuu u;;u;;u;;u
alias uuuuu u;;u;;u;;u;;u
alias dd d;;d
alias ddd d;;d;;d
alias dddd d;;d;;d;;d
alias ddddd d;;d;;d;;d;;d
```

Copy the above text into the clipboard and paste it into your `~/.pdbrc` file
with one command:

```
pbpaste > ~/.pdbrc
```

`pbpaste` stands for "Pasteboard" paste, which takes the contents of your
clipboard so you can use it on the command line. There's also `pbcopy` which
you can pipe `stdout` into the clipboard, e.g. to paste your `~/.pdbrc` file:


```
cat ~/.pdbrc | pbcopy
```

### Integrated development environment (IDE)

[PyCharm](https://www.jetbrains.com/pycharm/) is a fantastic IDE for Python
developers. It's excellent in part because it leverages the entire JetBrains
ecosystem, which has great plugins e.g. for Markdown and `.gitignore` files.

- Set margin columns to 79
- Enable soft wrapping
- Solarized theme: https://github.com/jkaving/intellij-colors-solarized

Plugins:

- [Markdown Navigator](https://vladsch.com/product/markdown-navigator)
- [`.ignore`](https://plugins.jetbrains.com/plugin/7495--ignore)


### Terminal preferences

- oh my zsh: https://github.com/robbyrussell/oh-my-zsh
- Edit `~/.zshrc`:
  - Add a few plugins: `plugins=(git osx python)`
  - Uncomment a few lines:

```bash
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

```bash
# Alias to Triton Supercomputing Cluster (TSCC)
alias tscc="ssh obotvinnik@tscc-login2.sdsc.edu"
```

Never use `vi`/`vim`:

```bash
# >:)
alias vim=emacs
alias vi=emacs
```

### `ssh` keys

- [Create a new `ssh` key](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)
- [Add `ssh` key to GitHub](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/)
- Log on to TSCC and add ssh key to accepted keys with
[one line](http://www.linuxproblem.org/art_9.html):

```bash
cat .ssh/id_rsa.pub | ssh obotvinnik@tscc.sdsc.edu 'cat >> .ssh/authorized_keys'
```

### Mac OS Terminal program settings
Here are my personal preferences for setting up the terminal in Mac OS.

*Side
Note: Mac OS Sierra's high contrast I-beam is on point. I've lost that cursor
so many times in El Capitan.*

- [Solarized scheme](https://github.com/tomislav/osx-terminal.app-colors-solarized)
- [Inconsolata font, 14 point](https://fonts.google.com/specimen/Inconsolata)
- [Set `option` as the `Meta` key for `emacs`](https://www.emacswiki.org/emacs/EmacsForMacOS#toc21): Preferences > Settings > Keyboard > Use option as meta key

### Python (Anaconda Distribution)

Installing scientific Python packages from scratch is a pain and you will lose
weeks of your life setting up your `LD_LIBRARY_PATH` and hunting down Math
Kernel Libraries (if you're really interested, check out
[this blog post](http://alexsavio.github.io/numpy_scipy_mkl.html)). Enter the
[Anaconda Python Distribution](https://www.continuum.io/downloads), which makes
installing math-heavy python a total breeze.

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
### Homebrew

[Homebrew](https://brew.sh/) is the "missing package manager" for Mac OS. It
lets you install software from the command line in an `sudo apt-get`-like way
like you can do in Linux systems! It's super useful.

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Here are all the programs I installed. For all of them, you install them with
`brew install commandname`, e.g. `brew install hub` for the command `hub`.

- [`hub`](https://hub.github.com/) which a command line wrapper for git that
  lets you do pull requests and such from the command line!
- Add
  [GitHub access token ](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/)token
  for command line access so you can do `hub pull-request` on the command line.
  To save this personal access token securely so you'll never have to type in
  your password for the command line again, you need to do two things:

  1. Tell the command line git to use the
  [credential-osxkeychain](https://help.github.com/articles/caching-your-github-password-in-git/)
  as a place to look for passwords.

  ```
  ➜  manuscript git:(master) git config --global credential.helper osxkeychain
  ```

  2. Push to a repository, using your username (mine is `olgabot`) and the
  token as th1e password. From now on, your computer should remember your token

  ```
  ➜  manuscript git:(master) git push -u origin master   Username for 'https://github.com': olgabot
  Password for 'https://olgabot@github.com': 
  Counting objects: 636, done.
  Delta compression using up to 8 threads.
  Compressing objects: 100% (273/273), done.
  Writing objects: 100% (636/636), 174.08 KiB | 0 bytes/s, done.
  Total 636 (delta 350), reused 636 (delta 350)
  remote: Resolving deltas: 100% (350/350), done.
  To https://github.com/singlecell-batches/manuscript.git
  * [new branch]      master -> master
  Branch master set up to track remote branch master from origin.
  ```

  3. Double check that it worked. Open "Keychain" and check that
  `https://github.com` is listed a website (the `https` is important)

- `brew install git-lfs` for git large file storage
- `tree` to view directory trees from the command line
- `watch` to rerun commands forever, e.g. use `watch --interval 1 ls` to
rerun ls every second so you can see files get updated while some process
is running.
- `hg` for Mercurial source code repositories
- `cmake` for software that uses `cmake` instead of Make to build stuff
- [`gifsicle`](https://www.lcdf.org/gifsicle/) for making Gifs on the command line
- [`imagemagick`](https://www.imagemagick.org/script/index.php) for
manipulating image types on the command line
- `ruby` for managing Ruby Gems such as Jekyll and Travis-CI. Plus there's a
  nice `gist` tool for creating gists from the command line Then ...
    - `brew install gem`
    - `brew install jekyll`
    - `brew install travis`
  - `brew install gist` - nice tool for creating gists from files via the
    command line

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