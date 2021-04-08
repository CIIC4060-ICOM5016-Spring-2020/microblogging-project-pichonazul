from re import error
from flask import jsonify
from model.likes import LikesDAO

class BaseLikes:
    def build_map_dict(self, row):
        result = {}
        result['lid'] = row[0]
        result['mid'] = row[1]
        result['uid'] = row[2]
        return result

    def build_like_attr_dict(self, lid):
        result = {}
        result['lid'] = lid
        return result

    def getLikedById(self, l_mid):
        dao = LikesDAO()
        liked_list = dao.getLikedById(l_mid)
        result_list = []
        for row in liked_list:
            obj = self.build_map_dict(row)
            result_list.append(obj)
        return jsonify(result_list), 200

    def getAllLikesId(self, l_mid):
        dao = LikesDAO()
        liked_list = dao.getAllLikesId(l_mid)
        result_list = []
        for row in liked_list:
            obj = self.build_map_dict(row)
            result_list.append(obj)
        return jsonify(result_list), 200


    def likeMessage(self, json, l_mid):
        uid = json['RegisteredUser']
        dao = LikesDAO()
        lid = dao.likeMessage(l_mid, uid)
        result = self.build_like_attr_dict(lid)
        return jsonify(result), 201

    def unlikeMessage(self, json, l_mid):
        r_uid = json['RegisteredUser']
        dao = LikesDAO()
        lid = dao.unlikeMessage(r_uid, l_mid)
        result = self.build_like_attr_dict(lid)
        return jsonify(result), 201