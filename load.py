try: #py3
    import tkinter as tk
except: #py2
    import Tkinter as tk
import requests
import sys
import os
import time
from datetime import datetime
from l10n import Locale
import myNotebook as nb
from ttkHyperlinkLabel import HyperlinkLabel
import json
import textwrap
from queue import Queue
from threading import Thread
from monitor import monitor

if __debug__:
    from traceback import print_exc

_TIMEOUT = 20
_EDPSAPPVERSION = "1.3"

this = sys.modules[__name__]  # For holding module globals
#this.session = requests.Session()
this.queueEDPS = Queue()
this.label2 = None
this.label4 = None

try:
    from config import config
except ImportError:
    config = dict()

def updatePlugin(version):
    print('Beginning file download with requests')
    url = 'https://raw.githubusercontent.com/RocketMan1988/EDMC-Passport-System/' + version + '/load.py'
    r = requests.get(url)
    print(url)

    if r.ok:
        with open(__file__.replace('load.py', 'load_temp'), 'wb') as f:
            f.write(r.content)
        try:
            os.replace(__file__.replace('load.py', 'load_temp'), __file__)
        except OSError:
            os.remove(__file__)
            os.rename(__file__.replace('load.py', 'load_temp'), __file__)
        print('Update Complete...')
        this.label4["text"] = "Update Complete! Please Restart EDMC!"
    else:
        this.label4["text"] = "Update Failed"
        print('Update Failed...')

