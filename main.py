import paramiko
import time
import pandas as pd

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="<ip mgmt>",username="<username>",password="<password>")
conn = ssh.invoke_shell()

rishad = "ganteng"

output2 = 0; output3 =[]; netself_data=[]; ipnetself =[]; output2arr =[]; output_perbariskecil = []; output4 = ""; output5 = ""; vlan_data = []; netself_data_nama =[]; netroute_data=[]; netroute_data_judul =[]
vlan_data_judul = []; netself_data_judul = []; pool_no = []; pool_status = []; pool_name = []; pool_port = []; pool_weight = []; pool_Minimumactivemember = []; pool_heathcheck = []; pool_loadbalancing = []; farr = []; farr2= []; output6 = []
pooldf =[]; irule = []; output5 = ""; profiles = []; countbiasa=0; countprofile=0; mac_address = []


def paramiko_process(jeda):
    time.sleep(jeda)
    output = conn.recv(1000000000000000000000000000000000000000000)
    output2 = output.decode("ascii")

def sendcommand(command,jeda):
    conn.send(command)
    paramiko_process(jeda)
    return (output2)

def mac():

    conn.send("show sys mac-address | grep -i mac-true \n")
    time.sleep(10)
    output = conn.recv(1000000000000000000000000000000000000000000)
    output2 = output.decode("ascii")
    while "Display all" in output2:
        conn.send("y \n")
        time.sleep(10)
        output = conn.recv(1000000000000000000000000000000000000000000)
        output2 = output.decode("ascii")
        continue
    output2 = clear_data(output2)
    output2 =output2[5:]
    output3 = output2.split("\n")
    return (output3)

def clear_data(output2):
    if "Display all" in output2:
        conn.send("y \n")
        paramiko_process(0.3)
        output4 = output2
        while ("(less" in output2):
            conn.send(" " + "\n")
            paramiko_process(0.3)
            output4 = output4 + output2
            output4 = output2
            while ("(less" in output2):
                conn.send(" " + "\n")
                paramiko_process(0.3)
                output4 = output4 + output2
                output4 = output4[:1] + output4[3:]
                while "\r\n\x1b[7m" and "---\x1b[m\x1b[K\r\x1b[K" in output4:
                    less_awal = output4.find("\r\n\x1b[7m")
                    less_akhir = output4.find("---\x1b[m\x1b[K\r\x1b[K") + 13
                    output4 = output4[:less_awal+2] + output4[less_akhir:]
                    continue
                while "\r\n\x1b[?1h\x1b=\rnet" in output4:
                    less_3 = output4.find("\r\n\x1b[?1h\x1b=\rnet")
                    output4 = output4[:less_3+2] + output4[less_3 + 15:]
                    continue
                while "\r\n\x1b[7m(END)\x1b[m\x1b[K\r\x1b[K\x07\r\x1b[K\x1b[7m(END)\x1b[m\x1b[K" in output4:
                    end = output4.find("\r\n\x1b[7m(END)\x1b[m\x1b[K\r\x1b[K\x07\r\x1b[K\x1b[7m(END)\x1b[m\x1b[K")
                    output4 = output4[:end+2] + output4[end + 30:]
                continue
            if "(END)" in output4:
                conn.send("q \n")
                paramiko_process(0.3)

            continue
        if "(END)" in output4:
            conn.send("q \n")
            paramiko_process(0.3)
            output2 = output4

    elif "(less" in output2:
        output4 = output2
        while ("(less" in output2):
            conn.send(" " + "\n")
            time.sleep(0.2)
            output = conn.recv(1000000000000000000000000000000000000000000)
            output2 = output.decode("ascii")
            output4 = output4 + output2
            output4 = output4[:1] + output4[3:]
            while "\r\n\x1b[7m" and "---\x1b[m\x1b[K\r\x1b[K" in output4:
                less_awal = output4.find("\r\n\x1b[7m")
                less_akhir = output4.find("---\x1b[m\x1b[K\r\x1b[K") + 13
                output4 = output4[:less_awal+2] + output4[less_akhir:]
                continue
            while "\r\n\x1b[?1h\x1b=\rnet" in output4:
                less_3 = output4.find("\r\n\x1b[?1h\x1b=\rnet")
                output4 = output4[:less_3+2] + output4[less_3 + 15:]
                continue
            while "\r\n\x1b[7m(END)\x1b[m\x1b[K\r\x1b[K\x07\r\x1b[K\x1b[7m(END)\x1b[m\x1b[K" in output4:
                end = output4.find("\r\n\x1b[7m(END)\x1b[m\x1b[K\r\x1b[K\x07\r\x1b[K\x1b[7m(END)\x1b[m\x1b[K")
                output4 = output4[:end+2] + output4[end+30:]
            continue
        if "(END)" in output4:
            conn.send("q \n")
            paramiko_process(0.3)
            output2 = output4

    return (output2)

