# ExtendedAndroidTools
Extended Android Tools is a set of makefiles and build environment cross compiling Linux tools we all love for Android. All tools are built using their native build systems (autotools, cmake, etc) and Android NDK. Reference build environment is provided via Docker.

# List of supported software
- [bpftrace](https://github.com/iovisor/bpftrace)
- [bcc](https://github.com/iovisor/bcc)
- [llvm & clang](https://github.com/llvm/llvm-project)
- [python](https://github.com/python/cpython)
- [libffi](https://github.com/libffi/libffi)
- [flex](https://github.com/westes/flex)
- [libelf (part of elfutils)](https://sourceware.org/elfutils/)
- [argp (part of gnulib)](https://www.gnu.org/software/gnulib/)
- [XZ Utils](https://tukaani.org/xz/)

# Build environment
## Docker (recommended)
Provided [Dockerfile](https://github.com/facebookexperimental/ExtendedAndroidTools/blob/main/docker/Dockerfile) defines the reference build environment. You can access it using the following commands:
```
# Build the Docker image
./scripts/build-docker-image.sh

# Run the environment
./scripts/run-docker-build-env.sh

# Build a target of your choice from within the container
> make python
> make bpftools

# Build and run host tools
> make python-host
> eval `make setup-env`
> python3
```

## Vagrant
ExtendedAndroidTools also provides a [Vagrantfile](https://github.com/facebookexperimental/ExtendedAndroidTools/blob/main/Vagrantfile):
```
# Startup (potentially provision new) VM
vagrant up

# ssh into a running VM
vagrant ssh

# Go to the shared directory
> cd /vagrant

# build the project of your choise
> make python
> make bpftools
```

## Setting up enviornment on your own
ExtendedAndroidTools depends on Android NDK and few programs and libraries that are listed in [this script](https://github.com/facebookexperimental/ExtendedAndroidTools/blob/main/scripts/jammy-install-deps.sh). You should be be able to install them with a package manager of your choice. NDK can be downloaded using [this script](https://github.com/facebookexperimental/ExtendedAndroidTools/blob/main/scripts/download-ndk.sh).

```
make python NDK_PATH=<path-to-ndk>
make bpftools NDK_PATH=<path-to-ndk>

# Build and run host tools
> make python-host
> eval `make setup-env`
> python3
```
# Sysroots
When projects are built the resulting binaries/libraries are placed in `bin` and `lib` subdirectories of `out/android/$ARCH/` directory. To run a particular tool on an Android device it needs to be pushed together with all the libraries it depends on to the device. In addition the shell environment needs to be configured appropriately for the runtime loader to be able to locate and load those libraries when the tool is executed. To help automate these steps ExtendedAndroidTools provides helper targets preparing sysroot archives consisting of selected executables and libraries, together with scripts setting up the environment. Those archives can be pushed to a device, extracted, and used without any further setup.

```
# build bpftools, sysroot containing bpftrace, python and bcc
# see the 'Build environment' section for more details on building
make bpftools

adb push bpftools-arm64.tar.gz /data/local/tmp
adb shell "cd /data/local/tmp && tar xf bpftools-arm64.tar.gz"

# enjoy new tools
adb shell /data/local/tmp/bpftools/bpftrace -e 'uprobe:/system/lib64/libc.so:malloc { @ = hist(arg0); }'
```

# Android device requirements
Some of the tools require root privileges to run. In addition BPF tools require Linux kernel to provide BPF capabilities: BPF, Kprobes and Uprobes. Most of Android kernels are based on Linux versions that are either too old, or have some or all of the necessary features disabled. The most straigtforward way to access Android environment providing root access and some BPF capabilities (BPF + Uprobes) is to use API 30 Android emulator **without** Google Play Store. To read more on preparing other devices see [dedicated documentation](docs/phone_setup.md).

# Variables impacting build process
- `THREADS` - number of jobs to run simultaneously. This value is passed to nested make invocations via `-j` option. The default value is 4.
- `NDK_ARCH` - x86_64 or arm64. Architecture to cross compile for. The default value is arm64
- `BUILD_TYPE` - Release or Debug, controlls amount of debug info to be included in resulting libs and binaries. The default value is Release.

```
# The following builds debug version of bpftools sysroot for x86_64
# Warning: this takes very long and resulting binaries are big, prepare ~100GB of disk space

make bpftools NDK_ARCH=x86_64 BUILD_TYPE=Debug THREADS=1
```

# Variables impacting execution of tools
- `BPFTRACE_KERNEL_SOURCE` - if set indicates directory bpftrace should read kernel headers from
- `BCC_KERNEL_SOURCE` - if set indicates directory bcc should read kernel headers from
- `BCC_SYMFS` - if set indicates directory containing unstripped elf binaries for better stack symbolication

## Contributing
See the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License
See the [LICENSE](LICENSE) file.
