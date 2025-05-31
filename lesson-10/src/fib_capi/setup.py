from setuptools import setup, Extension


def main():
    setup(
        name="fibutils_capi",
        version="1.0.0",
        ext_modules=[Extension("fibutils_capi", ["fibutils_capi.c"])],
    )


if __name__ == "__main__":
    main()
