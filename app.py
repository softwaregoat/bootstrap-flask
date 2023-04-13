from flask_bootstrap import Bootstrap5
from flask import Flask, request, render_template, url_for
from include.image_info import image_info
import random
import cv2

app = Flask(__name__)

bootstrap = Bootstrap5(app)


@app.route('/')
def index():
    randomlist = random.sample(range(0, len(image_info)), 3)

    images = []
    for i in randomlist:
        images.append(image_info[i])

    return render_template('index.html', images=images)


@app.route('/picture/<image_id>')
def img_view(image_id):

    imgs = list(filter(lambda f: (f["id"] == image_id), image_info))
    img = imgs[0]
    src = f'./static/images/{image_id}.jpg'
    im = cv2.imread(src)
    h, w, c = im.shape

    image = {
        'id': image_id,
        'title': img["title"],
        'width': w,
        'height': h,
    }

    print(image)

    return render_template('img_view.html', image=image)
