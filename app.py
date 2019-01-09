from distutils.log import Log

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
        db.close()


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
    return jsonify({"desc": dict})


@app.route('/api/beverage', methods=["POST"])
def add_an_item():
    content = request.get_json()
    barcode = request.json.get('barcode')
    date = int(time.time())
    price = request.json.get('price')
    postcode = request.json.get('postcode')
    city = request.json.get('city')

    print(content)
    print(barcode)
    print(date)
    print(price)
    print(postcode)
    print(city)

    database = get_db()
    cur = database.cursor()
    try:

        cur.execute("INSERT INTO alcolometrix_api (date, barcode, price, postcode, localization) VALUES (?,?,?,?,?)"
                    , (date, barcode, price, postcode, city))

        success = jsonify({'task': 'success'})

    except Exception:
        database.rollback()
        success = jsonify({'task': 'failure'})

    finally:
        database.commit()
        return success


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
                     [barcode, postcode], one=True)
    if infos is None or infos == []:
        return jsonify({'task': 'failure'}), 404
    else:
        return jsonify(infos[0]), 200


if __name__ == '__main__':
    init_db()
    db = get_db()
    app.run(debug=True, host='0.0.0.0')
