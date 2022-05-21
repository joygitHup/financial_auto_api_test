# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/13 18:11
@Auth ： 你赖大爷
@File ：data_config.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

host='http://financial.xt-qa.com'


#===================================== 调整质押率==========================================
#case01 接口正常访问
borrow_append_borrowId_path_data=4
borrow_append_borrowId_url='/api/financial-loan-app/borrow/append/{0}'.format(borrow_append_borrowId_path_data)
borrow_append_borrowId_data="{'appendAmount':3}"
# case02 borrowId输入不符合规则的数据-小数0.8
borrow_append_borrowId_path_data02=0.8
borrow_append_borrowId_url02='/api/financial-loan-app/borrow/append/{0}'.format(borrow_append_borrowId_path_data02)
# borrow_append_borrowId_data02="{'appendAmount':3}"

# case03 borrowId输入不符合规则的数据-负小数-0.8
borrow_append_borrowId_path_data03=0.8
borrow_append_borrowId_url03='/api/financial-loan-app/borrow/append/{0}'.format(borrow_append_borrowId_path_data03)

# case04 borrowId输入不符合规则的数据-负整数-8
borrow_append_borrowId_path_data04=-8
borrow_append_borrowId_url04='/api/financial-loan-app/borrow/append/{0}'.format(borrow_append_borrowId_path_data04)

# case05 borrowId输入不符合规则的数据-字符串"test"
borrow_append_borrowId_path_data05='test'
borrow_append_borrowId_url05='/api/financial-loan-app/borrow/append/{0}'.format(borrow_append_borrowId_path_data05)

# case06 borrowId输入不符合规则的数据-超长正整数12231232 超过int64
borrow_append_borrowId_path_data06='test'
borrow_append_borrowId_url06='/api/financial-loan-app/borrow/append/{0}'.format(borrow_append_borrowId_path_data06)

# case07 borrowId不传入该属性值
borrow_append_borrowId_path_data07=""
borrow_append_borrowId_url07='/api/financial-loan-app/borrow/append/{0}'.format(borrow_append_borrowId_path_data07)

# case08 borrowId通过SQL语句查询
borrow_append_borrowId_path_data08="select * from borrow where borrowId=1"
borrow_append_borrowId_url08='/api/financial-loan-app/borrow/append/{0}'.format(borrow_append_borrowId_path_data08)

# case09 appendAmount不传入
borrow_append_borrowId_data09="{'appendAmount':}"

# case010 appendAmount输入不符合规则的数据-超长字符123123123 超过int64
borrow_append_borrowId_data010="{'appendAmount':21323123123}"
# case011 appendAmount输入不符合规则的数据-字符串”test“
borrow_append_borrowId_data011="{'appendAmount':’test‘}"

# case012 appendAmount输入不符合规则的数据-小数0.8
borrow_append_borrowId_data012="{'appendAmount':0.8}"
# case013 appendAmount输入不符合规则的数据-负小数-0.8
borrow_append_borrowId_data013="{'appendAmount':-0.8}"

# case014 appendAmount输入不符合规则的数据-负整数8
borrow_append_borrowId_data014="{'appendAmount':-8}"
# case015 appendAmount and borrowId输入错误的属性值appendAmount=test borrowId=test
borrow_append_borrowId_path_data015="test"
borrow_append_borrowId_url015='/api/financial-loan-app/borrow/append/{0}'.format(borrow_append_borrowId_path_data015)
borrow_append_borrowId_data015="{'appendAmount':’test‘}"



# ========================================自动调整质押率===============================
# case01 正常访问接口
auto_adjust_path_data=2
auto_adjust_url='/api/financial-loan-app/borrow/auto-adjust/{0}'.format(auto_adjust_path_data)
auto_adjust_data='{"isAutoAdjust":"true"}'
# case02 isAutoAdjust 设置为false
auto_adjust_data02='{"isAutoAdjust":"false"}'
# case03 isAutoAdjust  设置为T
auto_adjust_data03='{"isAutoAdjust":"T"}'
# case04 isAutoAdjust  设置为F
auto_adjust_data04='{"isAutoAdjust":"F"}'
# case05 isAutoAdjust  设置为12223
auto_adjust_data05='{"isAutoAdjust":"12223"}'
# case06 isAutoAdjust  空参
auto_adjust_data06='{"isAutoAdjust":""}'
# case07  isAutoAdjust  borrowID空参
auto_adjust_path_data=''
auto_adjust_url07='/api/financial-loan-app/borrow/auto-adjust/{0}'.format(auto_adjust_path_data)
auto_adjust_data07='{"isAutoAdjust":""}'


