from flask import Flask
from flask import request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from sqlalchemy.exc import IntegrityError


app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


def add_save_to_db(db):

    def save(model):
        try:
            db.session.add(model)
            db.session.commit()
        except exc.IntegrityError as e:
            db.session().rollback()
            db.session.close()
            return False, 'Duplicate ID'
        return True, 'Created'
    db.Model.save = save

add_save_to_db(db)


@app.route("/", methods=["GET"])
def Home():
    return render_template("home.html")


@app.route("/input/", methods=['POST'])
def InputPost():
    if request.method == 'POST':
        from models import Features
        result = request.form.to_dict()
        task = Features(**result)
        task.save()
        return render_template('output.html')
    else:
        pass


@app.route("/output/", methods=['Get'])
def Inputget():

    if request.method == 'GET':
        from models import Features
        outputdec = Features.query.order_by(Features.TargetDate.desc())
        output = outputdec.all()
        return render_template('response.html', output=output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
