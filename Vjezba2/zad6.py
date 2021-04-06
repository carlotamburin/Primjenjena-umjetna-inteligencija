def zadatak():
    print(kombinacijeSlova(3, ""))


def kombinacijeSlova(duzinaStringa, string):
    if duzinaStringa == 0:
        return [string]

    return kombinacijeSlova(duzinaStringa-1, string+'a')+kombinacijeSlova(duzinaStringa -
                                                                          1, string+'b') + kombinacijeSlova(duzinaStringa-1, string+'c')


if __name__ == "__main__":
    zadatak()
