import ctypes


def test_sum():
    lib = ctypes.cdll.LoadLibrary("./libfibutils.so")
    lib.sum.argstype = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
    lib.sum.restype = ctypes.c_int

    lst = list(range(10, 20))
    lst = [2 ** 99, 1, 32]
    len_lst = len(lst)

    arr_int_type = ctypes.c_int * len_lst
    res = int(lib.sum(arr_int_type(*lst), ctypes.c_int(len_lst)))

    print(f"{res=}, {sum(lst)=}")


def test_strstr():
    lib = ctypes.CDLL(None)
    lib.strstr.argstype = [ctypes.c_char_p, ctypes.c_char_p]
    lib.strstr.restype = ctypes.c_char_p

    print(f"{lib.strstr(b'qwerty', b'er')=}")
    print(f"{lib.strstr(b'qwerty', b'sd')=}")
    print(f"{lib.strstr(b'qwerty', b'ty')=}")


if __name__ == "__main__":
    test_sum()
    test_strstr()