def netself():
    # print ("output2arr = " + str(output2arr) + ", output3 = " str(output3) + ",output2 = " + str(output2))

    output2 = sendcommand("list net self | grep -i net \n",1)
    output2 = clear_data(output2)
    output2arr = output2.split("\n")
    for l in range(len(output2arr)):
        if "[7m---(less" in output2arr[l]:
            output2arr[l] = output2arr[l][30:]
    for i in range(len(output2arr)):
        if "{" in output2arr[i]:
            output3.append("list " + output2arr[i][output2arr[i].find("net"):-3])

    for j in range(len(output3)):
        conn.send(output3[j]+"\n")
        time.sleep(0.3)
        output = conn.recv(10000000000000000000000000000000000000)
        output2 = output.decode("ascii")
        output2 = clear_data(output2)
        netself_data.append(output3[j][14:])
        netself_data_judul.append("Name")
        netself_data.append(output2[(output2.find("address")+8):(output2.find("/")+3)])
        netself_data_judul.append("IP address")
        netself_data.append(output2[(output2.find("vlan")+5):][:output2[(output2.find("vlan")+5):].find("}")-2]) #untuk masukin nama vlan
        netself_data_judul.append("VLAN")
        if "allow-service" in output2:
            a = output2[(output2.find("allow") +25):(output2.find("traffic-group") -13)]
            if "tcp:53" and "udp:53" and "swipe:0" in a:
                a = "tcp:53, udp:53, swipe:0"
            elif "default" in a:
                a = "default"
            netself_data.append(a)
            netself_data_judul.append("Port Lockdown (Allow)")
        else:
            netself_data.append("none")
            netself_data_judul.append("Port Lockdown (Allow)")
        # output2[(output2.find("traffic-group")+14):(output2.find("vlan")-2)]
        netself_data.append(output2[(output2.find("traffic-group")+14):(output2.find("vlan")-6)])
        print(output2[(output2.find("traffic-group")+14):(output2.find("vlan")-6)])
        netself_data_judul.append("Traffic Group")
    print(netself_data)

    netselfdf = list(zip(netself_data_judul, netself_data))
    dframe_netself = pd.DataFrame(netselfdf)
    dframe_netself.to_csv("netself.csv", index=False)
    output2arr.clear(); output3.clear(); output2=None
    print("output2arr = " + str(output2))

def vlan():
    mac_address = mac()
    conn.send("list net vlan | grep -i net \n")
    time.sleep(0.5)
    output = conn.recv(1000000000000000000000000000000000000000000)
    output2 = output.decode("ascii")
    output2 = clear_data(output2)
    output2arr = output2.split("\n")
    print(output2arr)
    for i in range(len(output2arr)):
        if "{" in output2arr[i]:
            print ("step1")
            output3.append("list " + output2arr[i][output2arr[i].find("net"):-3])
    # print(output3)
    for j in range(len(output3)):
        conn.send(output3[j] + " all-properties " + "\n")
        time.sleep(0.3)
        output = conn.recv(10000000000000000000000000000000000000)
        output2 = output.decode("ascii")
        output2 = clear_data(output2)
        print(output2)
        output2 = output2[:(output2.find("(END)") - 8)]

        vlan_data.append(output3[j][14:])
        print("step3")
        vlan_data_judul.append("Name")
        print(vlan_data)

        vlan_data.append(output2[-3:])
        vlan_data_judul.append("Tag")

        for t in range(len(mac_address)):
            if (" "+output3[j][14:]+" ") in mac_address[t]:
                vlan_data.append(mac_address[t][:(mac_address[t].find("net vlan")-2)])
                print(mac_address[t][:(mac_address[t].find("net vlan")-2)])
        vlan_data_judul.append("mac-address")
        vlan_data.append(output2[(output2.find("cmp-hash") + 9): (output2.find("cmp-hash") + 16)])
        vlan_data_judul.append("cmp-hash")
        d = output2[output2.find("interfaces") + 14:][8:output2[output2.find("interfaces") + 14:].find("}")]

        vlan_data.append(output2[output2.find("interfaces") + 14:][8:output2[output2.find("interfaces") + 14:].find("{") - 1])  # untuk nambah interfaces
        vlan_data_judul.append("interface")
        if "tagged" in d:
            vlan_data.append("tagged")
            vlan_data_judul.append("Tagging")
        elif "untagged" in d:
            vlan_data.append("untagged")
            vlan_data_judul.append("Tagging")
    vlandf = list(zip(vlan_data_judul, vlan_data))
    dframe_vlan = pd.DataFrame(vlandf)
    dframe_vlan.to_csv("vlan.csv")
    output2arr.clear(); output3.clear(); output2 = None;

