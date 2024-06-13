import chemicals as chem


class Components:

    def __init__(self, name: str, identifier: str = None) -> None:
        self._name: str = name
        metadata = chem.search_chemical(identifier if identifier else name)
        self._CAS: int = metadata.CAS
        self._MW: float = metadata.MW
    

    @property
    def name(self):
        return self._name


    @property
    def CAS(self):
        return self._CAS
    

    @property
    def MW(self):
        return self._MW
    

if __name__ == '__main__':
    etanol = Components('Etanol', 'Ethanol')
    print(etanol.CAS)
    print(etanol.MW)