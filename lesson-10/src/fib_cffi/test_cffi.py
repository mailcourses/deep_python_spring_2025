import cffi


def test_sum():
    ffi = cffi.FFI()
    lib = ffi.dlopen("../fib_ctypes/libfibutils.so")

    ffi.cdef("int sum(int *arr, int len);")

    lst = list(range(10, 20))
    len_lst = len(lst)

    arr = ffi.new("int[]", lst)
    print(arr)

    res = lib.sum(arr, len_lst)
    print(f"{res=}, {sum(lst)=}, {type(res)}")


def test_build():
    builder = cffi.FFI()
    builder.cdef("int mult(int a, int b, int c);")

    builder.set_source(
        "tmp_mult",
        """
        int mult(int a, int b, int c)
        {
            return a * b * c;
        }
        """
    )
    builder.compile()

    print("compiled!")

    from tmp_mult import lib

    a, b, c = 2, 10, 4
    res = lib.mult(a, b, c)

    print(f"{res=}, {a * b * c=}")


if __name__ == "__main__":
    test_sum()
    test_build()
