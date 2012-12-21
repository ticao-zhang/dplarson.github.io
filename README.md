# Description
My personal research website/portfolio. Currently hosted at [http://ieng6.ucsd.edu/~dplarson/][dplarson-ieng6].


# Usage

## Requirements
* Python 2.7.3
* Hyde 0.8.4
* Fabric 1.4.3


## Installation
```
git clone git@github.com:dplarson/dplarson_site.git
```


## Generate and Serve the Site

### using Hyde
```shell
$ cd dplarson_site
$ hyde gen
$ hyde serve
$ open http://localhost:8080
```

### using Fabric (preferred)
```shell
$ cd dplarson_site
$ fab serve
$ open http://localhost:8080
``` 


## Publish the Site

### using Hyde
```shell
$ cd dplarson_site
$ hyde gen -c prod.yaml
```
then upload **deploy/** to your host.



### using Fabric (preferred)
```shell
$ cd dplarson_site
$ fabric push
```
**NOTE**: make sure to change the **rsync** command in **fabfile.py** with your host info


# Credits
Built by [David Larson][dplarson-github] using [Hyde][hyde] and [Bootstrap][bootstrap], based on [Jeremy Blanchard][auzigog]'s [hyde-bootstrap][].


# License
see **LICENSE.markdown**


[dplarson-ieng6]:http://ieng6.ucsd.edu/~dplarson/
[dplarson-github]: https://github.com/dplarson/
[hyde]: http://hyde.github.com/
[bootstrap]: http://twitter.github.com/bootstrap/
[auzigog]: https://github.com/auzigog
[hyde-bootstrap]: https://github.com/auzigog/hyde-bootstrap
