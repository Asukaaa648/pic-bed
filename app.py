from flask import Flask, redirect
import pandas as pd
import random

app = Flask(__name__)

# 读取url.csv文件
def read_image_urls(file_path):
    # 读取CSV文件，没有标题行
    df = pd.read_csv(file_path, header=None)
    # 手动设置列名
    df.columns = ['url']
    return df['url'].tolist()

# 加载图片URL列表
image_urls = read_image_urls('url.csv')

@app.route('/random-image', methods=['GET'])
def get_random_image():
    if not image_urls:
        return "No images found", 404
    random_url = random.choice(image_urls)
    return redirect(random_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
