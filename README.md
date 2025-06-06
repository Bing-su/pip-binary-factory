# pip binary factory

binary package with pip install

| package         | url                                                                | version                                                                                                                     | pip version                                                                                               |
| --------------- | ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| micro-editor    | https://github.com/zyedidia/micro                                  | [![GitHub version](https://badge.fury.io/gh/zyedidia%2Fmicro.svg)](https://badge.fury.io/gh/zyedidia%2Fmicro)               | [![PyPI version](https://badge.fury.io/py/micro-editor.svg)](https://badge.fury.io/py/micro-editor)       |
| eget-py         | https://github.com/zyedidia/eget                                   | [![GitHub version](https://badge.fury.io/gh/zyedidia%2Feget.svg)](https://badge.fury.io/gh/zyedidia%2Feget)                 | [![PyPI version](https://badge.fury.io/py/eget-py.svg)](https://badge.fury.io/py/eget-py)                 |
| lazygit-py      | https://github.com/jesseduffield/lazygit                           | [![GitHub version](https://badge.fury.io/gh/jesseduffield%2Flazygit.svg)](https://badge.fury.io/gh/jesseduffield%2Flazygit) | [![PyPI version](https://badge.fury.io/py/lazygit-py.svg)](https://badge.fury.io/py/lazygit-py)           |
| fzf-bin         | https://github.com/junegunn/fzf                                    | [![GitHub version](https://badge.fury.io/gh/junegunn%2Ffzf.svg)](https://badge.fury.io/gh/junegunn%2Ffzf)                   | [![PyPI version](https://badge.fury.io/py/fzf-bin.svg)](https://badge.fury.io/py/fzf-bin)                 |
| go-task-bin     | https://taskfile.dev<br/>https://github.com/go-task/task           | [![GitHub version](https://badge.fury.io/gh/go-task%2Ftask.svg)](https://badge.fury.io/gh/go-task%2Ftask)                   | [![PyPI version](https://badge.fury.io/py/go-task-bin.svg)](https://badge.fury.io/py/go-task-bin)         |
| zig-bin         | https://ziglang.org<br/>https://github.com/ziglang/zig             | [![GitHub version](https://badge.fury.io/gh/ziglang%2Fzig.svg)](https://badge.fury.io/gh/ziglang%2Fzig)                     | [![PyPI version](https://badge.fury.io/py/zig-bin.svg)](https://badge.fury.io/py/zig-bin)                 |
| pocketbase-bin  | https://pocketbase.io<br/>https://github.com/pocketbase/pocketbase | [![GitHub version](https://badge.fury.io/gh/pocketbase%2Fpocketbase.svg)](https://badge.fury.io/gh/pocketbase%2Fpocketbase) | [![PyPI version](https://badge.fury.io/py/pocketbase-bin.svg)](https://badge.fury.io/py/pocketbase-bin)   |
| act-bin         | https://nektosact.com<br/>https://github.com/nektos/act            | [![GitHub version](https://badge.fury.io/gh/nektos%2Fact.svg)](https://badge.fury.io/gh/nektos%2Fact)                       | [![PyPI version](https://badge.fury.io/py/act-bin.svg)](https://badge.fury.io/py/act-bin)                 |
| nats-server-bin | https://nats.io<br/>https://github.com/nats-io/nats-server         | [![GitHub version](https://badge.fury.io/gh/nats-io%2Fnats-server.svg)](https://badge.fury.io/gh/nats-io%2Fnats-server)     | [![PyPI version](https://badge.fury.io/py/nats-server-bin.svg)](https://badge.fury.io/py/nats-server-bin) |
| yazi-bin        | https://github.com/sxyazi/yazi                                     | [![GitHub version](https://badge.fury.io/gh/sxyazi%2Fyazi.svg)](https://badge.fury.io/gh/sxyazi%2Fyazi)                     | [![PyPI version](https://badge.fury.io/py/yazi-bin.svg)](https://badge.fury.io/py/yazi-bin)               |
| seaweedfs-bin   | https://github.com/seaweedfs/seaweedfs                             | ![GitHub Release](https://img.shields.io/github/v/release/seaweedfs/seaweedfs)                                              | [![PyPI version](https://badge.fury.io/py/seaweedfs-bin.svg)](https://badge.fury.io/py/seaweedfs-bin)     |
| juicefs-bin     | https://juicefs.com<br/>https://github.com/juicedata/juicefs       | [![GitHub version](https://badge.fury.io/gh/juicedata%2Fjuicefs.svg)](https://badge.fury.io/gh/juicedata%2Fjuicefs)         | [![PyPI version](https://badge.fury.io/py/juicefs-bin.svg)](https://badge.fury.io/py/juicefs-bin)         |
| xh-bin          | https://github.com/ducaale/xh                                      | [![GitHub version](https://badge.fury.io/gh/ducaale%2Fxh.svg)](https://badge.fury.io/gh/ducaale%2Fxh)                       | [![PyPI version](https://badge.fury.io/py/xh-bin.svg)](https://badge.fury.io/py/xh-bin)                   |

## pipx, uv

To install the packages listed above using pipx or uv, you can use the following commands:

| package         | pipx                           | uv                                | binary name |
| --------------- | ------------------------------ | --------------------------------- | ----------- |
| micro-editor    | `pipx install micro-editor`    | `uv tool install micro-editor`    | micro       |
| eget-py         | `pipx install eget-py`         | `uv tool install eget-py`         | eget        |
| lazygit-py      | `pipx install lazygit-py`      | `uv tool install lazygit-py`      | lazygit     |
| fzf-bin         | `pipx install fzf-bin`         | `uv tool install fzf-bin`         | fzf         |
| go-task-bin     | `pipx install go-task-bin`     | `uv tool install go-task-bin`     | task        |
| zig-bin         | `pipx install zig-bin`         | `uv tool install zig-bin`         | zig         |
| pocketbase-bin  | `pipx install pocketbase-bin`  | `uv tool install pocketbase-bin`  | pocketbase  |
| act-bin         | `pipx install act-bin`         | `uv tool install act-bin`         | act         |
| nats-server-bin | `pipx install nats-server-bin` | `uv tool install nats-server-bin` | nats-server |
| yazi-bin        | `pipx install yazi-bin`        | `uv tool install yazi-bin`        | yazi<br/>ya |
| seaweedfs-bin   | `pipx install seaweedfs-bin`   | `uv tool install seaweedfs-bin`   | weed        |
| juicefs-bin     | `pipx install juicefs-bin`     | `uv tool install juicefs-bin`     | juicefs     |
| xh-bin          | `pipx install xh-bin`          | `uv tool install xh-bin`          | xh          |

Please note that you need to have pipx or uv installed on your system before running these commands.
