from flask import Flask
import os
from flask_sqlalchemy  import SQLAlchemy
import pymysql
app=Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:123456@127.0.0.1/douban"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db=SQLAlchemy(app)#听说这叫配置数据库

class movie(db.Model):
    __tablename__='movie'
    m_name=db.Column(db.String,primary_key=True)
    m_score=db.Column(db.String,unique=False)
    m_intro=db.Column(db.String,unique=False)

    def __init__(self,m_name,m_score,m_intro):
        self.m_name = m_name
        self.m_score=m_score
        self.m_intro=m_intro

    def __repr__(self):
        return  "影名：%s- - - -豆瓣评分：%s- - - - - - 一句话评价：%s"%(self.m_name,self.m_score,self.m_intro)





