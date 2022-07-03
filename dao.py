import MySQLdb

conn= MySQLdb.connect(host='127.0.0.1', user='root', password='Gogoll90@', port=3306)
cursor= conn.cursor()



def verificar_login(nome):
    cursor.execute(f'select registro_funcionario,nome,senha,ADM from farmacia.usuarios where nome="{nome}"')
    dados= cursor.fetchall()
    if dados == ():
        return False
    registro= dados[0][0]
    login= dados[0][1]
    senha= dados[0][2]
    ADM= dados[0][3]
    listadb= [registro,login,senha,ADM]

    return listadb

def verificar_autorizacao(registro):
    cursor.execute(f'select ADM from farmacia.usuarios where registro_funcionario= "{registro}"')
    ADM= cursor.fetchall()
    if ADM[0][0] == 1:
        return True
    else:
        return False

def salvar_funcionario(nome,senha,funcao,setor,unidade,salario,CPF,ADM):
    cursor.execute('insert into farmacia.usuarios (nome,senha,funcao,setor,unidade,salarios_min,CPF,ADM)' 
                    f'values ("{nome}","{senha}","{funcao}","{setor}","{unidade}",{salario},{CPF},{ADM})')
    conn.commit()
    return True

class funcionario():
    def __init__(self,nome,funcao,setor,unidade,CPF,codigo):
        self.codigo = codigo
        self.nome=nome
        self.funcao=funcao
        self.setor=setor
        self.unidade=unidade
        self.CPF=CPF

    def ler_funcionario(self):
        lista=[]
        cursor.execute('select registro_funcionario,nome,funcao,setor,unidade,CPF from farmacia.usuarios')
        for usuario in cursor.fetchall():
            obj= funcionario(usuario[0],usuario[1],usuario[2],usuario[3],usuario[4],usuario[5])
            if obj in lista:
                return
            lista.append(obj)
        return lista

def deletar_funcionario(codigo):
    cursor.execute(f'delete from farmacia.usuarios where registro_funcionario= "{codigo}"')
    conn.commit()
    return


def buscar_dativo(ativo):
    cursor.execute(f'select densidade from farmacia.ativos where nome="{ativo}"')
    densidade_ativo= cursor.fetchall()
    return densidade_ativo[0][0]

def buscar_dexcipiente(excipiente):
    cursor.execute(f'select densidade from farmacia.excipientes where nome="{excipiente}"')
    densidade_excipiente = cursor.fetchall()
    return densidade_excipiente[0][0]

def salvar_receita(nome_paciente,medico,unidadeO,massa_ativo,massa_exp,quantidade,excipiente,ativo,capsula_usada):
    cursor.execute(f'INSERT INTO farmacia.receitas (nome_paciente,medico,ativo,mativo,excipiente,mexcp,numero_d_caps'
                   f',tamanho_caps,unidadeO) VALUES ("{nome_paciente}","{medico}","{ativo}",{massa_ativo},"{excipiente}",'
                   f'{massa_exp},{quantidade},{capsula_usada},"{unidadeO}")')
    conn.commit()
    return
