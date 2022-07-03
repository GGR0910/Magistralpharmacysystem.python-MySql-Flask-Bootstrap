from flask import request
import dao



def request_login():
    login=request.form['login']
    senha=request.form['senha']
    dados= [login,senha]
    return dados


def caucula_capsula():
    cap4=0.21
    cap3=0.3
    cap2=0.37
    cap1=0.5
    cap0=0.68
    cap00=0.95

    nome_ativo= request.form['PA']
    ativo=int(request.form['dosagem'])/100
    excipiente= request.form['excipiente']
    densidade=float(dao.buscar_dativo(ativo=nome_ativo))
    volume_ativo= round(ativo/densidade,3)
    if volume_ativo < cap4:
        volume_exp=cap4-volume_ativo
        massa_exp= dao.buscar_dexcipiente(excipiente=excipiente) * volume_exp
        return [massa_exp,4]
    elif volume_ativo < cap3:
        volume_exp=cap3-volume_ativo
        massa_exp= dao.buscar_dexcipiente(excipiente=excipiente) * volume_exp
        return [massa_exp,3]
    elif volume_ativo < cap2:
        volume_exp=cap2-volume_ativo
        massa_exp= dao.buscar_dexcipiente(excipiente=excipiente) * volume_exp
        return [massa_exp,2]
    elif volume_ativo < cap1:
        volume_exp=cap1-volume_ativo
        massa_exp= dao.buscar_dexcipiente(excipiente=excipiente) * volume_exp
        return [massa_exp,1]
    elif volume_ativo < cap0:
        volume_exp=cap0-volume_ativo
        massa_exp= dao.buscar_dexcipiente(excipiente=excipiente) * volume_exp
        return [massa_exp,0]
    elif volume_ativo < cap00:
        volume_exp=cap00-volume_ativo
        massa_exp= dao.buscar_dexcipiente(excipiente=excipiente) * volume_exp
        return [massa_exp,00]

