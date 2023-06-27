# is-packages

> [Conan](https://conan.io/) is an open source, decentralized and multi-platform package manager for C and C++ that allows you to create and share all your native binaries. Not only different binaries but also different build configurations, including different architectures, compilers, compiler versions, runtimes, C++ standard library, etc. When binaries are not available for one configuration, they can be built from sources on-demand. Conan can create, upload and download binaries with the same commands and flows on every platform, saving lots of time in development and continuous integration.

At the [Conan Center](https://conan.io/center/) you can find and share popular C/C++ Conan packages. However, it does not include all the packages and specific versions necessary to build our Intelligent Space applications. So, here we keep build recipes for some specific packages that we use. If you want to use these packages, **contact the maintainers to gain access to download from our conan server**. It's not public for everyone. Nevertheless, you can also build all these packages locally if you wish. Below are the instructions on how to do it.

## Running a conan server

A Conan server is a dedicated server instance that stores and provides Conan packages to developers. It acts as a centralized repository where packages can be published, queried, and downloaded. Conan servers are used to facilitate the sharing and distribution of libraries and dependencies among development teams. By setting up a Conan server, developers can host packages internally within their organizations or in a public environment such as the [ConanCenter server](https://conan.io/center/). This allows other developers to access and use these packages in their own projects.

You can check Conan documentation on how to run a Conan server at: [Setting-up a Conan Server](https://docs.conan.io/2/tutorial/conan_repositories/setting_up_conan_remotes/conan_server.html#conan-server). The Conan developers also provide a version of the Conan server as a Docker image [conanio/conan_server](https://github.com/conan-io/conan-docker-tools/tree/master#conan-server),

```bash
docker run -d -p <HOST_PORT>:9300 -d $(pwd)/data:/root/.conan_server/data --name conan_server conanio/conan_server
```
The default username and password for the Conan server Docker image are as follows:
- User: **demo**
- Password: **demo**


## Building

When executing the following command, a Docker image will be built with all the necessary applications to build the Conan packages. If you check the script, it requires providing two arguments: the first one is the URL of your Conan server, then user/password and the version of gcc compiler on which you would like to build all the packages:

```bash
./scripts/build.sh http://0.0.0.0:9300 demo demo 11.4
```

Upon completion, the script runs an interactive terminal in a container from the built image. Then, inside the container, you can simply manually upload the built packages to your Conan server, e.g.:

```bash
conan upload is-msgs/1.1.17@is/stable -r is
```