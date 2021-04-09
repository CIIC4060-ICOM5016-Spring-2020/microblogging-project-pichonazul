from re import error
from flask import jsonify
from model.dislikes import DislikesDAO

class BaseDislikes:
    def build_map_dict(self, row):
        result = {}
        result['did'] = row[0]
        result['mid'] = row[1]
        result['uid'] = row[2]
        return result

    def build_dislike_attr_dict(self, did):
        result = {}
        result['did'] = did
        return result

    def getDislikedById(self, d_mid):
        dao = DislikesDAO()
        disliked_list = dao.getLikedById(d_mid)
        result_list = []
        for row in disliked_list:
            obj = self.build_map_dict(row)
            result_list.append(obj)
        return jsonify(result_list), 200

    def getAllDislikesId(self, d_mid):
        dao = DislikesDAO()
        disliked_list = dao.getAllDislikesId(d_mid)
        result_list = []
        for row in disliked_list:
            obj = self.build_map_dict(row)
            result_list.append(obj)
        return jsonify(result_list), 200


    def dislikeMessage(self, json, d_mid):
        uid = json['RegisteredUser']
        dao = DislikesDAO()
        did = dao.dislikeMessage(d_mid, uid)
        result = self.build_dislike_attr_dict(did)
        return jsonify(result), 201

    def undislikeMessage(self, json, d_mid):
        r_uid = json['RegisteredUser']
        dao = DislikesDAO()
        did = dao.undislikeMessage(d_mid, r_uid)
        result = self.build_dislike_attr_dict(did)
        return jsonify(result), 201