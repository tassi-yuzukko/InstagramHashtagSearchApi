# coding: utf-8

import json

from HotpepperApi import * 

#testModule.py�����s����ƈȉ������s�����i���W���[���Ƃ��ēǂݍ��񂾏ꍇ�͎��s����Ȃ��j
if __name__ == '__main__': 
	# json �t�@�C���Ɂukey�L�[�v��������̂Ƃ���
	# �ikey:API�L�[�j
	f = open("HotPepperApiSetting.json", 'r')
	json_data = json.load(f)
	
	obj = HotpepperApi(json_data["key"])
	result = obj.get_shop_name_list("33.590543", "130.420096")
	
	print(result)
