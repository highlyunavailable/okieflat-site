from werkzeug.contrib.cache import SimpleCache
import yaml
cache = SimpleCache()

def get_products():
    cache.clear()
    rv = cache.get('products_list')
    if rv is None:
        rv = yaml.load(open('static/data/products.yaml'))
        cache.set('products_list', rv, timeout=30)
    return rv