import asyncio

async def handle_connection(reader,writer):

    writer.write("Hello new user, type something ... \n".encode())

    "Read until a given byte string, expected, is encountered or until timeout seconds have passed."
    data = await reader.readuntil(b"\n")

    writer.write('You sent: '.encode() + data)

    # wait for data to be transmitted write put it in a buffer but if the data not used  by os the buffer will grow 
    # till we have memory issue. Drain wait for the data to be used by the os 
    await writer.drain()

    # close the socket/connection and clean-up

    writer.close()

    # wait for the socket to be closed
    await writer.wait_closed()

async def main():

    server = await asyncio.start_server(handle_connection,"0.0.0.0",8888)

    async with server :
        await server.serve_forever()
        
asyncio.run(main())