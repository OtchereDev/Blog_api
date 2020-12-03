import json

# try_json = '''{  
#   "event":"charge.success",
#   "data":{  
#     "id":302961,
#     "domain":"live",
#     "status":"success",
#     "reference":"qTPrJoy9Bx",
#     "amount":10000,
#     "message":null,
#     "gateway_response":"Approved by Financial Institution",
#     "paid_at":"2016-09-30T21:10:19.000Z",
#     "created_at":"2016-09-30T21:09:56.000Z",
#     "channel":"card",
#     "currency":"NGN",
#     "ip_address":"41.242.49.37",
#     "metadata":0,
#     "fees":null,
#     "customer": {
#       "id": 902735,
#       "first_name": null,
#       "last_name": null,
#       "email": "customer@email.com",
#       "customer_code": "CUS_1psu1flkeh1dzm8",
#       "phone": null,
#       "metadata": null,
#       "risk_action": "default"
#     },
#     "plan": "PLN_tq8ur7pqz80fbpi",
#     "paidAt": "2018-06-10T18:00:25.000Z",
#     "createdAt": "2018-06-10T17:59:59.000Z",
#     "transaction_date": "2018-06-10T17:59:59.000Z",
#     "plan_object": {
#       "id": 6743,
#       "name": "Test Plans",
#       "plan_code": "PLN_tq8ur7pqz80fbpi",
#       "description": "This is to test listing plans, etc etc",
#       "amount": 200000,
#       "interval": "hourly",
#       "send_invoices": true,
#       "send_sms": true,
#       "currency": "NGN"
#     },
#     "subaccount": {}
#   }
# }'''

# print(json.loads(try_json))
import requests,os

# curl https://api.paystack.co/plan -H "Authorization: Bearer sk_test_674915312481ea6e87b541d50ca4ec77118942b6" -H "Content-Type: application/json" -d '{ name: "Monthly Retainer", interval: "monthly", amount: "500000"}' -X POST


# access_token='sk_test_674915312481ea6e87b541d50ca4ec77118942b6'
# url='https://api.paystack.co/plan'


# tyr=requests.post(url,headers={
#     "Content-Type":"application/json",
#     "Authorization":"Bearer sk_test_674915312481ea6e87b541d50ca4ec77118942b6",
# },json={
#     'name': "Free", 'interval': "monthly", 'amount': "0",
#     "currency":"GHS"
# })

# print(tyr.text)

# curl https://api.paystack.co/transaction/initialize
# -H "Authorization: Bearer YOUR_SECRET_KEY"
# -H "Content-Type: application/json"
# -d '{ email: "customer@email.com", amount: "500000", 
# 	 plan: "PLN_xxxxxxxxxx" }'
# -X POST

# url ='https://api.paystack.co/transaction/initialize'
# tyr=requests.post(url,headers={
#     "Content-Type":"application/json",
#     "Authorization":"Bearer sk_test_674915312481ea6e87b541d50ca4ec77118942b6",
# },json={
#     'email': "oliverotchere4@email.com", 'amount': "50000",
#     "currency":"GHS",'plan':"PLN_0nwj4801zoxex9o"
# })
# print(tyr)


def init_payment():
            url='https://api.paystack.co/transaction/initialize'
            header={
                'Authorization':'Bearer sk_test_674915312481ea6e87b541d50ca4ec77118942b6',
                'Conent-Type':'application/json',
            }
            datum ={
                'email':'oliverotchere4@gmail.comm',
                'amount':10*100,
                "currency":"GHS",
                # 'plan':"PLN_w8gjf3pv4xrng6e"
            }
            # data=json.dumps(datum)
            x = requests.post(url,headers=header,json=datum)
            print(str(x))
            if x.status_code !=200:
                return str(x.status_code)
            result = x.json()
            print(result['data']['reference'])
            return result

i=init_payment()
print(i,i.reason)


# curl https://api.paystack.co/plan
# -H "Authorization: Bearer YOUR_SECRET_KEY"
# -H "Content-Type: application/json"
# -d '{ name: "Monthly Retainer", interval: "monthly", amount: "500000"}'
# -X POST

# touch=requests.post(url='https://api.paystack.co/plan',headers={
#                 'Authorization':'Bearer sk_test_674915312481ea6e87b541d50ca4ec77118942b6',
#                 'Conent-Type':'application/json',
#             },json={ "name": "Monthly freebe", "interval": "monthly", "amount": "50000"})

# print(touch)