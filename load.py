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
from queue import Queue
from threading import Thread

if __debug__:
    from traceback import print_exc

_TIMEOUT = 20
_APPVERSION = "0.1"

this = sys.modules[__name__]  # For holding module globals
#this.session = requests.Session()
this.queue = Queue()
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
   this.FCs = [{'number': 1, 'name': 'DSSA Sleeper Service', 'callsign': 'TFF34Z', 'callsign_formatted': 'TFF-34Z',
                'patch_url': 'https://imgur.com/RMUeVxe.png', 'system': 'Oorb Broae DF-A e6', 'location_x': 2123.65625,
                'location_y': 29718.625, 'lng': 2356.182813, 'lat': 2485.93125, 'market_id': 3700272128},
               {'number': 2, 'name': 'DSSA Distant Worlds', 'callsign': 'V2W85Z', 'callsign_formatted': 'V2W-85Z',
                'patch_url': 'https://imgur.com/VrbEIrV.png', 'system': 'Beagle Point', 'location_x': -1111.5625,
                'location_y': 65269.75, 'lng': 2194.421875, 'lat': 4263.4875, 'market_id': 3700283136},
               {'number': 4, 'name': 'NECFC Huginn', 'callsign': 'Q9VW3G', 'callsign_formatted': 'Q9V-W3G',
                'patch_url': 'https://imgur.com/AP5W7Yg.png', 'system': 'Schee Flyi DN-I D10-8604',
                'location_x': -4773.59375, 'location_y': 22859, 'lng': 2011.320313, 'lat': 2142.95,
                'market_id': 3702860032},
               {'number': 5, 'name': 'DSSA Gam Nine', 'callsign': 'X9Z4XG', 'callsign_formatted': 'X9Z-4XG',
                'patch_url': 'https://imgur.com/DEdHWUq.png', 'system': 'PLA AICK GA-A e1', 'location_x': 35413.159,
                'location_y': 9181.96875, 'lng': 4020.65795, 'lat': 1459.098438, 'market_id': 3700212224},
               {'number': 7, 'name': 'NECFC Muninn', 'callsign': 'J4F01X', 'callsign_formatted': 'J4F-01X',
                'patch_url': 'https://imgur.com/Ei4ai2x.png', 'system': 'SCAULOU SZ-M D8-911',
                'location_x': -6759.34375, 'location_y': 29166.1875, 'lng': 1912.032813, 'lat': 2458.309375,
                'market_id': 3701640960},
               {'number': 8, 'name': 'DSSA Ironside', 'callsign': 'QLZNQZ', 'callsign_formatted': 'QLZ-NQZ',
                'patch_url': 'https://imgur.com/aleAP7f.png', 'system': 'PLAA AEC RY-B B41-1', 'location_x': 10881.093,
                'location_y': 7500.6875, 'lng': 2794.05465, 'lat': 1375.034375, 'market_id': 3701678848},
               {'number': 10, 'name': 'DSSA Black Adder Port', 'callsign': 'QHM51Z', 'callsign_formatted': 'QHM-51Z',
                'patch_url': 'https://imgur.com/gQEPA3r.png', 'system': 'Eembaitl DL-Y d13', 'location_x': 29456.5,
                'location_y': 29782.0625, 'lng': 3722.825, 'lat': 2489.103125, 'market_id': 3701009152},
               {'number': 11, 'name': 'DSSA Pride of Tel Fyr', 'callsign': 'K8NLTJ', 'callsign_formatted': 'K8N-LTJ',
                'patch_url': 'https://imgur.com/UyR4izM.png', 'system': 'Aiphaisty OD-T e3-4',
                'location_x': -17932.5625, 'location_y': 34160.28125, 'lng': 1353.371875, 'lat': 2708.014063,
                'market_id': 3700054784},
               {'number': 12, 'name': 'DSSA Gene Roddenberry', 'callsign': 'K1F32K', 'callsign_formatted': 'K1F-32K',
                'patch_url': 'https://imgur.com/p4dTzxB.png', 'system': 'Loijoae ZV-T c17-0', 'location_x': 40561.521,
                'location_y': 32990.90625, 'lng': 4278.07605, 'lat': 2649.545313, 'market_id': 3700708608},
               {'number': 14, 'name': '[EDS] DSSA Enigma', 'callsign': 'QBNLKW', 'callsign_formatted': 'QBN-LKW',
                'patch_url': 'https://imgur.com/5BsWITB.png', 'system': 'Hypuejaa RT-Q E5-83',
                'location_x': -11653.59375, 'location_y': 28123.03125, 'lng': 1667.320313, 'lat': 2406.151563,
                'market_id': 3700072960},
               {'number': 15, 'name': 'DSSA Nest', 'callsign': 'KLL1KJ', 'callsign_formatted': 'KLL-1KJ',
                'patch_url': 'https://imgur.com/2QS4yzx.png', 'system': 'Uctailts UD-S d4-3', 'location_x': 27648.65625,
                'location_y': 42867.65625, 'lng': 3632.432813, 'lat': 3143.382813, 'market_id': 3701336576},
               {'number': 16, 'name': '[IGAU] Paradox Destiny', 'callsign': 'K3KL1N', 'callsign_formatted': 'K3K-L1N',
                'patch_url': 'https://imgur.com/OcvTxv2.png', 'system': 'Prai Hypoo TX-B d4', 'location_x': -9214.875,
                'location_y': 7908.21875, 'lng': 1789.25625, 'lat': 1395.410938, 'market_id': 3700204800},
               {'number': 17, 'name': "DSSA Dryman's Hope", 'callsign': 'QHW0XX', 'callsign_formatted': 'QHW-0XX',
                'patch_url': 'https://imgur.com/pnwSIxT.png', 'system': 'Eock Prau WD-T d3-1',
                'location_x': 26230.03125, 'location_y': 19811, 'lng': 3561.501563, 'lat': 1990.55,
                'market_id': 3700577024},
               {'number': 21, 'name': 'DSSA Chrysaetos Refuge', 'callsign': 'WNBW5Z', 'callsign_formatted': 'WNB-W5Z',
                'patch_url': 'https://imgur.com/T4MSbzR.png', 'system': 'Xothae MA-A d2', 'location_x': -36207.90625,
                'location_y': 29671.40625, 'lng': 439.6046875, 'lat': 2483.570313, 'market_id': 3700739328},
               {'number': 22, 'name': 'CCN Tranquility', 'callsign': 'FZKL9Z', 'callsign_formatted': 'FZK-L9Z',
                'patch_url': 'https://imgur.com/IHjTCjw.png', 'system': 'Phreia Flyou FG-V d3-116',
                'location_x': -14327, 'location_y': 23596.875, 'lng': 1533.65, 'lat': 2179.84375,
                'market_id': 3700917504},
               {'number': 23, 'name': 'DSSA Buurian Anchorage', 'callsign': 'K5T56Q', 'callsign_formatted': 'K5T-56Q',
                'patch_url': 'https://imgur.com/RvbkorE.png', 'system': 'Dryau Ausms KG-Y E3390 (Dryau Awesomes)',
                'location_x': -1523.75, 'location_y': 20976.59375, 'lng': 2173.8125, 'lat': 2048.829688,
                'market_id': 3700926208},
               {'number': 27, 'name': "HSRC Limpet's Call", 'callsign': 'V0G2VY', 'callsign_formatted': 'V0G-2VY',
                'patch_url': 'https://imgur.com/93kPjvk.png', 'system': 'Phroi Bluae QI-T e3-3454',
                'location_x': -681.09375, 'location_y': 34219.34375, 'lng': 2215.945313, 'lat': 2710.967188,
                'market_id': 0},
               {'number': 28, 'name': '[IGAU] Deep Space 12', 'callsign': 'K8Y85J', 'callsign_formatted': 'K8Y-85J',
                'patch_url': 'https://imgur.com/RuehpqP.png', 'system': 'Flyoo Prao JC-B d1-5',
                'location_x': 22469.8125, 'location_y': 40008.34375, 'lng': 3373.490625, 'lat': 3000.417188,
                'market_id': 3700273408},
               {'number': 29, 'name': '[IGAU] Deep Space 27', 'callsign': 'KNX2KY', 'callsign_formatted': 'KNX-2KY',
                'patch_url': 'https://imgur.com/w4ZIQkn.png', 'system': 'Eishoqs QM-J C10-1', 'location_x': -27067.9375,
                'location_y': 17297.71875, 'lng': 896.603125, 'lat': 1864.885938, 'market_id': 3701199360},
               {'number': 30, 'name': 'DSSA Reginleif', 'callsign': 'X5W63Z', 'callsign_formatted': 'X5W-63Z',
                'patch_url': 'https://imgur.com/jy5HFF0.png', 'system': 'Dryau Aec JF-A d11', 'location_x': 8552.28125,
                'location_y': -12582, 'lng': 2677.614063, 'lat': 370.9, 'market_id': 3700106496},
               {'number': 31, 'name': 'DSSA Unicorns Rest', 'callsign': 'X5G6HZ', 'callsign_formatted': 'X5G-6HZ',
                'patch_url': 'https://imgur.com/oTBWZok.png', 'system': 'The Conduit', 'location_x': 757.125,
                'location_y': -96.0625, 'lng': 2287.85625, 'lat': 995.196875, 'market_id': 3700080128},
               {'number': 33, 'name': 'DSSA Ronin', 'callsign': 'V1Q95G', 'callsign_formatted': 'V1Q-95G',
                'patch_url': 'https://imgur.com/QSHElSe.png', 'system': 'Phipoea WK-E d12-1374',
                'location_x': -497.09375, 'location_y': 28184.875, 'lng': 2225.145313, 'lat': 2409.24375,
                'market_id': 3700911872},
               {'number': 36, 'name': 'DSSA Flamingo', 'callsign': 'XBJGVQ', 'callsign_formatted': 'XBJ-GVQ',
                'patch_url': 'https://imgur.com/Cpp0tcf.png', 'system': 'flyai pre hr-v c2-1',
                'location_x': -22903.09375, 'location_y': 40017.09375, 'lng': 1104.845313, 'lat': 3000.854688,
                'market_id': 3700305920},
               {'number': 37, 'name': '[IGAU] The Lemon Drop', 'callsign': 'XFK0TW', 'callsign_formatted': 'XFK-0TW',
                'patch_url': 'https://imgur.com/AFF1zgv.png', 'system': 'Gleeque HW-N e6-149', 'location_x': 4995.59375,
                'location_y': 25791.9375, 'lng': 2499.779688, 'lat': 2289.596875, 'market_id': 3700047616},
               {'number': 38, 'name': 'KTL Frontier Sanctuary', 'callsign': 'J2W5XF', 'callsign_formatted': 'J2W-5XF',
                'patch_url': 'https://imgur.com/w6BIQ43.png', 'system': 'Syreadiae JX-F c0', 'location_x': 12082.881,
                'location_y': -7428.4375, 'lng': 2854.14405, 'lat': 628.578125, 'market_id': 3700367104},
               {'number': 40, 'name': 'DSSA Argonautica', 'callsign': 'Y54P6Z', 'callsign_formatted': 'Y54-P6Z',
                'patch_url': 'https://imgur.com/GmVIxWA.png', 'system': 'FEDGIE FN-Q D6-45', 'location_x': 13322.6875,
                'location_y': -3035.71875, 'lng': 2916.134375, 'lat': 848.2140625, 'market_id': 3700261376},
               {'number': 41, 'name': 'DSSA Tartarus', 'callsign': 'XBQLVV', 'callsign_formatted': 'XBQ-LVV',
                'patch_url': 'https://imgur.com/jy5HFF0.png', 'system': 'Eishaw DB-W E2-0', 'location_x': 4587.03125,
                'location_y': 59589.09375, 'lng': 2479.351563, 'lat': 3979.454688, 'market_id': 3700110336},
               {'number': 43, 'name': 'DSSA Andromeda Calling', 'callsign': 'JFHGXB', 'callsign_formatted': 'JFH-GXB',
                'patch_url': 'https://imgur.com/Ug3tSnQ.png', 'system': 'Byeia Thoea CA-A d2',
                'location_x': -33157.1875, 'location_y': 2846.8125, 'lng': 592.140625, 'lat': 1142.340625,
                'market_id': 3700147200},
               {'number': 44, 'name': 'DSSA Kraut', 'callsign': 'J4T0QB', 'callsign_formatted': 'J4T-0QB',
                'patch_url': 'https://imgur.com/SAVikAI.png', 'system': 'NGC 3199 Sector XJ-A D10',
                'location_x': 14544.0625, 'location_y': 3489.375, 'lng': 2977.203125, 'lat': 1174.46875,
                'market_id': 3700419072},
               {'number': 46, 'name': 'DSSA Callisto', 'callsign': 'KBZB0Z', 'callsign_formatted': 'KBZ-B0Z',
                'patch_url': 'https://imgur.com/Ut3KaIj.png', 'system': 'Phraa Blao HO-S c20-7',
                'location_x': 11261.21875, 'location_y': 34409.5625, 'lng': 2813.060938, 'lat': 2720.478125,
                'market_id': 3700268288},
               {'number': 47, 'name': "DSSA Hecate's Grace", 'callsign': 'J8L41H', 'callsign_formatted': 'J8L-41H',
                'patch_url': 'https://imgur.com/ntliWMd.png', 'system': 'EX CANCRI', 'location_x': 1412.21875,
                'location_y': -1967.34375, 'lng': 2320.610938, 'lat': 901.6328125, 'market_id': 3703559424},
               {'number': 48, 'name': 'DSSA Aristarchos', 'callsign': 'J6MG2L', 'callsign_formatted': 'J6M-G2L',
                'patch_url': 'https://imgur.com/t7hwChZ.png', 'system': 'Eocs Aihm XX-U d2-6', 'location_x': 22759.375,
                'location_y': -11033.40625, 'lng': 3387.96875, 'lat': 448.3296875, 'market_id': 3700216064},
               {'number': 51, 'name': 'DSSA Sesame', 'callsign': 'K3FL0V', 'callsign_formatted': 'K3F-L0V',
                'patch_url': 'https://imgur.com/VEtayXu.png', 'system': 'Floarps PI-B e2', 'location_x': -859.90625,
                'location_y': 14426.34375, 'lng': 2207.004688, 'lat': 1721.317188, 'market_id': 3700075776},
               {'number': 53, 'name': 'CLB Voqooway', 'callsign': 'J3G3QZ', 'callsign_formatted': 'J3G-3QZ',
                'patch_url': 'https://imgur.com/lqBtGyo.png', 'system': 'Voqooe BI-H D11-864', 'location_x': -4770.75,
                'location_y': 17819.75, 'lng': 2011.4625, 'lat': 1890.9875, 'market_id': 3700116224},
               {'number': 58, 'name': 'DSSA Bougainville', 'callsign': 'X8N0KL', 'callsign_formatted': 'X8N-0KL',
                'patch_url': 'https://imgur.com/YeCRmhG.png', 'system': 'Eock Bluae QL-X c1-1',
                'location_x': 16025.21875, 'location_y': 27206.59375, 'lng': 3051.260938, 'lat': 2360.329688,
                'market_id': 3700243456},
               {'number': 61, 'name': 'DSSA[TFGI]Kitty Corner', 'callsign': 'X3M7HY', 'callsign_formatted': 'X3M-7HY',
                'patch_url': 'https://imgur.com/vg5bCcj.png', 'system': 'DROETT XD-T D3-22', 'location_x': 26305.84375,
                'location_y': 15908.40625, 'lng': 3565.292188, 'lat': 1795.420313, 'market_id': 3700625920},
               {'number': 62, 'name': 'DSSA - Stellar Oasis', 'callsign': 'J8Y8HT', 'callsign_formatted': 'J8Y-8HT',
                'patch_url': 'https://imgur.com/aMO7oK6.png', 'system': 'IHAB JI-B D13-16', 'location_x': 23399.1875,
                'location_y': 46161.3125, 'lng': 3419.959375, 'lat': 3308.065625, 'market_id': 3700071424},
               {'number': 65, 'name': "DSSA King's Pass", 'callsign': 'FHH7QZ', 'callsign_formatted': 'FHH-7QZ',
                'patch_url': 'https://imgur.com/tWteOjb.png', 'system': 'Nuekea RP-M D8-161', 'location_x': 9475.5,
                'location_y': 13771.21875, 'lng': 2723.775, 'lat': 1688.560938, 'market_id': 3700507904},
               {'number': 66, 'name': "Explorer's Bar & Grill", 'callsign': 'Q8J0HW', 'callsign_formatted': 'Q8J-0HW',
                'patch_url': 'https://imgur.com/IcRIHpH.png', 'system': 'Hypau Aec IO-Z d13-0', 'location_x': 27894.06,
                'location_y': -7473.59375, 'lng': 3644.703, 'lat': 626.3203125, 'market_id': 3700718848},
               {'number': 72, 'name': "DSSA Nereus' Deep", 'callsign': 'MNGB0Z', 'callsign_formatted': 'MNG-B0Z',
                'patch_url': 'https://imgur.com/9kePniS.png', 'system': 'Engopr YH-L B14-2', 'location_x': 24463.625,
                'location_y': 3088.71875, 'lng': 3473.18125, 'lat': 1154.435938, 'market_id': 3700088576},
               {'number': 73, 'name': "DSSA Alvin's Rest", 'callsign': 'VHM2VZ', 'callsign_formatted': 'VHM-2VZ',
                'patch_url': 'https://imgur.com/OUEMATh.png', 'system': 'BLIA CHRAEI QU-M C21-0',
                'location_x': 13378.59375, 'location_y': 53634.03125, 'lng': 2918.929688, 'lat': 3681.701563,
                'market_id': 3700942592},
               {'number': 77, 'name': 'DSSA Skarapa', 'callsign': 'K6WWQY', 'callsign_formatted': 'K6W-WQY',
                'patch_url': 'https://imgur.com/SoENUdf.png', 'system': 'Oob Aeb XI-X c28-0',
                'location_x': -11428.21875, 'location_y': -12613.96875, 'lng': 1678.589063, 'lat': 369.3015625,
                'market_id': 3701239808},
               {'number': 82, 'name': "DSSA Leo's Vision", 'callsign': 'KLB44V', 'callsign_formatted': 'KLB-44V',
                'patch_url': 'https://imgur.com/2v1FtmL.png', 'system': "Hyueths HS-H d11-5 (The Twins' Garden)",
                'location_x': -93.9375, 'location_y': -12836.96875, 'lng': 2245.303125, 'lat': 358.1515625,
                'market_id': 3702451968},
               {'number': 84, 'name': 'DSSA Artemis Rest', 'callsign': 'K1B75W', 'callsign_formatted': 'K1B-75W',
                'patch_url': 'https://imgur.com/ekX5JIp.png', 'system': 'Synuefuae CM-J d10-42',
                'location_x': 6233.65625, 'location_y': -113.6875, 'lng': 2561.682813, 'lat': 994.315625,
                'market_id': 3701056512},
               {'number': 85, 'name': 'DSSA Nostromo', 'callsign': 'JBG4QZ', 'callsign_formatted': 'JBG-4QZ',
                'patch_url': 'https://imgur.com/E6Ghtqk.png', 'system': 'MYCAPP PJ-T B6-1', 'location_x': 36762.465,
                'location_y': 24681.65625, 'lng': 4088.12325, 'lat': 2234.082813, 'market_id': 3700434688},
               {'number': 86, 'name': 'Lost Sanity', 'callsign': 'KHXNKW', 'callsign_formatted': 'KHX-NKW',
                'patch_url': 'https://imgur.com/hhxnCdy.png', 'system': 'PHRAE DRYIAE AM-J D10-0',
                'location_x': 20102.6875, 'location_y': -14260.3125, 'lng': 3255.134375, 'lat': 286.984375,
                'market_id': 3701242112},
               {'number': 87, 'name': "Will's Haven", 'callsign': 'Q9N12F', 'callsign_formatted': 'Q9N-12F',
                'patch_url': 'https://imgur.com/P29NGhP.png', 'system': 'BYEEQUE ST-A B4-4', 'location_x': -25007.28125,
                'location_y': 24627.375, 'lng': 999.6359375, 'lat': 2231.36875, 'market_id': 3700338944},
               {'number': 88, 'name': 'Four Corners Monument', 'callsign': 'X4J85Z', 'callsign_formatted': 'X4J-85Z',
                'patch_url': 'https://imgur.com/Rj6WIS0.png', 'system': 'PLOEA AUSCS ZA-A c16', 'location_x': 3534.4375,
                'location_y': 39901.0625, 'lng': 2426.721875, 'lat': 2995.053125, 'market_id': 3700407040},
               {'number': 90, 'name': 'DSSA Jolly Roger', 'callsign': 'K4ZB7Z', 'callsign_formatted': 'K4Z-B7Z',
                'patch_url': 'https://imgur.com/OFXSG2T.png', 'system': 'Ooctarbs NR-W e1-0', 'location_x': 12578.53125,
                'location_y': 59505.46875, 'lng': 2878.926563, 'lat': 3975.273438, 'market_id': 3700044032},
               {'number': 91, 'name': 'DSSA Nova Blues', 'callsign': 'KFXW3Z', 'callsign_formatted': 'KFX-W3Z',
                'patch_url': 'https://imgur.com/v1WL1Gf.png', 'system': 'Eord Prau ZK-N d7-711',
                'location_x': 5832.03125, 'location_y': 20083.5, 'lng': 2541.601563, 'lat': 2004.175,
                'market_id': 3701086464},
               {'number': 92, 'name': "[ISF] Mandy's Rest", 'callsign': 'B6LL0Z', 'callsign_formatted': 'B6L-L0Z',
                'patch_url': 'https://imgur.com/0hwGJsx.png', 'system': 'PLAE BROAE DL-P D5-0', 'location_x': 27225.75,
                'location_y': 50621.09375, 'lng': 3611.2875, 'lat': 3531.054688, 'market_id': 3700583424},
               {'number': 93, 'name': 'DSSA Manatee', 'callsign': 'J4WW8K', 'callsign_formatted': 'J4W-W8K',
                'patch_url': 'https://imgur.com/RqapNhW.png', 'system': 'Eolls Graae TA-K c10-5',
                'location_x': -18792.5625, 'location_y': 30120.3125, 'lng': 1310.371875, 'lat': 2506.015625,
                'market_id': 3701531392},
               {'number': 94, 'name': 'Hayholt', 'callsign': 'JZQGXZ', 'callsign_formatted': 'JZQ-GXZ',
                'patch_url': 'https://imgur.com/2uOXltL.png', 'system': 'Aiphaitt AA-A h7', 'location_x': 34379.68,
                'location_y': 34009, 'lng': 3968.984, 'lat': 2700.45, 'market_id': 3700997376},
               {'number': 95, 'name': 'Galactic Unity', 'callsign': 'QNYBQN', 'callsign_formatted': 'QNY-BQN',
                'patch_url': 'https://imgur.com/yrVqpWY.png', 'system': 'Byoi Aowsy XD-L b40-0',
                'location_x': -5466.90625, 'location_y': 44603.40625, 'lng': 1976.654688, 'lat': 3230.170313,
                'market_id': 3701041664},
               {'number': 97, 'name': 'DSSA Totoro', 'callsign': 'NNW23Z', 'callsign_formatted': 'NNW-23Z',
                'patch_url': 'https://imgur.com/5ALa9K5.png', 'system': 'GREAE PHOEA XF-D D13-507',
                'location_x': 4826.25, 'location_y': 16702.15625, 'lng': 2491.3125, 'lat': 1835.107813,
                'market_id': 3701265408},
               {'number': 100, 'name': "DSSA Solsen's Alastor", 'callsign': 'KOYLKF', 'callsign_formatted': 'KOY-LKF',
                'patch_url': 'https://imgur.com/kfwzDMH.png', 'system': 'Flyoo Groa SO-Z e0 (Alastor)',
                'location_x': -26482.4375, 'location_y': 50335.125, 'lng': 925.878125, 'lat': 3516.75625,
                'market_id': 3701638912},
               {'number': 103, 'name': "DSSA Wanderer's Rest", 'callsign': 'NNTW4Z', 'callsign_formatted': 'NNT-W4Z',
                'patch_url': 'https://imgur.com/VScCgTh.png', 'system': 'FLYAI PRE HR-V C2-1',
                'location_x': -22903.09375, 'location_y': 40017.09375, 'lng': 1104.845313, 'lat': 3000.854688,
                'market_id': 3700515840},
               {'number': 105, 'name': 'RR-DSSA Rocksteady', 'callsign': 'KBHT2Z', 'callsign_formatted': 'KBH-T2Z',
                'patch_url': 'https://imgur.com/cYU2PLO.png', 'system': 'PROOE HYPUE FH-U E3-2', 'location_x': 8687.425,
                'location_y': 8671.5, 'lng': 2684.37125, 'lat': 1433.575, 'market_id': 3700311808},
               {'number': 108, 'name': 'The Helix', 'callsign': 'X0FN1J', 'callsign_formatted': 'X0F-N1J',
                'patch_url': 'https://imgur.com/uY15ule.png', 'system': 'Phrae Prau NY-Y d1-15', 'location_x': 29786.75,
                'location_y': 26047.875, 'lng': 3739.3375, 'lat': 2302.39375, 'market_id': 3702278144},
               {'number': 109, 'name': "DSSA Erikson's Gateway", 'callsign': 'X6Z06M', 'callsign_formatted': 'X6Z-06M',
                'patch_url': 'https://imgur.com/DNnMkHV.png', 'system': 'Hypoe Bloae KZ-Z c16-6',
                'location_x': -31101.71875, 'location_y': 32944.625, 'lng': 694.9140625, 'lat': 2647.23125,
                'market_id': 3700577024},
               {'number': 110, 'name': 'TFS Carpe Vinum', 'callsign': 'TZNL3Z', 'callsign_formatted': 'TZN-L3Z',
                'patch_url': 'https://imgur.com/Zftle7r.png', 'system': 'Byae Aowsy GR-N d6-52',
                'location_x': 14407.625, 'location_y': 44312.59375, 'lng': 2970.38125, 'lat': 3215.629688,
                'market_id': 3700137728},
               {'number': 123, 'name': 'DSSA Heart of Gold', 'callsign': 'Q9G9TL', 'callsign_formatted': 'Q9G-9TL',
                'patch_url': 'https://imgur.com/Zftle7r.png', 'system': 'Cloomeia FG-Y e95', 'location_x': 14407.625,
                'location_y': 44312.59375, 'lng': 0.0, 'lat': 0.0, 'market_id': 3700137728},
               {'number': 124, 'name': 'Michelle’s Legacy', 'callsign': 'QHYG8J', 'callsign_formatted': 'QHY-G8J',
                'patch_url': 'https://imgur.com/fhfPWND.png', 'system': 'Eorm Chreou XS-U d2-14',
                'location_x': -31117.15625, 'location_y': 27367, 'lng': 694.1421875, 'lat': 2368.35,
                'market_id': 3700226816},
               {'number': 125, 'name': 'Rouge One', 'callsign': 'X3XW9G', 'callsign_formatted': 'X3X-W9G',
                'patch_url': 'https://imgur.com/IdKST1C.png', 'system': 'MYRIELK PJ-Y C1-4363', 'location_x': 8.375,
                'location_y': 24654, 'lng': 2250.41875, 'lat': 2232.7, 'market_id': 0},
               {'number': 126, 'name': 'TWITCHTVSOMDY', 'callsign': 'KZQ24Q', 'callsign_formatted': 'KZQ-24Q',
                'patch_url': 'https://imgur.com/EyN8Sfi.png', 'system': 'Lyed YJ-I d9-0', 'location_x': 11007.46875,
                'location_y': -16899.75, 'lng': 2800.373438, 'lat': 155.0125, 'market_id': 3700951808},
               {'number': 130, 'name': 'Emerald Tablet', 'callsign': 'M2Z44Z', 'callsign_formatted': 'M2Z-44Z',
                'patch_url': 'https://imgur.com/760ZjBT.png', 'system': 'Truechooe MR-S c18-2',
                'location_x': -9097.84375, 'location_y': 53526.96875, 'lng': 1795.107813, 'lat': 3676.348438,
                'market_id': 3701259520},
               {'number': 132, 'name': 'DSSA - Void Crusader', 'callsign': 'KFF86M', 'callsign_formatted': 'KFF-86M',
                'patch_url': 'https://imgur.com/lAFKjmh.png', 'system': 'GREAE PHIO VK-O E6-4343',
                'location_x': 1474.875, 'location_y': 16723.75, 'lng': 2323.74375, 'lat': 1836.1875,
                'market_id': 3702843904}]

   this.thread = Thread(target=worker, name='EDPS worker')
   this.thread.daemon = True
   this.thread.start()
   print("ED Passport System Plugin Loading...")
   this.queue.put(('does not matter',{},None, 'getAppInformation', ""))
   this.queue.put(('does not matter', {}, None, 'getFCsList',""))
   this.queue.put(('does not matter', {}, None, 'getPassport',""))

   return "EDPS"

