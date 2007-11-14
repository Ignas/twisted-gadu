#(C) Marek Chrusciel, 
#    Jakub Kosinski, 
#    Marcin Krupowicz,
#    Mateusz Strycharski
#
# $Id$

import struct

class GGIncomingPacket(object):
	"""
	"Abstrakcyjna" klasa pakietow przychodzacych od serwera
	"""
	def read(self):
		pass


class GGWelcome(GGIncomingPacket):
	"""
	Pakiet wysylany przez serwer zaraz po nawiazaniu polaczenia.
	Znajduje sie w nim 'seed' konieczny do zalogowania sie do serwera.
	"""
	def __init__(self):
		self.seed = None
	
	def read(self, connection):
		self.seed = struct.unpack("<I", connection.read())[0]
		
