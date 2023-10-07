# go-task-bin

https://github.com/go-task/task

https://taskfile.dev/

**Task** is a task runner / build tool that aims to be simpler and easier to use than, for example, [GNU Make](https://www.gnu.org/software/make/).

Since it's written in Go, Task is just a single binary and has no other dependencies, which means you don't need to mess with any complicated install setups just to use a build tool.

Once [installed](https://taskfile.dev/installation/), you just need to describe your build tasks using a simple [YAML](http://yaml.org/) schema in a file called Taskfile.yml:

```yaml
Taskfile.yaml
---
version: '3'

tasks:
  hello:
    cmds:
      - echo 'Hello World from Task!'
    silent: true
```

And call it by running task hello from your terminal.

The above example is just the start, you can take a look at the [usage](https://taskfile.dev/usage) guide to check the full schema documentation and Task features.


This is a python wrapper that can be installed with pip.

## install

```sh
pip install go-task-bin
```