def plugin_stop():
    """
    EDMC is closing
    """
    this.queue.put(None)
    this.thread.join()
    this.thread = None
    print("Clossing ED Passport System Plugin")

# Worker thread
def worker():
    while True:
        item = this.queue.get()
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
                        this.edpsConsoleMessage = 'Passport Already Acquired'
                        this.label4.event_generate('<<edpsUpdateConsoleEvent>>', when="tail")
                        retrying = 3
                        break
                    else:
                        print("Add Passport!")
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
                                    this.edpsConsoleMessage = 'API Key Wrong - Update in File-->Settings - If Lost then Generate New one on edps.dev'
                                    this.label4.event_generate('<<edpsUpdateConsoleEvent>>', when="tail")
                                    retrying = 3
                                    break
                                else:
                                    this.edpsConsoleMessage = 'Error Adding to Passport - Restart EDMC and Try to Redock?'
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
                    headers = {'x-api-key': 'bn9oCD5lqp7Yavh3l7VLB4lixo1FI69F2aiOmznB'}
                    r = requests.get('https://www.edps.dev/AppInformation.json', headers=headers, timeout=_TIMEOUT)
                    this.AppInformation = json.loads(r.text)
                    if r.ok:
                        if this.AppInformation['EDMCApp'] != _APPVERSION:
                            this.edpsConsoleMessage = 'Outdated Plugin Version - Please Download New Version'
                            this.label4.event_generate('<<edpsUpdateConsoleEvent>>', when="tail")
                            retrying = 3
                            break
                        else:
                            this.edpsConsoleMessage = 'EDPS Plugin is Up To Date'
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
                    headers = {'x-api-key': 'bn9oCD5lqp7Yavh3l7VLB4lixo1FI69F2aiOmznB'}
                    r = requests.get('https://edps-api.d3develop.com/passports/passport?cmder_name=' + config.get("edpscmder"), headers=headers, timeout=_TIMEOUT)
                    if r.ok:
                        if r.text == '"No User Found"':
                            print('User not found in database')
                            this.edpsConsoleMessage = 'Cmder not found! Sign up at edps.dev! (Important: Commander Name during sign up is Case Sensitive)'
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
                    pass
            except:
                print(sys.exc_info()[0])
                print('Error!')
                retrying += 1
                if retrying == 3:
                    time.sleep(2)
                    this.edpsConsoleMessage = 'Cannot connect to Server - Check Internet Connection and Relaunch! (You may need to kill EDMC in the Task Manger)'
                    this.label4.event_generate('<<edpsUpdateConsoleEvent>>', when="tail")


