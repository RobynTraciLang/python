from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import cookie_order_model


@app.route('/cookies')
def display_cookie_orders_page():
    cookie_order = cookie_order_model.Cookie_order.get_all_cookie_orders()
    return render_template('cookie_orders.html', cookie_order = cookie_order)

@app.route('/cookies/new')
def display_log_new_order_page():
    cookie_type = cookie_order_model.Cookie_order.create_cookie_order(request.form)
    return render_template('log_a_new_order.html', cookie_type = cookie_type)

@app.route('/cookies/new', methods = ['POST'])
def log_new_cookie_order():
    if cookie_order_model.Cookie_order.validate_cookie_order(request.form):
        cookie_order_model.Cookie_order.create_cookie_order(request.form)
        return redirect('/cookies')
    return redirect('/cookies/new')

@app.route('/cookies/edit/<int:id>')
def display_change_order_page(id):
    update_this_cookie_order = cookie_order_model.Cookie_order.get_one_cookie_order(id)
    return render_template('change_order.html', cookie_order = update_this_cookie_order)

@app.route('/cookies/edit/<int:id>', methods = ['POST'])
def change_cookie_order(id):
    data = {
        'id': id,
        'customer_name': request.form['customer_name'],
        'cookie_type': request.form['cookie_type'],
        'number_of_boxes': request.form['number_of_boxes'],
        }
    if cookie_order_model.Cookie_order.validate_cookie_order(request.form):
        cookie_order_model.Cookie_order.update_cookie_order(data)
        return redirect('/cookies')
    return redirect(f'/cookies/edit/{id}')