# 借币记录app
borrow_list_url='/api/financial-loan-app/borrow/borrow-list'

# 可借款列表
borrow_coin_list_url="/api/financial-loan-app/borrow/coin-list"

# 配置详情  {configId}
config_details_path_data=76
config_details_url="/api/financial-loan-app/borrow/config/{0}".format(config_details_path_data)

# 当前借币列表
borrow_current_list_url="/api/financial-loan-app/borrow/current-list"

#填补穿仓金额 {borrowId}
borrow_fill_borrowId_Path_data=4
borrow_fill_borrowId_url="/api/financial-loan-app/borrow/fill/{0}".format(borrow_fill_borrowId_Path_data)

# 强平信息 {borrowId} --get
borrowId=4
borrow_force_info_url="/api/financial-loan-app/borrow/force-info/{0}".format(borrowId)


# =================================================历史借币列表web
borrow_history_list_url='/api/financial-loan-app/borrow/history-list'
borrow_history_list_data="{'coinType':'','day':'',‘page’:'','size':'','status':''}"





# ================================================发 起借款  post
# case01 正常访问接口
borrow_order_add_url="/api/financial-loan-app/borrow/order-add"
borrow_order_add_data='{"amount": "1","configId": "1","day": "1","dayInterestRate": "1","isAutoAdjust": true,"pledgeAmount": "1","pledgeCoinType": "1"}'

#case02 不传入任何值
borrow_order_add_data02='{"amount": "","configId": "","day": "","dayInterestRate": "","isAutoAdjust": ,"pledgeAmount": "","pledgeCoinType": ""}'
# {
#   "amount": number
# 	"configId": integer(int64),
# 	"day": integer(int32),
# 	"dayInterestRate":number,
# 	"isAutoAdjust": boolean,
# 	"pledgeAmount": number,
# 	"pledgeCoinType": string
# }
# Number(p , s) p(precision)为精度 s(scale)表示小数点右边的数字个数
# s的情况：
# s > 0 :精确到小数点右边s位，并四舍五入。然后检查有效位是否 <= p.
# s > 0 :精确到小数点左边s位，并四舍五入。然后检查有效位是否 <= p+|s|.
# s = 0:此时number表示整数。
# case03 amount数量为整数
borrow_order_add_data03='{"amount": "1","configId": "1","day": "1","dayInterestRate": "1","isAutoAdjust": true,"pledgeAmount": "1","pledgeCoinType": "1"}'
# case04 amount数量为小数0.232
borrow_order_add_data04='{"amount": "0.232","configId": "1","day": "1","dayInterestRate": "1","isAutoAdjust": true,"pledgeAmount": "1","pledgeCoinType": "1"}'

# case05 amount数量为负小数-0.232
borrow_order_add_data05='{"amount": "-0.232","configId": "1","day": "1","dayInterestRate": "1","isAutoAdjust": true,"pledgeAmount": "1","pledgeCoinType": "1"}'

# case06 amount数量为字符串”test“
borrow_order_add_data06='{"amount": "test","configId": "1","day": "1","dayInterestRate": "1","isAutoAdjust": true,"pledgeAmount": "1","pledgeCoinType": "1"}'

# case07 amount数量为空
borrow_order_add_data07='{"amount": "","configId": "1","day": "1","dayInterestRate": "1","isAutoAdjust": true,"pledgeAmount": "1","pledgeCoinType": "1"}'


# 质押率信息 {borrowId} get
borrow_ledge_info_path_data=4
borrow_ledge_info_url="/api/financial-loan-app/borrow/pledge-info/{0}".format(borrow_ledge_info_path_data)

# 借贷记录列表 {borrowId} get
borrow_record_path_data=4
borrow_record_url="/api/financial-loan-app/borrow/record/{0}".format(borrow_record_path_data)

#还款信息
borrow_repay_path_data=3
borrow_repay_info_url="/api/financial-loan-app/borrow/repay-info/{0}".format(borrow_repay_path_data)

# 还款
borrow_repay_url_data=4
borrow_repay_url="/api/financial-loan-app/borrow/repay/{0}".format(borrow_repay_url_data)
borrow_repay_data={'isUsePledge':"true"}

# 测试接口-获取实时质押
borrow_rate_path_data=2
borrow_rate_url="/api/financial-loan-app/borrow/borrow-rate/{0}".format(borrow_rate_path_data)

