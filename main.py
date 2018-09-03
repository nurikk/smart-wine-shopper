from parse import fetchData, fetchData2
from render import renderImage


if __name__ == '__main__':
    renderImage(fetchData2(), '/tmp/img1.jpg')