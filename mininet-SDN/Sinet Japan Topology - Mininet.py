from mininet.topo import Topo

class TATopo(Topo):
	def __init__(self):
		Topo.__init__(self)

		s1 = self.addSwitch('s1')
		s2 = self.addSwitch('s2')
		s3 = self.addSwitch('s3')
		s4 = self.addSwitch('s4')
		s5 = self.addSwitch('s5')
		s6 = self.addSwitch('s6')
		s7 = self.addSwitch('s7')
		s8 = self.addSwitch('s8')
		s9 = self.addSwitch('s9')
		s10 = self.addSwitch('s10')
		s11 = self.addSwitch('s11')
		s12 = self.addSwitch('s12')

		h1 = self.addHost('h1')
		h2 = self.addHost('h2')
		h3 = self.addHost('h3')
		h4 = self.addHost('h4')
		h5 = self.addHost('h5')
		h6 = self.addHost('h6')
		h7 = self.addHost('h7')
		h8 = self.addHost('h8')
		h9 = self.addHost('h9')
		h10 = self.addHost('h10')
		h11 = self.addHost('h11')
		h12 = self.addHost('h12')

		self.addLink(s1,h1)
		self.addLink(s1,s2)
		self.addLink(s1,s6)

		self.addLink(s2,h2)
		self.addLink(s2,s3)

		self.addLink (s3,h3)
		self.addLink (s3,s4)

		self.addLink (s4,h4)
		self.addLink (s4,s5)
		self.addLink (s4,s7)

		self.addLink (s5,h5)
		self.addLink (s5,s6)

		self.addLink(s6,h6)
		self.addLink(s6,s8)

		self.addLink(s7,h7)
		self.addLink(s7,s9)

		self.addLink(s8,h8)
		self.addLink(s8,s9)
		self.addLink(s8,s10)

		self.addLink(s9,s11)
		self.addLink(s9,h9)

		self.addLink(s10,s12)
		self.addLink(s10,h10)

		self.addLink(s11,h11)
		self.addLink(s11,s12)

		self.addLink(s12,h12)

topos = { 'tatopo': (lambda: TATopo() ) }

# Run command : sudo mn --controller remote,ip=<SDN Address> --switch=ovs,protocols=OpenFlow13 --custom <path to this code> --topo tatopo
