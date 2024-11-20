from flask import Flask, jsonify, request
from findbook.findbook import *
from VideoPlay.playVideo import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/Spider/*": {"origins": "*"}})

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/Spider/find_xuanhuan')
def xuanhuan():
    return jsonify(find_xuanhuan())

@app.route('/Spider/find/inType')
def find_inType():
    sortid = request.args.get('sortid')  # 获取查询参数
    page = request.args.get('page')
    response = inType(sortid, page)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/Spider/find/search')
def find_search():
    keyword = request.args.get('keyword')
    res = search(keyword)
    return res

@app.route('/Spider/find/readBook')
def find_readBook():
    url = request.args.get('url')
    url = 'https://www.bqgui.cc'+url
    readbook(url)


@app.route('/Spider/yinhua/home')
def yinhua_home():
    res = jsonify(get_yinhua_home_scroll('https://www.yinhuadm.vip/'))
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res

@app.route('/Video/getPlay')
def getPlay():
    res = getVideoUrl('https://www.yinhuadm.vip/p/25365-2-1.html')
    while res == None: res = getVideoUrl('https://www.yinhuadm.vip/p/25365-2-1.html')
    res = jsonify(res)
    # res = getVideoUrlWithTimeOut('https://www.yinhuadm.vip/p/25365-2-1.html')
    # if res == None: 
    #     res = jsonify({'error': 'timeout'})
    # else:
    #     res = res.replace('index.m3u8', '2100k/hls/mixed.m3u8')
    #     resp = request.get(res)
    #     if resp.status_code == 200: 
    #         res = jsonify(res)
    #     else:
    #         res.replace('2100k/hls/mixed.m3u8', '2000k/hls/mixed.m3u8')
    #         res = jsonify(res)
    #res = jsonify(getVideoM3U8('https://v.cdnlz14.com/20240402/36529_66126ae8/2100k/hls/mixed.m3u8'))
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res


if __name__ == '__main__':
    app.run(debug=True, port=5001)