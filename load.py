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

if __debug__:
    from traceback import print_exc

_TIMEOUT = 20
_EDPSAPPVERSION = "0.2"

this = sys.modules[__name__]  # For holding module globals
#this.session = requests.Session()
this.queueEDPS = Queue()
this.label2 = None
this.label4 = None

try:
    from config import config
except ImportError:
    config = dict()


def plugin_start3(plugin_dir):
   """
   Load this plugin into EDMC
   """
   #Set Default FC List
   this.FCs = [{"number":1,"name":"DSSA Sleeper Service","callsign_formatted":"TFF-34Z","callsign":"TFF34Z","system":"Oorb Broae DF-A e6","patch_url":"https://imgur.com/RMUeVxe.png","location_x":2123.65625,"location_y":29718.625,"lat":2485.93125,"lng":2356.182813,"patch_credit":""},{"number":2,"name":"DSSA Distant Worlds","callsign_formatted":"V2W-85Z","callsign":"V2W85Z","system":"Beagle Point","patch_url":"https://imgur.com/VrbEIrV.png","location_x":-1111.5625,"location_y":65269.75,"lat":4263.4875,"lng":2194.421875,"patch_credit":""},{"number":4,"name":"NECFC Huginn","callsign_formatted":"Q9V-W3G","callsign":"Q9VW3G","system":"Schee Flyi DN-I D10-8604","patch_url":"https://imgur.com/AP5W7Yg.png","location_x":-4773.59375,"location_y":22859,"lat":2142.95,"lng":2011.320313,"patch_credit":""},{"number":5,"name":"DSSA Gam Nine","callsign_formatted":"X9Z-4XG","callsign":"X9Z4XG","system":"PLA AICK GA-A e1","patch_url":"https://imgur.com/DEdHWUq.png","location_x":35413.159,"location_y":9181.96875,"lat":1459.098438,"lng":4020.65795,"patch_credit":""},{"number":7,"name":"NECFC Muninn","callsign_formatted":"J4F-01X","callsign":"J4F01X","system":"SCAULOU SZ-M D8-911","patch_url":"https://imgur.com/Ei4ai2x.png","location_x":-6759.34375,"location_y":29166.1875,"lat":2458.309375,"lng":1912.032813,"patch_credit":""},{"number":8,"name":"DSSA Ironside","callsign_formatted":"QLZ-NQZ","callsign":"QLZNQZ","system":"PLAA AEC RY-B B41-1","patch_url":"https://imgur.com/aleAP7f.png","location_x":7881.59375,"location_y":7500.6875,"lat":1375.034375,"lng":2644.079688,"patch_credit":""},{"number":10,"name":"DSSA Black Adder Port","callsign_formatted":"QHM-51Z","callsign":"QHM51Z","system":"Eembaitl DL-Y d13","patch_url":"https://imgur.com/gQEPA3r.png","location_x":29456.5,"location_y":29782.0625,"lat":2489.103125,"lng":3722.825,"patch_credit":""},{"number":11,"name":"DSSA Pride of Tel Fyr","callsign_formatted":"K8N-LTJ","callsign":"K8NLTJ","system":"Aiphaisty OD-T e3-4","patch_url":"https://imgur.com/UyR4izM.png","location_x":-17932.5625,"location_y":34160.28125,"lat":2708.014063,"lng":1353.371875,"patch_credit":""},{"number":12,"name":"DSSA Gene Roddenberry","callsign_formatted":"K1F-32K","callsign":"K1F32K","system":"Loijoae ZV-T c17-0","patch_url":"https://imgur.com/p4dTzxB.png","location_x":23595.90625,"location_y":32990.90625,"lat":2649.545313,"lng":3429.795313,"patch_credit":""},{"number":14,"name":"[EDS] DSSA Enigma","callsign_formatted":"QBN-LKW","callsign":"QBNLKW","system":"Hypuejaa RT-Q E5-83","patch_url":"https://imgur.com/5BsWITB.png","location_x":-11653.59375,"location_y":28123.03125,"lat":2406.151563,"lng":1667.320313,"patch_credit":""},{"number":15,"name":"DSSA Nest","callsign_formatted":"KLL-1KJ","callsign":"KLL1KJ","system":"Uctailts UD-S d4-3","patch_url":"https://imgur.com/2QS4yzx.png","location_x":27648.65625,"location_y":42867.65625,"lat":3143.382813,"lng":3632.432813,"patch_credit":""},{"number":16,"name":"[IGAU] Paradox Destiny","callsign_formatted":"K3K-L1N","callsign":"K3KL1N","system":"Prai Hypoo TX-B d4","patch_url":"https://imgur.com/OcvTxv2.png","location_x":-9214.875,"location_y":7908.21875,"lat":1395.410938,"lng":1789.25625,"patch_credit":""},{"number":17,"name":"DSSA Dryman's Hope","callsign_formatted":"QHW-0XX","callsign":"QHW0XX","system":"Eock Prau WD-T d3-1","patch_url":"https://imgur.com/pnwSIxT.png","location_x":26230.03125,"location_y":19811,"lat":1990.55,"lng":3561.501563,"patch_credit":""},{"number":21,"name":"DSSA Chrysaetos Refuge","callsign_formatted":"WNB-W5Z","callsign":"WNBW5Z","system":"Xothae MA-A d2","patch_url":"https://imgur.com/T4MSbzR.png","location_x":-36207.90625,"location_y":29671.40625,"lat":2483.570313,"lng":439.6046875,"patch_credit":""},{"number":22,"name":"CCN Tranquility","callsign_formatted":"FZK-L9Z","callsign":"FZKL9Z","system":"Phreia Flyou FG-V d3-116","patch_url":"https://imgur.com/IHjTCjw.png","location_x":-14327,"location_y":23596.875,"lat":2179.84375,"lng":1533.65,"patch_credit":""},{"number":23,"name":"DSSA Buurian Anchorage","callsign_formatted":"K5T-56Q","callsign":"K5T56Q","system":"Dryau Ausms KG-Y E3390","patch_url":"https://imgur.com/RvbkorE.png","location_x":-1523.75,"location_y":20976.59375,"lat":2048.829688,"lng":2173.8125,"patch_credit":"Rheeney"},{"number":27,"name":"HSRC Limpet's Call","callsign_formatted":"V0G-2VY","callsign":"V0G2VY","system":"Phroi Bluae QI-T e3-3454","patch_url":"https://imgur.com/93kPjvk.png","location_x":-681.09375,"location_y":34219.34375,"lat":2710.967188,"lng":2215.945313,"patch_credit":""},{"number":28,"name":"[IGAU] Deep Space 12","callsign_formatted":"K8Y-85J","callsign":"K8Y85J","system":"Flyoo Prao JC-B d1-5","patch_url":"https://imgur.com/RuehpqP.png","location_x":22469.8125,"location_y":40008.34375,"lat":3000.417188,"lng":3373.490625,"patch_credit":""},{"number":29,"name":"[IGAU] Deep Space 27","callsign_formatted":"KNX-2KY","callsign":"KNX2KY","system":"Eishoqs QM-J C10-1","patch_url":"https://imgur.com/w4ZIQkn.png","location_x":-27067.9375,"location_y":17297.71875,"lat":1864.885938,"lng":896.603125,"patch_credit":""},{"number":30,"name":"DSSA Reginleif","callsign_formatted":"X5W-63Z","callsign":"X5W63Z","system":"Dryau Aec JF-A d11","patch_url":"https://imgur.com/jy5HFF0.png","location_x":8552.28125,"location_y":-12582,"lat":370.9,"lng":2677.614063,"patch_credit":""},{"number":31,"name":"DSSA Unicorns Rest","callsign_formatted":"X5G-6HZ","callsign":"X5G6HZ","system":"MYOANGEIA AT-U D2-244","patch_url":"https://imgur.com/oTBWZok.png","location_x":-12989.9375,"location_y":41429.0625,"lat":3071.453125,"lng":1600.503125,"patch_credit":""},{"number":33,"name":"DSSA Ronin","callsign_formatted":"V1Q-95G","callsign":"V1Q95G","system":"Phipoea WK-E d12-1374","patch_url":"https://imgur.com/QSHElSe.png","location_x":-497.09375,"location_y":28184.875,"lat":2409.24375,"lng":2225.145313,"patch_credit":""},{"number":36,"name":"DSSA Flamingo","callsign_formatted":"XBJ-GVQ","callsign":"XBJGVQ","system":"flyai pre hr-v c2-1","patch_url":"https://imgur.com/YRrSFEP.png","location_x":-22903.09375,"location_y":40017.09375,"lat":3000.854688,"lng":1104.845313,"patch_credit":""},{"number":37,"name":"[IGAU] The Lemon Drop","callsign_formatted":"XFK-0TW","callsign":"XFK0TW","system":"Gleeque HW-N e6-149","patch_url":"https://imgur.com/AFF1zgv.png","location_x":4995.59375,"location_y":25791.9375,"lat":2289.596875,"lng":2499.779688,"patch_credit":""},{"number":38,"name":"KTL Frontier Sanctuary","callsign_formatted":"J2W-5XF","callsign":"J2W5XF","system":"Syreadiae JX-F c0","patch_url":"https://imgur.com/w6BIQ43.png","location_x":-9529.4375,"location_y":-7428.4375,"lat":628.578125,"lng":1773.528125,"patch_credit":""},{"number":40,"name":"DSSA Argonautica","callsign_formatted":"KBB-34Z","callsign":"KBB34Z","system":"FEDGIE FN-Q D6-45","patch_url":"https://imgur.com/GmVIxWA.png","location_x":13322.6875,"location_y":-3035.71875,"lat":848.2140625,"lng":2916.134375,"patch_credit":""},{"number":41,"name":"DSSA Tartarus","callsign_formatted":"XBQ-LVV","callsign":"XBQLVV","system":"Eishaw DB-W E2-0","patch_url":"https://imgur.com/jy5HFF0.png","location_x":4587.03125,"location_y":59589.09375,"lat":3979.454688,"lng":2479.351563,"patch_credit":""},{"number":43,"name":"DSSA Andromeda Calling","callsign_formatted":"JFH-GXB","callsign":"JFHGXB","system":"Byeia Thoea CA-A d2","patch_url":"https://imgur.com/Ug3tSnQ.png","location_x":-33157.1875,"location_y":2846.8125,"lat":1142.340625,"lng":592.140625,"patch_credit":""},{"number":44,"name":"DSSA Kraut","callsign_formatted":"J4T-0QB","callsign":"J4T0QB","system":"NGC 3199 Sector XJ-A D10","patch_url":"https://imgur.com/SAVikAI.png","location_x":14544.0625,"location_y":3489.375,"lat":1174.46875,"lng":2977.203125,"patch_credit":""},{"number":46,"name":"DSSA Callisto","callsign_formatted":"KBZ-B0Z","callsign":"KBZB0Z","system":"Phraa Blao HO-S c20-7","patch_url":"https://imgur.com/Ut3KaIj.png","location_x":11261.21875,"location_y":34409.5625,"lat":2720.478125,"lng":2813.060938,"patch_credit":"Gnauty"},{"number":47,"name":"DSSA Hecate's Grace","callsign_formatted":"J8L-41H","callsign":"J8L41H","system":"EX CANCRI","patch_url":"https://imgur.com/ntliWMd.png","location_x":1412.21875,"location_y":-1967.34375,"lat":901.6328125,"lng":2320.610938,"patch_credit":""},{"number":48,"name":"DSSA Aristarchos","callsign_formatted":"J6M-G2L","callsign":"J6MG2L","system":"Eocs Aihm XX-U d2-6","patch_url":"https://imgur.com/t7hwChZ.png","location_x":22759.375,"location_y":-11033.40625,"lat":448.3296875,"lng":3387.96875,"patch_credit":""},{"number":51,"name":"DSSA Sésame","callsign_formatted":"K3F-L0V","callsign":"K3FL0V","system":"Floarps PI-B e2","patch_url":"https://imgur.com/VEtayXu.png","location_x":-859.90625,"location_y":14426.34375,"lat":1721.317188,"lng":2207.004688,"patch_credit":""},{"number":53,"name":"CLB Voqooway","callsign_formatted":"J3G-3QZ","callsign":"J3G3QZ","system":"Voqooe BI-H D11-864","patch_url":"https://imgur.com/lqBtGyo.png","location_x":-4770.75,"location_y":17819.75,"lat":1890.9875,"lng":2011.4625,"patch_credit":""},{"number":58,"name":"DSSA Bougainville","callsign_formatted":"X8N-0KL","callsign":"X8N0KL","system":"Eock Bluae QL-X c1-1","patch_url":"https://imgur.com/YeCRmhG.png","location_x":16025.21875,"location_y":27206.59375,"lat":2360.329688,"lng":3051.260938,"patch_credit":""},{"number":61,"name":"DSSA[TFGI]Kitty Corner","callsign_formatted":"X3M-7HY","callsign":"X3M7HY","system":"DROETT XD-T D3-22","patch_url":"https://imgur.com/vg5bCcj.png","location_x":26305.84375,"location_y":15908.40625,"lat":1795.420313,"lng":3565.292188,"patch_credit":""},{"number":62,"name":"DSSA - Stellar Oasis","callsign_formatted":"J8Y-8HT","callsign":"J8Y8HT","system":"IHAB JI-B D13-16","patch_url":"https://imgur.com/aMO7oK6.png","location_x":23399.1875,"location_y":46161.3125,"lat":3308.065625,"lng":3419.959375,"patch_credit":""},{"number":65,"name":"DSSA King's Pass","callsign_formatted":"FHH-7QZ","callsign":"FHH7QZ","system":"Nuekea RP-M D8-161","patch_url":"https://imgur.com/tWteOjb.png","location_x":9475.5,"location_y":13771.21875,"lat":1688.560938,"lng":2723.775,"patch_credit":""},{"number":66,"name":"Explorer's Bar & Grill","callsign_formatted":"Q8J-0HW","callsign":"Q8J0HW","system":"Hypau Aec IO-Z d13-0","patch_url":"https://imgur.com/IcRIHpH.png","location_x":26874.21875,"location_y":-7473.59375,"lat":626.3203125,"lng":3593.710938,"patch_credit":""},{"number":72,"name":"DSSA Nereus' Deep","callsign_formatted":"MNG-B0Z","callsign":"MNGB0Z","system":"Engopr YH-L B14-2","patch_url":"https://imgur.com/9kePniS.png","location_x":24463.625,"location_y":3088.71875,"lat":1154.435938,"lng":3473.18125,"patch_credit":""},{"number":73,"name":"DSSA Alvin's Rest","callsign_formatted":"VHM-2VZ","callsign":"VHM2VZ","system":"BLIA CHRAEI QU-M C21-0","patch_url":"https://imgur.com/OUEMATh.png","location_x":13378.59375,"location_y":53634.03125,"lat":3681.701563,"lng":2918.929688,"patch_credit":""},{"number":77,"name":"DSSA Skarapa","callsign_formatted":"K6W-WQY","callsign":"K6WWQY","system":"Oob Aeb XI-X c28-0","patch_url":"https://imgur.com/SoENUdf.png","location_x":-11428.21875,"location_y":-12613.96875,"lat":369.3015625,"lng":1678.589063,"patch_credit":""},{"number":82,"name":"DSSA Leo's Vision","callsign_formatted":"KLB-44V","callsign":"KLB44V","system":"Hyueths HS-H d11-5","patch_url":"https://imgur.com/DCNp1g2.png","location_x":-93.9375,"location_y":-12836.96875,"lat":358.1515625,"lng":2245.303125,"patch_credit":""},{"number":84,"name":"DSSA Artemis Rest","callsign_formatted":"K1B-75W","callsign":"K1B75W","system":"Synuefuae CM-J d10-42","patch_url":"https://imgur.com/ekX5JIp.png","location_x":6233.65625,"location_y":-113.6875,"lat":994.315625,"lng":2561.682813,"patch_credit":""},{"number":85,"name":"DSSA Nostromo","callsign_formatted":"JBG-4QZ","callsign":"JBG4QZ","system":"MYCAPP PJ-T B6-1","patch_url":"https://imgur.com/E6Ghtqk.png","location_x":27236,"location_y":24681.65625,"lat":2234.082813,"lng":3611.8,"patch_credit":""},{"number":86,"name":"Lost Sanity","callsign_formatted":"KHX-NKW","callsign":"KHXNKW","system":"PHRAE DRYIAE AM-J D10-0","patch_url":"https://imgur.com/hhxnCdy.png","location_x":20102.6875,"location_y":-14260.3125,"lat":286.984375,"lng":3255.134375,"patch_credit":""},{"number":87,"name":"Will's Haven","callsign_formatted":"Q9N-12F","callsign":"Q9N12F","system":"BYEEQUE ST-A B4-4","patch_url":"https://imgur.com/P29NGhP.png","location_x":-25007.28125,"location_y":24627.375,"lat":2231.36875,"lng":999.6359375,"patch_credit":""},{"number":88,"name":"Four Corners Monument","callsign_formatted":"X4J-85Z","callsign":"X4J85Z","system":"PLOEA AUSCS ZA-A c16","patch_url":"https://imgur.com/Rj6WIS0.png","location_x":3534.4375,"location_y":39901.0625,"lat":2995.053125,"lng":2426.721875,"patch_credit":""},{"number":90,"name":"DSSA Jolly Roger","callsign_formatted":"K4Z-B7Z","callsign":"K4ZB7Z","system":"Ooctarbs NR-W e1-0","patch_url":"https://imgur.com/OFXSG2T.png","location_x":12578.53125,"location_y":59505.46875,"lat":3975.273438,"lng":2878.926563,"patch_credit":""},{"number":91,"name":"DSSA Nova Blues","callsign_formatted":"KFX-W3Z","callsign":"KFXW3Z","system":"Eord Prau ZK-N d7-711","patch_url":"https://imgur.com/v1WL1Gf.png","location_x":5832.03125,"location_y":20083.5,"lat":2004.175,"lng":2541.601563,"patch_credit":""},{"number":92,"name":"[ISF] Mandy's Rest","callsign_formatted":"B6L-L0Z","callsign":"B6LL0Z","system":"PLAE BROAE DL-P D5-0","patch_url":"https://imgur.com/0hwGJsx.png","location_x":27225.75,"location_y":50621.09375,"lat":3531.054688,"lng":3611.2875,"patch_credit":""},{"number":93,"name":"DSSA Manatee","callsign_formatted":"J4W-W8K","callsign":"J4WW8K","system":"Eolls Graae TA-K c10-5","patch_url":"https://imgur.com/RqapNhW.png","location_x":-18792.5625,"location_y":30120.3125,"lat":2506.015625,"lng":1310.371875,"patch_credit":""},{"number":94,"name":"Hayholt","callsign_formatted":"JZQ-GXZ","callsign":"JZQGXZ","system":"Aiphaitt AA-A h7","patch_url":"https://imgur.com/2uOXltL.png","location_x":-5034.875,"location_y":34009,"lat":2700.45,"lng":1998.25625,"patch_credit":""},{"number":95,"name":"Galactic Unity","callsign_formatted":"QNY-BQN","callsign":"QNYBQN","system":"Byoi Aowsy XD-L b40-0","patch_url":"https://imgur.com/yrVqpWY.png","location_x":-5466.90625,"location_y":44603.40625,"lat":3230.170313,"lng":1976.654688,"patch_credit":""},{"number":97,"name":"DSSA Totoro","callsign_formatted":"NNW-23Z","callsign":"NNW23Z","system":"GREAE PHOEA XF-D D13-507","patch_url":"https://imgur.com/5ALa9K5.png","location_x":4826.25,"location_y":16702.15625,"lat":1835.107813,"lng":2491.3125,"patch_credit":""},{"number":100,"name":"DSSA Solsen's Alastor","callsign_formatted":"KOY-LKF","callsign":"KOYLKF","system":"Flyoo Groa SO-Z e0","patch_url":"https://imgur.com/kfwzDMH.png","location_x":-26482.4375,"location_y":50335.125,"lat":3516.75625,"lng":925.878125,"patch_credit":""},{"number":103,"name":"DSSA Wanderer's Rest","callsign_formatted":"NNT-W4Z","callsign":"NNTW4Z","system":"FLYAI PRE HR-V C2-1","patch_url":"https://imgur.com/VScCgTh.png","location_x":-22903.09375,"location_y":40017.09375,"lat":3000.854688,"lng":1104.845313,"patch_credit":""},{"number":105,"name":"RR-DSSA Rocksteady","callsign_formatted":"KBH-T2Z","callsign":"KBHT2Z","system":"PROOE HYPUE FH-U E3-2","patch_url":"https://imgur.com/cYU2PLO.png","location_x":519.625,"location_y":8671.5,"lat":1433.575,"lng":2275.98125,"patch_credit":""},{"number":108,"name":"The Helix","callsign_formatted":"X0F-N1J","callsign":"X0FN1J","system":"Phrae Prau NY-Y d1-15","patch_url":"https://imgur.com/uY15ule.png","location_x":29786.75,"location_y":26047.875,"lat":2302.39375,"lng":3739.3375,"patch_credit":""},{"number":109,"name":"DSSA Erikson's Gateway","callsign_formatted":"X6Z-06M","callsign":"X6Z06M","system":"Hypoe Bloae KZ-Z c16-6","patch_url":"https://imgur.com/DNnMkHV.png","location_x":-31101.71875,"location_y":32944.625,"lat":2647.23125,"lng":694.9140625,"patch_credit":""},{"number":110,"name":"TFS Carpe Vinum","callsign_formatted":"TZN-L3Z","callsign":"TZNL3Z","system":"Byae Aowsy GR-N d6-52","patch_url":"https://imgur.com/Zftle7r.png","location_x":14407.625,"location_y":44312.59375,"lat":3215.629688,"lng":2970.38125,"patch_credit":""},{"number":112,"name":"DSSA Pegasus","callsign_formatted":"K6V-G3B","callsign":"K6VG3B","system":"Hyuqau WU-N c23-79","patch_url":"https://imgur.com/pm7NLAp.png","location_x":-925.25,"location_y":35791.75,"lat":2789.5875,"lng":2203.7375,"patch_credit":""},{"number":123,"name":"DSSA Heart of Gold","callsign_formatted":"Q9G-9TL","callsign":"Q9G9TL","system":"Cloomeia FG-Y e95","patch_url":"https://imgur.com/7i4UpGL.png","location_x":11719.15625,"location_y":24717.375,"lat":2235.86875,"lng":2835.957813,"patch_credit":""},{"number":124,"name":"Michelle’s Legacy","callsign_formatted":"QHY-G8J","callsign":"QHYG8J","system":"Eorm Chreou XS-U d2-14","patch_url":"https://imgur.com/fhfPWND.png","location_x":-31117.15625,"location_y":27367,"lat":2368.35,"lng":694.1421875,"patch_credit":""},{"number":125,"name":"Rouge One","callsign_formatted":"X3X-W9G","callsign":"X3XW9G","system":"MYRIELK PJ-Y C1-4363","patch_url":"https://imgur.com/Ot1dWZZ.png","location_x":8.375,"location_y":24654,"lat":2232.7,"lng":2250.41875,"patch_credit":""},{"number":126,"name":"TWITCHTVSOMDY","callsign_formatted":"KZQ-24Q","callsign":"KZQ24Q","system":"Lyed YJ-I d9-0","patch_url":"https://imgur.com/EyN8Sfi.png","location_x":11007.46875,"location_y":-16899.75,"lat":155.0125,"lng":2800.373438,"patch_credit":""},{"number":130,"name":"Emerald Tablet","callsign_formatted":"M2Z-44Z","callsign":"M2Z44Z","system":"Eactaisky IR-N E6-2","patch_url":"https://imgur.com/efCgsew.png","location_x":-19483.84375,"location_y":43610.375,"lat":3180.51875,"lng":1275.807813,"patch_credit":""},{"number":132,"name":"DSSA - Void Crusader","callsign_formatted":"KFF-86M","callsign":"KFF86M","system":"GREAE PHIO VK-O E6-4343","patch_url":"https://imgur.com/lAFKjmh.png","location_x":1474.875,"location_y":16723.75,"lat":1836.1875,"lng":2323.74375,"patch_credit":""}]


   this.threadEDPS = Thread(target=workerEDPS, name='EDPS worker')
   this.threadEDPS.daemon = True
   this.threadEDPS.start()
   print("ED Passport System Plugin Loading...")
   this.queueEDPS.put(('does not matter',{},None, 'getAppInformation', ""))
   this.queueEDPS.put(('does not matter', {}, None, 'getFCsList',""))
   this.queueEDPS.put(('does not matter', {}, None, 'getPassport',""))

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
                            cred = credentials(config.get("edpscmder"))
                            if cred:
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
                                this.edpsConsoleMessage = 'No credentials'
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
                    time.sleep(3)
                    headers = {'x-api-key': 'bn9oCD5lqp7Yavh3l7VLB4lixo1FI69F2aiOmznB'}
                    r = requests.get('https://www.edps.dev/AppInformation.json', headers=headers, timeout=_TIMEOUT)
                    this.AppInformationEDPS = json.loads(r.text)
                    if r.ok:
                        print('Status is Ok')
                        if this.AppInformationEDPS['EDMCApp'] != _EDPSAPPVERSION:
                            print('EDPS needs to be updated')
                            this.edpsConsoleMessage = 'Outdated Plugin Version - Please Download New Version'
                            this.label4.event_generate('<<edpsUpdateConsoleEvent>>', when="tail")
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
                    if this.edpsCmderName is None:
                        this.edpsConsoleMessage = 'EDPS Started (No API Key)'
                        this.label4.event_generate('<<edpsUpdateConsoleEvent>>', when="tail")
                        this.edpsPassportCountMessage = 'No API Key in Settings'
                        this.label2.event_generate('<<edpsUpdatePassportCountEvent>>', when="tail")
                        retrying = 3
                        break
                    cred = credentials(config.get("edpscmder"))
                    if cred:
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
    this.apikey = nb.Entry(this.edps_frame, textvariable=edpsapikey)
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
    set_state_frame_childs(this.edps_frame, tk.NORMAL)
    this.apikey.delete(0, tk.END)
    if cmdr:
        this.cmdr_text["text"] = cmdr + (is_beta and " [Beta]" or "")
        cred = credentials(config.get("edpscmder"))
        if cred:
            this.apikey.insert(0, cred)
    else:
        this.cmdr_text["text"] = _("None")

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
            emails.append(this.email.get().strip())
            apikeys.append(this.apikey.get().strip())
        config.set("edps_apikeys", apikeys)


def credentials(cmdr):
    # Credentials for cmdr
    if cmdr:
        cmdrs = config.get("edps_cmdrs")
        if not cmdrs:
            # Migrate from single setting, first commander gets the old settings
            cmdrs = [cmdr]
            config.set("edps_cmdrs", cmdrs)
        apikeys = config.get("edps_apikeys")
        if cmdr in cmdrs and apikeys:
            idx = cmdrs.index(cmdr)
            return (apikeys[idx])
    return None

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

def journal_entry(cmdr, is_beta, system, station, entry, state):
    if entry['event'] == 'LoadGame':
        #Adding multi-commander support
        if 'Commander' in entry:
            config.set('edpscmder', entry['Commander'])
            this.queueEDPS.put(('does not matter', {}, None, 'getPassport', ""))
            this.edpsConsoleMessage = 'Welcome Commander ' + entry['Commander'] + '!'
            this.label4.event_generate('<<edpsUpdateConsoleEvent>>', when="tail")
    if entry['event'] == 'Docked':
        # Docking Event Detected
        if entry['StationType'] == 'FleetCarrier' and any(x['callsign_formatted'] == entry['StationName'] for x in this.FCs) and any(y['system'] == entry['StarSystem'] for y in this.FCs):
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