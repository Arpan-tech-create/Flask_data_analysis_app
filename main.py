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
app = Flask(__name__,template_folder='templptes')

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

    return "HI"

app.run(debug=True)