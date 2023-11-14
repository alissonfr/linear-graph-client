import asyncio
import json
import websockets
from path_solver import PathSolver, LinearPathSolver

async def init_client():
    async with websockets.connect("ws://localhost:8080") as websocket:
        print("Conectado ao servidor")
        
        while True:
            data = json.loads(await websocket.recv())
            print("Resolvendo caminho...")
            path_solver = LinearPathSolver(id=data['id'], path=data['path'])
            path_solver.start()
            path_solver.join()
            print("Caminho resolvido com sucesso...")
            
            await websocket.send(json.dumps(path_solver.to_dict()))

asyncio.run(init_client())
