import asyncio
import telnetlib3

async def main():
    reader, writer = await telnetlib3.open_connection("192.168.31.12",23)
    try:
        writer.write("admin\n")
        writer.write("cisco123\n")
        await asyncio.sleep(0.5)

        writer.write("en\n")
        await asyncio.sleep(0.5)

        writer.write("cisco123\n")
        await asyncio.sleep(0.5)

        writer.write("conf t\n")
        await asyncio.sleep(0.5)

        writer.write("interface fastEthernet0/1 \n")
        await asyncio.sleep(0.5)

        writer.write("ip address 192.168.20.1 255.255.255.0 \n")
        await asyncio.sleep(0.5)

        writer.write("no shutdown \n")
        await asyncio.sleep(0.5)

        writer.write("end\n")
        await asyncio.sleep(0.5)

        writer.write("exit\n")
        await asyncio.sleep(0.5)

        output = await reader.read()
        if output:
            print(output)



    except asyncio.TimeoutError:
        print("Timeout waiting for device response")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        writer.close()
        await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())










enable secret cisco123
username admin password cisco123
line vty 0 4
login local
transport input telnet
exit
end
wr mem