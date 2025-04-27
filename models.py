from sqlalchemy import Column, Integer, String, Date, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from backend.database import Base

class Escola(Base):
    __tablename__ = "escola"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), unique=True, nullable=False)
    cursos = relationship("Curso", back_populates="escola")

class Curso(Base):
    __tablename__ = "curso"
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(10), unique=True, nullable=False)
    nome = Column(String(100), nullable=False)
    status = Column(String(15), nullable=False)
    escola_id = Column(Integer, ForeignKey("escola.id"))
    previsao_inicio = Column(Date)
    previsao_fim = Column(Date)
    valor_mensal = Column(Numeric(10, 2))
    escola = relationship("Escola", back_populates="cursos")
    turmas = relationship("Turma", back_populates="curso")
    receitas = relationship("Receita", back_populates="curso")

class Turma(Base):
    __tablename__ = "turma"
    id = Column(Integer, primary_key=True, index=True)
    curso_id = Column(Integer, ForeignKey("curso.id"))
    nome = Column(String(50))
    quantidade_alunos = Column(Integer)
    curso = relationship("Curso", back_populates="turmas")
    matriculas = relationship("Matricula", back_populates="turma")

class Aluno(Base):
    __tablename__ = "aluno"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    email = Column(String(100))
    matriculas = relationship("Matricula", back_populates="aluno")

class Matricula(Base):
    __tablename__ = "matricula"
    id = Column(Integer, primary_key=True, index=True)
    aluno_id = Column(Integer, ForeignKey("aluno.id"))
    turma_id = Column(Integer, ForeignKey("turma.id"))
    data_matricula = Column(Date)
    status = Column(String(10))
    aluno = relationship("Aluno", back_populates="matriculas")
    turma = relationship("Turma", back_populates="matriculas")

class Receita(Base):
    __tablename__ = "receita"
    id = Column(Integer, primary_key=True, index=True)
    curso_id = Column(Integer, ForeignKey("curso.id"))
    data_recebimento = Column(Date)
    valor = Column(Numeric(10,2))
    curso = relationship("Curso", back_populates="receitas")
