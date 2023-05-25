from  flask import Flask,render_template,request
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import os

static_dir = os.path.join(os.getcwd(), 'static')
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

images_dir = os.path.join(static_dir, 'images')
if not os.path.exists(images_dir):
    os.makedirs(images_dir)
css_dir = os.path.join(static_dir, 'css')
if not os.path.exists(css_dir):
    os.makedirs(css_dir)
js_dir = os.path.join(static_dir, 'js')
if not os.path.exists(js_dir):
    os.makedirs(js_dir)
app = Flask(__name__,template_folder='templates')

@app.route('/')
def main():
    
    data=pd.read_csv('sparks001.csv')
    print(data)

    cnt=data['Segment'].value_counts()
    sns.barplot(x=cnt.index,y=cnt,data=cnt)
    plt.savefig('static/images/barplot.png') 
    plt.close()


    ship=data['Ship_Mode'].value_counts()
    sns.barplot(x=ship.index,y=ship,data=ship)
    plt.savefig('static/images/shipplot.png')
    plt.close()

    cnt=data['State'].value_counts()
    fig1=px.bar(cnt,x=cnt.index,y=cnt,text=cnt)
    image_path = os.path.join(images_dir, 'country.png')
    fig1.write_image(image_path)

    return render_template('index.html')

app.run(debug=True)