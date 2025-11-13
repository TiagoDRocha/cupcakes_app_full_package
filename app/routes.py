from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from . import db
from .models import Produto, Pedido, ItemPedido, Feedback
main_bp = Blueprint('main', __name__)
@main_bp.route('/')
def index():
    produtos = Produto.query.all()
    return render_template('index.html', produtos=produtos)
@main_bp.route('/produto/<int:pid>')
def produto(pid):
    p = Produto.query.get_or_404(pid)
    return render_template('produto.html', produto=p)
@main_bp.route('/admin/produto/criar', methods=['GET','POST'])
def admin_criar_produto():
    if request.method == 'POST':
        nome = request.form.get('nome')
        preco = float(request.form.get('preco',0))
        estoque = int(request.form.get('estoque',0))
        descricao = request.form.get('descricao','')
        p = Produto(nome=nome, preco=preco, estoque=estoque, descricao=descricao)
        db.session.add(p)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('admin_criar.html')
@main_bp.route('/feedback', methods=['GET','POST'])
def feedback():
    if request.method == 'POST':
        nome = request.form.get('nome') or None
        contato = request.form.get('contato') or None
        tipo = request.form.get('tipo') or 'outro'
        descricao = request.form.get('descricao') or ''
        screenshot = request.form.get('screenshot') or None
        if not descricao.strip():
            return render_template('feedback.html', error='Descrição é obrigatória', form=request.form)
        fdb = Feedback(nome=nome, contato=contato, tipo=tipo, descricao=descricao, screenshot=screenshot)
        db.session.add(fdb)
        db.session.commit()
        return render_template('feedback.html', success=True)
    return render_template('feedback.html')
