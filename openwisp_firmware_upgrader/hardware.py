"""
Mapping between hardware models and firwmare image
This if focused on OpenWRT only fpr now, but it should
be possible to add support for different embedded
systems in the future.
"""
from collections import OrderedDict

from . import settings as app_settings

if app_settings.CUSTOM_OPENWRT_IMAGES:
    OPENWRT_FIRMWARE_IMAGE_MAP = OrderedDict(app_settings.CUSTOM_OPENWRT_IMAGES)
else:  # pragma: no cover
    OPENWRT_FIRMWARE_IMAGE_MAP = OrderedDict()

OPENWRT_FIRMWARE_IMAGE_MAP.update(
    OrderedDict(
        (
            (
                'ramips-mt76x8-gl-mt300n-v2-squashfs-sysupgrade.bin',
                {'label': 'GL.iNet GL-MT300N-V2', 'boards': ('GL-MT300N-V2',)},
            ),
            (
                'ar71xx-generic-tl-wdr4300-v1-il-squashfs-sysupgrade.bin',
                {
                    'label': 'TP-Link WDR4300 v1 (IL)',
                    'boards': ('TP-LINK TL-WDR4300 v1 (IL)',),
                },
            ),
            (
                'ar71xx-generic-tl-wdr4300-v1-squashfs-sysupgrade.bin',
                {'label': 'TP-Link WDR4300 v1', 'boards': ('TP-Link TL-WDR4300 v1',)},
            ),
            (
                'ar71xx-generic-xd3200-squashfs-sysupgrade.bin',
                {'label': 'YunCore XD3200', 'boards': ('YunCore XD3200',)},
            ),
            (
                'ar71xx-generic-ubnt-airrouter-squashfs-sysupgrade.bin',
                {'label': 'Ubiquiti AirRouter', 'boards': ('Ubiquiti AirRouter',)},
            ),
            (
                'ramips-mt7621-zbt-wg3526-16M-squashfs-sysupgrade.bin',
                {'label': 'ZBT-WG3526 (16M)', 'boards': ('ZBT-WG3526 (16M)',)},
            ),
            (
                'ath79-generic-tplink_tl-wr2543-v1-squashfs-sysupgrade.bin',
                {
                    'label': 'TP-Link TL-WR2543N/ND',
                    'boards': ('TP-Link TL-WR2543N/ND',),
                },
            ),
            (
                'ath79-generic-tplink_cpe210-v3-squashfs-sysupgrade.bin',
                {'label': 'TP-LINK CPE210 v3', 'boards': ('TP-LINK CPE210 v3',)},
            ),
            (
                'ath79-generic-tplink_cpe510-v3-squashfs-sysupgrade.bin',
                {'label': 'TP-LINK CPE510 v3', 'boards': ('TP-LINK CPE510 v3',)},
            ),
            (
                'ath79-generic-tplink_archer-c7-v1-squashfs-sysupgrade.bin',
                {'label': 'TP-Link Archer C7 v1', 'boards': ('tplink,archer-c7-v1',)},
            ),
            (
                'ath79-generic-tplink_archer-c7-v2-squashfs-sysupgrade.bin',
                {
                    'label': 'TP-Link Archer C7 v2',
                    'boards': ('TP-Link Archer C7 v2', 'TP-Link Archer C7 v3'),
                },
            ),
            (
                'ath79-generic-tplink_archer-c7-v4-squashfs-sysupgrade.bin',
                {'label': 'TP-Link Archer C7 v4', 'boards': ('TP-Link Archer C7 v4',)},
            ),
            (
                'ath79-generic-tplink_archer-c7-v5-squashfs-sysupgrade.bin',
                {'label': 'TP-Link Archer C7 v5', 'boards': ('TP-Link Archer C7 v5',)},
            ),
            (
                'ramips-mt76x8-tplink_tl-wr902ac-v3-squashfs-sysupgrade.bin',
                {
                    'label': 'TP-Link TL-WR902AC v3',
                    'boards': ('TP-Link TL-WR902AC v3',),
                },
            ),
            (
                'brcm2708-bcm2710-rpi-3-ext4-sysupgrade.img.gz',
                {
                    'label': 'Raspberry Pi 3 Model B',
                    'boards': ('Raspberry Pi 3 Model B Rev 1.2',),
                },
            ),
            (
                'brcm2708-bcm2709-rpi-2-ext4-sysupgrade.img.gz',
                {
                    'label': 'Raspberry Pi 2 Model B',
                    'boards': (
                        'Raspberry Pi 2 Model B Rev 1.0',
                        'Raspberry Pi 2 Model B Rev 1.1',
                        'Raspberry Pi 2 Model B Rev 1.2',
                    ),
                },
            ),
            (
                'x86-64-generic-squashfs-sysupgrade.bin',
                {
                    'label': 'VMware, Inc. VMware Virtual Platform',
                    'boards': ('VMware, Inc. VMware Virtual Platform',),
                },
            ),
            (
                'mvebu-cortexa9-linksys_wrt1900acs-squashfs-sysupgrade.img',
                {'label': 'Linksys WRT1900ACS', 'boards': ('Linksys WRT1900ACS',)},
            ),
            (
                'mvebu-cortexa9-linksys_wrt3200acm-squashfs-sysupgrade.img',
                {'label': 'Linksys WRT3200ACM', 'boards': ('Linksys WRT3200ACM',)},
            ),
        )
    )
)

# OpenWRT only for now, in the future we'll merge
# different dictionaries representing different firmwares
# eg: AirOS, Raspbian
FIRMWARE_IMAGE_MAP = OPENWRT_FIRMWARE_IMAGE_MAP

# Allows getting type from image board
REVERSE_FIRMWARE_IMAGE_MAP = {}
# Choices used in model
FIRMWARE_IMAGE_TYPE_CHOICES = []

for key, info in FIRMWARE_IMAGE_MAP.items():
    FIRMWARE_IMAGE_TYPE_CHOICES.append((key, info['label']))
    for board in info['boards']:
        REVERSE_FIRMWARE_IMAGE_MAP[board] = key
