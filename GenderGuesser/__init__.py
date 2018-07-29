# -*- coding:utf-8 -*-
import json, os
import pickle

class GenderGuesser():
	charProDic = None

	def __init__( self, pkl_path = None ):
		if pkl_path:
			self.load_pkl_file(pkl_path)

	def load_pkl_file( self, pkl_path ):
		if not pkl_path or not os.path.isfile(pkl_path):
			print("error", pkl_path)
			return False
		elif self.charProDic:
			return True
		else:
			with open( pkl_path, "rb" ) as ff:
				self.charProDic = pickle.load(ff)['chars']

	def getMaleProbability( self, name ): #w = 0.45
		prob = 0.0
		if not name or not self.charProDic:
			return prob 
		chars = []
		for char in name:
			chars.append(char)
		if len(chars) < 2 or len(chars) > 4:
			return prob
		elif len(chars) == 4:
			chars.pop(0)
			chars.pop(1)
		else:
			chars.pop(0)

		if len(chars) == 1:
			if chars[0] in self.charProDic:
				prob = self.charProDic[chars[0]]
			else:
				prob = 0.5
		else:
			if chars[0] in self.charProDic:
				prob = self.charProDic[chars[0]] * 0.45
			else:
				prob = 0.5 * 0.45
			if chars[1] in self.charProDic:
				prob += self.charProDic[chars[1]] * (1 - 0.45)
			else:
				prob += 0.5 * (1 - 0.45)
		return prob;

genderGuesser = GenderGuesser()