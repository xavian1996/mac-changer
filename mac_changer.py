import optparse
import subprocess

#Function to show args for users
def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface",dest="interface", help="Interface Name To Change Its Mac Addr")
    parser.add_option("-m", "--mac",dest="mac_addr", help="NEW MAC ADDR")
    (options, arguments) =  parser.parse_args()

    if not options.interface:
        #code to handle error
        parser.error("[-] Please Select An Interface ! Use '--help for info'")
    elif not options.mac_addr:
        #code to handle error2
        parser.error("[-] Please Type Mac Addr ! Use '--help for info'")
    return options


#Function to change Mac Addr
def mac_changer(net,mac):
    #safer methode to use
    print("===============================================================")
    print('[+] Changing MAC adress To '+ mac +" and Interface To "+ net)
    print("===============================================================")
    print("=                         Please Wait ...                     =")
    print("===============================================================")
    subprocess.call(["sudo", "ifconfig", net, "down"]) # shutdown interface
    subprocess.call(["sudo", "ifconfig", net, "hw", "ether", mac]) # change interface mac addr
    subprocess.call(["sudo", "ifconfig", net, "up"]) # setup interface
    subprocess.call(["sudo", "ifconfig"]) # print ifconfig command
    print("===============================================================")
    print("=                    [-] MAC ADRESS CHANGED                   =")
    print("===============================================================")
    print("===============================================================")
    print("=               [-] Script Writed BY 'XxavianxX'              =")
    print("===============================================================")


options = get_args()
mac_changer(options.interface, options.mac_addr)
