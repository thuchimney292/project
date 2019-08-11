from mongoDB import get_book, sortt
from timkiem import no_vietnamese
from flask import Flask, render_template, request, url_for, session, redirect
app = Flask(__name__)
app.secret_key = "f4book"
# xemnhieu=sortt()
xemnhieu = get_book('kiemhiep')
@app.route('/', methods=['GET'])
def index():
    if 'username' not in session:
        return render_template('index.html', book=xemnhieu)
    return render_template('indexuser.html')


@app.route('/login')
def get_login():
    if 'username' in session:
        session.clear()
    return render_template('login.html')


@app.route('/login', methods=["POST"])
def post_login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == "1" and password == "1":
        session['username'] = username
        return redirect(url_for('index'))


@app.route("/kiemhiep", methods="GET")
def kiemhiep():
    data = get_book("kiemhiep")
    return render_template("kiemhiep.html", books=data)


@app.route("/tamly_kynangsong")
def tamly_kynangsong():
    data = get_book("tamly_kynangsong")
    return render_template("tamly_kynangsong.html", books=data)


@app.route("/huyenbi_giatuong")
def huyenbigiatuong():
    data = get_book("huyenbi_giatuong")
    return render_template("huyenbi_giatuong.html", books=data)


@app.route("/kinhte_quanly")
def kinhte_quanly():
    data = get_book("kinhte_quanly")
    return render_template("kinhte_quanly.html", books=data)


@app.route("/ma_kinhdi")
def ma_kinhdi():
    data = get_book("ma_kinhdi")
    return render_template("ma_kinhdi.html", books=data)


@app.route("/tieuthuyet_TrungQuoc")
def tieuthuyet_TrungQuoc():
    data = get_book("tieuthuyet_TrungQuoc")
    return render_template("tieuthuyet_TrungQuoc.html", books=data)


@app.route("/tieuthuyet_phuongTay")
def tieuthuyet_phuongTay():
    data = get_book("tieuthuyet_phuongTay")
    return render_template("tieuthuyet_phuongTay.html", books=data)


@app.route("/truyentranh")
def truyentranh():
    data = get_book("truyentranh")
    return render_template("truyentranh.html", books=data)


@app.route("/vanhoc_VietNam")
def vanhoc_VietNam():
    data = get_book("vanhoc_VietNam")
    return render_template("vanhoc_VietNam.html", books=data)


@app.route("/marketing_banhang")
def marketing_banhang():
    data = get_book("marketing_banhang")
    return render_template("marketing_banhang.html", books=data)


@app.route("/truyenngan_ngontinh")
def truyenngan_ngontinh():
    data = get_book("truyenngan_ngontinh")
    return render_template("truyenngan_ngontinh.html", books=data)


@app.route("/trinhtham_hinhsu")
def trinhtham_hinhsu():
    data = get_book("trinhtham_hinhsu")
    return render_template("trinhtham_hinhsu.html", books=data)


@app.route("/", methods=["POST"])
def search_():
    sr = no_vietnamese(request.form.get('search'))
    return redirect("/search/" + sr)


@app.route("/kiemhiep", methods=["POST"])
def search1():
    sr = no_vietnamese(request.form.get('search'))
    return redirect("/search/" + sr)


data = get_book('all')
@app.route('/search/<sr>')
def search(sr):
    ketqua = []
    count = 0
    for v in data:
        v_name = no_vietnamese(v['name'])
        if sr in list(v_name):
            ketqua.append(v)
            count += 1
    count = count//20
    return render_template('search.html', timkiem=ketqua, _key=sr, ct=count)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
