import sqlite3
from wsgiref.util import request_uri
from flask import Flask, jsonify, render_template, request, redirect 
from flask_mail import Mail, Message 
import email
import smtplib


banco = sqlite3.connect('correio_elegante.db')

cursor = banco.cursor()

cursor.execute("CREATE TABLE cartas (prime_nome text, ulti_nome text, mensagem text)")


app = Flask(name)


@app.route("/")
@app.route("/home")
def cartinha():
    return render_template('index.html')


# formulario html 
@app.route("/msg", methods=['GET', 'POST'])
def mensagem():

    if request.method == "POST":
        req = request.form

        primeiroNome = req['primeiroNome']
        segundoNome = req['segundoNome']
        mensagem = req['msg']

        msg = email.message_from_string(mensagem)
        msg['From'] = "correioelegante.impacta@outlook.com"
        msg['To'] = f"{primeiroNome}.{segundoNome}@aluno.faculdadeimpacta.com.br"
        msg['Subject'] = "Corre io Elegante Impacta 2020"

        cursor.execute("INSERT INTO cartas (prime_nome, ulti_nome, mensagem) VALUES (?,?,?,?)", (primeiroNome, segundoNome, mensagem))
        banco.commit()
        cursor.execute("SELECT * FROM cartas")
        print(cursor.fetchall())


        s = smtplib.SMTP("smtp.office365.com",587)
        s.ehlo() 
        s.starttls() 
        s.ehlo()
        with open("senha.txt", 'r') as senha:
            s.login(msg['From'], senha.read())

        s.sendmail(msg['To'], 
        msg['From'], msg.as_string())

        s.quit()




        return redirect(request.url)

    return render_template('formulario.html')







if name  == 'main':
    app.run(debug = True)
