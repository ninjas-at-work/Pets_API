from flask import *
import json, time

from matplotlib.font_manager import json_dump


app = Flask(__name__, static_url_path='/static')

@app.route('/', methods = ['GET'])
def home():
    return json.dumps({'message':'access /kitties for cute af kitty pictures'})

@app.route('/kitties', methods = ['GET'])
def defaultPosts():
    cat_data = [{'Type':'Kitties', 'Name':'Tiger', 'Image':'static/images/Tiger.jpg', 'Says': "Rawr~"},
    {'Type':'Kitties', 'Name':'Dr.NotImpressed', 'Image':'static/images/Dr-notimpressed.jpg', 'Says': "Huh, what do you want? -_-"},
    {'Type':'Kitties', 'Name':'SmolBoi', 'Image':'static/images/smol-boi.jpg', 'Says': "mew? mew mew mew~"},
    {'Type':'Kitties', 'Name':'KawaiiBoi', 'Image':'static/images/kawaii-boi.jpg', 'Says': "Am I cute or am i cute wuvuvu~"},
    {'Type':'Kitties', 'Name':'MsGrumpy', 'Image':'static/images/what.jpg', 'Says': "Did you steal my cookies? huh? nvm"},
    {'Type':'Kitties', 'Name':'MsPepper', 'Image':'static/images/pretty.jpg', 'Says': "I am beautiful and I know it~"}]

    json_dump = json.dumps(cat_data)
    return json_dump


@app.route('/puppies', methods = ['GET'])
def get_puppies():
    json_dump = json.dumps({'message':'In progress'})


if __name__ == '__main__':
    app.run(port =7775 )