import os

class Config:
   
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///meudb.db'
    SECRET_KEY = 'dguhguihjghfdgçhakghfkahkaçhjiuriuqtoúgiqyrtyídksçakgeahyqt8qu´9ugjojaçkhroyr9WJÇLSDJGKAIATY´9QUÝJROGJAFKAALHDTYY943860[IP~ÇLÇJKHYF58RT7IPJIHYFU6GOYHUIHÇ'
    MAIL_USERNAME        = os.environ.get('EMAIL_USERNAME')
    MAIL_PASSWORD        = os.environ.get('EMAIL_PASSWORD')
    MAIL_SERVER          = os.environ.get('EMAIL_SERVER')
    MAIL_PORT            = os.environ.get('EMAIL_PORT')
    MAIL_DEFAULT_SENDER  = os.environ.get('EMAIL_DEFAULT_SENDER')
    MAIL_USE_TLS         = os.environ.get('EMAIL_USE_TLS')
    MAIL_USE_SSL         = os.environ.get('EMAIL_USE_SSL')
    print (MAIL_USERNAME)
    print (MAIL_PASSWORD)
    print (MAIL_SERVER)
    print (MAIL_PORT)
    print (MAIL_DEFAULT_SENDER)
    print (MAIL_USE_TLS)
    print (MAIL_USE_SSL)
    
class DevolopmentConfig(Config):
    DEBUG = True

class TestConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    
class ProductionConfig(Config):
    DEBUG = True
    
app_config ={
            'development': DevolopmentConfig,
            'test': TestConfig,
            'production': ProductionConfig
            }