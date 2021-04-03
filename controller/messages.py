from flask import jsonify
from model.messages import MessagesDAO

class BaseMsg:   
    def build_map_dict(self, row):
        result = {}
        result['mid'] = row[0]
        result['uid'] = row[1]
        result['text'] = row[2]
        result['created_date'] = str(row[3])
        result['created_time'] = str(row[4])
        return result
    
    def build_map_dict2(self, row):
        result = {}
        result['mid'] = row[0]
        result['uid'] = row[1]
        result['text'] = row[2]
        result['created_date'] = str(row[3])
        result['created_time'] = str(row[4])
        return result
    
    def build_post_attr_dict(self, uid, text):
        result = {}
        result['uid'] = uid
        result['text'] = text
        return result
    
    def build_reply_attr_dict(self, uid, text, mid):
        result = {}
        result['uid'] = uid
        result['text'] = text
        result['mid'] = mid
        return result
    
    def build_share_attr_dict(self, uid, mid):
        result = {}
        result['uid'] = uid
        result['mid'] = mid
        return result

    def getAllMessages(self):
        dao = MessagesDAO()
        message_list = dao.getAllMessages()
        result_list = []
        for row in message_list:
            obj = self.build_map_dict(row)
            result_list.append(obj)
        return jsonify(result_list)

    def getMessageById(self, mid):
        dao = MessagesDAO()
        message_tuple = dao.getMessageById(mid)
        if not message_tuple:
            return jsonify("Not Found"), 404
        else:
            result = self.build_map_dict2(message_tuple)
            return jsonify(result), 200
    
    def postMessage(self, json):
        uid = json['uid']
        text = json['text']
        dao = MessagesDAO()
        mid = dao.postMessage(uid, text)
        result = self.build_post_attr_dict(uid, text)
        return jsonify(result), 201
    
    def replyMessage(self, json):
        uid = json['uid']
        text = json['text']
        mid = json['mid']
        dao = MessagesDAO()
        rid = dao.replyMessage(uid, text, mid)
        result = self.build_reply_attr_dict(uid, text, mid)
        return jsonify(result), 201
    
    def shareMessage(self, json):
        uid = json['uid']
        mid = json['mid']
        dao = MessagesDAO()
        sid = dao.shareMessage(uid, mid)
        result = self.build_share_attr_dict(uid, mid)
        return jsonify(result), 201
    
    