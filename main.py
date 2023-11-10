import requests
import yaml
import time
import csv
import os
import random
import datetime
import platform

# 获取当前操作系统类型
os_type = platform.system()

if os_type == 'Windows':
    # Windows系统
    os.system('cls')
elif os_type == 'Linux' or os_type == 'Darwin':
    # 类Unix系统（Linux和macOS）
    os.system('clear')

url = ["https://fastly.jsdelivr.net/gh/XiaomiFirmwareUpdater/xiaomifirmwareupdater.github.io@master/data/devices/full/",
       'https://ghproxy.com/https://raw.githubusercontent.com/XiaomiFirmwareUpdater/xiaomifirmwareupdater.github.io/master/data/devices/full/',
       "https://gcore.jsdelivr.net/gh/XiaomiFirmwareUpdater/xiaomifirmwareupdater.github.io@master/data/devices/full/",
       "https://raw.fgit.cf/XiaomiFirmwareUpdater/xiaomifirmwareupdater.github.io/master/data/devices/full/",
       "https://github.com/XiaomiFirmwareUpdater/xiaomifirmwareupdater.github.io/raw/master/data/devices/full/"]
devices = ["agate.yml", "alioth.yml", "andromeda.yml", "angelica.yml", "angelicain.yml", "angelican.yml", "apollo.yml", "aqua.yml", "ares.yml", "aristotle.yml", "atom.yml", "babylon.yml", "begonia.yml", "begoniain.yml", "beryllium.yml", "biloba.yml", "bomb.yml", "cactus.yml", "camellia.yml", "camellian.yml", "cannon.yml", "cannong.yml", "cappu.yml", "capricorn.yml", "cas.yml", "cattail.yml", "cepheus.yml", "cereus.yml", "cetus.yml", "cezanne.yml", "chiron.yml", "chopin.yml", "citrus.yml", "clover.yml", "cmi.yml", "corot.yml", "courbet.yml", "crux.yml", "cupid.yml", "curtana.yml", "dagu.yml", "daisy.yml", "dandelion.yml", "daumier.yml", "davinci.yml", "davinciin.yml", "dipper.yml", "diting.yml", "earth.yml", "elish.yml", "enuma.yml", "equuleus.yml", "evergo.yml", "evergreen.yml", "excalibur.yml", "fire.yml", "fleur.yml", "fog.yml", "frost.yml", "fuxi.yml", "garnet.yml", "gauguin.yml", "gemini.yml", "ginkgo.yml", "gold.yml", "gram.yml", "grus.yml", "haydn.yml", "helium.yml", "houji.yml", "hydrogen.yml", "ice.yml", "ido.yml", "ingres.yml", "ishtar.yml", "jasmine.yml", "jason.yml", "joyeuse.yml", "kate.yml", "kenzo.yml", "lancelot.yml", "land.yml", "laurel.yml", "laurus.yml", "lavender.yml", "libra.yml", "light.yml", "lightcm.yml", "lime.yml", "lisa.yml", "lithium.yml", "liuqin.yml", "lmi.yml", "lotus.yml", "marble.yml", "markw.yml", "matisse.yml", "mayfly.yml", "merlin.yml", "mido.yml", "mojito.yml", "mona.yml", "mondrian.yml", "monet.yml", "moonstone.yml", "munch.yml", "nabu.yml", "natrium.yml", "nitrogen.yml", "nuwa.yml", "odin.yml", "olive.yml", "olivelite.yml", "olivewood.yml", "onc.yml", "onclite.yml", "opal.yml", "oxygen.yml", "pearl.yml", "perseus.yml", "phoenix.yml", "phoenixin.yml", "picasso.yml", "pine.yml", "pipa.yml", "pissarro.yml", "platina.yml", "plato.yml", "polaris.yml", "prada.yml", "psyche.yml", "pyxis.yml", "raphael.yml", "raphaelin.yml", "redwood.yml", "rembrandt.yml", "renoir.yml", "riva.yml", "rock.yml", "rolex.yml", "rosemary.yml", "rosy.yml", "rubens.yml", "ruby.yml", "sagit.yml", "sakura.yml", "santoni.yml", "scorpio.yml", "sea.yml", "selene.yml", "selenes.yml", "shennong.yml", "shiva.yml", "sirius.yml", "sky.yml", "socrates.yml", "spes.yml", "spesn.yml", "star.yml", "sunstone.yml", "surya.yml", "sweet.yml", "sweetin.yml", "taoyao.yml", "tapas.yml", "thor.yml", "thyme.yml", "tiffany.yml", "toco.yml", "topaz.yml", "tucana.yml", "tulip.yml", "ugg.yml", "ugglite.yml", "umi.yml", "unicorn.yml", "ursa.yml", "vangogh.yml", "vayu.yml", "vela.yml", "venus.yml", "veux.yml", "vida.yml", "vili.yml", "vince.yml", "violet.yml", "viva.yml", "water.yml", "wayne.yml", "whyred.yml", "willow.yml", "xaga.yml", "xun.yml", "ysl.yml", "yudi.yml", "yuechu.yml", "yunluo.yml", "zeus.yml", "zijin.yml", "zircon.yml", "ziyi.yml", "zizhan.yml"]

# 获取今天的日期
today = datetime.date.today().strftime('%Y-%m-%d')

# 创建一个CSV文件，用于汇总今天的数据
csv_filename = f'firmware_updates_{today}.csv'
# 检查文件是否存在并删除
if os.path.exists(csv_filename):
    os.remove(csv_filename)
num = len(devices)

for i in devices:
    # 获取网页内容
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
    success = False

    while not success and url:
        random_url = random.choice(url)
        full_url = random_url + i

        try:
            response = requests.get(full_url, headers=headers)
            response.raise_for_status()  # 检查是否有请求错误
            success = True
        except requests.exceptions.RequestException as e:
            print(f'Error: 更换节点..')
            url.remove(random_url)  # 移除失败的URL
            if not url:
                print("所有节点失效,退出脚本.")
                break

    if success:
        content = response.text

        # 解析为字典
        data = yaml.safe_load(content)

        # 开始判断
        path = os.getcwd()
        with open(path + '//' + csv_filename, 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            for entry in data:
                code = i.replace('.yml','')
                filename = entry['filename']
                branch = entry['branch']
                date = entry['date']
                github_download = entry['downloads']['github']
                osdn_download = entry['downloads']['osdn']
                region = entry['region']
                android_version = entry['versions']['android']
                miui_version = entry['versions']['miui']

                # if date == today:
                csv_writer.writerow([code, branch, date, github_download, osdn_download, filename, region, android_version, miui_version])
        num -= 1
        print(f'[{num}] {code} saved!')
        # ttime = random.uniform(1,2)
        # print('等待:',ttime)
        # time.sleep(ttime)        
            

    
