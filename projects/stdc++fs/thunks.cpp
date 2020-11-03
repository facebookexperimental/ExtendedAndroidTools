// Copyright (c) Facebook, Inc. and its affiliates.

#include <stdlib.h>
#include <unistd.h>

#include <experimental/filesystem>

namespace std {
namespace experimental {
namespace filesystem {
namespace v1 {

path __current_path(error_code *__ec) {
  char buf[256];
  char* cwd = getcwd(buf, sizeof(buf));
  if (cwd == nullptr) {
    abort();
  }
  return path{cwd};
}

path absolute(const path& p, const path& base) {
  return base / p;
}

path __canonical(const path& p, const path& base, error_code *__ec) {
  char buf[PATH_MAX];
  char* rpath = realpath((base / p).c_str(), buf);
  if (rpath == nullptr) {
    abort();
  }
  return path{rpath};
}

} // namespace v1
} // namespace filesystem
} // namespace experimental
} // namespace std
