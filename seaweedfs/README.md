# seaweedfs-bin

https://github.com/seaweedfs/seaweedfs

SeaweedFS is a simple and highly scalable distributed file system. There are two objectives:

1. to store billions of files!
2. to serve the files fast!

SeaweedFS started as an Object Store to handle small files efficiently.
Instead of managing all file metadata in a central master,
the central master only manages volumes on volume servers,
and these volume servers manage files and their metadata.
This relieves concurrency pressure from the central master and spreads file metadata into volume servers,
allowing faster file access (O(1), usually just one disk read operation).

There is only 40 bytes of disk storage overhead for each file's metadata.
It is so simple with O(1) disk reads that you are welcome to challenge the performance with your actual use cases.

SeaweedFS started by implementing [Facebook's Haystack design paper](http://www.usenix.org/event/osdi10/tech/full_papers/Beaver.pdf).
Also, SeaweedFS implements erasure coding with ideas from
[f4: Facebook’s Warm BLOB Storage System](https://www.usenix.org/system/files/conference/osdi14/osdi14-paper-muralidhar.pdf), and has a lot of similarities with [Facebook’s Tectonic Filesystem](https://www.usenix.org/system/files/fast21-pan.pdf)

On top of the object store, optional [Filer] can support directories and POSIX attributes.
Filer is a separate linearly-scalable stateless server with customizable metadata stores,
e.g., MySql, Postgres, Redis, Cassandra, HBase, Mongodb, Elastic Search, LevelDB, RocksDB, Sqlite, MemSql, TiDB, Etcd, CockroachDB, YDB, etc.

For any distributed key value stores, the large values can be offloaded to SeaweedFS.
With the fast access speed and linearly scalable capacity,
SeaweedFS can work as a distributed [Key-Large-Value store][KeyLargeValueStore].

SeaweedFS can transparently integrate with the cloud.
With hot data on local cluster, and warm data on the cloud with O(1) access time,
SeaweedFS can achieve both fast local access time and elastic cloud storage capacity.
What's more, the cloud storage access API cost is minimized.
Faster and cheaper than direct cloud storage!

## install

```sh
pip install seaweedfs-bin
```
