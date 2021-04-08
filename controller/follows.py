from re import error
from flask import jsonify
from model.follows import FollowsDAO

class BaseFollows:
    def build_map_dict(self, row):
        result = {}
        result['fid'] = row[0]
        result['uid'] = row[1]
        result['followed_user'] = row[2]
        return result

    def build_follow_attr_dict(self, fid):
        result = {}
        result['fid'] = fid
        return result

    def getFollowedById(self, r_uid):
        dao = FollowsDAO()
        followed_list = dao.getFollowedById(r_uid)
        result_list = []
        for row in followed_list:
            obj = self.build_map_dict(row)
            result_list.append(obj)
        return jsonify(result_list), 200

    def getAllUsersFollowingId(self, f_uid):
        dao = FollowsDAO()
        followed_list = dao.getAllUsersFollowingId(f_uid)
        result_list = []
        for row in followed_list:
            obj = self.build_map_dict(row)
            result_list.append(obj)
        return jsonify(result_list), 200

    def followUser(self, json, f_uid):
        r_uid = json['RegisteredUser']
  
        print(r_uid)
        if(r_uid == f_uid):
            return jsonify("Users cannot follow themselves."), 400
        dao = FollowsDAO()
        fid = dao.followUser(r_uid, f_uid)
        result = self.build_follow_attr_dict(fid)
        return jsonify(result), 201

    def unfollowUser(self, json, f_uid):
        r_uid = json['RegisteredUser']
        dao = FollowsDAO()
        fid = dao.unfollowUser(r_uid, f_uid)
        result = self.build_follow_attr_dict(fid)
        return jsonify(result), 201