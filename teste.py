from base64 import b64encode, b64decode
from datetime import datetime
import ast



strnow = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
now = datetime.now()
#strnow = strftime(now)


print(type(now))
print(now)
print(type(strnow))
print(strnow)
print('-----------------------------------------------')
strnow = str.encode(str(strnow))
print(strnow)

pheripheralId = b64encode(strnow).decode("utf-8") print(pheripheralId)



def teste1():
	s = {"email": "user.email","passwd": "user.passwd"}
	print('1')
	print(type(s))
	print(s)

	s = str.encode(str(s))
	print('2')
	print(s)

	data = b64encode(s).decode("utf-8")
	print('3')
	print(data)


	data = b64encode(s)
	print('4')
	print(data)


	uid = b64encode(data).decode("utf-8")
	print('5')
	print(uid)


	user = b64decode(uid).decode("utf-8")
	print('6')
	print(user)


	user = b64decode(user)
	print('7')
	print(user)


	print('8')
	#b64encode(user).decode("utf-8")
	print(type(user))
	user = ast.literal_eval(user.decode('utf-8'))
	print(type(user))
	print(user)








#b64_color = pickle.dumps().encode('base64', 'strict')
#s = pickle.loads(b64_color.decode('base64', 'strict'))
#print()
#print('data: ' + data)


#decoded_color = b64decode(data)
#print(decoded_color)




#data = str.encode(str(s))
#print(data)
#print(data)



#encoded_color = str(s).encode('base64','strict')
#print(encoded_color)


#data =  str.encode(s)
#e = b64encode(s).decode("utf-8")
#print(e) #-> b'Z3VydQ=='




#data = str.encode(user.email)
#s = b64encode(data).decode("utf-8")
#print('encode: ' + s)