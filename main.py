from stream.components import Components
from stream.stream_base import teste


if __name__ == '__main__':

    etanol = Components('etanol', 'Ethanol')
    agua = Components('aguinha', 'Water')


    c1 = teste(
        name='teste1',
        mass_flow=100,
        composition={
            etanol: .5,
            agua: .5
        })
    
    c2 = teste(
        name='teste2',
        mass_flow=100,
        composition={
            etanol: 1,
            agua: 0,
        })

    c3 = c1 + c2

    print(c3.name)
    print(c3.mass_flow)
    for c, x in c3.composition.items():
        print(c.name, x)