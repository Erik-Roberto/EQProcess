from abc import ABC
import itertools


class StreamBase(ABC):
    
    id_iter = itertools.count()
    
    def __init__(self, name: str, mass_flow: float = None, composition: dict = None) -> None:
        self._stream_id: int = next(StreamBase.id_iter)
        self._name: str = name
        self._mass_flow: float = mass_flow if mass_flow else 0
        self._composition: dict = composition
        

    @property
    def stream_id(self):
        return self._stream_id
    

    @property
    def name(self):
        return self._name
    

    @property
    def mass_flow(self):
        return self._mass_flow
    

    @property
    def composition(self):
        return self._composition


    def __add__(self, stream): # TODO: Descobrir como colocar os type hint
        if not self.composition or not stream.composition:
            raise ValueError('Missing composition')
        if not self.mass_flow or not stream.mass_flow:
            raise ValueError('Missing mass_flow')

        new_comp = {}
        for comp, x in stream.composition.items():
            new_comp[comp] = (stream.mass_flow * x + self.mass_flow * self.composition.get(comp))/(stream.mass_flow + self.mass_flow)

        return StreamBase(name='new stream', mass_flow=stream.mass_flow + self.mass_flow, composition=new_comp)





class teste(StreamBase):
    pass

