import gzip
import pickle

def load_world(blob):
    return gzip.decompress(blob)

def store_world(blob):
    data = pickle.dumps(blob)
    return gzip.compress(data)