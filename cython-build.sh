
set -x # verbose
set -e # exit on error

cython apiserver.py --embed

gcc apiserver.c -o apiserver $(pkg-config --cflags --libs python-3.11-embed)
# gcc apiserver.c -o apiserver $(pkg-config --cflags --libs --static python-3.11-embed) -L /usr/lib/python3.11/config-3.11-x86_64-linux-gnu/ -lm -static -static-libgcc


