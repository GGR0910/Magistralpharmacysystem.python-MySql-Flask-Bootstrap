from flask import Flask,render_template,session,flash,url_for,redirect,request
import Funções
import dao

app= Flask(__name__)

app.secret_key= 'Faus37@gaus'


@app.route('/')
def inicial():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    return render_template('inicial.html',titulo="Farmácia quatro elementos.")


#receitas
@app.route('/ordem_de_manipulaçao')
def pedido():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    return render_template('Registro_pedido.html', titulo= "Nova ordem de manipulação")

@app.route('/processando_ordem', methods= ['POST',])
def processar_pedido():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    calculo= Funções.caucula_capsula()
    capsula_usada= calculo[1]
    nome_paciente= request.form['nome_paciente']
    medico=request.form['nomemd']
    quantidade= int(request.form['quantidade'])
    unidadeO= request.form['UnidadeO']
    ativo= request.form['PA']
    excipiente= request.form['excipiente']
    massa_exp = round(calculo[0] * quantidade,3)
    dosagem=float(request.form['dosagem'])
    massa_ativo= dosagem/100 * quantidade

    dao.salvar_receita(quantidade=quantidade,excipiente=excipiente,ativo=ativo,
                       capsula_usada=capsula_usada,nome_paciente=nome_paciente,medico=medico,unidadeO=unidadeO,
                       massa_exp=massa_exp,massa_ativo=massa_ativo)
    return redirect(url_for('pedido'))




#estoque
@app.route('/estoque')
def estoque():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    pass

#Usuarios
@app.route('/login')
def login():
    return render_template('login.html',titulo="Login")

@app.route('/autenticar', methods=['POST',])
def autenticar():
    dados= Funções.request_login()
    listadb=dao.verificar_login(nome=dados[0])
    if listadb == False:
        flash('Usuário não reconhecido.')
        return redirect(url_for('login'))
    elif dados[0] in listadb:
        if dados[1] in listadb:
            flash('Usuario logado.')
            session['usuario_logado']= listadb[0]

            return redirect(url_for('inicial'))
        else:
            flash('Senha incorreta.')
            return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash("logout efetuado.")
    return redirect(url_for('login'))

@app.route('/Cadastro')
def cadastro_usuario():
    ADM=dao.verificar_autorizacao(session['usuario_logado'])
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    if ADM == True:
        return render_template('cadastro_funcionario.html', titulo= "Cadastrar novo funcionário.")
    if ADM == False:
        flash('Funcionário não altorizado a realizar este procedimento.')
        return redirect(url_for('inicial'))

@app.route('/registrar', methods=['POST',])
def registrar():
    nome = request.form['nome']
    funcao = request.form['funcao']
    senha = request.form['senha']
    setor = request.form['setor']
    unidade = request.form['Unidade']
    salario = request.form['salario']
    ADM = request.form['ADM']
    CPF = request.form['CPF']
    dao.salvar_funcionario(nome=nome,funcao=funcao,senha=senha,setor=setor,unidade=unidade,salario=salario,
                           ADM=ADM,CPF=CPF)
    flash('Funcionário registrado com sucesso.')
    return redirect(url_for('inicial'))

@app.route('/funcionarios')
def lista_funcionario():
    lista=dao.funcionario.ler_funcionario(self='self')
    return render_template('lista_funcionarios.html',titulo="Lista de funcionários.",lista=lista)

@app.route('/deletar_funcionario/<int:codigo>')
def deletar_funcionario(codigo):
    ADM = dao.verificar_autorizacao(session['usuario_logado'])
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    elif ADM == True:
        pass
    elif ADM == False:
        flash('Funcionário não altorizado a realizar este procedimento.')
        return redirect(url_for('inicial'))
    dao.deletar_funcionario(codigo=codigo)
    flash("Funcionário deletado dos registros.")
    lista = dao.funcionario.ler_funcionario(self='self')
    return render_template('lista_funcionarios.html', titulo="Lista de funcionários.", lista=lista)

@app.route('/editar_funcionario')
def editar_funcionario():
    pass



app.run(debug=True)
