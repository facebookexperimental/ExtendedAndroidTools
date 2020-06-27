# Setting up a phone
This document describes steps necessary to enable BPF, Uprobes and Kprobes on some Android devices. Note that these steps reduce security and might result in voiding warranties. Follow the steps at your own risk.

## Root
There are multiple ways of acquiring root access on an Android devices:
- using Android emulator without Google Play Store
- rooting
- building and flashing userdebug AOSP images

Procedure of acquiring AOSP sources, configuring, building and flashing is documented [here](https://source.android.com/setup/build).

## BPF enabled kernel
Most recent Android kernels support limited BPF tracing out of the box. Pixel 4 and API 30 emulator ship with Linux kernel having BPF and Uprobes enabled. Older devices run kernels that predate many of BPF capabilities (Pixel 3a runs 4.9, Pixel 2 runs 4.4) and require some essential commits to be backported, including arm64 Uprobes support (added in 4.10). Kprobes on the other hand are disabled even in the newest kernels as they might be considered a security risk (at least in the past Kprobe support collided with a security mechanism enforcing control flow: [CFI](https://source.android.com/devices/tech/debug/kcfi))

Extended Android Tools does not provide kernel sources. You might need to address mentioned issues in your own fork or use kernels from other sources. Here is a list of some BPF-enabled Android kernels that are not part of Extended Android Tools:
- [Pixel 3a](https://github.com/michalgr/kernel_msm/tree/QP1A.190711.020.C3.bpf)
- [Pixel 2](https://github.com/michalgr/kernel_msm/tree/bpf_wahoo_defconfig)
- [API 28 emulator](https://github.com/michalgr/kernel_goldfish)

Compiling and flashing Android kernels is described [here](https://source.android.com/setup/build/building-kernels).

## Updating kernel modules
Since Android 9 some kernel modules are compiled as standalone `.ko` files. Those files need to be kept in sync with the kernel in order for wifi or touch screen to work properly. Those files are located on vendor partition which is not built as part of AOSP and is downloaded as standalone `.img` file instead (at least this is the case with Google phones). In addition [verified boot](https://source.android.com/security/verifiedboot) mechanism prevents modifications to vendor partition on device. To work around that you might need to disable dm-verity (`adb disable-verity`), remounting vendor partition writable (`adb remount -R`) and pushing kernel modules to `/vendor/lib/modules/`.
