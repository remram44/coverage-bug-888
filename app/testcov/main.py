import pkg_resources


def main():
    for entry_point in pkg_resources.iter_entry_points('plugins'):
        func = entry_point.load()
        func()


if __name__ == '__main__':
    main()
