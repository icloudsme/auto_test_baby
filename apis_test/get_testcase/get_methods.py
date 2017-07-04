#coding:utf8
import inspect

"""
获取指定文件下需要执行的方法
"""

import datetime

class TestCase(object):

    def test01(self):
        """接口返回code:200，success节点为:true，msg节点为:success，初始化HOUSING_FUND_APPLY申请表"""
        #删除上一次申请表里的测试数据
        # sql="DELETE from HOUSING_FUND_APPLY where ORDER_ID ='%s'"% (
        #     self.data["applyId"])
        # self.db.execute(sql)
        self.response = self.api.sendrequest(data=self.data,headers={"Content-Type":"application/x-www-form-urlencoded","Access-Token":"%s" %getenv("token")},logger=self.logger)
        assert self.response.status_code == 200,"接口返回code:%s,期望值:200" %self.response.status_code
        lines = self.response.json()
        # print json.dumps(lines, indent=4, sort_keys=True,ensure_ascii=False)  # 树形打印json，ensure_ascii必须设为False否则中文会显示为unicode

    def test02(self):
        """更新HOUSING_FUND_APPLY记录及查询预授信数值是否与返回结果一致"""
        #调用预授信时间
        PRE_APPROVE_DATE=datetime.datetime.now()
        # 预授信过期时间
        PRE_APPROVE_END_DATE=(datetime.datetime.now() + datetime.timedelta(days = 5))
        sql = "select * from HOUSING_FUND_APPLY " \
              "where order_id='%s' " \
              "and name='任义祥' " \
              "and idcard='429001199004295656' " \
              "and apply_status='1'"\
              "and RISK_LEVEL='B1' " \
              "and PRE_LOAN_AMOUNT='23000' " \
              "and PRE_LOAN_TERM='36' " \
              "and INTEREST='1.0%' " \
              "and INTEREST_LOW='1.0%' " \
              "and INTEREST_UP='1.3%'" \
              "and PRODUCT_CODE='J2' " \
              "and PRODUCT_CID='32'" \
              "and PRE_APPROVE_DATE='PRE_APPROVE_DATE'" \
              "and PRE_APPROVE_END_DATE='PRE_APPROVE_END_DATE'"% (
                  self.data["applyId"])
        db_ids = self.db.execute(sql)
        # assertEquals(len(db_ids),1,"errorMsg")
        assert len(db_ids) == 1, "HOUSING_FUND_APPLY是否有请求记录到表(%s)，order_id:%s " % (
        len(db_ids), self.data["applyId"])
        self.db_id = db_ids[0]

        sql2 = "select apply_Id from HOUSING_FUND_APPLY where order_id='%s' " % (
            self.data["applyId"])
        db_ids = self.db.execute(sql2)

    def test03(self):
        """housing_fund_phone：公积金电话运营商信息表是否有请求记录"""
        sql = "select order_id from HOUSING_FUND_PHONE where order_id='%s' " % (
            self.data["applyId"])
        db_ids = self.db.execute(sql)
        # assertEquals(len(db_ids),1,"errorMsg")
        assert len(db_ids) > 1, "HOUSING_FUND_PHONE是否有请求记录到表(%s)，order_id:%s " % (len(db_ids), self.data["applyId"])
        self.db_id = db_ids[0]

    def test04(self):
        """HOUSING_FUND_PHONE_CALL：公积金通话详情表是否有请求记录"""
        sql = "select order_id from HOUSING_FUND_PHONE_CALL where order_id='%s' " % (
            self.data["applyId"])
        db_ids = self.db.execute(sql)
        # assertEquals(len(db_ids),1,"errorMsg")
        # len(db_ids)这个是数据库的纪录条数
        assert len(db_ids) > 1, "HOUSING_FUND_PHONE_CALL是否有请求记录到表(%s)，order_id:%s " % (
            len(db_ids), self.data["applyId"])
        self.db_id = db_ids[0]

    def test05(self):
        """HOUSING_FUND_INFO：公积金汇总信息是否有请求记录"""
        sql = "select order_id from HOUSING_FUND_INFO where order_id='%s' " % (
            self.data["applyId"])
        db_ids = self.db.execute(sql)
        # assertEquals(len(db_ids),1,"errorMsg")
        assert len(db_ids) > 1, "HOUSING_FUND_INFO是否有请求记录到表(%s)，order_id:%s " % (
            len(db_ids), self.data["applyId"])
        self.db_id = db_ids[0]

    def test06(self):
        """HOUSING_FUND_DETAIL：公积金明细表是否有请求记录"""
        sql = "select order_id from HOUSING_FUND_DETAIL where order_id='%s' " % (
            self.data["applyId"])
        db_ids = self.db.execute(sql)
        # assertEquals(len(db_ids),1,"errorMsg")
        assert len(db_ids) > 1, "HOUSING_FUND_DETAIL是否有请求记录到表(%s)，order_id:%s " % (
            len(db_ids), self.data["applyId"])
        self.db_id = db_ids[0]

        # 因51公积金端数据都是加密的，默认与51公积金APP客户端程序交互是正确的

    def test07(self):
        """预授信结果返回给51后，补充数据信息，使其可以推送到审批端"""
        self.data["applyId"] = getenv("db_ids")
        sql = "update HOUSING_FUND_APPLY " \
              "set APPLY_AMOUNT='20000.00',OCR_ID_NUM='429001199004295656',OCR_NAME='任义祥',OCR_BIRTH=TO_DATE('1993-08-29 00:00:00', 'YYYY-MM-DD HH24:MI:SS'),OCR_SEX='男',OCR_ADDRESS='武汉市武昌区中南二路7号',OCR_NATION＝'汉',OCR_ISSUED_BY='武汉市公安局武昌分局',OCR_DATE_START='2016.09.30',OCR_DATE_END='2036.09.30',BANK_NAME='招商银行',BANK_CODE＝'308',DEBIT_CARD_NO＝'6214831210211741',DEBIT_CARD_PHONE＝'17717392244',COMPANY='世贸大厦股份',EDUCATION＝'Bachelor' " \
              " where apply_id='%s'" % (self.data["applyId"])
        db_ids = self.db.execute(sql)
        # 更新用户身份证识别正反信息表
        sql2 = """INSERT INTO FACE_VERIFY_INFO VALUES (SYS_GUID(), 'Y', '{"face_genuineness":{"mask_confidence":0.0,"mask_threshold":0.5,"screen_replay_confidence":0.001,"screen_replay_threshold":0.5,"synthetic_face_confidence":0.0,"synthetic_face_threshold":0.5},"id_exceptions":{"id_attacked":0,"id_photo_monochrome":0},"request_id":"1478162188,d797e528-d740-45b5-b36c-841e4a26042d","result_faceid":{"confidence":87.742,"thresholds":{"1e-3":65.3,"1e-4":71.8,"1e-5":76.5,"1e-6":79.9}},"time_used":774}', '1e-3', '%s', 'SYSTEM', TO_DATE('2016-11-03 16:33:52', 'YYYY-MM-DD HH24:MI:SS'), null, null, 87.74)""" % (
        self.data["applyId"])
        db_ids = self.db.execute(sql2)
        # 向用户面部识别信息表插入数据
        sql4 = """INSERT INTO APPLY_IMAGES VALUES (SYS_GUID(), '%s', '14781619230062.jpg', '1', '/data/files/wangxiao/2016/11/3/N2016110301000009/14781619230062.jpg', 'Y', 'Y', 'SYSTEM', TO_DATE('2016-11-03 16:32:55', 'YYYY-MM-DD HH24:MI:SS'), null, null, '{"address":"广东省深圳市福田区黄槐道3号深福保科技工业园B栋5楼","birthday":{"day":"21","month":"9","year":"1986"},"gender":"男","head_rect":{"lb":{"x":0.63262194,"y":0.7132867},"lt":{"x":0.63414633,"y":0.2004662},"rb":{"x":0.91920733,"y":0.71095574},"rt":{"x":0.91920733,"y":0.20512821}},"id_card_number":"220181198609215513","legality":{"Edited":0.0,"ID Photo":0.907,"Photocopy":0.001,"Screen":0.092,"Temporary ID Photo":0.0},"name":"焦通","race":"汉","request_id":"1478162130,2a497a79-ade9-4e8c-af35-886d110ad62d","side":"front","time_used":1285}', null)""" % (
        self.data["applyId"])
        db_ids = self.db.execute(sql4)
        sql5 = """INSERT INTO APPLY_IMAGES VALUES (SYS_GUID(), '%s', '14781619230062.jpg', '2', '/data/files/wangxiao/2016/11/3/N2016110301000009/14781619230062.jpg', 'Y', 'Y', 'SYSTEM', TO_DATE('2016-11-03 16:33:34', 'YYYY-MM-DD HH24:MI:SS'), null, null, null, '{"issued_by":"深圳市公安局福田分局","legality":{"Edited":0.0,"ID Photo":0.961,"Photocopy":0.0,"Screen":0.039,"Temporary ID Photo":0.0},"request_id":"1478162169,5a27a9b3-91b2-4269-8885-d333cc68c2cd","side":"back","time_used":1106,"valid_date":"2012.10.13-2032.10.13"}')""" % (
        self.data["applyId"])
        db_ids = self.db.execute(sql5)
        sql6 = """INSERT INTO APPLY_IMAGES VALUES (SYS_GUID(), '%s', '14781619230062.jpg', '4', '/data/files/wangxiao/2016/11/3/N2016110301000009/14781619230062.jpg', 'Y', 'Y', 'SYSTEM', TO_DATE('2016-11-03 16:33:51', 'YYYY-MM-DD HH24:MI:SS'), 'SYSTEM', TO_DATE('2016-11-03 16:33:52', 'YYYY-MM-DD HH24:MI:SS'), null, null)""" % (
        self.data["applyId"])
        db_ids = self.db.execute(sql6)
        sql7 = """INSERT INTO APPLY_IMAGES VALUES (SYS_GUID(), '%s', '14781619230062.jpg', '5', '/data/files/wangxiao/2016/11/3/N2016110301000009/14781619230062.jpg', 'Y', 'Y', 'SYSTEM', TO_DATE('2016-11-03 16:33:51', 'YYYY-MM-DD HH24:MI:SS'), 'SYSTEM', TO_DATE('2016-11-03 16:33:52', 'YYYY-MM-DD HH24:MI:SS'), null, null)""" % (
        self.data["applyId"])
        db_ids = self.db.execute(sql7)
        sql8 = """INSERT INTO APPLY_IMAGES VALUES (SYS_GUID(), '%s', '14781619230062.jpg', '6', '/data/files/wangxiao/2016/11/3/N2016110301000009/14781619230062.jpg', 'Y', 'Y', 'SYSTEM', TO_DATE('2016-11-03 16:33:51', 'YYYY-MM-DD HH24:MI:SS'), 'SYSTEM', TO_DATE('2016-11-03 16:33:52', 'YYYY-MM-DD HH24:MI:SS'), null, null)""" % (
        self.data["applyId"])
        db_ids = self.db.execute(sql8)
        sql9 = """INSERT INTO APPLY_IMAGES VALUES (SYS_GUID(), '%s', '14781619230062.jpg', '7', '/data/files/wangxiao/2016/11/3/N2016110301000009/14781619230062.jpg', 'Y', 'Y', 'SYSTEM', TO_DATE('2016-11-03 16:33:51', 'YYYY-MM-DD HH24:MI:SS'), 'SYSTEM', TO_DATE('2016-11-03 16:33:52', 'YYYY-MM-DD HH24:MI:SS'), null, null)""" % (
        self.data["applyId"])
        db_ids = self.db.execute(sql9)
        sql10 = """INSERT INTO APPLY_IMAGES  VALUES (SYS_GUID(), '%s', '14781619230062.jpg', '8', '/data/files/wangxiao/2016/11/3/N2016110301000009/14781619230062.jpg', 'Y', 'Y', 'SYSTEM', TO_DATE('2016-11-03 16:33:51', 'YYYY-MM-DD HH24:MI:SS'), 'SYSTEM', TO_DATE('2016-11-03 16:33:52', 'YYYY-MM-DD HH24:MI:SS'), null, null)""" % (
        self.data["applyId"])
        db_ids = self.db.execute(sql10)

cls = inspect.getmembers(TestCase,inspect.ismethod)
print cls