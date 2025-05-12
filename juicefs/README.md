# juicefs-bin

https://github.com/juicedata/juicefs

<p align="center"><a href="https://github.com/juicedata/juicefs"><img alt="JuiceFS Logo" src="https://github.com/juicedata/juicefs/raw/main/docs/en/images/juicefs-logo-new.svg" width="50%" /></a></p>

**JuiceFS** is a high-performance [POSIX](https://en.wikipedia.org/wiki/POSIX) file system released under Apache License 2.0, particularly designed for the cloud-native environment. The data, stored via JuiceFS, will be persisted in Object Storage _(e.g. Amazon S3)_, and the corresponding metadata can be persisted in various compatible database engines such as Redis, MySQL, and TiKV based on the scenarios and requirements.

With JuiceFS, massive cloud storage can be directly connected to big data, machine learning, artificial intelligence, and various application platforms in production environments. Without modifying code, the massive cloud storage can be used as efficiently as local storage.

📖 **Document**: [Quick Start Guide](https://juicefs.com/docs/community/quick_start_guide)

## install

```sh
pip install juicefs-bin
```