def plugin_prefs(parent, cmdr, is_beta):

    PADX = 10
    BUTTONX = 12	# indent Checkbuttons and Radiobuttons
    PADY = 2		# close spacing

    frame = nb.Frame(parent)
    frame.columnconfigure(1, weight=1)

    this.edpslog = tk.IntVar(value=config.getint("edpslog"))
    this.edpsapikey = tk.StringVar(value=config.get("edpsapikey"))

    HyperlinkLabel(frame, text='Elite Dangerous Passport System', background=nb.Label().cget('background'), url='https://www.edps.dev', underline=True).grid(columnspan=2, padx=PADX, sticky=tk.W)	# Don't translate
    this.log_button = nb.Checkbutton(frame, text=_('Send passport data to EDPS'), variable=this.edpslog)
    this.log_button.grid(columnspan=2, padx=BUTTONX, pady=(5,0), sticky=tk.W)

    nb.Label(frame).grid(sticky=tk.W)	# big spacer
    this.label = HyperlinkLabel(frame, text=_('Elite Dangerous Passport Credentials'), background=nb.Label().cget('background'), url='https://www.edps.dev', underline=True)	# Section heading in settings
    this.label.grid(columnspan=2, padx=PADX, sticky=tk.W)

    this.cmdr_label = nb.Label(frame, text=_('Commander Name'))  # Main window
    this.cmdr_label.grid(row=10, padx=PADX, sticky=tk.W)
    this.cmdr_text = nb.Label(frame, text=cmdr)
    this.cmdr_text.grid(row=10, column=1, padx=PADX, pady=PADY, sticky=tk.W)

    this.apikey_label = nb.Label(frame, text=_('API Key'))	# EDPS setting
    this.apikey_label.grid(row=12, padx=PADX, sticky=tk.W)
    this.apikey = nb.Entry(frame, textvariable=edpsapikey)
    this.apikey.grid(row=12, column=1, padx=PADX, pady=PADY, sticky=tk.EW)

    nb.Label(frame).grid(sticky=tk.W)	# big spacer

    config.set('edpscmder', cmdr)

    this.progressComplete = nb.Label(frame, text=_('0%'))
    this.progressComplete.grid(row=15, padx=PADX, sticky=tk.W)

    this.import_Journal = nb.Button(frame, text="Send Local Journal Files", command=load_Journal_Logs)   # Main window
    this.import_Journal.grid(row=16, padx=(PADX+8), sticky=tk.W)


    return frame

