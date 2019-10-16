# coding: utf-8

import json

from HotpepperApi import * 

#testModule.pyを実行すると以下が実行される（モジュールとして読み込んだ場合は実行されない）
if __name__ == '__main__': 
	# json ファイルに「keyキー」があるものとする
	# （key:APIキー）
	f = open("HotPepperApiSetting.json", 'r')
	json_data = json.load(f)
	
	obj = HotpepperApi(json_data["key"])
	result = obj.get_shop_name_list("33.590543", "130.420096")
	
	print(result)
