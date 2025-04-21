class taterial:
    def __init__(self, nome, elasticidade, poisson, densidade, escoamento=None, ruptura=None, tipo='isotrópico'):
        """
        Inicializa um novo material para simulações mecânicas.

        Parâmetros:
        - nome (str): Nome do material (ex: Aço 1020, Alumínio 6061)
        - elasticidade (float): Módulo de elasticidade (E) em Pa
        - poisson (float): Coeficiente de Poisson
        - densidade (float): Densidade em kg/m³
        - escoamento (float): Limite de escoamento em Pa (opcional)
        - ruptura (float): Limite de ruptura em Pa (opcional)
        - tipo (str): Tipo de material (ex: isotrópico, ortotrópico)
        """
        self.nome = nome
        self.elasticidade = elasticidade
        self.poisson = poisson
        self.densidade = densidade
        self.escoamento = escoamento
        self.ruptura = ruptura
        self.tipo = tipo
    
    def __str__(self):
        return (
            f"Material: {self.nome}\n"
            f"  Tipo: {self.tipo}\n"
            f"  Módulo de Elasticidade: {self.elasticidade / 1e6:.2f} MPa\n"
            f"  Coeficiente de Poisson: {self.poisson:.3f}\n"
            f"  Densidade: {self.densidade:.1f} kg/m³\n"
            f"  Limite de Escoamento: {self.escoamento / 1e6:.2f} MPa\n" if self.escoamento else "  Limite de Escoamento: N/A\n"
            f"  Limite de Ruptura: {self.ruptura / 1e6:.2f} MPa\n" if self.ruptura else "  Limite de Ruptura: N/A\n"
        )


    def to_dict(self):
        return {
            "nome": self.nome,
            "tipo": self.tipo,
            "elasticidade": self.elasticidade,
            "poisson": self.poisson,
            "densidade": self.densidade,
            "escoamento": self.escoamento,
            "ruptura": self.ruptura
        }
