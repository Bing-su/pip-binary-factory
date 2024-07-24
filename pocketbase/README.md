# pocketbase-bin

https://pocketbase.io/

https://github.com/pocketbase/pocketbase

[PocketBase](https://pocketbase.io) is an open source Go backend, consisting of:

- embedded database (_SQLite_) with **realtime subscriptions**
- built-in **files and users management**
- convenient **Admin dashboard UI**
- and simple **REST-ish API**

**For documentation and examples, please visit https://pocketbase.io/docs.**

> [!WARNING]
> Please keep in mind that PocketBase is still under active development
> and therefore full backward compatibility is not guaranteed before reaching v1.0.0.

## PyPI package

```sh
pip install pocketbase-bin
```

Compared to the original, this package has the following differences

- The `pb_data`, `pb_migrations` directories are created in the current working directory, not next to the executable.

- The default value of `publicDir` is also set to `pb_public` in the current working directory.

- `pocketbase update` command is disabled.

## Python SDK

[pocketbase](https://pypi.org/project/pocketbase/)

[pocketbase-async](https://pypi.org/project/pocketbase-async/)
