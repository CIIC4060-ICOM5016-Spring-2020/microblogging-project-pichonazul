from re import error
from flask import jsonify
from model.blocks import BlocksDAO

class BaseBlocks:
    def build_map_dict(self, row):
        result = {}
        result['bid'] = row[0]
        result['registered_uid'] = row[1]
        result['blocked_uid'] = row[2]
        return result

    def build_block_attr_dict(self, bid):
        result = {}
        result['bid'] = bid
        return result

    def getBlockedById(self, r_uid):
        dao = BlocksDAO()
        blocked_list = dao.getBlockedById(r_uid)
        result_list = []
        for row in blocked_list:
            obj = self.build_map_dict(row)
            result_list.append(obj)
        return jsonify(result_list), 200

    def getAllUsersBlockingId(self, b_uid):
        dao = BlocksDAO()
        blocked_list = dao.getAllUsersBlockingId(b_uid)
        result_list = []
        for row in blocked_list:
            obj = self.build_map_dict(row)
            result_list.append(obj)
        return jsonify(result_list), 200


    def blockUser(self, json, b_uid):
        r_uid = json['RegisteredUser']
        if(r_uid == b_uid):
            return jsonify("Users cannot block themselves."), 400
        dao = BlocksDAO()
        bid = dao.blockUser(r_uid, b_uid)
        result = self.build_block_attr_dict(bid)
        return jsonify(result), 201

    def unblockUser(self, json, b_uid):
        r_uid = json['RegisteredUser']
        dao = BlocksDAO()
        bid = dao.unblockUser(r_uid, b_uid)
        result = self.build_block_attr_dict(bid)
        return jsonify(result), 201