def netroute():
    output2 = sendcommand('list net route | grep -i "net route" \n', 1)
    output2 = clear_data(output2)
    output2arr = output2.split("\n")

    for i in range(len(output2arr)):
        if "{" in output2arr[i]:
            output3.append("list " + output2arr[i][output2arr[i].find("net"):-3])

    for j in range(len(output3)):
        conn.send(output3[j]+"\n")
        time.sleep(0.3)
        output = conn.recv(10000000000000000000000000000000000000)
        output2 = output.decode("ascii")
        output2 = clear_data(output2)
        netroute_data.append(output3[j][15:])
        netroute_data_judul.append("Name")

        if "gw " in output2:
            a = output2.find("gw ")+3
            d = output2[a:] #batas awa
            b = d.find("network ")-6
            c = d[:b]
            netroute_data.append(output2[output2.find("network ")+8:][:output2[output2.find("network ")+8:].find("}")-2])
            netroute_data_judul.append("Destination")
            netroute_data.append("gateway")
            netroute_data_judul.append("Resource")
            netroute_data.append(output2[output2.find("gw ")+3:][:output2[output2.find("gw ")+3:].find("network" )-6])
            netroute_data_judul.append("Gateway Address")
        else:
            netroute_data.append(output2[output2.find("network") + 8:][:output2[output2.find("network") + 8:].find("pool ") - 6])
            netroute_data_judul.append("Destination")
            netroute_data.append(output2[output2.find("pool "):output2.find("}")-2])
            netroute_data_judul.append("Resource")

    netroutedf = list(zip(netroute_data_judul,netroute_data))
    dframenetroute = pd.DataFrame(netroutedf)
    dframenetroute.to_csv("netroute.csv", index=False)
    output2arr.clear(); output3.clear(); output2 = None
    print("output2arr = " + str(output2))
def pool():
    output2 = sendcommand('list ltm pool | grep -i "ltm pool" \n', 1)
    output2 = clear_data(output2)
    output2arr = output2.split("\n")
    for l in range(len(output2arr)):
        if "[7m---(less" in output2arr[l]:
            output2arr[l] = output2arr[l][30:]


    for i in range(len(output2arr)):
        if "{" in output2arr[i]:
            output3.append("list " + output2arr[i][output2arr[i].find("ltm"):-3])

    for j in range(len(output3)):

        conn.send(output3[j]+" all-properties \n")
        time.sleep(0.2)
        output = conn.recv(10000000000000000000000000000000000000)
        output2 = output.decode("ascii")
        output2 = clear_data(output2)

        conn.send("show" + output3[j][4:] + " | grep -i availability \n")
        time.sleep(0.2)
        outputstat1 = conn.recv(10000000000000000000000000000000000000)
        outputstat = outputstat1.decode("ascii")
        print(outputstat)
        outputstat = clear_data(outputstat)

        if "available       " in outputstat:
            pool_status.append("online")
        else:
            pool_status.append("offline")

        pool_name.append(output3[j][14:])

        pool_port.append("")
        pool_weight.append("")
        pool_Minimumactivemember.append(output2[(output2.find("min-active-members")+19):(output2.find("min-up-members")-6)])
        a = output2[output2.find("min-active-members"):]
        b = a.find("monitor")+8
        c = a.find("partition")-6
        d = a[b:c]
        pool_heathcheck.append(d) #ngeprint healthcheck
        e = output2[(output2.find("load-balancing-mode")+20):(output2.find("members")-6)]
        pool_loadbalancing.append(e)
        pool_no.append(j+1)
        f = output2[(output2.find("members")+12):(output2.find("min-active-members")-32)]

        farr = f.split("\n")
        for i in range(len(farr)):
            if "{" in farr[i]:
                output6.append(farr[i])

                if "fqdn" not in farr[i]:
                    farr2.append(farr[i][7:-3])
            if "priority-group" in farr[i]:
                weight = farr[i][farr[i].find("priority"):]
                pool_weight.append(weight[15:])

            if "state" in farr[i]:
                output6.append(farr[i][farr[i].find("state")+6:-1])
                print(output6)

                if farr[i][farr[i].find("state")+6:-1] in "up":
                    pool_status.append("online")
                else:
                    pool_status.append("offline")


        for y in range(len(farr2)):
            pool_name.append(farr2[y])
            pool_port.append(farr2[y][(farr2[y].find(":")+1):])
            pool_Minimumactivemember.append("")
            pool_loadbalancing.append((""))
            pool_heathcheck.append("")
            pool_no.append("")

        farr2.clear();

    pooldf = list(zip(pool_no,pool_status,pool_name, pool_port, pool_weight, pool_Minimumactivemember, pool_heathcheck, pool_loadbalancing))
    dframe_pool = pd.DataFrame(pooldf)
    dframe_pool.to_csv("pool.csv")
    output2arr.clear(); output3.clear(); output6.clear(); output2 = None


if __name__ == '__main__':
    netself()
    netroute()
    pool()
    vlan()
