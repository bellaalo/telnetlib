import telnetlib

host = "10.10.10.1"
user = "dharmo"
password = "dharmo"

tn = telnetlib.Telnet(host)

tn.read_until("Username: ")
tn.write(user + "\n")

tn.read_until("Password: ")
tn.write(password + "\n")

tn.write("conf t\n")
tn.write("int lo0\n")
tn.write("ip address 1.1.1.1 255.255.255.255\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()
