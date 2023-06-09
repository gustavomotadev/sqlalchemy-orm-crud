import sqlalchemy as sa
import sqlalchemy.orm as orm
from typing import Tuple
from locacao.modelos.modelo_base import ModeloBase

class Veiculo(ModeloBase):
    __tablename__ = "veiculo"

    uuid: orm.Mapped[str] = orm.mapped_column(sa.String(36), primary_key=True)
    uuid_condutor: orm.Mapped[str] = orm.mapped_column(sa.ForeignKey("pessoa.uuid"))
    placa: orm.Mapped[str] = orm.mapped_column(sa.String(7), unique=True)
    modelo: orm.Mapped[str] = orm.mapped_column(sa.String(50))
    tipo: orm.Mapped[str] = orm.mapped_column(sa.String(30))
    combustivel: orm.Mapped[str] = orm.mapped_column(sa.String(30))
    capacidade: orm.Mapped[int] = orm.mapped_column(sa.Integer)
    cor: orm.Mapped[str] = orm.mapped_column(sa.String(30))

    # pessoa: orm.Mapped["Pessoa"] = orm.relationship(back_populates="veiculos")

    def tupla(self) -> Tuple[str]:
        return (str(self.uuid), str(self.uuid_condutor), str(self.placa), 
            str(self.modelo), str(self.tipo), str(self.combustivel), 
            str(self.capacidade), str(self.cor))

    def __repr__(self) -> str:
        return (f"Veiculo(uuid={self.uuid}, uuid_condutor={self.uuid_condutor}, " + 
                f"placa={self.placa}, modelo={self.modelo}, tipo={self.tipo}, " + 
                f"combustivel={self.combustivel}, capacidade={self.capacidade}, " + 
                f"cor={self.cor})")
