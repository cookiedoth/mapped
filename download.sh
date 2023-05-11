#!/bin/zsh

# rm maps.tar.gz
# wget http://efrosgans.eecs.berkeley.edu/pix2pix/datasets/maps.tar.gz

rm -r maps
rm -r dataset
tar -xvf maps.tar.gz
mv maps dataset
rm maps.tar.gz
