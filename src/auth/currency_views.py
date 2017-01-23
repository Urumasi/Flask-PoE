from flask import (Blueprint, escape, flash, render_template,
                   redirect, request, url_for)
from flask_login import current_user, login_required
from flask_wtf import Form
from wtforms.fields import IntegerField
from selenium import webdriver
from pyvirtualdisplay import Display
from fractions import Fraction

from ..data.models import CurrencyTypes, Transaction
from ..data.database import db

display = Display(visible=0, size=(800, 600))
display.start()

blueprint = Blueprint('currency', __name__)

URL_FORMAT = "http://currency.poe.trade/search?league=Standard&online=x&want=%s&have=%s"

@blueprint.route('/rates')
@login_required
def rates():
    return render_template('currency/rates_select.tmpl', currency_types=CurrencyTypes, str=str)

@blueprint.route('/rates/<int:curr>')
@login_required
def currency_rate(curr):
    if curr<0 or curr>=CurrencyTypes.__len__():
        redirect(url_for('.rates'))
    return render_template('currency/rates.tmpl', currency_types=CurrencyTypes, cid=curr-1, getattr=getattr, float=float, round=round, Fraction=Fraction)

@blueprint.route('/update_sell/<int:curr>', methods=['GET', 'POST'])
@login_required
def update_sell(curr):
    driver = webdriver.Firefox()
    driver.get(URL_FORMAT % ('-'.join([str(x.cid) for x in CurrencyTypes if x.cid!=curr]), curr))
    driver.implicitly_wait(10)
    elements = driver.find_elements_by_class_name('displayoffer')

    sell = []
    for i in range(CurrencyTypes.__len__()):
        sell.append(-1)
    for element in elements:
        x = (int(element.get_attribute('data-sellcurrency')), Fraction(Fraction(float(element.get_attribute('data-sellvalue'))), Fraction(float(element.get_attribute('data-buyvalue')))))
        if sell[x[0]-1]==-1:
            sell[x[0]-1] = x[1]
        else:
            sell[x[0]-1] = max(sell[x[0]-1], x[1])
    c = CurrencyTypes[curr-1]()
    for ct in CurrencyTypes:
        if sell[ct.cid-1]!=-1:
            setattr(c, ct.alt_name, str(sell[ct.cid-1]))
    c.save()

    driver.quit()
    return redirect(url_for('currency.currency_rate', curr=curr))

@blueprint.route('/update_buy/<int:curr>', methods=['GET', 'POST'])
@login_required
def update_buy(curr):
    driver = webdriver.Firefox()
    driver.get(URL_FORMAT % (curr, '-'.join([str(x.cid) for x in CurrencyTypes if x.cid!=curr])))
    driver.implicitly_wait(10)
    elements = driver.find_elements_by_class_name('displayoffer')

    buy = []
    for i in range(CurrencyTypes.__len__()):
        buy.append(-1)
    for element in elements:
        x = (int(element.get_attribute('data-buycurrency')), Fraction(Fraction(float(element.get_attribute('data-sellvalue'))), Fraction(float(element.get_attribute('data-buyvalue')))))
        if buy[x[0]-1]==-1:
            buy[x[0]-1] = x[1]
        else:
            buy[x[0]-1] = max(buy[x[0]-1], x[1])
    for ct in CurrencyTypes:
        if buy[ct.cid-1]!=-1:
            c = CurrencyTypes[ct.cid-1].get_latest() or CurrencyTypes[ct.cid-1]()
            setattr(c, CurrencyTypes[curr-1].alt_name, str(buy[ct.cid-1]))
            c.save()

    driver.quit()
    return redirect(url_for('currency.currency_rate', curr=curr))


@blueprint.route('/transactions', methods=['GET', 'POST'])
@login_required
def transactions():
    class F(Form):
        pass
    for c in CurrencyTypes:
        setattr(F, c.alt_name, IntegerField(default=0))
    form = F(request.form)
    print(request.form)
    if form.validate_on_submit():
        d = dict()
        for c in CurrencyTypes:
            if getattr(form, c.alt_name).data:
                d[c.alt_name] = getattr(form, c.alt_name).data
        Transaction.create(d)
    trans = db.session.query(Transaction).all()
    return render_template('currency/transactions.tmpl', currency_types=CurrencyTypes, trans=trans, getattr=getattr, form=form)
