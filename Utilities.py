class Material:
    def __init__(self, name:str, **kwargs):
        self.name = name

        self.tensile_modulus: float = kwargs['tensile_modulus']
        self.tensile_strength: float = kwargs['tensile_strength']

        self.compressive_modulus: float = kwargs['compressive_modulus']
        self.compressive_strength: float = kwargs['compressive_strength']

        self.cte: float = kwargs['coefficient_thermal_expansion']
    

    