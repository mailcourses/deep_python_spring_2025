import ctypes
import time

import cffi
from fib_native import fib_rec_py, fib_iter_py
import fibutils_capi
import fibcyth


def perf_native(n_rec, n_iter):
    start = time.time()
    res = fib_rec_py(n_rec)
    finish = time.time()
    print(f"[python] fib_rec_py({n_rec}) = {res}, time = {finish - start}")

    start = time.time()
    res = fib_iter_py(n_iter)
    finish = time.time()
    print(f"[python] fib_iter_py({n_iter}) = {res}, time = {finish - start}")
    print("------------ \n")


def perf_ctypes(n_rec, n_iter):
    lib = ctypes.cdll.LoadLibrary("./fib_ctypes/libfibutils.so")

    lib.fib_rec_ctypes.argstype = [ctypes.c_int]
    lib.fib_rec_ctypes.restype = ctypes.c_int

    lib.fib_iter_ctypes.argstype = [ctypes.c_int]
    lib.fib_iter_ctypes.restype = ctypes.c_int

    start = time.time()
    res = lib.fib_rec_ctypes(n_rec)
    finish = time.time()
    print(f"[ctypes] fib_rec_ctypes({n_rec}) = {res}, time = {finish - start}")

    start = time.time()
    res = lib.fib_iter_ctypes(n_iter)
    finish = time.time()
    print(f"[ctypes] fib_iter_ctypes({n_iter}) = {res}, time = {finish - start}")
    print("------------ \n")


def perf_cffi(n_rec, n_iter):
    ffi = cffi.FFI()
    lib = ffi.dlopen("./fib_ctypes/libfibutils.so")

    ffi.cdef(
        "int fib_rec_ctypes(int n);\n"
        "int fib_iter_ctypes(int n);\n"
    )

    start = time.time()
    res = lib.fib_rec_ctypes(n_rec)
    finish = time.time()
    print(f"[cffi] fib_rec_ctypes({n_rec}) = {res}, time = {finish - start}")

    start = time.time()
    res = lib.fib_iter_ctypes(n_iter)
    finish = time.time()
    print(f"[cffi] fib_iter_ctypes({n_iter}) = {res}, time = {finish - start}")
    print("------------ \n")


def perf_capi(n_rec, n_iter):
    start = time.time()
    res = fibutils_capi.fib_rec_c(n_rec)
    finish = time.time()
    print(f"[capi] fib_rec_c({n_rec}) = {res}, time = {finish - start}")

    start = time.time()
    res = fibutils_capi.fib_iter_c(n_iter)
    finish = time.time()
    print(f"[capi] fib_iter_c({n_iter}) = {res}, time = {finish - start}")
    print("------------ \n")


def perf_cython(n_rec, n_iter):
    start = time.time()
    res = fibcyth.fib_rec_cy(n_rec)
    finish = time.time()
    print(f"[cython] fib_rec_cy({n_rec}) = {res}, time = {finish - start}")

    start = time.time()
    res = fibcyth.fib_iter_cy(n_iter)
    finish = time.time()
    print(f"[cython] fib_iter_cy({n_iter}) = {res}, time = {finish - start}")
    print("------------ \n")


def run():
    n_rec = 37
    n_iter = 45

    perf_native(n_rec, n_iter)
    perf_ctypes(n_rec, n_iter)
    perf_cffi(n_rec, n_iter)
    perf_capi(n_rec, n_iter)
    perf_cython(n_rec, n_iter)


if __name__ == "__main__":
    run()
