import tkinter as tk
from tkinter import ttk
from typing import List, Tuple, Callable, Optional
from math import ceil

class InterfaceGrafica(object):

    def __init__(self) -> None:

        self.configurar_raiz()

        self.configurar_frames()

        self.gerar_linha_de_modelos()

        self.variaveis_formulario: List[tk.StringVar] = []
        self.gerar_formulario(['Nome', 'Idade', 'E-mail'])

        self.gerar_linha_de_botoes()

        self.ultima_ordenacao: int = -1
        self.gerar_tabela_dados(['Nome', 'Idade', 'E-mail'], 
            [
                ('João', 25, 'aaa@mail.com'), ('Júlia', 23, 'bbb@mail.com'), 
                ('Jorge', 20, 'ccc@mail.com'), ('Pedro', 30, 'ddd@mail.com'),
                ('João', 25, 'aaa@mail.com'), ('Júlia', 23, 'bbb@mail.com'), 
                ('Jorge', 20, 'ccc@mail.com'), ('Pedro', 30, 'ddd@mail.com'),
                ('João', 25, 'aaa@mail.com'), ('Júlia', 23, 'bbb@mail.com'), 
                ('Jorge', 20, 'ccc@mail.com'), ('Pedro', 30, 'ddd@mail.com'),
                ('João', 25, 'aaa@mail.com'), ('Júlia', 23, 'bbb@mail.com'), 
                ('Jorge', 20, 'ccc@mail.com'), ('Pedro', 30, 'ddd@mail.com'),
                ('João', 25, 'aaa@mail.com'), ('Júlia', 23, 'bbb@mail.com'), 
                ('Jorge', 20, 'ccc@mail.com'), ('Pedro', 30, 'ddd@mail.com'),
                ('João', 25, 'aaa@mail.com'), ('Júlia', 23, 'bbb@mail.com'), 
                ('Jorge', 20, 'ccc@mail.com'), ('Pedro', 30, 'ddd@mail.com'),
                ('João', 25, 'aaa@mail.com'), ('Júlia', 23, 'bbb@mail.com'), 
                ('Jorge', 20, 'ccc@mail.com'), ('Pedro', 30, 'ddd@mail.com'),
                ('João', 25, 'aaa@mail.com'), ('Júlia', 23, 'bbb@mail.com'), 
                ('Jorge', 20, 'ccc@mail.com'), ('Pedro', 30, 'ddd@mail.com'),
            ], 
            self.linha_selecionada)
        
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

        self.frame_modelos = ttk.LabelFrame(self.frame_principal, padding=(10, 5, 10, 10), text='Modelos')
        self.frame_modelos.rowconfigure(0, weight=1)
        self.frame_modelos.columnconfigure(0, weight=1)
        self.frame_modelos.columnconfigure(1, weight=1)
        self.frame_modelos.columnconfigure(2, weight=1)
        self.frame_modelos.grid(row=0, column=0, sticky=tk.NSEW)

        self.frame_formulario = ttk.LabelFrame(self.frame_principal, padding=(0, 5, 0, 5), text='Formulário')
        self.frame_formulario.columnconfigure(0, weight=0)
        self.frame_formulario.columnconfigure(1, weight=1)
        self.frame_formulario.columnconfigure(2, weight=0)
        self.frame_formulario.columnconfigure(3, weight=1)
        self.frame_formulario.columnconfigure(4, weight=0)
        self.frame_formulario.columnconfigure(5, weight=1)
        self.frame_formulario.grid(row=1, column=0, sticky=tk.NSEW)

        self.frame_botoes = ttk.LabelFrame(self.frame_principal, padding=(10, 5, 10, 10), text='Ações')
        self.frame_formulario.rowconfigure(0, weight=1)
        self.frame_botoes.columnconfigure(0, weight=1)
        self.frame_botoes.columnconfigure(1, weight=1)
        self.frame_botoes.columnconfigure(2, weight=1)
        self.frame_botoes.columnconfigure(3, weight=1)
        self.frame_botoes.grid(row=2, column=0, sticky=tk.NSEW)

        self.frame_tabela = ttk.Frame(self.frame_principal, padding=(0, 10, 0, 0))
        self.frame_tabela.rowconfigure(0, weight=1)
        self.frame_tabela.columnconfigure(0, weight=1)
        self.frame_tabela.grid(row=3, column=0, sticky=tk.NSEW)
        
    def gerar_linha_de_modelos(self):

        for widget in self.frame_modelos.winfo_children():
            widget.destroy()

        botao_locadora = ttk.Button(self.frame_modelos, text='Locadora', 
            command=lambda *args: print('locadora'))
        botao_locadora.grid(row=0, column=0, padx=(0, 5), sticky=tk.NSEW)

        botao_pessoa = ttk.Button(self.frame_modelos, text='Pessoa', 
            command=lambda *args: print('pessoa'))
        botao_pessoa.grid(row=0, column=1, padx=(5, 5), sticky=tk.NSEW)

        botao_veiculo = ttk.Button(self.frame_modelos, text='Veículo', 
            command=lambda *args: print('veículo'))
        botao_veiculo.grid(row=0, column=2, padx=(5, 0), sticky=tk.NSEW)
        
    def gerar_formulario(self, legendas: List[str], 
        conteudo: Optional[List[str]] = None):

        for widget in self.frame_formulario.winfo_children():
            widget.destroy()

        numero_entradas = len(legendas)
        if conteudo is None:
            conteudo = ['' for _ in range(numero_entradas)]

        numero_linhas = ceil(numero_entradas/3)
        for i in range(numero_linhas):
            self.frame_formulario.rowconfigure(i, weight=1)

        self.variaveis_formulario = []
        for i in range(numero_entradas):
            label = ttk.Label(self.frame_formulario, text=legendas[i]+':')
            label.grid(row=i//3, column=(i%3)*2, sticky=tk.NSEW, pady=5)
            self.variaveis_formulario.append(tk.StringVar())
            entrada = ttk.Entry(self.frame_formulario, 
                textvariable=self.variaveis_formulario[i])
            entrada.grid(row=i//3, column=((i%3)*2)+1, padx=10, pady=5, sticky=tk.NSEW)

    def limpar_formulario(self):
        for var in self.variaveis_formulario:
            var.set('')

    def obter_formulario(self):
        return list(map(lambda v: v.get(), self.variaveis_formulario))
        
    def gerar_linha_de_botoes(self):

        for widget in self.frame_botoes.winfo_children():
            widget.destroy()

        botao_limpar = ttk.Button(self.frame_botoes, text='Limpar', 
            command=self.limpar_formulario)
        botao_limpar.grid(row=0, column=0, padx=(0, 5), sticky=tk.NSEW)

        botao_pesquisar = ttk.Button(self.frame_botoes, text='Pesquisar', 
            command=lambda *args: print('pesquisar', self.obter_formulario()))
        botao_pesquisar.grid(row=0, column=1, padx=(5, 5), sticky=tk.NSEW)

        botao_salvar = ttk.Button(self.frame_botoes, text='Salvar', 
            command=lambda *args: print('salvar', self.obter_formulario()))
        botao_salvar.grid(row=0, column=2, padx=(5, 5), sticky=tk.NSEW)

        botao_remover = ttk.Button(self.frame_botoes, text='Remover', 
            command=lambda *args: print('remover', self.obter_formulario()))
        botao_remover.grid(row=0, column=3, padx=(5, 0), sticky=tk.NSEW)

    def gerar_tabela_dados(self, cabecalhos: List[str], dados: List[Tuple], 
        func_selecao: Callable[[Tuple], None] = lambda t: None,
        ordenar_indice: Optional[int] = None) -> None:

        for widget in self.frame_tabela.winfo_children():
            widget.destroy()

        tabela = ttk.Treeview(self.frame_tabela, columns=cabecalhos, 
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
        
        for i in range(len(cabecalhos)):
            tabela.heading(cabecalhos[i], text=cabecalhos[i] + 
                (seta if i == ordenar_indice else ''), 
                command=lambda ordenado=i: self.gerar_tabela_dados(
                self.frame_tabela, cabecalhos, dados, func_selecao, ordenado))

        for linha in dados:
            tabela.insert('', tk.END, values=linha)

        tabela.grid(row=0, column=0, sticky=tk.NSEW)

        def func_bind(evento):
            return func_selecao(tuple(tabela.item(tabela.focus())['values']))

        tabela.bind('<<TreeviewSelect>>', func_bind)

    @staticmethod
    def linha_selecionada(linha: Tuple):
        print(linha)

    def iniciar(self):
        self.root.mainloop()