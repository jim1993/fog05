import uuid
import sys
import os
sys.path.append(os.path.join(sys.path[0].rstrip("tests")))
from DStore import *
import dds
import json
import time

def test_miss(sid, root, home):

    sroot = "fos://{0}".format(root)
    shome= "fos://{0}/{1}".format(root, home)

    store = DStore(sid, sroot, home, 1024)

    uri_prefix = "fos://{0}/{1}/{2}".format(root, home, sid)
    store.put(uri_prefix, 'I am a store fos://{0}/{1}/{2}!'.format(root, home, sid))

    print("Store written, press a key to continue")
    input()
    # local get
    v = store.get(uri_prefix)
    print('=========> store[{0}] = {1}'.format(uri_prefix, v))
    print("\nStore get exectured, press a key to continue")
    input()
    # try get that need resolving
    for id in store.discovered_stores:
        uri = "fos://{0}/{1}/{2}".format(root, home, id)
        v = store.get(uri)
        print('=========> store[{0}] = {1}'.format(uri, v))

    print("\nStore remote get exectured, press a key to continue")
    input()
    # try to get them in a single shot -- locally:

    uri = "fos://{0}/{1}/*".format(root, home)
    vs = store.getAll(uri)
    print('=========> store[{0}] = {1}'.format(uri, vs))

    print("\nStore local get-all exectured, press a key to continue")
    input()

    vs = store.resolveAll(uri)
    print('=========> store[{0}] = {1}'.format(uri, vs))

    print("\nStore remote resolve-all exectured, press a key to continue")
    input()


if __name__ == "__main__":
    argc = len(sys.argv)

    if argc > 3:
        test_miss(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print('USAGE:\n\tpython3 test_miss.py <sid> <store-root> <store-home>')