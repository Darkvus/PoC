from aiohttp import web
import socket
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('localhost', 27017)
db = client['database']
collection = db['col_last']
cont = 0


async def handle_view(request):
    output = socket.getfqdn()
    _dict = sum_cont_dict(output)
    result = await collection.insert_one(_dict)
    data = {}
    async for doc in collection.find({}):
        data.update({output: doc[output]})
    return web.json_response({"Respuesta de:": output,
                              "collection": data
    })

app = web.Application()
app.add_routes([web.get('/', handle_view)])


async def do_insert(dict_col):
    await collection.insert_one(dict_col)
    

def sum_cont_dict(output):
    global cont
    cont +=1
    return {output: cont}

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8000)