def plugin_start3(plugin_dir):
   """
   Load this plugin into EDMC
   """
   #Set Default FC List
   this.FCs = [{"number":1,"type":"FC","name":"DSSA Sleeper Service","system":"Oorb Broae DF-A e6","callsign_formatted":"TFF-34Z","callsign":"TFF34Z","patch_url":"https://imgur.com/RMUeVxe.png","location_x":2123.65625,"location_y":29718.625,"lat":2485.93125,"lng":2356.182813,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":2,"type":"FC","name":"DSSA Distant Worlds","system":"Beagle Point","callsign_formatted":"V2W-85Z","callsign":"V2W85Z","patch_url":"https://imgur.com/VrbEIrV.png","location_x":-1111.5625,"location_y":65269.75,"lat":4263.4875,"lng":2194.421875,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":4,"type":"FC","name":"NECFC Huginn","system":"Schee Flyi DN-I D10-8604","callsign_formatted":"Q9V-W3G","callsign":"Q9VW3G","patch_url":"https://imgur.com/AP5W7Yg.png","location_x":-4773.59375,"location_y":22859,"lat":2142.95,"lng":2011.320313,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":5,"type":"FC","name":"DSSA Gam Nine","system":"PLA AICK GA-A e1","callsign_formatted":"X9Z-4XG","callsign":"X9Z4XG","patch_url":"https://imgur.com/DEdHWUq.png","location_x":35413.159,"location_y":9181.96875,"lat":1459.098438,"lng":4020.65795,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":7,"type":"FC","name":"NECFC Muninn","system":"SCAULOU SZ-M D8-911","callsign_formatted":"J4F-01X","callsign":"J4F01X","patch_url":"https://imgur.com/Ei4ai2x.png","location_x":-6759.34375,"location_y":29166.1875,"lat":2458.309375,"lng":1912.032813,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":8,"type":"FC","name":"DSSA Ironside","system":"PLAA AEC RY-B B41-1","callsign_formatted":"QLZ-NQZ","callsign":"QLZNQZ","patch_url":"https://imgur.com/aleAP7f.png","location_x":7881.59375,"location_y":7500.6875,"lat":1375.034375,"lng":2644.079688,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":10,"type":"FC","name":"DSSA Black Adder Port","system":"Eembaitl DL-Y d13","callsign_formatted":"QHM-51Z","callsign":"QHM51Z","patch_url":"https://imgur.com/gQEPA3r.png","location_x":29456.5,"location_y":29782.0625,"lat":2489.103125,"lng":3722.825,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":11,"type":"FC","name":"DSSA Pride of Tel Fyr","system":"Aiphaisty OD-T e3-4","callsign_formatted":"K8N-LTJ","callsign":"K8NLTJ","patch_url":"https://imgur.com/U5eEZDK.png","location_x":-17932.5625,"location_y":34160.28125,"lat":2708.014063,"lng":1353.371875,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":12,"type":"FC","name":"DSSA Gene Roddenberry","system":"Loijoae ZV-T c17-0","callsign_formatted":"K1F-32K","callsign":"K1F32K","patch_url":"https://imgur.com/p4dTzxB.png","location_x":23595.90625,"location_y":32990.90625,"lat":2649.545313,"lng":3429.795313,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":14,"type":"FC","name":"[EDS] DSSA Enigma","system":"Hypuejaa RT-Q E5-83","callsign_formatted":"QBN-LKW","callsign":"QBNLKW","patch_url":"https://imgur.com/5BsWITB.png","location_x":-11653.59375,"location_y":28123.03125,"lat":2406.151563,"lng":1667.320313,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":15,"type":"FC","name":"DSSA Nest","system":"Uctailts UD-S d4-3","callsign_formatted":"KLL-1KJ","callsign":"KLL1KJ","patch_url":"https://imgur.com/Sd0b3hB.png","location_x":27648.65625,"location_y":42867.65625,"lat":3143.382813,"lng":3632.432813,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":16,"type":"FC","name":"[IGAU] Paradox Destiny","system":"Prai Hypoo TX-B d4","callsign_formatted":"K3K-L1N","callsign":"K3KL1N","patch_url":"https://imgur.com/OcvTxv2.png","location_x":-9214.875,"location_y":7908.21875,"lat":1395.410938,"lng":1789.25625,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":17,"type":"FC","name":"DSSA Dryman's Hope","system":"Eock Prau WD-T d3-1","callsign_formatted":"QHW-0XX","callsign":"QHW0XX","patch_url":"https://imgur.com/pnwSIxT.png","location_x":26230.03125,"location_y":19811,"lat":1990.55,"lng":3561.501563,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":21,"type":"FC","name":"DSSA Chrysaetos Refuge","system":"Xothae MA-A d2","callsign_formatted":"WNB-W5Z","callsign":"WNBW5Z","patch_url":"https://imgur.com/T4MSbzR.png","location_x":-36207.90625,"location_y":29671.40625,"lat":2483.570313,"lng":439.6046875,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":22,"type":"FC","name":"CCN Tranquility","system":"Phreia Flyou FG-V d3-116","callsign_formatted":"FZK-L9Z","callsign":"FZKL9Z","patch_url":"https://imgur.com/IHjTCjw.png","location_x":-14327,"location_y":23596.875,"lat":2179.84375,"lng":1533.65,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":23,"type":"FC","name":"DSSA Buurian Anchorage","system":"Dryau Ausms KG-Y E3390","callsign_formatted":"K5T-56Q","callsign":"K5T56Q","patch_url":"https://imgur.com/RvbkorE.png","location_x":-1523.75,"location_y":20976.59375,"lat":2048.829688,"lng":2173.8125,"patch_credit":"Rheeney","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":27,"type":"FC","name":"HSRC Limpet's Call","system":"Phroi Bluae QI-T e3-3454","callsign_formatted":"V0G-2VY","callsign":"V0G2VY","patch_url":"https://imgur.com/93kPjvk.png","location_x":-681.09375,"location_y":34219.34375,"lat":2710.967188,"lng":2215.945313,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":28,"type":"FC","name":"[IGAU] Deep Space 12","system":"Flyoo Prao JC-B d1-5","callsign_formatted":"K8Y-85J","callsign":"K8Y85J","patch_url":"https://imgur.com/RuehpqP.png","location_x":22469.8125,"location_y":40008.34375,"lat":3000.417188,"lng":3373.490625,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":29,"type":"FC","name":"[IGAU] Deep Space 27","system":"Eishoqs QM-J C10-1","callsign_formatted":"KNX-2KY","callsign":"KNX2KY","patch_url":"https://imgur.com/w4ZIQkn.png","location_x":-27067.9375,"location_y":17297.71875,"lat":1864.885938,"lng":896.603125,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":30,"type":"FC","name":"DSSA Reginleif","system":"Dryau Aec JF-A d11","callsign_formatted":"X5W-63Z","callsign":"X5W63Z","patch_url":"https://imgur.com/jy5HFF0.png","location_x":8552.28125,"location_y":-12582,"lat":370.9,"lng":2677.614063,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":31,"type":"FC","name":"DSSA Unicorns Rest","system":"MYOANGEIA AT-U D2-244","callsign_formatted":"X5G-6HZ","callsign":"X5G6HZ","patch_url":"https://imgur.com/oTBWZok.png","location_x":-12989.9375,"location_y":41429.0625,"lat":3071.453125,"lng":1600.503125,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":32,"type":"FC","name":"DSSA Eleanor","system":"CHO THUA NL-C B40-0","callsign_formatted":"QLQ-5QY","callsign":"QLQ5QY","patch_url":"https://imgur.com/pm7NLAp.png","location_x":-305.3125,"location_y":58686.4375,"lat":3934.321875,"lng":2234.734375,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":33,"type":"FC","name":"DSSA Ronin","system":"Phipoea WK-E d12-1374","callsign_formatted":"V1Q-95G","callsign":"V1Q95G","patch_url":"https://imgur.com/QSHElSe.png","location_x":-497.09375,"location_y":28184.875,"lat":2409.24375,"lng":2225.145313,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":37,"type":"FC","name":"[IGAU] The Lemon Drop","system":"Gleeque HW-N e6-149","callsign_formatted":"XFK-0TW","callsign":"XFK0TW","patch_url":"https://imgur.com/AFF1zgv.png","location_x":4995.59375,"location_y":25791.9375,"lat":2289.596875,"lng":2499.779688,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":38,"type":"FC","name":"KTL Frontier Sanctuary","system":"Syreadiae JX-F c0","callsign_formatted":"J2W-5XF","callsign":"J2W5XF","patch_url":"https://imgur.com/w6BIQ43.png","location_x":-9529.4375,"location_y":-7428.4375,"lat":628.578125,"lng":1773.528125,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":40,"type":"FC","name":"DSSA Argonautica","system":"FEDGIE FN-Q D6-45","callsign_formatted":"KBB-34Z","callsign":"KBB34Z","patch_url":"https://imgur.com/GmVIxWA.png","location_x":13322.6875,"location_y":-3035.71875,"lat":848.2140625,"lng":2916.134375,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":41,"type":"FC","name":"DSSA Tartarus","system":"Eishaw DB-W E2-0","callsign_formatted":"XBQ-LVV","callsign":"XBQLVV","patch_url":"https://imgur.com/jy5HFF0.png","location_x":4587.03125,"location_y":59589.09375,"lat":3979.454688,"lng":2479.351563,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":43,"type":"FC","name":"DSSA Andromeda Calling","system":"Byeia Thoea CA-A d2","callsign_formatted":"JFH-GXB","callsign":"JFHGXB","patch_url":"https://imgur.com/Ug3tSnQ.png","location_x":-33157.1875,"location_y":2846.8125,"lat":1142.340625,"lng":592.140625,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":44,"type":"FC","name":"DSSA Kraut","system":"NGC 3199 Sector XJ-A D10","callsign_formatted":"J4T-0QB","callsign":"J4T0QB","patch_url":"https://imgur.com/SAVikAI.png","location_x":14544.0625,"location_y":3489.375,"lat":1174.46875,"lng":2977.203125,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":46,"type":"FC","name":"DSSA Callisto","system":"Phraa Blao HO-S c20-7","callsign_formatted":"KBZ-B0Z","callsign":"KBZB0Z","patch_url":"https://imgur.com/Ut3KaIj.png","location_x":11261.21875,"location_y":34409.5625,"lat":2720.478125,"lng":2813.060938,"patch_credit":"Gnauty","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":47,"type":"FC","name":"DSSA Hecate's Grace","system":"EX CANCRI","callsign_formatted":"J8L-41H","callsign":"J8L41H","patch_url":"https://imgur.com/ntliWMd.png","location_x":1412.21875,"location_y":-1967.34375,"lat":901.6328125,"lng":2320.610938,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":48,"type":"FC","name":"DSSA Aristarchos","system":"Eocs Aihm XX-U d2-6","callsign_formatted":"J6M-G2L","callsign":"J6MG2L","patch_url":"https://imgur.com/t7hwChZ.png","location_x":22759.375,"location_y":-11033.40625,"lat":448.3296875,"lng":3387.96875,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":51,"type":"FC","name":"DSSA Sésame","system":"Floarps PI-B e2","callsign_formatted":"K3F-L0V","callsign":"K3FL0V","patch_url":"https://imgur.com/VEtayXu.png","location_x":-859.90625,"location_y":14426.34375,"lat":1721.317188,"lng":2207.004688,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":53,"type":"FC","name":"CLB Voqooway","system":"Voqooe BI-H D11-864","callsign_formatted":"J3G-3QZ","callsign":"J3G3QZ","patch_url":"https://imgur.com/lqBtGyo.png","location_x":-4770.75,"location_y":17819.75,"lat":1890.9875,"lng":2011.4625,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":57,"type":"FC","name":"HSRC Deep Thought","system":"ABAIRDY XR-I B26-0","callsign_formatted":"Q4L-5TY","callsign":"Q4L5TY","patch_url":"https://imgur.com/OyS2OVp.png","location_x":28187.75,"location_y":35378.5,"lat":2768.925,"lng":3659.3875,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":58,"type":"FC","name":"DSSA Bougainville","system":"Eock Bluae QL-X c1-1","callsign_formatted":"X8N-0KL","callsign":"X8N0KL","patch_url":"https://imgur.com/YeCRmhG.png","location_x":16025.21875,"location_y":27206.59375,"lat":2360.329688,"lng":3051.260938,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":61,"type":"FC","name":"DSSA[TFGI]Kitty Corner","system":"DROETT XD-T D3-22","callsign_formatted":"X3M-7HY","callsign":"X3M7HY","patch_url":"https://imgur.com/vg5bCcj.png","location_x":26305.84375,"location_y":15908.40625,"lat":1795.420313,"lng":3565.292188,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":62,"type":"FC","name":"DSSA - Stellar Oasis","system":"IHAB JI-B D13-16","callsign_formatted":"J8Y-8HT","callsign":"J8Y8HT","patch_url":"https://imgur.com/aMO7oK6.png","location_x":23399.1875,"location_y":46161.3125,"lat":3308.065625,"lng":3419.959375,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":65,"type":"FC","name":"DSSA King's Pass","system":"Nuekea RP-M D8-161","callsign_formatted":"FHH-7QZ","callsign":"FHH7QZ","patch_url":"https://imgur.com/tWteOjb.png","location_x":9475.5,"location_y":13771.21875,"lat":1688.560938,"lng":2723.775,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":66,"type":"FC","name":"Explorer's Bar & Grill","system":"Hypau Aec IO-Z d13-0","callsign_formatted":"Q8J-0HW","callsign":"Q8J0HW","patch_url":"https://imgur.com/IcRIHpH.png","location_x":26874.21875,"location_y":-7473.59375,"lat":626.3203125,"lng":3593.710938,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":71,"type":"FC","name":"Cheetah Labs","system":"Nuelou LX-A d1-0","callsign_formatted":"V4H-B2V","callsign":"V4HB2V","patch_url":"https://imgur.com/pm7NLAp.png","location_x":37792.25,"location_y":13129.90625,"lat":1656.495313,"lng":4139.6125,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":72,"type":"FC","name":"DSSA Nereus' Deep","system":"Engopr YH-L B14-2","callsign_formatted":"MNG-B0Z","callsign":"MNGB0Z","patch_url":"https://imgur.com/9kePniS.png","location_x":24463.625,"location_y":3088.71875,"lat":1154.435938,"lng":3473.18125,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":73,"type":"FC","name":"DSSA Alvin's Rest","system":"BLIA CHRAEI QU-M C21-0","callsign_formatted":"VHM-2VZ","callsign":"VHM2VZ","patch_url":"https://imgur.com/OUEMATh.png","location_x":13378.59375,"location_y":53634.03125,"lat":3681.701563,"lng":2918.929688,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":75,"type":"FC","name":"DSSA Glomar Explorer","system":"Oob Aoscs BW-E d11-52","callsign_formatted":"Y6K-74Z","callsign":"Y6K74Z","patch_url":"https://imgur.com/pm7NLAp.png","location_x":16976.1875,"location_y":17829.375,"lat":1891.46875,"lng":3098.809375,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":82,"type":"FC","name":"DSSA Leo's Vision","system":"Hyueths HS-H d11-5","callsign_formatted":"KLB-44V","callsign":"KLB44V","patch_url":"https://imgur.com/DCNp1g2.png","location_x":-93.9375,"location_y":-12836.96875,"lat":358.1515625,"lng":2245.303125,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":84,"type":"FC","name":"DSSA Artemis Rest","system":"Synuefuae CM-J d10-42","callsign_formatted":"K1B-75W","callsign":"K1B75W","patch_url":"https://imgur.com/ekX5JIp.png","location_x":6233.65625,"location_y":-113.6875,"lat":994.315625,"lng":2561.682813,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":85,"type":"FC","name":"DSSA Nostromo","system":"MYCAPP PJ-T B6-1","callsign_formatted":"JBG-4QZ","callsign":"JBG4QZ","patch_url":"https://imgur.com/E6Ghtqk.png","location_x":27236,"location_y":24681.65625,"lat":2234.082813,"lng":3611.8,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":86,"type":"FC","name":"Lost Sanity","system":"PHRAE DRYIAE AM-J D10-0","callsign_formatted":"KHX-NKW","callsign":"KHXNKW","patch_url":"https://imgur.com/hhxnCdy.png","location_x":20102.6875,"location_y":-14260.3125,"lat":286.984375,"lng":3255.134375,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":87,"type":"FC","name":"Will's Haven","system":"BYEEQUE ST-A B4-4","callsign_formatted":"Q9N-12F","callsign":"Q9N12F","patch_url":"https://imgur.com/P29NGhP.png","location_x":-25007.28125,"location_y":24627.375,"lat":2231.36875,"lng":999.6359375,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":88,"type":"FC","name":"Four Corners Monument","system":"PLOEA AUSCS ZA-A c16","callsign_formatted":"X4J-85Z","callsign":"X4J85Z","patch_url":"https://imgur.com/Rj6WIS0.png","location_x":3534.4375,"location_y":39901.0625,"lat":2995.053125,"lng":2426.721875,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":90,"type":"FC","name":"DSSA Jolly Roger","system":"Ooctarbs NR-W e1-0","callsign_formatted":"K4Z-B7Z","callsign":"K4ZB7Z","patch_url":"https://imgur.com/OFXSG2T.png","location_x":12578.53125,"location_y":59505.46875,"lat":3975.273438,"lng":2878.926563,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":91,"type":"FC","name":"DSSA Nova Blues","system":"Eord Prau ZK-N d7-711","callsign_formatted":"KFX-W3Z","callsign":"KFXW3Z","patch_url":"https://imgur.com/v1WL1Gf.png","location_x":5832.03125,"location_y":20083.5,"lat":2004.175,"lng":2541.601563,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":92,"type":"FC","name":"[ISF] Mandy's Rest","system":"PLAE BROAE DL-P D5-0","callsign_formatted":"B6L-L0Z","callsign":"B6LL0Z","patch_url":"https://imgur.com/0hwGJsx.png","location_x":27225.75,"location_y":50621.09375,"lat":3531.054688,"lng":3611.2875,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":93,"type":"FC","name":"DSSA Manatee","system":"Eolls Graae TA-K c10-5","callsign_formatted":"J4W-W8K","callsign":"J4WW8K","patch_url":"https://imgur.com/RqapNhW.png","location_x":-18792.5625,"location_y":30120.3125,"lat":2506.015625,"lng":1310.371875,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":94,"type":"FC","name":"Hayholt","system":"Aiphaitt AA-A h7","callsign_formatted":"JZQ-GXZ","callsign":"JZQGXZ","patch_url":"https://imgur.com/2uOXltL.png","location_x":-5034.875,"location_y":34009,"lat":2700.45,"lng":1998.25625,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":95,"type":"FC","name":"Galactic Unity","system":"Byoi Aowsy XD-L b40-0","callsign_formatted":"QNY-BQN","callsign":"QNYBQN","patch_url":"https://imgur.com/yrVqpWY.png","location_x":-5466.90625,"location_y":44603.40625,"lat":3230.170313,"lng":1976.654688,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":97,"type":"FC","name":"DSSA Totoro","system":"GREAE PHOEA XF-D D13-507","callsign_formatted":"NNW-23Z","callsign":"NNW23Z","patch_url":"https://imgur.com/5ALa9K5.png","location_x":4826.25,"location_y":16702.15625,"lat":1835.107813,"lng":2491.3125,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":100,"type":"FC","name":"DSSA Solsen's Alastor","system":"Flyoo Groa SO-Z e0","callsign_formatted":"KOY-LKF","callsign":"KOYLKF","patch_url":"https://imgur.com/kfwzDMH.png","location_x":-26482.4375,"location_y":50335.125,"lat":3516.75625,"lng":925.878125,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":103,"type":"FC","name":"DSSA Wanderer's Rest","system":"FLYAI PRE HR-V C2-1","callsign_formatted":"NNT-W4Z","callsign":"NNTW4Z","patch_url":"https://imgur.com/VScCgTh.png","location_x":-22903.09375,"location_y":40017.09375,"lat":3000.854688,"lng":1104.845313,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":105,"type":"FC","name":"RR-DSSA Rocksteady","system":"PROOE HYPUE FH-U E3-2","callsign_formatted":"KBH-T2Z","callsign":"KBHT2Z","patch_url":"https://imgur.com/cYU2PLO.png","location_x":519.625,"location_y":8671.5,"lat":1433.575,"lng":2275.98125,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":108,"type":"FC","name":"The Helix","system":"Phrae Prau NY-Y d1-15","callsign_formatted":"X0F-N1J","callsign":"X0FN1J","patch_url":"https://imgur.com/uY15ule.png","location_x":29786.75,"location_y":26047.875,"lat":2302.39375,"lng":3739.3375,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":109,"type":"FC","name":"DSSA Erikson's Gateway","system":"Hypoe Bloae KZ-Z c16-6","callsign_formatted":"X6Z-06M","callsign":"X6Z06M","patch_url":"https://imgur.com/DNnMkHV.png","location_x":-31101.71875,"location_y":32944.625,"lat":2647.23125,"lng":694.9140625,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":110,"type":"FC","name":"TFS Carpe Vinum","system":"Byae Aowsy GR-N d6-52","callsign_formatted":"TZN-L3Z","callsign":"TZNL3Z","patch_url":"https://imgur.com/Zftle7r.png","location_x":14407.625,"location_y":44312.59375,"lat":3215.629688,"lng":2970.38125,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":112,"type":"FC","name":"DSSA Pegasus","system":"Hyuqau WU-N c23-79","callsign_formatted":"K6V-G3B","callsign":"K6VG3B","patch_url":"https://imgur.com/pm7NLAp.png","location_x":-925.25,"location_y":35791.75,"lat":2789.5875,"lng":2203.7375,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":113,"type":"FC","name":"CEC Deus Vult!","system":"Ooc Fleau GG-F d11-0","callsign_formatted":"XFH-W4Y","callsign":"XFHW4Y","patch_url":"https://imgur.com/pm7NLAp.png","location_x":36945.625,"location_y":17868.0625,"lat":1893.403125,"lng":4097.28125,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":123,"type":"FC","name":"DSSA Heart of Gold","system":"Cloomeia FG-Y e95","callsign_formatted":"Q9G-9TL","callsign":"Q9G9TL","patch_url":"https://imgur.com/7i4UpGL.png","location_x":11719.15625,"location_y":24717.375,"lat":2235.86875,"lng":2835.957813,"patch_credit":"FlyDangerous o7","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":124,"type":"FC","name":"Michelle’s Legacy","system":"Eorm Chreou XS-U d2-14","callsign_formatted":"QHY-G8J","callsign":"QHYG8J","patch_url":"https://imgur.com/fhfPWND.png","location_x":-31117.15625,"location_y":27367,"lat":2368.35,"lng":694.1421875,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":126,"type":"FC","name":"TWITCHTVSOMDY","system":"Lyed YJ-I d9-0","callsign_formatted":"KZQ-24Q","callsign":"KZQ24Q","patch_url":"https://imgur.com/EyN8Sfi.png","location_x":11007.46875,"location_y":-16899.75,"lat":155.0125,"lng":2800.373438,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":127,"type":"FC","name":"IGAU Inverness","system":"Thraikoo PS-U e2-4","callsign_formatted":"X8V-6LZ","callsign":"X8V6LZ","patch_url":"https://imgur.com/pm7NLAp.png","location_x":-18646,"location_y":7135.9375,"lat":1356.796875,"lng":1317.7,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":130,"type":"FC","name":"DSSA Emerald Tablet","system":"THUECHE XK-B C2-1","callsign_formatted":"M2Z-44Z","callsign":"M2Z44Z","patch_url":"https://imgur.com/efCgsew.png","location_x":-13531.96875,"location_y":52802.8125,"lat":3640.140625,"lng":1573.401563,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":131,"type":"FC","name":"DSSA Nowhere","system":"Scheau Prou SO-X D2-1","callsign_formatted":"K0H-1KK","callsign":"K0H1KK","patch_url":"https://imgur.com/pm7NLAp.png","location_x":-36365.03125,"location_y":24786.78125,"lat":2239.339063,"lng":431.7484375,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":132,"type":"FC","name":"DSSA - Void Crusader","system":"GREAE PHIO VK-O E6-4343","callsign_formatted":"KFF-86M","callsign":"KFF86M","patch_url":"https://imgur.com/lAFKjmh.png","location_x":1474.875,"location_y":16723.75,"lat":1836.1875,"lng":2323.74375,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":133,"type":"FC","name":"DSSA133/Cygni-Vanguard","system":"Floalk QQ-Q c20-2","callsign_formatted":"XZ4-NXF","callsign":"XZ4NXF","patch_url":"https://imgur.com/pm7NLAp.png","location_x":-16043.34375,"location_y":15207.375,"lat":1760.36875,"lng":1447.832813,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":136,"type":"FC","name":"RCS Chatsworth","system":"BLA BYOE PR-U C19-1","callsign_formatted":"XZG-L0V","callsign":"XZGL0V","patch_url":"https://imgur.com/pm7NLAp.png","location_x":19851.9375,"location_y":56114.75,"lat":3805.7375,"lng":3242.596875,"patch_credit":"","location_z":"","edsmUrl":"","EDSMid":"","description":"","scan_type":"","scan_id":""},{"number":200,"type":"historical","name":"Sol","system":"Sol","callsign_formatted":"Sol","callsign":"Sol","patch_url":"https://imgur.com/pm7NLAp.png","location_x":0,"location_y":0,"lat":1000,"lng":2250,"patch_credit":"","location_z":0,"edsmUrl":"https://www.edsm.net/en/system/id/27/name/Sol","EDSMid":182,"description":"Historic system famous as both the birthplace of humanity and as the political capital of the Federation. Mostly Harmless.","scan_type":"system","scan_id":"Sol"},{"number":201,"type":"historical","name":"Sagittarius A*","system":"Sagittarius A*","callsign_formatted":"Sagittarius A*","callsign":"Sagittarius A*","patch_url":"https://imgur.com/pm7NLAp.png","location_x":25.21875,"location_y":25899.96875,"lat":2294.998438,"lng":2251.260938,"patch_credit":"","location_z":-20.9063,"edsmUrl":"https://www.edsm.net/en/system/id/25635/name/Sagittarius+A%2A","EDSMid":15,"description":"The supermassive black hole at the centre of the galaxy.","scan_type":"system","scan_id":"Sagittarius A*"},{"number":202,"type":"historical","name":"Salomé's World","system":"Eafots RX-T d3-3","callsign_formatted":"Salomé's World","callsign":"Eafots RX-T d3-3","patch_url":"https://imgur.com/pm7NLAp.png","location_x":-5579.25,"location_y":-5795.0625,"lat":710.246875,"lng":1971.0375,"patch_credit":"","location_z":450.0938,"edsmUrl":"https://www.edsm.net/en/system/id/4673210/name/Eafots+RX-T+d3-3","EDSMid":1362,"description":"The system contains many worlds but interestingly Salomé only scanned the two Ammonia worlds within the system. Salomé was killed trying to expose the Exodus Conspiracy on 29th April 3303, so it is believed that this system and the worlds she scanned could be some of her final exploration-related discoveries.","scan_type":"system","scan_id":"Eafots RX-T d3-3"},{"number":203,"type":"historical","name":"Anaconda's Graveyard","system":"HD 76133","callsign_formatted":"Anaconda's Graveyard","callsign":"HD 76133","patch_url":"https://imgur.com/pm7NLAp.png","location_x":1645.344,"location_y":-2128.59375,"lat":893.5703125,"lng":2332.2672,"patch_credit":"","location_z":1728.313,"edsmUrl":"https://www.edsm.net/en/system/id/6212217/name/HD+76133","EDSMid":1153,"description":"The Anaconda's Graveyard is the final resting place of the Distant Stars Expedition 3303","scan_type":"system","scan_id":"HD 76133"},{"number":204,"type":"historical","name":"Pallaeni","system":"Pallaeni","callsign_formatted":"Pallaeni","callsign":"Pallaeni","patch_url":"https://imgur.com/pm7NLAp.png","location_x":112.6875,"location_y":128.4375,"lat":1006.421875,"lng":2255.634375,"patch_credit":"","location_z":47.125,"edsmUrl":"https://www.edsm.net/en/system/id/1093/name/Pallaeni","EDSMid":1831,"description":"Starting location for Distant Suns, Distant Worlds, and Distant Worlds 2 Expeditions. Distant Worlds 2 launched on January 13th 3305 and contained over 13,500 ships.","scan_type":"system","scan_id":"Pallaeni"},{"number":205,"type":"historical","name":"Gibb's Bridge","system":"Syralia JT-V b7-0","callsign_formatted":"Gibb's Bridge","callsign":"Syralia JT-V b7-0","patch_url":"https://imgur.com/pm7NLAp.png","location_x":1276.188,"location_y":5509.09375,"lat":1275.454688,"lng":2313.8094,"patch_credit":"","location_z":1016.844,"edsmUrl":"https://www.edsm.net/en/system/id/2031182/name/Syralia+JT-V+b7-0","EDSMid":442,"description":"Discovered in the days before planetary landings was possible, this system was highlighted as interesting candidate to study just HOW close a planet and its moon may orbit each other.","scan_type":"system","scan_id":"Syralia JT-V b7-0"},{"number":206,"type":"historical","name":"Nereus (& Tranquility)","system":"Metztli","callsign_formatted":"Nereus (& Tranquility)","callsign":"Metztli","patch_url":"https://imgur.com/pm7NLAp.png","location_x":-9518.41,"location_y":19823.625,"lat":1991.18125,"lng":1774.0795,"patch_credit":"","location_z":-911.969,"edsmUrl":"https://www.edsm.net/en/system/id/13728193/name/Metztli","EDSMid":714,"description":"Nereus was one of the first systems to be colonized near Colonia. The system was later renamed to 'Metztli' by Universal Cartographics.","scan_type":"system","scan_id":"Metztli"},{"number":207,"type":"historical","name":"Wren's Rest","system":"Aishaint XI-K d8-127","callsign_formatted":"Wren's Rest","callsign":"Aishaint XI-K d8-127","patch_url":"https://imgur.com/pm7NLAp.png","location_x":11416.28,"location_y":34242.9375,"lat":2712.146875,"lng":2820.814,"patch_credit":"","location_z":72.375,"edsmUrl":"https://www.edsm.net/en/system/id/53705645/name/Aishaint+XI-K+d8-127","EDSMid":2125,"description":"Discovered by Nax Wren on June 23rd 3306 during the DSSA Callisto's Respite Expedition, this is the first Tritium 3 Hotspot discovered beyond the local Orion Spur.","scan_type":"system","scan_id":"Aishaint XI-K d8-127"},{"number":208,"type":"historical","name":"Eärendil","system":"Thaae Byoe AA-A h2","callsign_formatted":"Eärendil","callsign":"Thaae Byoe AA-A h2","patch_url":"https://imgur.com/pm7NLAp.png","location_x":-6089.06,"location_y":30156.875,"lat":2507.84375,"lng":1945.547,"patch_credit":"","location_z":-3432.66,"edsmUrl":"https://www.edsm.net/en/system/id/28005514/name/Thaae+Byoe+AA-A+h2","EDSMid":1793,"description":"This lonely system was reached in August 3304, and as of that date, is believed to be the lowest point beneath the galactic plane ever reached at -3433LY.","scan_type":"system","scan_id":"Thaae Byoe AA-A h2"},{"number":209,"type":"historical","name":"The Great Escape","system":"Trieneou AA-A h2","callsign_formatted":"The Great Escape","callsign":"Trieneou AA-A h2","patch_url":"https://imgur.com/pm7NLAp.png","location_x":-7958.66,"location_y":21491.0625,"lat":2074.553125,"lng":1852.067,"patch_credit":"","location_z":-3393.31,"edsmUrl":"https://www.edsm.net/en/system/id/26757497/name/Trieneou+AA-A+h2","EDSMid":1979,"description":"The Great Escape is believed to be the system furthest below the galactic plane from which any CMDR has succesfully returned. The system is incredibly difficult to reach and return from - requiring extensive planning, specialist outfitting as well as skillfull cooperation with a wingman acting as support tanker.","scan_type":"system","scan_id":"Trieneou AA-A h2"},{"number":210,"type":"historical","name":"Lemmings Rest Stop","system":"Systeia Free AA-A h2","callsign_formatted":"Lemmings Rest Stop","callsign":"Systeia Free AA-A h2","patch_url":"https://imgur.com/pm7NLAp.png","location_x":-6957.44,"location_y":25155.375,"lat":2257.76875,"lng":1902.128,"patch_credit":"","location_z":3450.219,"edsmUrl":"https://www.edsm.net/en/system/id/28674044/name/Systeia+Free+AA-A+h2","EDSMid":1881,"description":"At 3450.22 light years above the galactic plane this was the highest known system reached by a pilot as of September 3304.","scan_type":"system","scan_id":"Systeia Free AA-A h2"},{"number":211,"type":"POI","name":"Jaques Station","system":"Colonia","callsign_formatted":"Jaques Station","callsign":"Colonia","patch_url":"https://imgur.com/pm7NLAp.png","location_x":-9530.5,"location_y":19808.125,"lat":1990.40625,"lng":1773.475,"patch_credit":"","location_z":-910.281,"edsmUrl":"https://www.edsm.net/en/system/id/3384966/name/Colonia","EDSMid":510,"description":"Jaques Station is an Orbis Starport currently located in the Colonia system. Owned by the eccentric Jaques, it is unique among stations in that it is equipped with engines and is capable of traveling to different systems; all other stations, with the exception of those undergoing construction, are permanently stationary. Jaques Quinentian Still, a Rare Commodity, is exclusively available at Jaques Station.","scan_type":"system","scan_id":"Colonia"},{"number":212,"type":"POI","name":"Hawking's Gap Abandoned Settlements","system":"Plaa Aec IZ-N c20-1","callsign_formatted":"Hawking's Gap Abandoned Settlements","callsign":"Plaa Aec IZ-N c20-1","patch_url":"https://imgur.com/pm7NLAp.png","location_x":7890.469,"location_y":7508.03125,"lat":1375.401563,"lng":2644.52345,"patch_credit":"","location_z":137.3125,"edsmUrl":"https://www.edsm.net/en/system/id/7002265/name/Plaa+Aec+IZ-N+c20-1","EDSMid":824,"description":"Project Dynasty was a secret exploration initiative conceived by The Club in 3270. In response to the likelihood of a Thargoid civil war spilling into human space, The Club sought potential safe havens where humanity could flee in order to escape the conflict and survive. Project Dynasty was intended to identify Earth-like worlds beyond human space and mark them with beacons for later reference. When the settlements were discovered there were no survivors.","scan_type":"system","scan_id":"Plaa Aec IZ-N c20-1"},{"number":213,"type":"historical","name":"Beagle Point","system":"Beagle Point","callsign_formatted":"Beagle Point","callsign":"Beagle Point","patch_url":"https://imgur.com/pm7NLAp.png","location_x":-1111.56,"location_y":65269.75,"lat":4263.4875,"lng":2194.422,"patch_credit":"","location_z":-134.219,"edsmUrl":"https://www.edsm.net/en/system/id/124406/name/Beagle+Point","EDSMid":51,"description":"Beagle Point, one of the most distant star systems currently surveyed at 65,279 LYs from Sol.","scan_type":"system","scan_id":"Beagle Point"},{"number":214,"type":"POI","name":"Jameson's Demise","system":"HIP 12099","callsign_formatted":"Jameson's Demise","callsign":"HIP 12099","patch_url":"https://imgur.com/pm7NLAp.png","location_x":-101.906,"location_y":-165.59375,"lat":991.7203125,"lng":2244.9047,"patch_credit":"","location_z":-95.4688,"edsmUrl":"https://www.edsm.net/en/system/id/176846/name/HIP+12099","EDSMid":1556,"description":"Final resting place of Commander John Jameson.","scan_type":"system","scan_id":"HIP 12099"},{"number":215,"type":"POI","name":"Black in Green (Tourist Installation)","system":"Shrogea MH-V e2-1763","callsign_formatted":"Black in Green (Tourist Installation)","callsign":"Shrogea MH-V e2-1763","patch_url":"https://imgur.com/pm7NLAp.png","location_x":971.0313,"location_y":21307.3125,"lat":2065.365625,"lng":2298.551565,"patch_credit":"","location_z":613.2188,"edsmUrl":"https://www.edsm.net/en/system/id/1610727/name/Shrogea+MH-V+e2-1763","EDSMid":1676,"description":"Tranquility’s Stop maintains a tourist installation in orbit of the black hole within a planetary nebula found in Shrogea MH-V e2-1763. Located in a beautiful green nebula.","scan_type":"system","scan_id":"Shrogea MH-V e2-1763"},{"number":216,"type":"POI","name":"Zurara","system":"Syreadiae JX-F c0","callsign_formatted":"Zurara","callsign":"Syreadiae JX-F c0","patch_url":"https://imgur.com/pm7NLAp.png","location_x":-9529.44,"location_y":-7428.4375,"lat":628.578125,"lng":1773.528,"patch_credit":"","location_z":-64.5,"edsmUrl":"https://www.edsm.net/en/system/id/11351065/name/Syreadiae+JX-F+c0","EDSMid":1047,"description":"This megaship from the mysterius Dynasty Expedition was found deep within the Formidine Rift on April 17th 3303.Audio logs on the site tell the story of the unfortunate crew. It is a haunted place...","scan_type":"system","scan_id":"Syreadiae JX-F c0"},{"number":217,"type":"historical","name":"First Human Colony","system":"Tau Ceti","callsign_formatted":"First Human Colony","callsign":"Tau Ceti","patch_url":"https://imgur.com/pm7NLAp.png","location_x":-0.375,"location_y":-3.5,"lat":999.825,"lng":2249.98125,"patch_credit":"","location_z":-11.4063,"edsmUrl":"https://www.edsm.net/en/system/id/1293/name/Tau+Ceti","EDSMid":99999,"description":"First colony outside the Sol system, where the first alien life was discovered. Unfortunately the last remnants are now in zoo enclosures for tourists.","scan_type":"system","scan_id":"Tau Ceti"},{"number":218,"type":"POI","name":"VY Canis Majoris","system":"VY Canis Majoris","callsign_formatted":"VY Canis Majoris","callsign":"VY Canis Majoris","patch_url":"https://imgur.com/pm7NLAp.png","location_x":1576.063,"location_y":-922.53125,"lat":953.8734375,"lng":2328.80315,"patch_credit":"","location_z":-150.219,"edsmUrl":"https://www.edsm.net/en/system/id/25862/name/VY+Canis+Majoris","EDSMid":194,"description":"The largest known star currently discovered, and just a mere 1,800 LYs from Sol. VY Canis Majoris was one of the first destinations for pioneer explorers during the early \"gamma-phase\" of testing current FSD technology.","scan_type":"system","scan_id":"VY Canis Majoris"},{"number":219,"type":"POI","name":"Great Annihilator Black Hole","system":"Great Annihilator","callsign_formatted":"Great Annihilator Black Hole","callsign":"Great Annihilator","patch_url":"https://imgur.com/pm7NLAp.png","location_x":354.8438,"location_y":22997.21875,"lat":2149.860938,"lng":2267.74219,"patch_credit":"","location_z":-42.4375,"edsmUrl":"https://www.edsm.net/en/system/id/65259/name/Great+Annihilator","EDSMid":8,"description":"20th century astronomers discovered a source of intense photons at 511 keV, which was known to be the result of positron-electron annihilation. After study determined that the source was equal to annihilation events of 10 billion tons per second of positron-electron pairs, it was dubbed The Great Annihilator. The only possible explanation was a large black hole.","scan_type":"system","scan_id":"Great Annihilator"},{"number":220,"type":"POI","name":"Arm's End","system":"Hypau Aec IO-Z d13-0","callsign_formatted":"Arm's End","callsign":"Hypau Aec IO-Z d13-0","patch_url":"https://imgur.com/pm7NLAp.png","location_x":26874.22,"location_y":-7473.59375,"lat":626.3203125,"lng":3593.711,"patch_credit":"","location_z":-18.6875,"edsmUrl":"https://www.edsm.net/en/system/id/5858416/name/Hypau+Aec+IO-Z+d13-0","EDSMid":1403,"description":"One of the furthest reachable points along the Outer Arm, and home of DSSA's Explorer's Bar & Grill.","scan_type":"system","scan_id":"Hypau Aec IO-Z d13-0"}]

   this.threadEDPS = Thread(target=workerEDPS, name='EDPS worker')
   this.threadEDPS.daemon = True
   this.threadEDPS.start()
   print("ED Passport System Plugin Loading...")

   cmder = config.get("edpscmder")

   this.queueEDPS.put(('does not matter',{},None, 'getAppInformation', ""))
   this.queueEDPS.put(('does not matter', {}, None, 'getFCsList',""))
   this.queueEDPS.put(('does not matter', {}, None, 'getPassportStartUp',""))

   #wipeSettings()

   return "EDPS"

def plugin_stop():
    """
    EDMC is closing
    """
    this.queueEDPS.put(None)
    this.threadEDPS.join()
    this.threadEDPS = None
    print("Clossing ED Passport System Plugin")

# Worker thread
def workerEDPS():
    while True:
        item = this.queueEDPS.get()
        if not item:
            print('Closing')
            return  # Closing
        else:
            print('Request Added to Queue')
            (url, data, callback, callType, input) = item

        retrying = 0
        while retrying < 3:
            try:
                if callType == 'postDate':
                    print('In Post Date!')
                    #Look if they already have the FC in their passport
                    if input in this.Passport['visited']:
                        print("Passport Already Acquired!")
                        this.edpsConsoleMessage = 'DSSA Docking Added to Passport'
                        this.label4.event_generate('<<edpsUpdateConsoleEvent>>', when="tail")
                        retrying = 3
                        break
                    else:
                        print("Add FC to Passport!")
                        if config.getint("edpslog"):
                            headers = {'x-api-key': 'bn9oCD5lqp7Yavh3l7VLB4lixo1FI69F2aiOmznB'}
                            r = requests.post(url, data=json.dumps(data, separators=(',', ':')), headers=headers, timeout=_TIMEOUT)
                            time.sleep(1)
                            reply = r.json()

                            if r.text == '"Date Added"':
                                print('Posted!')
                                this.edpsConsoleMessage = 'DSSA Docking Added to Passport'
                                this.label4.event_generate('<<edpsUpdateConsoleEvent>>', when="tail")
                                time.sleep(1)
                                this.edpsPassportCountMessage = str(this.PassortLength + 1) + ' of ' + str(this.FCLength)
                                this.label2.event_generate('<<edpsUpdatePassportCountEvent>>', when="tail")
                                this.Passport['visited'].update({data['callsign']:data['date']})
                                this.PassortLength = (len(this.Passport['visited']) - 1)
                                time.sleep(1)
                                #this.queue.put(('does not matter', {}, None, 'getPassport', ""))
                                retrying = 3
                                break
                            else:
                                print('Error Posting!')
                                if r.text == '"Wrong API Key"':
                                    this.edpsConsoleMessage = 'API Key Wrong in Settings'
                                    this.label4.event_generate('<<edpsUpdateConsoleEvent>>', when="tail")
                                    retrying = 3
                                    break
                                elif r.text == '"Passport does not exists"':
                                    this.edpsConsoleMessage = 'Cmder not found! Sign up at edps.dev!'
                                    this.label4.event_generate('<<edpsUpdateConsoleEvent>>', when="tail")
                                    retrying = 3
                                    break
                                else:
                                    this.edpsConsoleMessage = 'Unknown Error Adding to Passport'
                                    this.label4.event_generate('<<edpsUpdateConsoleEvent>>', when="tail")
                                    retrying = 3
                                    break

                        else:
                            print('User does not want to send data')
                            this.edpsConsoleMessage = 'DSSA Docking Detected, but User needs to enable sending data to EDPS in File-->Settings! Please Redock afterwards!'
                            this.label4.event_generate('<<edpsUpdateConsoleEvent>>', when="tail")
                            retrying = 3
                            break

                elif callType == 'getAppInformation':
                    print('Getting App Information')
                    time.sleep(2)
                    headers = {'x-api-key': 'bn9oCD5lqp7Yavh3l7VLB4lixo1FI69F2aiOmznB'}
                    r = requests.get('https://www.edps.dev/AppInformation.json', headers=headers, timeout=_TIMEOUT)
                    this.AppInformationEDPS = json.loads(r.text)
                    if r.ok:
                        print('Status is Ok')
                        if this.AppInformationEDPS['EDMCApp'] != _EDPSAPPVERSION:
                            print('EDPS needs to be updated')
                            this.edpsConsoleMessage = 'Outdated Plugin Version - Updating...'
                            this.label4.event_generate('<<edpsUpdateConsoleEvent>>', when="tail")
                            updatePlugin(this.AppInformationEDPS['EDMCApp'])
                            time.sleep(1)
                            retrying = 3
                            break
                        else:
                            this.edpsConsoleMessage = this.AppInformationEDPS['EDMCAppMessage']
                            this.label4.event_generate('<<edpsUpdateConsoleEvent>>', when="tail")
                            retrying = 3
                            break
                    else:
                        print('Error: Request returned a non-200 status code in AppInformation')
                        this.edpsConsoleMessage = 'Unknown Error Reaching Server'
                        this.label4.event_generate('<<edpsUpdateConsoleEvent>>', when="tail")
                        retrying = 3
                        break
                    time.sleep(5)
                    retrying = 3
                    break
                elif callType == 'getFCsList':
                    print('Getting FC List')
                    headers = {'x-api-key': 'bn9oCD5lqp7Yavh3l7VLB4lixo1FI69F2aiOmznB'}
                    r = requests.get('https://www.edps.dev/FCs.json', headers=headers, timeout=_TIMEOUT)
                    this.FCs = json.loads(r.text)
                    if r.ok:
                        this.FCLength = len(this.FCs)
                        retrying = 3
                        break
                    else:
                        print('Error: Request returned a non-200 status code in FCs')
                        this.edpsConsoleMessage = 'Unknown Error Reaching Server'
                        this.label4.event_generate('<<edpsUpdateConsoleEvent>>', when="tail")
                        retrying = 3
                        break
                    time.sleep(5)
                    retrying = 3
                    break

                elif callType == 'getPassport':
                    print('Getting Commanders Passport')
                    this.edpsCmderName = config.get("edpscmder")
                    print(this.edpsCmderName)
                    if this.edpsCmderName is None:
                        this.edpsConsoleMessage = 'EDPS Started (No API Key)'
                        this.label4.event_generate('<<edpsUpdateConsoleEvent>>', when="tail")
                        this.edpsPassportCountMessage = 'No API Key in Settings'
                        this.label2.event_generate('<<edpsUpdatePassportCountEvent>>', when="tail")
                        retrying = 3
                        break
                    print("Here")
                    cred = credentials(config.get("edpscmder"))
                    print('trace')
                    print(cred)
                    print("Here2")
                    if cred:
                        print("Here3")
                        headers = {'x-api-key': 'bn9oCD5lqp7Yavh3l7VLB4lixo1FI69F2aiOmznB'}
                        r = requests.get('https://edps-api.d3develop.com/passports/passport?cmder_name=' + this.edpsCmderName, headers=headers, timeout=_TIMEOUT)
                        if r.ok:
                            if r.text == '"No User Found"':
                                print('User not found in database')
                                this.edpsConsoleMessage = 'Cmder not found! Sign up at edps.dev!'
                                this.label4.event_generate('<<edpsUpdateConsoleEvent>>', when="tail")
                                retrying = 3
                                break
                            else:
                                this.Passport = json.loads(r.text)
                                this.PassortLength = (len(this.Passport['visited'])-1)
                                this.edpsPassportCountMessage = str(this.PassortLength) + ' of ' + str(this.FCLength)
                                this.label2.event_generate('<<edpsUpdatePassportCountEvent>>', when="tail")
                                retrying = 3
                                break
                        else:
                            print('Error: Request returned a non-200 status code in Passport')
                            this.edpsConsoleMessage = 'Unknown Error Reaching Server'
                            this.label4.event_generate('<<edpsUpdateConsoleEvent>>', when="tail")
                            retrying = 3
                            break
                        time.sleep(5)
                        retrying = 3
                        break
                    else:
                        this.edpsConsoleMessage = 'No Credentials'
                        this.label4.event_generate('<<edpsUpdateConsoleEvent>>', when="tail")
                        retrying = 3
                        break
                elif callType == 'getPassportStartUp':
                    print('Getting Commanders Passport - Startup')
                    time.sleep(1)
                    if monitor.cmdr:
                        config.set('edpscmder', monitor.cmdr)
                    if config.get("edpscmder") is None:
                        this.edpsConsoleMessage = 'EDPS Started (No API Key)'
                        this.label4.event_generate('<<edpsUpdateConsoleEvent>>', when="tail")
                        this.edpsPassportCountMessage = 'No API Key in Settings'
                        this.label2.event_generate('<<edpsUpdatePassportCountEvent>>', when="tail")
                        retrying = 3
                        break
                    print(config.get("edpscmder"))
                    this.edpsCmderName = config.get("edpscmder")
                    cred = credentials(this.edpsCmderName)
                    print(cred)
                    if cred:
                        print("Here3")
                        headers = {'x-api-key': 'bn9oCD5lqp7Yavh3l7VLB4lixo1FI69F2aiOmznB'}
                        r = requests.get('https://edps-api.d3develop.com/passports/passport?cmder_name=' + this.edpsCmderName, headers=headers, timeout=_TIMEOUT)
                        if r.ok:
                            if r.text == '"No User Found"':
                                print('User not found in database')
                                this.edpsConsoleMessage = 'Cmder not found! Sign up at edps.dev!'
                                this.label4.event_generate('<<edpsUpdateConsoleEvent>>', when="tail")
                                retrying = 3
                                break
                            else:
                                this.Passport = json.loads(r.text)
                                this.PassortLength = (len(this.Passport['visited'])-1)
                                this.edpsPassportCountMessage = str(this.PassortLength) + ' of ' + str(this.FCLength)
                                this.label2.event_generate('<<edpsUpdatePassportCountEvent>>', when="tail")
                                retrying = 3
                                break
                        else:
                            print('Error: Request returned a non-200 status code in Passport')
                            this.edpsConsoleMessage = 'Unknown Error Reaching Server'
                            this.label4.event_generate('<<edpsUpdateConsoleEvent>>', when="tail")
                            retrying = 3
                            break
                        time.sleep(5)
                        retrying = 3
                        break
                    else:
                        this.edpsConsoleMessage = 'No Credentials'
                        this.label4.event_generate('<<edpsUpdateConsoleEvent>>', when="tail")
                        retrying = 3
                        break
                else:
                    retrying = 3
                    break
            except:
                print(sys.exc_info()[0])
                print('Error!')
                retrying += 1
                if retrying == 3:
                    time.sleep(2)
                    this.edpsConsoleMessage = 'Unknown Error'
                    this.label4.event_generate('<<edpsUpdateConsoleEvent>>', when="tail")


def plugin_prefs(parent, cmdr, is_beta):
    config.set('edpscmder', cmdr)

    print('Plugin Prefs Ran')
    PADX = 10
    BUTTONX = 12	# indent Checkbuttons and Radiobuttons
    PADY = 2		# close spacing

    this.edps_frame = nb.Frame(parent)
    this.edps_frame.columnconfigure(1, weight=1)

    cred = credentials(cmdr)

    if cred:
        this.edpslog = tk.IntVar(value=config.getint("edpslog"))
        this.edpsapikey = tk.StringVar(value=cred)
    else:
        this.edpslog = tk.IntVar(value=config.getint("edpslog"))
        this.edpsapikey = tk.StringVar(value="")

    HyperlinkLabel(this.edps_frame, text='Elite Dangerous Passport System', background=nb.Label().cget('background'), url='https://www.edps.dev', underline=True).grid(columnspan=2, padx=PADX, sticky=tk.W)	# Don't translate
    this.log_button = nb.Checkbutton(this.edps_frame, text=_('Send passport data to EDPS'), variable=this.edpslog)
    this.log_button.grid(columnspan=2, padx=BUTTONX, pady=(5,0), sticky=tk.W)

    nb.Label(this.edps_frame).grid(sticky=tk.W)	# big spacer
    this.label = HyperlinkLabel(this.edps_frame, text=_('Elite Dangerous Passport Credentials'), background=nb.Label().cget('background'), url='https://www.edps.dev', underline=True)	# Section heading in settings
    this.label.grid(columnspan=2, padx=PADX, sticky=tk.W)

    this.cmdr_label = nb.Label(this.edps_frame, text=_('Commander Name'))  # Main window
    this.cmdr_label.grid(row=10, padx=PADX, sticky=tk.W)
    this.cmdr_text = nb.Label(this.edps_frame, text=cmdr)
    this.cmdr_text.grid(row=10, column=1, padx=PADX, pady=PADY, sticky=tk.W)

    this.apikey_label = nb.Label(this.edps_frame, text=_('API Key'))	# EDPS setting
    this.apikey_label.grid(row=12, padx=PADX, sticky=tk.W)
    this.apikey = nb.Entry(this.edps_frame, textvariable=this.edpsapikey)
    this.apikey.grid(row=12, column=1, padx=PADX, pady=PADY, sticky=tk.EW)

    nb.Label(this.edps_frame).grid(sticky=tk.W)	# big spacer

    this.progressComplete = nb.Label(this.edps_frame, text=_('0%'))
    this.progressComplete.grid(row=15, padx=PADX, sticky=tk.W)

    this.import_Journal = nb.Button(this.edps_frame, text="Send Local Journal Files", command=load_Journal_Logs)   # Main window
    this.import_Journal.grid(row=16, padx=(PADX+8), sticky=tk.W)

    prefs_cmdr_changed(cmdr, is_beta)

    return this.edps_frame

def set_state_frame_childs(frame, state):
    for child in frame.winfo_children():
        if child.winfo_class() in ("TFrame", "Frame", "Labelframe"):
            set_state_frame_childs(child, state)
        else:
            child["state"] = state

def prefs_cmdr_changed(cmdr, is_beta):
    config.set('edpscmder', cmdr)
    config.set('edpslog', this.edpslog.get())
    set_state_frame_childs(this.edps_frame, tk.NORMAL)
    this.apikey.delete(0, tk.END)
    if cmdr:
        print("In pref change cmd")
        this.cmdr_text["text"] = cmdr + (is_beta and " [Beta]" or "")
        cred = credentials(cmdr)
        if cred:
            this.apikey.insert(0, cred)
    else:
        this.cmdr_text["text"] = _("None")
        print("In pref change cmd None")

    if not cmdr or is_beta:
        set_state_frame_childs(this.edps_frame, tk.DISABLED)


def prefs_changed(cmdr, is_beta):
    if cmdr and not is_beta:
        cmdrs = config.get("edps_cmdrs")
        apikeys = config.get("edps_apikeys") or []
        if cmdr in cmdrs:
            idx = cmdrs.index(cmdr)
            apikeys.extend([""] * (1 + idx - len(apikeys)))
            apikeys[idx] = this.apikey.get().strip()
        else:
            config.set("edps_cmdrs", cmdrs + [cmdr])
            apikeys.append(this.apikey.get().strip())
        config.set("edps_apikeys", apikeys)
    config.set('edpslog', this.edpslog.get())



#----------------------------------------------------------------------------------
#Credentials management
#----------------------------------------------------------------------------------
def wipeSettings():
    config.set("edps_apikeys", [''])
    config.set("edps_cmdrs", [''])
    config.set('edpscmder', '')
    print('Settings Wiped')
    printDebugInfo()

def printDebugInfo():
    cmder = config.get("edpscmder")
    apikeys = config.get("edps_apikeys")
    cmdrs = config.get("edps_cmdrs")
    print(cmder)
    print(apikeys)
    print(cmdrs)

def createNewSettings():
    if monitor.cmdr:
        cmdrs = [monitor.cmdr]
        config.set("edps_cmdrs", cmdrs)
        config.set("edps_apikeys", [''])
        config.set('edpscmder', monitor.cmdr)
    else:
        cmdrs = ['']
        config.set("edps_cmdrs", cmdrs)
        config.set("edps_apikeys", [''])
        config.set('edpscmder', '')

def addNewCmdr(cmdr):
    print('Adding new cmdr')
    cmdrs = config.get("edps_cmdrs")
    apikeys = config.get("edps_apikeys")
    apikeys.append('')
    config.set("edps_cmdrs", cmdrs + [cmdr])
    config.set("edps_apikeys", apikeys)

def credentials(cmdr):
    # Credentials for cmdr
    print('In Credit')
    #Confirm that a cmdr was given
    if cmdr:
        cmdrs = config.get("edps_cmdrs")
        apikeys = config.get("edps_apikeys")
        #See if cmdrs exists if not then create (First time app use)
        if not cmdrs:
            #First time using the app
            createNewSettings()
            cmdrs = config.get("edps_cmdrs")
            apikeys = config.get("edps_apikeys")
            return(apikeys[0])
        # Check if older version of the app exists
        if not apikeys or len(apikeys) != len(cmdrs):
            #Old version of the app - Clear Settings
            createNewSettings()
            cmdrs = config.get("edps_cmdrs")
            apikeys = config.get("edps_apikeys")
            return (apikeys[0])
        if cmdr in cmdrs and apikeys:
            idx = cmdrs.index(cmdr)
            return (apikeys[idx])
        else:
            #No Cmdr Found
            addNewCmdr(cmdr)
    else:
        print('No cmdr Supplied')
        return None






#----------------------------------------------------------------------------------
#Load Journal Function
#----------------------------------------------------------------------------------
def load_Journal_Logs():
    print("Loading Logs Function TBD...")
    rootdir = config.default_journal_dir
    extensions = ('.log')
    root = tk.Tk()
    root.title("Import Widget")
    root.geometry("400x400")

    w = tk.Label(root, text="Importing Journal Files... Please wait!")
    w.pack()

    this.edpscommanderimport = config.get("edpscmder")

    if monitor.cmdr:
        prefs_cmdr_changed(monitor.cmdr, False)
        pass
    else:
        this.label4["text"] = 'No Cmdr - Login!'
        return

    for subdir, dirs, files in os.walk(rootdir):
        this.processingFile = 0
        for file in files:
            this.processingFile = this.processingFile + 1.0
            this.totalFiles = len(files)
            this.progress = str(((this.processingFile / this.totalFiles) * 100)) + '%'
            this.progressComplete['text'] = this.progress
            root.update()
            time.sleep(0.001)
            ext = os.path.splitext(file)[-1].lower()
            if ext in extensions:
                with open(rootdir + '\\' + file, 'r', encoding ="utf8") as f:
                    try:
                        for line in f:
                            try:
                                data = json.loads(line)
                                if data['event'] == 'LoadGame':
                                    #change of comander
                                    if 'Commander' in data:
                                        this.edpscommanderimport = data['Commander']
                                        config.set('edpscmder', data['Commander'])
                                if data['event'] == 'Docked':
                                    if data['StationType'] == 'FleetCarrier' and any(x['callsign_formatted'] == data['StationName'] and x['system'].lower() == data['StarSystem'].lower() for x in this.FCs):
                                        #if this.edpscommanderimport == config.get("edpscmder"):
                                        cred = credentials(this.edpscommanderimport)
                                        if cred:
                                            if this.edpscommanderimport == monitor.cmdr:
                                                d1 = datetime.strptime(data['timestamp'],"%Y-%m-%dT%H:%M:%SZ")
                                                w['text'] = w['text'] + "\nDocked to DSSA FC: " + data['StationName']
                                                this.queueEDPS.put(('https://edps-api.d3develop.com/passports/passport/date',
                                                                {'cmder_name': this.edpscommanderimport, 'api_key': cred,
                                                                 'callsign': data['StationName'].replace("-", ""),
                                                                 'date': d1.strftime('%m/%d/%Y')}, None, 'postDate',
                                                                data['StationName'].replace("-", "")))
                                                time.sleep(.01)
                                        else:
                                            w['text'] = w['text'] + "\nNo Credinitals for commander " + this.edpscommanderimport
                                if data['event'] == 'FSDJump':
                                    # Jumped into new System
                                    if any(x['callsign'].lower() == data['StarSystem'].lower() for x in this.FCs):
                                        d1 = datetime.strptime(data['timestamp'], "%Y-%m-%dT%H:%M:%SZ")
                                        w['text'] = w['text'] + "\nVisited POI: " + data['StarSystem']
                                        cred = credentials(this.edpscommanderimport)
                                        if cred:
                                            headers = {'Content-Type': 'application/json"'}
                                            this.queueEDPS.put(
                                                ('https://edps-api.d3develop.com/passports/passport/date',
                                                 {'cmder_name': this.edpscommanderimport, 'api_key': cred,
                                                  'callsign': data['StarSystem'],
                                                  'date': d1.strftime('%m/%d/%Y')}, None, 'postDate',
                                                 data['StarSystem']))
                                            time.sleep(.01)
                                        else:
                                            this.label4["text"] = "No Credentials in Settings"

                            except json.decoder.JSONDecodeError:
                                print('Error Reading Line in this file:')
                                print(f)
                                print('The line is:')
                                print(line)
                                continue
                    except UnicodeDecodeError:
                        console.log("Error Reading a line from the data file")
                        continue
    w['text'] = 'Import complete - You can now close this window!'



def plugin_app(parent):
    """
    Create a pair of TK widgets for the EDMC main window
    """
    frame = tk.Frame(parent)

    this.label = tk.Label(frame, text="Passports:", justify=tk.LEFT)
    this.label2 = tk.Label(frame, text="Loading...", justify=tk.RIGHT)
    this.label.grid(row=0, column=0, sticky=tk.W)
    this.label2.grid(row=0, column=2, sticky=tk.E)

    this.label3 = tk.Label(frame, text="EDPS:", justify=tk.LEFT)
    this.label4 = tk.Label(frame, text='Loading Data from Server...', justify=tk.RIGHT)
    label3.grid(row=1, column=0, sticky=tk.W)
    label4.grid(row=1, column=2, sticky=tk.E)
    #return (label3, label4)

    #Register Events used from other worker:
    this.label2.bind_all('<<edpsUpdatePassportCountEvent>>', update_Edps_Passport_Count)
    this.label4.bind_all('<<edpsUpdateConsoleEvent>>', update_Edps_Console)

    return (frame)

def cmdr_data(data, is_beta):
    """
    We have new data on our commander
    """
    print('Event Fires Commander Data')

def journal_entry(cmdr, is_beta, system, station, entry, state):
    print('Event Fires')
    if entry['event'] == 'LoadGame':
        #Adding multi-commander support
        if 'Commander' in entry:
            config.set('edpscmder', entry['Commander'])
            this.queueEDPS.put(('does not matter', {}, None, 'getPassport', ""))
            this.edpsConsoleMessage = 'Welcome Commander ' + entry['Commander'] + '!'
            this.label4.event_generate('<<edpsUpdateConsoleEvent>>', when="tail")
    if entry['event'] == 'Docked':
        # Docking Event Detected
        if entry['StationType'] == 'FleetCarrier' and any(x['callsign_formatted'] == entry['StationName'] for x in this.FCs) and any(y['system'].lower() == entry['StarSystem'].lower() for y in this.FCs):
            print('Detected FC Docking')
            config.set('edpscmder', cmdr)
            cred = credentials(config.get("edpscmder"))
            if cred:
                headers = {'Content-Type': 'application/json"'}
                this.queueEDPS.put(('https://edps-api.d3develop.com/passports/passport/date', {'cmder_name': cmdr, 'api_key': cred, 'callsign':entry['StationName'].replace("-",""), 'date':datetime.today().strftime('%m/%d/%Y')}, None, 'postDate',entry['StationName'].replace("-","")))
            else:
                this.label4["text"] = "No Credentials in Settings"
        else:
            print('No FC detected')
            #this.label4["text"] = 'Docked to ' + entry['StationName']
    if entry['event'] == 'FSDJump':
        #Jumped into new System
        if any(x['callsign'].lower() == entry['StarSystem'].lower() for x in this.FCs):
            print('Visted System in List')
            config.set('edpscmder', cmdr)
            cred = credentials(config.get("edpscmder"))
            if cred:
                headers = {'Content-Type': 'application/json"'}
                this.queueEDPS.put(('https://edps-api.d3develop.com/passports/passport/date',
                                    {'cmder_name': cmdr, 'api_key': cred,
                                     'callsign': entry['StarSystem'],
                                     'date': datetime.today().strftime('%m/%d/%Y')}, None, 'postDate',
                                    entry['StarSystem']))
            else:
                this.label4["text"] = "No Credentials in Settings"

def update_Edps_Console(event=None):
    wrapper = textwrap.TextWrapper(width=35)
    this.label4["text"] = wrapper.fill(text=this.edpsConsoleMessage)

def update_Edps_Passport_Count(event=None):
    this.label2["text"] = this.edpsPassportCountMessage

def set_state_frame_childs(frame, state):
    for child in frame.winfo_children():
        if child.winfo_class() in ("TFrame", "Frame", "Labelframe"):
            set_state_frame_childs(child, state)
        else:
            child["state"] = state