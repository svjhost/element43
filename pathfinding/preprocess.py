#!/usr/bin/env python

"""
Preprocess for pathfinding tables
Greg Oberfield - gregoberfield@gmail.com
"""

import psycopg2
import psycopg2.extras
import time
import ConfigParser
import os
import re
import networkx as nx
from hotqueue import HotQueue
import sys

# Load connection params from the configuration file
config = ConfigParser.ConfigParser()
config.read(['processor.conf', 'local_processor.conf'])
dbhost = config.get('Database', 'dbhost')
dbname = config.get('Database', 'dbname')
dbuser = config.get('Database', 'dbuser')
dbpass = config.get('Database', 'dbpass')
dbport = config.get('Database', 'dbport')
redisdb = config.get('Redis', 'redishost')
TERM_OUT = config.get('Consumer', 'term_out')

region_list = [10000001,10000002,10000003,10000005,10000006,10000007,10000008,10000009,10000010,10000011,10000012,10000013,10000014,10000015,10000016,10000018,10000020,10000021,10000022,10000023,10000025,10000027,10000028,10000067,10000029,10000030,10000031,10000032,10000033,10000034,10000035,10000036,10000037,10000038,10000039,10000040,10000041,10000042,10000043,10000044,10000045,10000046,10000047,10000048,10000049,10000050,10000051,10000052,10000053,10000054,10000055,10000056,10000057,10000058,10000059,10000060,10000061,10000062,10000063,10000064,10000065,10000066,10000068,10000069]

# Connect to PostgreSQL, auto commit.
dbcon = psycopg2.connect("host="+dbhost+" user="+dbuser+" password="+dbpass+" dbname="+dbname+" port="+dbport)
dbcon.autocommit = True
G = nx.Graph()

def main():
    curs = dbcon.cursor()
    sql = "SELECT id FROM eve_db_mapsolarsystem WHERE region_id IN (10000001,10000002,10000003,10000005,10000006,10000007,10000008,10000009,10000010,10000011,10000012,10000013,10000014,10000015,10000016,10000018,10000020,10000021,10000022,10000023,10000025,10000027,10000028,10000067,10000029,10000030,10000031,10000032,10000033,10000034,10000035,10000036,10000037,10000038,10000039,10000040,10000041,10000042,10000043,10000044,10000045,10000046,10000047,10000048,10000049,10000050,10000051,10000052,10000053,10000054,10000055,10000056,10000057,10000058,10000059,10000060,10000061,10000062,10000063,10000064,10000065,10000066,10000068,10000069)"
    curs.execute(sql)
    systems = curs.fetchall()
    for system in systems:
        G.add_node(system[0])
    sql = "SELECT from_solar_system_id, to_solar_system_id FROM eve_db_mapsolarsystemjump WHERE from_region_id IN (10000001,10000002,10000003,10000005,10000006,10000007,10000008,10000009,10000010,10000011,10000012,10000013,10000014,10000015,10000016,10000018,10000020,10000021,10000022,10000023,10000025,10000027,10000028,10000067,10000029,10000030,10000031,10000032,10000033,10000034,10000035,10000036,10000037,10000038,10000039,10000040,10000041,10000042,10000043,10000044,10000045,10000046,10000047,10000048,10000049,10000050,10000051,10000052,10000053,10000054,10000055,10000056,10000057,10000058,10000059,10000060,10000061,10000062,10000063,10000064,10000065,10000066,10000068,10000069)"
    curs.execute(sql)
    results = curs.fetchall()
    for row in results:
        G.add_edge(row[0], row[1])
    
    print len(results)
    print "Piak neighbors: ", G.neighbors(30001403)
    path = nx.shortest_path(G, source=30001403, target=30000142)
    print path

if __name__ == '__main__':
    main()