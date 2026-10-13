FROM ubuntu:22.04 AS shim
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libc6-dev \
    && rm -rf /var/lib/apt/lists/*

# Some WSL kernels omit /proc/self/io, which can crash Typesense/brpc at startup.
# Build the workaround into every local image so no WSL-specific launch is needed.
COPY <<'EOF' /src/procio-shim.c
#define _GNU_SOURCE
#include <dlfcn.h>
#include <errno.h>
#include <stdio.h>
#include <string.h>

static const char PROC_IO[] =
    "rchar: 0\n"
    "wchar: 0\n"
    "syscr: 0\n"
    "syscw: 0\n"
    "read_bytes: 0\n"
    "write_bytes: 0\n"
    "cancelled_write_bytes: 0\n";

typedef FILE *(*fopen_function)(const char *, const char *);

static FILE *fopen_with_fallback(const char *path, const char *mode,
                                 const char *symbol) {
    fopen_function real_fopen = (fopen_function)dlsym(RTLD_NEXT, symbol);
    if (!real_fopen) {
        errno = ENOSYS;
        return NULL;
    }

    FILE *stream = real_fopen(path, mode);
    // Preserve real IO statistics on Linux; use zeroes only for this missing file.
    if (stream || errno != ENOENT || !path || !mode || mode[0] != 'r' ||
        strcmp(path, "/proc/self/io") != 0) {
        return stream;
    }
    return fmemopen((void *)PROC_IO, sizeof(PROC_IO) - 1, "r");
}

FILE *fopen(const char *path, const char *mode) {
    return fopen_with_fallback(path, mode, "fopen");
}

FILE *fopen64(const char *path, const char *mode) {
    return fopen_with_fallback(path, mode, "fopen64");
}
EOF

RUN gcc -O2 -Wall -Wextra -shared -fPIC \
    -o /src/procio-shim.so /src/procio-shim.c -ldl

FROM typesense/typesense:30.2
COPY --from=shim /src/procio-shim.so /usr/local/lib/procio-shim.so
ENV LD_PRELOAD=/usr/local/lib/procio-shim.so
