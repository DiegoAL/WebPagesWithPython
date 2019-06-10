import requests
#import base64, os

if __name__ == '__main__':  
    
    #endpoint = 'https://d3o4o39z4evicu.cloudfront.net'
    
    endpoint = 'https://dh7xq6695shwu.cloudfront.net'
    
    #Chama funçãoo de login (ZURAM_FM185_PC_USER_LOGINV2)
    parameters_login = {"I_CANAL": 'CHAT', 
                 "I_CPF": '86008048849', 
                 #"I_CNPJ": '09277570000106',
                  "I_ANLAGE": '27804011',
                  #"I_ANLAGE": '2121589',
                  "I_COD_SERV": 'TC',
                  "I_LISTA_INST": 'X'}
      
    resp = requests.post(endpoint + '/api/sap/getloginv2',  
                         json=parameters_login)
    data_login = resp.json()
    header = resp.headers
    print ("Retorno da função de login")
    for key, value in data_login.items():
        print ( key, ' - ',value) 
        if (key == 'ET_INST'):
            for v in value:
                print (v)
    print ("---------") 


    ######Chamada da 199
    
    header_auth =  {"Authorization": header['Authorization']}
    parameters_199 = {"I_CANAL": 'CHAT', 
                      "I_COD_SERV": 'TC',
                      #"I_VKONT": '100005867203',
                      #"I_PARTNER": '11487259',
                      #"I_VERTRAG": '5117087',
                      #"I_ANLAGE": '27804011',
                      "I_TIPO_CONSULTA": '2',
                      "I_BLOCO_DADOS": 'WRK1',
                      "I_SSO_GUID": ''}
     
    resp = requests.post(endpoint + '/api/sap/workspacedata',  
                         json=parameters_199, headers=header_auth)    
    print(resp.status_code)
    data_199 = resp.json()
    header = resp.headers
    print('')
    print('')
    print ("Retorno da função 199")
   
    for key, value in data_199.items():
        print ( key, ' - ',value) 
