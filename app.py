from flask import Flask, render_template, request, redirect, url_for
from models import db, Item 


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///VOT_Proekt.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

with app.app_context():
    db.create_all()  


@app.route('/')
def index():
    items = Item.query.all()
    return render_template('index.html', items=items)


@app.route('/add', methods=['POST'])
def add_item():
    name = request.form.get('name')
    if name:
        new_item = Item(name=name)
        db.session.add(new_item)
        db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    item = Item.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
