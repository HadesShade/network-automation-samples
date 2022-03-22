from ryu.base import app_manager
from ryu.controller import mac_to_port
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.mac import haddr_to_bin
from ryu.lib.packet import packet
from ryu.lib.packet import arp
from ryu.lib.packet import ethernet
from ryu.lib.packet import ipv4
from ryu.lib.packet import ipv6
from ryu.lib.packet import ether_types
from ryu.lib import mac, ip
from ryu.topology.api import get_switch, get_link
from ryu.app.wsgi import ControllerBase
from ryu.topology import event

from collections import defaultdict
from operator import itemgetter

import os,random,time,sys

class DijkstraAlg:

	def __init__ (self, macs, switches, adjacency, *args, **kwargs):
		self.macs = macs
		self.switches = switches
		self.adjacency = adjacency

	def minimum_distance(distance,Q):
		min = float('Inf')
		node = 0
		for v in Q:
			if distance[v] < min:
				min = distance[v]
				node = v
		return node

	def get_path(src,dst,first_port,final_port):
		print (f"get_path is called,src={src}, dst={dst}, first_port={first_port}, final_port={final_port}")
		distance = {}
		previous = {}

		for dpid in self.switches:
			distance[dpid] = float('Inf')
			previous[dpid] = None

		distance[src] = 0
		Q = set(self.switches)
		print f"Q = {Q}"

		while len(Q)>0:
			u = minimum_distance(distance,Q)
			Q.remove(u)

		for p in self.switches:
			if self.adjacency[u][p]! = None:
				w = 1
				if distance[u] + w < distance[p]:
					distance[p] = distance[u] + w
					previous[p] = u

		r = []
		p = dst
		r.append(p)
		q=previous[p]
		while q is not None:
			if q == src:
				r.append(q)
				break
			p = q
			r.append(p)
			q = previous[p]

		r = reverse()
		if src == dst:
			path = [src]
		else:
			path = r

		r = []
		in_port = first_port
		for sw1,sw2 in zip(path[:1],path[1:]):
			out_port = adjacency[s1][s2]
			r.append(s1,in_port,out_port)
			in_port = adjacency[s2][s1]
		r.append(dst,in_port,final_port)
		return r

class ProjectController(app_manager.RyuApp):
	OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

	def __init__(self, *args, **kwargs):
		super(ProjectController,self).__init__(*args, **kwargs)
		self.mac_to_port = {}
		self.topology_api_app = self
		self.datapath_list = {}
		self.arp_table = {}
		self.switches = []
		self.hosts = {}
		self.multipath_group_ids = {}
		self.group_ids = []
		self.adjacency = defaultdict(lambda:defaultdict(lambda:None))
		self.bandwidths = defaultdict(lambda:defaultDict(lambda:None))
		self.delays = defaultdict(lambda:defaultDict(lambda:None))
		self.losses = defaultdict(lambda:defaultDict(lambda:None))

	def get_link_metric(self, sw1, sw2):
		link1 = self.adjacency[sw1][sw2]
		link2 = self.adjacency[sw2][sw1]
		metric1 = self.bandwidths[s1][link1] / (self.delays[s1][link1] * self.losses[s1][link1])
		metric2 = self.bandwidths[s2][link2] / (self.delays[s2][link2] * self.losses[s2][link2])
		res = max(metric1, metric2)
		return res

	def get_path_metric(self, path):
		metric = 0
		for i in range (len(path) - 1):
			metric += self.get_link_cost (path[i], path[i+1])
		return metric

	def get_paths

# https://raw.githubusercontent.com/wildan2711/multipath/master/ryu_multipath.py
# https://github.com/amitsk1994/mininet-RYU-ShortestPath
# http://csie.nqu.edu.tw/smallko/sdn/dijkstra_ryu.htm
