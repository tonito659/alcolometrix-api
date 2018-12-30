from flask import Flask, jsonify, make_response, request, abort, g
import time
import sqlite3

DATABASE = "db.sqlite"

app = Flask(__name__)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/')
def hello_world():
    dict = {
        'alcolometrix-api': 'drink safe',
        "version": 1.0
    }
    return jsonify({"desc" : dict})


@app.route('/api/beverage', methods = ["POST"])
def add_an_item():
    if not request.json or not ('barcode'|'price'|'postcode') in request.json:
        abort(400)

        barcode = request.json.get('barcode')
        date = int(time.time())
        price = request.json.get('price')
        postcode = request.json.get('postcode')
    try:
        db = get_db()
        cur = db.cursor()
        cur.execute("INSERT INTO alcolometrix_api (epoch, barcode, price, localization) VALUES (?,?,?,?)",(date, barcode, price, postcode))
        db.commit()
        return jsonify({'task': 'success'}), 201

    except:
        db.rollback()
        return jsonify({'task': 'failure'}), 500


@app.route('/api/beverage/', methods=['GET'])
def get_all_beverage():
    infos = query_db('select * from alcolometrix_api')
    if infos is None or infos == []:
        return jsonify({'task': 'failure'}), 404
    else:
        return jsonify(infos), 200


@app.route('/api/price/<int:barcode>', methods=['GET'])
def get_beverage(barcode):
    infos = query_db('select * from alcolometrix_api where barcode = ?',
                [barcode])
    if infos is None or infos == []:
        return jsonify({'task': 'failure'}), 404
    else:
        return jsonify(infos), 200


@app.route('/api/price/<int:barcode>/<int:postcode>', methods=['GET'])
def get_beverage_postcode(barcode, postcode):
    infos = query_db('select round(avg(price),2)  from alcolometrix_api where barcode = ? and postcode = ?',
                [barcode,postcode], one=True)
    if infos is None or infos == []:
        return jsonify({'task': 'failure'}), 404
    else:
        return jsonify(infos), 200


if __name__ == '__main__':
    init_db()
    app.run(debug=False, host= '0.0.0.0')
