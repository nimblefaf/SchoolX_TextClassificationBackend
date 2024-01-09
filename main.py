from flask import Flask
from flask import request
from flask import jsonify
import json
from socket import gethostname

from topics_classifier import prepare_prediction_response

ProductionPrints = True
ForceDebug = False

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def indx():
    if ProductionPrints: #принтим в консоли серва ip-адреса запросов если на проде
        print(request)
        print('Request from ' + str(request.remote_addr))
    if request.method == 'POST':
        if request.data:
            rcv_data = json.loads(request.data.decode(encoding='utf-8'))
            rsp = jsonify(prepare_prediction_response(rcv_data['text'])) #запаковываем ответ нейронки в JSON
            rsp.headers.add('Access-Control-Allow-Origin', '*')             #без этого через интеренет не отправляется, хз почему, не разобрался в тонкостях протокола  ¯\_(ツ)_/¯
            print(rsp)
            if rsp:
                return rsp  #отправляем ответ в виде JSON
            else:
                return '200'
        else:
            return '404'
        
if __name__ == "__main__":
    if (gethostname() == 'niisva-schoolx-6' and ForceDebug == False):                   #Запускаем сервер на waitress если на проде/сервере Спецвуза
        from waitress import serve
        serve(app, host='46.147.115.140', port=8080)
    else:
        app.run(host='localhost', port='43560', debug=True)     #если не Спецвуз, дебажим на локальной машине
