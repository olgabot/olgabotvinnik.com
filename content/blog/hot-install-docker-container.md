---
title: "Hot Install Docker Container"
date: 2020-02-19T08:36:13-08:00
draft: false
tags: [docker]
categories: [context-switch, deep-work]
---

Ever run into a situation where you need to update just *one* dependency in a docker image? I ran into this while working on [this](https://github.com/czbiohub/nf-predictorthologs) [Nextflow](http://nextflow.io/) pipeline made from the [nf-core](https://nf-co.re/) template. In this template, the `environment.yml` is used to specify the dependencies, which is awesome for reproducibility and portability, as `conda` works with virtually any system. But, if you're developing, the build time of the images is ~1 hour to resolve all the dependencies, which really reduces the developer's iteration time, and thus the efficiency of development. I personally really hate context switching between tasks and prefer to do [deep work](https://olgabotvinnik.com/blog/time-is-citations/) on one thing at a time. As Cal Newport says, [our brains our not multithreaded](https://www.calnewport.com/blog/2019/09/10/our-brains-are-not-multi-threaded/) like computers are.

So the workflow would look like:

1. Get an error in my Python package during the Nextflow Workflow
1. Make a change in the Python package, commit and push to GitHub
1. Rebuild the docker image
1. Wait an hour while the docker image rebuilds
1. Context switch to something else
1. Forget what I fixed in the first place
1. Docker build finishes --> Rerun Nextflow workflow
1. Get some new error and not understand it because I lost my train of thought


So you're writing a custom Python package on a Nextflow workflow, then you are constantly updating the underlying code, and don't want to have to wait for all the dependencies to get resolved.


Enter hot-installing. I just made that up. In web development, there's "[hot reloading](https://facebook.github.io/react-native/blog/2016/03/24/introducing-hot-reloading.html)" which refreshes the HTML page every time you touch the Javascript/CSS/HTMl that goes into making it. This is somewhat similar, but now when I make a change in a depending Python Package, instead of taking hours to rebuild the docker image, I can quickly reinstall that one package from GiHub, and move on my merry way.


So now my workflow looks like this:

1. Get an error in my Python package during the Nextflow Workflow
2. Make a change in the Python package, commit and push to GitHub
3. Hot-install Python package below
4. Rerun Nextflow workflow
5. Add tests to the Python package while the Nextflow workflow is running because I'm still in the "fixed the error" context and can remember what I did!

## Hot-install a Python package on a Docker container
Run the docker container with your installation command. In my case, this is `pip install -U git+https://github.com/czbiohub/kh-tools.git@olgabot/more-encodings#egg=khtools`

```
(kh-tools--more-encodings)
 Wed 19 Feb - 08:08  ~/code/nf-predictorthologs   origin ☊ olgabot/initial-outline ↑5 3● 
  docker run czbiohub/predictorthologs:dev pip install -U git+https://github.com/czbiohub/kh-tools.git@olgabot/more-encodings#egg=khtools
```

Next, use `docker ps -l` to show all docker processes, since this container is still running.

```
 Wed 19 Feb - 08:21  ~/code/nf-predictorthologs   origin ☊ olgabot/initial-outline ↑7 1● 
 docker ps -l                                                                                                       CONTAINER ID        IMAGE                           COMMAND                  CREATED             STATUS                      PORTS               NAMES
a4e7c3f7eed3        czbiohub/predictorthologs:dev   "pip install -U git+…"   33 seconds ago      Exited (0) 28 seconds ago                       brave_heisenberg
```

Copy that commit hash, in this case `a4e7c3f7eed3`, and commit the changes to the container using `docker commit`.

```
(kh-tools--more-encodings)
 Wed 19 Feb - 08:21  ~/code/nf-predictorthologs   origin ☊ olgabot/initial-outline ↑7 1● 
  docker commit a4e7c3f7eed3  czbiohub/predictorthologs:dev
sha256:af9153554838c8bea54260a3c8ab284e9b093b687c5f6b732b1a8c3c866da8b8
```

It doesn't seem that there's a single one-line command one can run to run and commit to a new image, other than using a `Dockerfile` and using your existing container with `FROM czbiohub/predictorthologs:dev` at the top. But then you run into overwriting the docker image tag with a new one, and the container name is hard-coded into the Nextflow pipeline... so I'd rather not.

Hope that helps you!
