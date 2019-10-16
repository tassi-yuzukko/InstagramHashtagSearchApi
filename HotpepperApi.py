# coding: utf-8

import requests
import json


class HotpepperApi:
    # API��URL
    api = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/?key={key}&lat={lat}&lng={lng}&range=2&order=1&format=json"
    
    # �R���X�g���N�^�����FAPI�L�[
    def __init__(self, api_key):
        self.api_key = api_key
        
    # �ܓx�E�o�x���w�肵�čŊ��̈��H�X�����X�g���擾�i�Ƃ肠�����������a��500m�Œ�j
    def get_shop_name_list(self, lat, lng):
        url = self.api.format(key=self.api_key, lat=lat, lng=lng)
        response = requests.get(url)
        result_list = json.loads(response.text)["results"]["shop"]
        return [d.get("name") for d in result_list]
