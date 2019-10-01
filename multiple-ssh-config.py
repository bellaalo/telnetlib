import telnetlib

host_list = ['10.10.10.1','10.10.10.2','10.10.10.3']
user = "dharmo"
password = "dharmo"
for host in host_list:
 tn = telnetlib.Telnet(host)

 tn.read_until("Username: ")
 tn.write(user + "\n")

 tn.read_until("Password: ")
 tn.write(password + "\n")

 tn.write("conf t\n")
 for x in range (1,4):
  tn.write("ip domain-name mydomain{}.local\n".format(x))
  tn.write("crypto key generate rsa modulus 1024\n")
  tn.write("line vty 0 4\n")
  tn.write("login local\n")
 tn.write("end\n")
 tn.write("exit\n")

 print tn.read_all()