# ----------------------------------------------------------------investapi---------------------------------------------
# c2c收益列表
c2c_interest_list_path_data=3
c2c_interest_list_url='/api/financial-loan-app/c2c/interest-list/{0}'.format(c2c_interest_list_path_data)

# c2c产品列表
c2c_list_url="/api/financial-loan-app/c2c/list"

#=====================================================c2c下单
#case1 正常访问 c2c下单
c2c_order_add_url="/api/financial-loan-app/c2c/order-add"
c2c_order_add_data='{"borrowId":"3","buyAmount":"2343","rankId":"2"}'
# "borrowId":"3","buyAmount":"2343","rankId":"2" 数据类型都为number
# case02 buyAmount数量为整数
c2c_order_add_data02='{"borrowId":"3","buyAmount":"2343","rankId":"2"}'
# case03 buyAmount数量为小数0.232
c2c_order_add_data03='{"borrowId":"3","buyAmount":"0.232","rankId":"2"}'

# case04 buyAmount数量为负小数-0.232
c2c_order_add_data04='{"borrowId":"3","buyAmount":"-0.232","rankId":"2"}'

# case05 buyAmount数量为字符串”test“
c2c_order_add_data05='{"borrowId":"3","buyAmount":"test","rankId":"2"}'

# case06 buyAmount数量为空
c2c_order_add_data06='{"borrowId":"3","buyAmount":"","rankId":"2"}'

# case07 buyAmount数量超大”214312421412414124“
c2c_order_add_data07='{"borrowId":"3","buyAmount":"214312421412414124","rankId":"2"}'
# case08 buyAmount数量为正小数
c2c_order_add_data08='{"borrowId":"3","buyAmount":"0.76567","rankId":"2"}'



# c2c订单列表
c2c_order_list_path_data=4
c2c_order_list_url="/api/financial-loan-app/c2c/order-list/{0}".format(c2c_order_list_path_data)

#c2c产品申购列表
c2c_purchase_list='/api/financial-loan-app/c2c/purchase-list'










# 开仓买入开多
# order_create_url='/dapi/trade/v1/order/create'
# order_create_data='{“symbol”:"btc_usdT","orderType": "LIMIT","price":"29485.67","timeInForce": "GTC","orderSide": "BUY","positionSide": "LONG","origQty": "12"}'


# header={"Accept":"application/json, text/plain, */*","Authorization":'Bearer eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxNTAxMTExIiwic2NvcGUiOiJhdXRoIiwiaXNzIjoieHQuY29tIiwibGFzdEF1dGhUaW1lIjoxNjUyMTY3NzkwODQ4LCJ1c2VyTmFtZSI6IjE1MDExMTEiLCJleHAiOjE2NTQ3NTk3OTAsImRldmljZSI6IndlYiIsInVzZXJJZCI6MTM1MzAxNjY3MjI1NiwidXNlckNvZGUiOiI0Yzg2MDQ3MTU1MTcxYjNkY2ZiNWQ5MDczOTFjZDczNCJ9.P7b3F-sIs0NJ9mkIu6DhroVUvLZourIvE028FuUCYiYnBTg6kmyos31AEpSneuPNGBNx2-e6cc89j8wwPjQapO9HiMeN0EsEzTgo4xCcDg-m3ddnuS2fTcII_7kh1n4Pz0r0nhhqSxgfF0kiA2-SDCly_O_-Q55gQo-uiNGBDgE',"Cookie":'currency=usd; _gid=GA1.2.18066500.1652148204; lang=cn; _ga=GA1.1.1661773890.1650521001; _ym_uid=1652167712410596843; _ym_d=1652167712; _ym_isad=2; _ym_visorc=w; token=eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxNTAxMTExIiwic2NvcGUiOiJhdXRoIiwiaXNzIjoieHQuY29tIiwibGFzdEF1dGhUaW1lIjoxNjUyMTY3NzkwODQ4LCJ1c2VyTmFtZSI6IjE1MDExMTEiLCJleHAiOjE2NTQ3NTk3OTAsImRldmljZSI6IndlYiIsInVzZXJJZCI6MTM1MzAxNjY3MjI1NiwidXNlckNvZGUiOiI0Yzg2MDQ3MTU1MTcxYjNkY2ZiNWQ5MDczOTFjZDczNCJ9.P7b3F-sIs0NJ9mkIu6DhroVUvLZourIvE028FuUCYiYnBTg6kmyos31AEpSneuPNGBNx2-e6cc89j8wwPjQapO9HiMeN0EsEzTgo4xCcDg-m3ddnuS2fTcII_7kh1n4Pz0r0nhhqSxgfF0kiA2-SDCly_O_-Q55gQo-uiNGBDgE; _ga_LTYEFTYFY8=GS1.1.1652167704.4.1.1652167791.0; _ga_MK8XKWK7DV=GS1.1.1652167704.18.1.1652167791.0; _ga_CY0DPVC3GS=GS1.1.1652167704.19.1.1652167791.0; JSESSIONID=91910785D3C189655F2E442DD7F54314',
# "lang":'cn',
# "User_Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
# }


