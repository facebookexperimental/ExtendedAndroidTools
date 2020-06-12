// stub definitions for compiling tests with bionic

#define RTLD_DI_LINKMAP 1

static inline int dlinfo(void *handle, int request, void *info) {
  return -1;
}
