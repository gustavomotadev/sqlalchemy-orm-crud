import tkinter as tk
from tkinter import ttk
from typing import List, Tuple, Optional, Literal, Dict
from math import ceil
from locacao.repositorios.repositorio_base import RepositorioBase
from locacao.repositorios.repositorio_locadora import RepositorioLocadora
from locacao.repositorios.repositorio_pessoa import RepositorioPessoa
from locacao.repositorios.repositorio_veiculo import RepositorioVeiculo
from locacao.modelos.modelo_base import ModeloBase
from locacao.modelos.locadora import Locadora
from locacao.modelos.pessoa import Pessoa
from locacao.modelos.veiculo import Veiculo

class InterfaceGrafica(object):

    def __init__(self, repo_locadora: RepositorioLocadora,
        repo_pessoa: RepositorioPessoa, 
        repo_veiculo: RepositorioVeiculo) -> None:

        self.repositorios: Dict[RepositorioBase] = {
            'Locadora': repo_locadora,
            'Pessoa': repo_pessoa,
            'Veículo': repo_veiculo
        }

        self.legendas: Dict[List[str]] = {
            'Locadora': ['UUID', 'Nome', 'Horário Abertura', 
                'Horário Fechamento', 'Endereço'],
            'Pessoa': ['UUID', 'CNH', 'Tipo', 'Nome'],
            'Veículo': ['UUID', 'UUID Condutor', 'Placa', 'Modelo', 
                'Tipo', 'Combustível', 'Capacidade', 'Cor']}
        
        self.classes_modelo: Dict[ModeloBase] = {
            'Locadora': Locadora,
            'Pessoa': Pessoa,
            'Veículo': Veiculo
        }
        
        self.modelo = 'Locadora'
        
        self.variaveis_formulario: List[tk.StringVar] = []

        self.configurar_raiz()

        self.configurar_frames()

        self.gerar_linha_de_modelos()

        self.gerar_formulario()

        self.gerar_linha_de_botoes()

        self.ultima_ordenacao: int = -1
        self.gerar_tabela_dados()
        
    def configurar_raiz(self):
        self.root = tk.Tk()
        self.root.title('CRUD Locadora')
        self.root.geometry('800x600')
        self.root.resizable(False, False)
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

    def configurar_frames(self):
        self.frame_principal = ttk.Frame(self.root, width=800, height=600, padding=10)
        self.frame_principal.rowconfigure(0, weight=0)
        self.frame_principal.rowconfigure(1, weight=0)
        self.frame_principal.rowconfigure(2, weight=0)
        self.frame_principal.rowconfigure(3, weight=1)
        self.frame_principal.columnconfigure(0, weight=1)
        self.frame_principal.grid(row=0, column=0, sticky=tk.NSEW)

        self.frame_modelos = ttk.LabelFrame(self.frame_principal, 
            padding=(10, 5, 10, 10), text='Modelos')
        self.frame_modelos.rowconfigure(0, weight=1)
        self.frame_modelos.columnconfigure(0, weight=1)
        self.frame_modelos.columnconfigure(1, weight=1)
        self.frame_modelos.columnconfigure(2, weight=1)
        self.frame_modelos.grid(row=0, column=0, sticky=tk.NSEW)

        self.frame_formulario = ttk.LabelFrame(self.frame_principal, 
            padding=(0, 5, 0, 5), text='Formulário')
        self.frame_formulario.columnconfigure(0, weight=0)
        self.frame_formulario.columnconfigure(1, weight=1)
        self.frame_formulario.columnconfigure(2, weight=0)
        self.frame_formulario.columnconfigure(3, weight=1)
        self.frame_formulario.columnconfigure(4, weight=0)
        self.frame_formulario.columnconfigure(5, weight=1)
        self.frame_formulario.grid(row=1, column=0, sticky=tk.NSEW)

        self.frame_botoes = ttk.LabelFrame(self.frame_principal, 
            padding=(10, 5, 10, 10), text='Ações')
        self.frame_formulario.rowconfigure(0, weight=1)
        self.frame_botoes.columnconfigure(0, weight=1)
        self.frame_botoes.columnconfigure(1, weight=1)
        self.frame_botoes.columnconfigure(2, weight=1)
        self.frame_botoes.columnconfigure(3, weight=1)
        self.frame_botoes.grid(row=2, column=0, sticky=tk.NSEW)

        self.frame_tabela = ttk.Frame(self.frame_principal, padding=(0, 10, 0, 0))
        self.frame_tabela.rowconfigure(0, weight=1)
        self.frame_tabela.rowconfigure(1, weight=0)
        self.frame_tabela.columnconfigure(0, weight=1)
        self.frame_tabela.grid(row=3, column=0, sticky=tk.NSEW)

    def limpar_frame(self, frame: ttk.Frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def selecionar_modelo(self, modelo: Literal['Locadora', 'Pessoa', 'Veículo']):
        self.modelo = modelo

        self.gerar_formulario()
        self.gerar_tabela_dados()
        
    def gerar_linha_de_modelos(self):

        self.limpar_frame(self.frame_modelos)

        botao_locadora = ttk.Button(self.frame_modelos, text='Locadora', 
            command=lambda *args: self.selecionar_modelo('Locadora'))
        botao_locadora.grid(row=0, column=0, padx=(0, 5), sticky=tk.NSEW)

        botao_pessoa = ttk.Button(self.frame_modelos, text='Pessoa', 
            command=lambda *args:self.selecionar_modelo('Pessoa'))
        botao_pessoa.grid(row=0, column=1, padx=(5, 5), sticky=tk.NSEW)

        botao_veiculo = ttk.Button(self.frame_modelos, text='Veículo', 
            command=lambda *args: self.selecionar_modelo('Veículo'))
        botao_veiculo.grid(row=0, column=2, padx=(5, 0), sticky=tk.NSEW)
        
    def gerar_formulario(self, conteudo: Optional[List[str]] = None):

        self.limpar_frame(self.frame_formulario)

        numero_entradas = len(self.legendas[self.modelo])
        if conteudo is None:
            conteudo = ['' for _ in range(numero_entradas)]

        numero_linhas = ceil(numero_entradas/3)
        for i in range(numero_linhas):
            self.frame_formulario.rowconfigure(i, weight=1)

        self.variaveis_formulario = []
        for i in range(numero_entradas):

            label = ttk.Label(self.frame_formulario, text=self.legendas[self.modelo][i]+':')
            label.grid(row=i//3, column=(i%3)*2, padx=5, pady=5, sticky=tk.NSEW)

            self.variaveis_formulario.append(tk.StringVar(value=conteudo[i]))

            entrada = ttk.Entry(self.frame_formulario, 
                textvariable=self.variaveis_formulario[i])
            entrada.grid(row=i//3, column=((i%3)*2)+1, padx=5, pady=5, sticky=tk.NSEW)

    def limpar_formulario(self):
        for var in self.variaveis_formulario:
            var.set('')

        # self.tabela_dados.selection_remove(self.tabela_dados.selection()[0])
        self.tabela_dados.selection_set([])

    def obter_formulario(self):
        return list(map(lambda v: v.get() or None, self.variaveis_formulario))
        
    def gerar_linha_de_botoes(self):

        self.limpar_frame(self.frame_botoes)

        botao_limpar = ttk.Button(self.frame_botoes, text='Limpar', 
            command=self.limpar_formulario)
        botao_limpar.grid(row=0, column=0, padx=(0, 5), sticky=tk.NSEW)

        botao_pesquisar = ttk.Button(self.frame_botoes, text='Pesquisar', 
            command=self.pesquisar)
        botao_pesquisar.grid(row=0, column=1, padx=(5, 5), sticky=tk.NSEW)

        botao_salvar = ttk.Button(self.frame_botoes, text='Salvar', 
            command=self.salvar)
        botao_salvar.grid(row=0, column=2, padx=(5, 5), sticky=tk.NSEW)

        botao_remover = ttk.Button(self.frame_botoes, text='Remover', 
            command=lambda *args: print('remover', self.obter_formulario()))
        botao_remover.grid(row=0, column=3, padx=(5, 0), sticky=tk.NSEW)

    def gerar_tabela_dados(self, dados: Optional[List[Tuple]] = [], 
        ordenar_indice: Optional[int] = None) -> None:

        self.limpar_frame(self.frame_tabela)

        tabela = ttk.Treeview(self.frame_tabela, columns=self.legendas[self.modelo], 
            show='headings', selectmode='browse')
        
        seta = ''
        if ordenar_indice is not None:
            if self.ultima_ordenacao == ordenar_indice:
                inverter = True 
                seta = ' ▼'
                self.ultima_ordenacao = -1
            else:
                inverter = False
                seta = ' ▲'
                self.ultima_ordenacao = ordenar_indice
            dados.sort(key=lambda t: t[ordenar_indice], reverse=inverter)
        
        for i in range(len(self.legendas[self.modelo])):
            tabela.heading(self.legendas[self.modelo][i], 
                text=self.legendas[self.modelo][i] + 
                (seta if i == ordenar_indice else ''), 
                command=lambda ordenado=i: self.gerar_tabela_dados(
                dados, ordenado))

        for linha in dados:
            tabela.insert('', tk.END, values=linha)

        tabela.grid(row=0, column=0, sticky=tk.NSEW)

        scroll = ttk.Scrollbar(self.frame_tabela, orient=tk.HORIZONTAL, command=tabela.xview)
        scroll.grid(row=1, column=0, sticky=tk.NSEW)
        tabela.configure(xscrollcommand=scroll.set)

        self.tabela_dados = tabela

        tabela.bind('<<TreeviewSelect>>', self.linha_selecionada)

    def preencher_formulario(self, conteudo: Optional[List[str]] = None):
        for i in range(len(conteudo)):
            self.variaveis_formulario[i].set(conteudo[i])

    def linha_selecionada(self, evento):
        if self.tabela_dados.selection():
            selecionado = self.tabela_dados.item(
                self.tabela_dados.selection()[0])['values']
            
            self.preencher_formulario(selecionado)

    def pesquisar(self):

        formulario = self.obter_formulario()

        vazio = all(valor == '' for valor in formulario)

        if vazio:
            dados = self.repositorios[self.modelo].listar_todos()
        else:
            dados = self.repositorios[self.modelo].filtrar(*formulario)

        dados = list(map(lambda dado: dado.tupla(), dados))

        self.gerar_tabela_dados(dados)

    def salvar(self):

        formulario = self.obter_formulario()

        objeto = self.classes_modelo[self.modelo](*formulario)
        
        print(objeto)

    def iniciar(self):
        self.root.mainloop()