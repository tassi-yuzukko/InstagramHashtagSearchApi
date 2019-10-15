# coding: utf-8

import json

from InstagramHashtagSearch import * 

#testModule.pyを実行すると以下が実行される（モジュールとして読み込んだ場合は実行されない）
if __name__ == '__main__': 
	# json ファイルに「accountキー」と「tokenキー」があるものとする
	# （account:ビジネスアカウントID、token：APIトークン）
	f = open("setting.json", 'r')
	json_data = json.load(f)
	
	obj = InstagramHashtagSearch(json_data["account"], json_data["token"])
	result = obj.get_media_url_list("coke")
	
	print(result)
