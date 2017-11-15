#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import cluster_index_lib.internal_index as ii
# import cluster_index_lib.external_index as ei
import argparse


def main(args):
    """Main."""
    data = np.loadtxt(args.data)
    labels = np.loadtxt(args.labels)

    print('c_index')
    print(ii.c_index(labels, data))

    print('calinski_harabasz')
    print(ii.calinski_harabasz(labels, data))

    print('log_ss_ratio')
    print(ii.log_ss_ratio(labels, data))

    print('ball_hall')
    print(ii.ball_hall(labels, data))

    print('sd_scat')
    print(ii.average_scattering(labels, data))

    print('sd_dis')
    print(ii.total_separation(labels, data))

    # print('S_Dbw')
    # print(ii.s_dbw(labels, data))

    print('Xie-Beni')
    print(ii.xie_beni(labels, data))

    print('Ray-Turi')
    print(ii.ray_turi(labels, data))

    print('Gamma')
    print(ii.gamma(labels, data))

    print('Tau')
    print(ii.tau(labels, data))

    print("Silhouette")
    print(ii.silhouette(labels, data))


parser = argparse.ArgumentParser(
    description="")

parser.add_argument(
    '-d',
    '--data',
    help='data file *.data'
)
parser.add_argument(
    '-l',
    '--labels',
    help='labels file *.labels'
)
parser.set_defaults(func=main)
args = parser.parse_args()
args.func(args)