# header={'Date': 'Wed, 18 May 2022 07:25:41 GMT', 'Content-Type': 'application/json', 'Content-Length': '64', 'Connection': 'keep-alive', 'Vary': 'Origin, Access-Control-Request-Method, Access-Control-Request-Headers'}


header={
'Accept':'application/json,text/plain, */*',
    "Accept-Language":"zh-CN,zh;q=0.9",
    "appId":"xt",
    "Connection":"keep-alive",
"Cookie":"_ym_d=1652666560;_ym_uid=1652666560863278736; currency=usd; lang=cn; _ga=GA1.1.2035199964.1652666559; _ym_isad=1; _ym_visorc=w; _ga_LTYEFTYFY8=GS1.1.1652863638.4.1.1652863702.0; _ga_MK8XKWK7DV=GS1.1.1652863639.4.1.1652863703.0; _ga_CY0DPVC3GS=GS1.1.1652863639.4.1.1652863714.0; token=eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxNTAxMTExIiwic2NvcGUiOiJhdXRoIiwiaXNzIjoieHQuY29tIiwibGFzdEF1dGhUaW1lIjoxNjUyODYzNzE4OTk5LCJzb3VyY2UiOiJ4dCIsInVzZXJOYW1lIjoiMTUwMTExMSIsImV4cCI6MTY1NTQ1NTcxOCwiZGV2aWNlIjoid2ViIiwidXNlcklkIjoxMzUzMDE2NjcyMjU2LCJ1c2VyQ29kZSI6IjRjODYwNDcxNTUxNzFiM2RjZmI1ZDkwNzM5MWNkNzM0In0.ZJGy2ZuPhhItujqRErXgp1T0NT72TrG0UtPadpGlDr4Y47kEgT5h6aqUPIAjOuOjv5Y7QX6EAXeUClXj0cC8Dp9jos4h9kcDmAD0C1xEdmb4ge-TsT1KxCdPCaXl24odirzWNII_8nqzizN3Tz2fHZrvLZXoN8-TM2_UtXaS7TU",
"Host": "financial.xt-qa.com",
"lang":"zh",
    "openId":"4c86047155171b3dcfb5d907391cd734",
"Referer": "http://financial.xt-qa.com/financing?appid=xt&source=pc&lang=zh&coinCode=USD&openid=4c86047155171b3dcfb5d907391cd734&token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb20uY29kZS5maW5hbmNpYWwuZG9tYWluLnJlcy5Ub2tlblJlcyI6IntcImFwcElkXCI6XCJ4dFwiLFwicmFuZG9tXCI6XCJkazc0MHFcIixcInNvdXJjZVwiOlwiUENcIixcInVzZXJJZFwiOjIwMjg2N30iLCJzdWIiOiJ0aGlzIGlzIGZyZWVseSB0b2tlbiIsImF1ZCI6IkFQUCIsImlzcyI6IkZSRUVMWSIsImV4cCI6MTY1MzQ2ODUxOSwiaWF0IjoxNjUyODYzNzE5fQ.7mISr87adN1E-16ZoPHIXSGT7_RLycN95uKzY4MpUx0&timestamp=1655542119442",
"source":"pc" ,
"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb20uY29kZS5maW5hbmNpYWwuZG9tYWluLnJlcy5Ub2tlblJlcyI6IntcImFwcElkXCI6XCJ4dFwiLFwicmFuZG9tXCI6XCJkazc0MHFcIixcInNvdXJjZVwiOlwiUENcIixcInVzZXJJZFwiOjIwMjg2N30iLCJzdWIiOiJ0aGlzIGlzIGZyZWVseSB0b2tlbiIsImF1ZCI6IkFQUCIsImlzcyI6IkZSRUVMWSIsImV4cCI6MTY1MzQ2ODUxOSwiaWF0IjoxNjUyODYzNzE5fQ.7mISr87adN1E-16ZoPHIXSGT7_RLycN95uKzY4MpUx0",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
'timeStamp':"1655542119442"
}