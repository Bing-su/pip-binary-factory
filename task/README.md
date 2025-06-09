# go-task-bin

https://github.com/go-task/task

https://taskfile.dev/

<div align="center">
  <img id="logo" src="https://taskfile.dev/img/logo.svg" height="250px" width="250px" />
</div>
<br />

Task is a task runner / build tool that aims to be simpler and easier to use than, for example, [GNU Make](https://www.gnu.org/software/make/).

Since it's written in [Go](https://go.dev/), Task is just a single binary and has no other dependencies, which means you don't need to mess with any complicated install setups just to use a build tool.

## Features

- [Easy installation](https://taskfile.dev/installation): just download a single binary, add to `$PATH` and you're done! Or you can also install using [Homebrew](https://brew.sh/), [Snapcraft](https://snapcraft.io/), or [Scoop](https://scoop.sh/) if you want.
- Available on CIs: by adding [this simple command](https://taskfile.dev/installation#install-script) to install on your CI script and you're ready to use Task as part of your CI pipeline;
- Truly cross-platform: while most build tools only work well on Linux or macOS, Task also supports Windows thanks to [this shell interpreter for Go](https://github.com/mvdan/sh).
- Great for code generation: you can easily [prevent a task from running](https://taskfile.dev/usage#prevent-unnecessary-work) if a given set of files haven't changed since last run (based either on its timestamp or content).

## Documentation

- If you're new to Task, we recommend taking a look at our [getting started guide](https://taskfile.dev/getting-started/) for an quick introduction.
- You can also browse our [usage documentation](https://taskfile.dev/usage/) for more details on how all the features work.
- Or use our quick reference documentation for the [Taskfile schema](https://taskfile.dev/reference/schema/) or [CLI](https://taskfile.dev/reference/cli/).

## install

```sh
pip install go-task-bin
```
