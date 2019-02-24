from flask import Flask,render_template,request
import datebase
app=Flask(__name__)


@datebase.app.route('/top250/list/<page>')#主页主体函数
def my_web(page):
    return render_template('top250.html',m_mes=datebase.movie.query.all(),pag=int(page))

@datebase.app.route('/top250/list/<page>',methods=['post','get'])#主页主体函数
def find(page):
    m_n = request.form.get('m_n')
    movie_get = datebase.movie.query.filter_by(m_name=m_n).first()
    return '<p>%s</p>' % movie_get


if __name__ == '__main__':
    datebase.app.run(debug=True)