def prefs_changed(cmdr, is_beta):
   """
   Save settings.
   """
   config.set('edpsapikey', this.apikey.get())  # Store new value in config
   config.set('edpslog', this.edpslog.get())

def load_Journal_Logs():
    print("Loading Logs Function TBD...")
    rootdir = config.default_journal_dir
    extensions = ('.log')
    root = tk.Tk()
    root.title("Import Widget")
    root.geometry("400x400")

    w = tk.Label(root, text="Importing Journal Files... Please wait!")
    w.pack()

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
                with open(rootdir + '\\' + file, 'r') as f:
                    for line in f:
                        data = json.loads(line)
                        if data['event'] == 'Docked':
                            if data['StationType'] == 'FleetCarrier' and any(x['callsign_formatted'] == data['StationName'] for x in this.FCs) and any(y['system'] == data['StarSystem'] for y in this.FCs):
                                d1 = datetime.strptime(data['timestamp'],"%Y-%m-%dT%H:%M:%SZ")
                                w['text'] = w['text'] + "\nDocked to DSSA FC: " + data['StationName']
                                this.queue.put(('https://edps-api.d3develop.com/passports/passport/date',
                                                {'cmder_name': config.get("edpscmder"), 'api_key': config.get("edpsapikey"),
                                                 'callsign': data['StationName'].replace("-", ""),
                                                 'date': d1.strftime('%m/%d/%Y')}, None, 'postDate',
                                                data['StationName'].replace("-", "")))
                                time.sleep(.01)

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
    if entry['event'] == 'Docked':
        # Docking Event Detected
        if entry['StationType'] == 'FleetCarrier' and any(x['callsign_formatted'] == entry['StationName'] for x in this.FCs) and any(y['system'] == entry['StarSystem'] for y in this.FCs):
            print('Detected FC Docking')
            headers = {'Content-Type': 'application/json"'}
            this.queue.put(('https://edps-api.d3develop.com/passports/passport/date', {'cmder_name': cmdr, 'api_key': config.get("edpsapikey"), 'callsign':entry['StationName'].replace("-",""), 'date':datetime.today().strftime('%m/%d/%Y')}, None, 'postDate',entry['StationName'].replace("-","")))
        else:
            print('No FC detected')
            #this.label4["text"] = 'Docked to ' + entry['StationName']

def update_Edps_Console(event=None):
    this.label4["text"] = this.edpsConsoleMessage

def update_Edps_Passport_Count(event=None):
    this.label2["text"] = this.edpsPassportCountMessage