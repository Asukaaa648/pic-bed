from flask import Flask, jsonify
import pandas as pd
import random

app = Flask(__name__)

# 读取url.csv文件
def read_image_urls(file_path):
    df = pd.read_csv(file_path)
    return df['url'].tolist()

# 加载图片URL列表
image_urls = read_image_urls('url.csv')

@app.route('/random-image', methods=['GET'])
def get_random_image():
    if not image_urls:
        return jsonify({'error': 'No images found'}), 404
    random_url = random.choice(image_urls)
    return jsonify({'url': random_url})

if __name__ == '__main__':
    app.run(debug=True)
