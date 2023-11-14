import asyncio
import json
import websockets

from path_solver import LinearPathSolver


async def solve_paths():
    async with websockets.connect('ws://localhost:8080') as websocket:
        print('Conectado ao servidor')
        running = True
        
        while running:
            try:
                data = json.loads(await websocket.recv())
                
                print('\nResolvendo caminho...')
                path_solver = LinearPathSolver(id=data['id'], path=data['path'])
                path_solver.start()
                path_solver.join()

                print('Caminho resolvido com sucesso!')
                await websocket.send(json.dumps(path_solver.to_dict()))
            except:
                running = False
                print('\nServidor desconectado')


if __name__ == '__main__':
    asyncio.run(solve_paths())
