"""
UBX Protocol Input payload definitions

THESE ARE THE PAYLOAD DEFINITIONS FOR _SET_ MESSAGES _TO_ THE RECEIVER
(e.g. configuration and calibration commands; AssistNow payloads)

Created on 27 Sep 2020

Information sourced from u-blox Interface Specifications © 2013-2021, u-blox AG

:author: semuadmin
"""
# pylint: disable=too-many-lines, line-too-long

from pyubx2.ubxtypes_core import (
    I1,
    I2,
    I4,
    R4,
    R8,
    U1,
    U2,
    U3,
    U4,
    U5,
    U6,
    U7,
    U40,
    U64,
    X1,
    X2,
    X4,
    X24,
)

from pyubx2.ubxtypes_get import UBX_PAYLOADS_GET as UBX_GET

UBX_PAYLOADS_SET = {
    # AssistNow Aiding Messages: i.e. Ephemeris, Almanac, other A-GPS data input.
    # Messages in the AID class are used to send GPS aiding data to the receiver
    # AID messages are deprecated in favour of MGA messages in >=Gen8
    "AID-ALM": {"svid": U4, "week": U4, "optBlock": ("None", {"dwrd": U4})},
    "AID-AOP": {"gnssId": U1, "svId": U1, "reserved1": U2, "data": U64},
    "AID-EPH": {
        "svid": U4,
        "how": U4,
        "optBlock": (
            "None",
            {
                "sf1d1": U4,
                "sf1d2": U4,
                "sf1d3": U4,
                "sf1d4": U4,
                "sf1d5": U4,
                "sf1d6": U4,
                "sf1d7": U4,
                "sf1d8": U4,
                "sf2d1": U4,
                "sf2d2": U4,
                "sf2d3": U4,
                "sf2d4": U4,
                "sf2d5": U4,
                "sf2d6": U4,
                "sf2d7": U4,
                "sf2d8": U4,
                "sf3d1": U4,
                "sf3d2": U4,
                "sf3d3": U4,
                "sf3d4": U4,
                "sf3d5": U4,
                "sf3d6": U4,
                "sf3d7": U4,
                "sf3d8": U4,
            },
        ),
    },
    "AID-HUI": {
        "health": X4,
        "utcA0": R8,
        "utcA1": R8,
        "utcTOW": I4,
        "utcWNT": I2,
        "utcLS": I2,
        "utcWNF": I2,
        "utcDNs": I2,
        "utcLSF": I2,
        "utcSpare": I2,
        "klobA0": R4,
        "klobA1": R4,
        "klobA2": R4,
        "klobA3": R4,
        "klobB0": R4,
        "klobB1": R4,
        "klobB2": R4,
        "klobB3": R4,
        "flags": X4,
    },
    "AID-INI": {
        "ecefXOrLat": I4,
        "ecefYOrLon": I4,
        "ecefZOrAlt": I4,
        "posAcc": U4,
        "tmCfg": X2,
        "wn": U2,
        "tow": U4,
        "towNs": I4,
        "tAccMs": U4,
        "tAccNs": U4,
        "clkDOrFreq": I4,
        "clkDAccOrFreqAcc": U4,
        "flags": X4,
    },
    # ********************************************************************
    # Configuration Input Messages: i.e. Set Dynamic Model, Set DOP Mask, Set Baud Rate, etc..
    # Messages in the CFG class are used to configure the receiver and read out current configuration values. Any
    # messages in the CFG class sent to the receiver are either acknowledged (with message UBX-ACK-ACK) if
    # processed successfully or rejected (with message UBX-ACK-NAK) if processing unsuccessfully.
    #
    # Most CFG-* GET & SET message payloads are identical, so reference
    # GET definitions here to avoid duplication
    "CFG-ANT": UBX_GET["CFG-ANT"],
    "CFG-BATCH": UBX_GET["CFG-BATCH"],
    "CFG-CFG": UBX_GET["CFG-CFG"],
    "CFG-DAT": UBX_GET["CFG-DAT"],
    "CFG-DGNSS": UBX_GET["CFG-DGNSS"],
    "CFG-DOSC": UBX_GET["CFG-DOSC"],
    "CFG-DYNSEED": UBX_GET["CFG-DYNSEED"],
    "CFG-ESFALG": UBX_GET["CFG-ESFALG"],
    "CFG-ESFA": UBX_GET["CFG-ESFA"],
    "CFG-ESFG": UBX_GET["CFG-ESFG"],
    "CFG-ESFWT": UBX_GET["CFG-ESFWT"],
    "CFG-ESRC": UBX_GET["CFG-ESRC"],
    "CFG-FIXSEED": UBX_GET["CFG-FIXSEED"],
    "CFG-GEOFENCE": UBX_GET["CFG-GEOFENCE"],
    "CFG-GNSS": UBX_GET["CFG-GNSS"],
    "CFG-HNR": UBX_GET["CFG-HNR"],
    "CFG-INF": UBX_GET["CFG-INF"],
    "CFG-ITFM": UBX_GET["CFG-ITFM"],
    "CFG-LOGFILTER": UBX_GET["CFG-LOGFILTER"],
    "CFG-MSG": UBX_GET["CFG-MSG"],
    "CFG-NAV5": UBX_GET["CFG-NAV5"],
    "CFG-NAVX5": UBX_GET["CFG-NAVX5"],
    "CFG-NMEA": UBX_GET["CFG-NMEA"],
    "CFG-ODO": UBX_GET["CFG-ODO"],
    "CFG-PM2": UBX_GET["CFG-PM2"],
    "CFG-PMS": UBX_GET["CFG-PMS"],
    "CFG-PRT": UBX_GET["CFG-PRT"],
    "CFG-PWR": UBX_GET["CFG-PWR"],
    "CFG-RATE": UBX_GET["CFG-RATE"],
    "CFG-RINV": UBX_GET["CFG-RINV"],
    "CFG-RST": UBX_GET["CFG-RST"],
    "CFG-RXM": UBX_GET["CFG-RXM"],
    "CFG-SBAS": UBX_GET["CFG-SBAS"],
    "CFG-SENIF": UBX_GET["CFG-SENIF"],
    "CFG-SLAS": UBX_GET["CFG-SLAS"],
    "CFG-SMGR": UBX_GET["CFG-SMGR"],
    "CFG-SPT": UBX_GET["CFG-SPT"],
    "CFG-TMODE2": UBX_GET["CFG-TMODE2"],
    "CFG-TMODE3": UBX_GET["CFG-TMODE3"],
    "CFG-TP5": UBX_GET["CFG-TP5"],
    "CFG-TXSLOT": UBX_GET["CFG-TXSLOT"],
    "CFG-USB": UBX_GET["CFG-USB"],
    "CFG-VALDEL": {
        "version": U1,  # = 0 no transaction, 1 with transaction
        "layers": X1,
        "transaction": X1,  # if version = 1, else reserved
        "reserved0": U1,
        "group": ("None", {"keys": U4}),  # repeating group
    },
    "CFG-VALSET": {
        "version": U1,  # = 0 no transaction, 1 with transaction
        "layers": X1,
        "transaction": U1,  # if version = 1, else reserved
        "reserved0": U1,
        "group": ("None", {"cfgData": U1}),  # repeating group
    },
    # ********************************************************************
    # External Sensor Fusion Messages: i.e. External Sensor Measurements and Status Information.
    # Messages in the ESF class are used to output external sensor fusion information from the receiver.
    # if calibTtagValid = 1; last dataField = calibTtag, numMeas = num of dataFields excluding calibTtag
    "ESF-MEAS": {
        "timeTag": U4,
        "flags": (
            X2,
            {
                "timeMarkSent": U2,
                "timeMarkEdge": U1,
                "calibTtagValid": U1,
                "reserved0": U7,
                "numMeas": U5,
            },
        ),
        "id": U2,
        "group": (
            "None",
            {  # repeating group * numMeas
                "data": (
                    X4,
                    {
                        "dataField": X24,
                        "dataType": U6,
                    },
                ),
            },
        ),
    },
    # ********************************************************************
    # Logging Messages: i.e. Log creation, deletion, info and retrieval.
    # Messages in the LOG class are used to configure and report status information of the logging feature.
    "LOG-CREATE": {
        "version": U1,
        "logCfg": X1,
        "reserved1": U1,
        "logSize": U1,
        "userDefinedSize": U4,
    },
    "LOG-ERASE": {},
    "LOG-FINDTIME": {
        "version": U1,
        "type": U1,
        "year": U2,
        "month": U1,
        "day": U1,
        "hour": U1,
        "minute": U1,
        "second": U1,
        "reserved1": U1,
    },
    "LOG-RETRIEVE": {
        "startNumber": U4,
        "entryCount": U4,
        "version": U1,
        "reserved": U3,
    },
    "LOG-RETRIEVEBATCH": {
        "version": U1,
        "flags": X1,
        "reserved0": U2,
    },
    "LOG-STRING": {"group": ("None", {"bytes": U1})},  # repeating group
    # ********************************************************************
    # Multiple GNSS Assistance Messages: i.e. Assistance data for various GNSS.
    # Messages in the MGA class are used for GNSS aiding information from and to the receiver.
    "MGA-ANO": {
        "type": U1,
        "version": U1,
        "svId": U1,
        "gnssId": U1,
        "year": U1,
        "month": U1,
        "day": U1,
        "reserved1": U1,
        "data": U64,
        "reserved2": U4,
    },
    "MGA-BDS-EPH": {
        "type": U1,
        "version": U1,
        "svId": U1,
        "reserved1": U1,
        "SatH1": U1,
        "IODC": U1,
        "a2": I2,
        "a1": I4,
        "a0": I4,
        "toc": U4,
        "TGD1": I2,
        "URAI": U1,
        "IODE": U1,
        "toe": U4,
        "sqrtA": U4,
        "e": U4,
        "omega": I4,
        "Deltan": I2,
        "IDOT": I2,
        "M0": I4,
        "Omega0": I4,
        "OmegaDot": I4,
        "i0": I4,
        "Cuc": I4,
        "Cus": I4,
        "Crc": I4,
        "Crs": I4,
        "Cic": I4,
        "Cis": I4,
        "reserved2": U4,
    },
    "MGA-BDS-ALM": {
        "type": U1,
        "version": U1,
        "svId": U1,
        "reserved1": U1,
        "Wna": U1,
        "toa": U1,
        "deltaI": I2,
        "sqrtA": U4,
        "e": U4,
        "omega": I4,
        "M0": I4,
        "Omega0": I4,
        "omegaDot": I4,
        "a0": I2,
        "a1": I2,
        "reserved2": U4,
    },
    "MGA-BDS-HEALTH": {
        "type": U1,  # 0x04
        "version": U1,
        "reserved0": U2,
        "grouphealthcode": (
            30,
            {
                "healthCode": U2,
            },
        ),  # repeating group * 30
        "reserved1": U4,
    },
    "MGA-BDS-UTC": {
        "type": U1,  # 0x05
        "version": U1,
        "reserved1": U2,
        "a0UTC": I4,
        "a1UTC": I4,
        "dtLS": I1,
        "reserved2": U1,
        "wnRec": U1,
        "wnLSF": U1,
        "dN": U1,
        "dtLSF": I1,
        "reserved3": U2,
    },
    "MGA-BDS-IONO": {
        "type": U1,  # 0x06
        "version": U1,
        "reserved1": U2,
        "alpha0": I1,
        "alpha1": I1,
        "alpha2": I1,
        "alpha3": I1,
        "beta0": I1,
        "beta1": I1,
        "beta2": I1,
        "beta3": I1,
        "reserved2": U4,
    },
    "MGA-FLASH-DATA": {
        "type": U1,
        "version": U1,
        "sequence": U2,
        "size": U2,
        "group": ("size", {"data": U1}),  # repeating group * size
    },
    "MGA-FLASH-STOP": {"type": U1, "version": U1},
    "MGA-GAL-EPH": {
        "type": U1,
        "version": U1,
        "svId": U1,
        "reserved1": U1,
        "iodNav": U2,
        "deltaN": I2,
        "m0": I4,
        "e": U4,
        "sqrtA": U4,
        "omega0": I4,
        "i0": I4,
        "omega": I4,
        "omegaDot": I4,
        "iDot": I2,
        "cuc": I2,
        "cus": I2,
        "crc": I2,
        "crs": I2,
        "cic": I2,
        "cis": I2,
        "toe": U2,
        "af0": I4,
        "af1": I4,
        "af2": I1,
        "sisaIndexE1E5b": U1,
        "toc": U2,
        "bgdE1E5b": I2,
        "reserved2": U2,
        "healthE1B": U1,
        "dataValidityE1B": U1,
        "healthE5b": U1,
        "dataValidityE5b": U1,
        "reserved3": U4,
    },
    "MGA-GAL-ALM": {
        "type": U1,
        "version": U1,
        "svId": U1,
        "reserved1": U1,
        "ioda": U1,
        "almWNa": U1,
        "toa": U2,
        "deltaSqrtA": I2,
        "e": U2,
        "deltaI": I2,
        "omega0": I2,
        "omegaDot": I2,
        "omega": I2,
        "m0": I2,
        "af0": I2,
        "af1": I2,
        "healthE1B": U1,
        "healthE5b": U1,
        "reserved2": U4,
    },
    "MGA-GAL-TIMEOFFSET": {
        "type": U1,
        "version": U1,
        "reserved1": U2,
        "a0G": I2,
        "a1G": I2,
        "t0G": U1,
        "wn0G": U1,
        "reserved2": U2,
    },
    "MGA-GAL-UTC": {
        "type": U1,
        "version": U1,
        "reserved1": U2,
        "a0": I4,
        "a1": I4,
        "dtLS": I1,
        "tot": U1,
        "wnt": U1,
        "wnLSF": U1,
        "dN": U1,
        "dTLSF": I1,
        "reserved2": U2,
    },
    "MGA-GLO-EPH": {
        "type": U1,
        "version": U1,
        "svId": U1,
        "reserved1": U1,
        "FT": U1,
        "B": U1,
        "M": U1,
        "H": I1,
        "x": I4,
        "y": I4,
        "z": I4,
        "dx": I4,
        "dy": I4,
        "dz": I4,
        "ddx": I1,
        "ddy": I1,
        "ddz": I1,
        "tb": U1,
        "gamma": I2,
        "E": U1,
        "deltaTau": I1,
        "tau": I4,
        "reserved2": U4,
    },
    "MGA-GLO-ALM": {
        "type": U1,
        "version": U1,
        "svId": U1,
        "reserved1": U1,
        "N": U2,
        "M": U1,
        "C": U1,
        "tau": I2,
        "epsilon": U2,
        "lambda": I4,
        "deltaI": I4,
        "tLambda": U4,
        "deltaT": I4,
        "deltaDT": I1,
        "H": I1,
        "omega": I2,
        "reserved2": U4,
    },
    "MGA-GLO-TIMEOFFSET": {
        "type": U1,
        "version": U1,
        "N": U2,
        "tauC": I4,
        "tauGps": I4,
        "B1": I2,
        "B2": I2,
        "reserved1": U4,
    },
    "MGA-GPS-EPH": {
        "type": U1,
        "version": U1,
        "svId": U1,
        "reserved1": U1,
        "fitInterval": U1,
        "uraIndex": U1,
        "svHealth": U1,
        "tgd": I1,
        "iodc": U2,
        "toc": U2,
        "reserved2": U1,
        "af2": I1,
        "af1": I2,
        "af0": I4,
        "crs": I2,
        "deltaN": I2,
        "m0": I4,
        "cuc": I2,
        "cus": I2,
        "e": U4,
        "sqrtA": U4,
        "toe": U2,
        "cic": I2,
        "omega0": I4,
        "cis": I2,
        "crc": I2,
        "i0": I4,
        "omega": I4,
        "omegaDot": I4,
        "idot": I2,
        "reserved3": U4,
    },
    "MGA-GPS-ALM": {
        "type": U1,
        "version": U1,
        "svId": U1,
        "svHealth": U1,
        "e": U2,
        "almWNa": U1,
        "toa": U1,
        "deltaI": I2,
        "omegaDot": I2,
        "sqrtA": U4,
        "omega0": I4,
        "omega": I4,
        "m0": I4,
        "af0": I2,
        "af1": I2,
        "reserved1": U4,
    },
    "MGA-GPS-HEALTH": {
        "type": U1,
        "version": U1,
        "reserved0": U2,
        "grouphealthcode": (
            32,
            {
                "healthCode": U1,
            },
        ),  # repeating group * 32
        "reserved1": U4,
    },
    "MGA-GPS-UTC": {
        "type": U1,
        "version": U1,
        "reserved1": U2,
        "utcA0": I4,
        "utcA1": I4,
        "utcDtLS": I1,
        "utcTot": U1,
        "utcWNt": U1,
        "utcWNlsf": U1,
        "utcDn": U1,
        "utcDtLSF": I1,
        "reserved2": U2,
    },
    "MGA-GPS-IONO": {
        "type": U1,
        "version": U1,
        "reserved1": U2,
        "ionoAlpha0": I1,
        "ionoAlpha1": I1,
        "ionoAlpha2": I1,
        "ionoAlpha3": I1,
        "ionoBeta0": I1,
        "ionoBeta1": I1,
        "ionoBeta2": I1,
        "ionoBeta3": I1,
        "reserved2": U4,
    },
    "MGA-INI-POS_XYZ": {
        "type": U1,
        "version": U1,
        "reserved1": U2,
        "ecefX": I4,
        "ecefY": I4,
        "ecefZ": I4,
        "posAcc": U4,
    },
    "MGA-INI-POS_LLH": {
        "type": U1,
        "version": U1,
        "reserved1": U2,
        "lat": I4,
        "lon": I4,
        "alt": I4,
        "posAcc": U4,
    },
    "MGA-INI-TIME_UTC": {
        "type": U1,
        "version": U1,
        "ref": X1,
        "leapSecs": I1,
        "year": U2,
        "month": U1,
        "day": U1,
        "hour": U1,
        "minute": U1,
        "second": U1,
        "reserved1": U1,
        "ns": U4,
        "tAccS": U2,
        "reserved2": U2,
        "tAccNs": U4,
    },
    "MGA-INI-TIME_GNSS": {
        "type": U1,
        "version": U1,
        "ref": X1,
        "gnssId": U1,
        "reserved1": U2,
        "week": U2,
        "tow": U4,
        "ns": U4,
        "tAccS": U2,
        "reserved2": U2,
        "tAccNs": U4,
    },
    "MGA-INI-CLKD": {
        "type": U1,
        "version": U1,
        "reserved1": U2,
        "clkD": I4,
        "clkDAcc": U4,
    },
    "MGA-INI-FREQ": {
        "type": U1,
        "version": U1,
        "reserved1": U1,
        "flags": X1,
        "freq": I4,
        "freqAcc": U4,
    },
    "MGA-INI-EOP": {
        "type": U1,
        "version": U1,
        "reserved1": U2,
        "d2kRef": U2,
        "d2kMax": U2,
        "xpP0": I4,
        "xpP1": I4,
        "ypP0": I4,
        "ypP1": I4,
        "dUT1": I4,
        "ddUT1": I4,
        "reserved2": U40,
    },
    "MGA-QZSS-EPH": {
        "type": U1,
        "version": U1,
        "svId": U1,
        "reserved1": U1,
        "fitInterval": U1,
        "uraIndex": U1,
        "svHealth": U1,
        "tgd": I1,
        "iodc": U2,
        "toc": U2,
        "reserved2": U1,
        "af2": I1,
        "af1": I2,
        "af0": I4,
        "crs": I2,
        "deltaN": I2,
        "m0": I4,
        "cuc": I2,
        "cus": I2,
        "e": U4,
        "sqrtA": U4,
        "toe": U2,
        "cic": I2,
        "omega0": I4,
        "cis": I2,
        "crc": I2,
        "i0": I4,
        "omega": I4,
        "omegaDot": I4,
        "idot": I2,
        "reserved3": U2,
    },
    "MGA-QZSS-ALM": {
        "type": U1,
        "version": U1,
        "svId": U1,
        "svHealth": U1,
        "e": U2,
        "almWNa": U1,
        "toa": U1,
        "deltaI": I2,
        "omegaDot": I2,
        "sqrtA": U4,
        "omega0": I4,
        "omega": I4,
        "m0": I4,
        "af0": I2,
        "af1": I2,
        "reserved1": U4,
    },
    "MGA-QZSS-HEALTH": {
        "type": U1,
        "version": U1,
        "reserved0": U2,
        "grouphealthcode": (
            5,
            {
                "healthCode": U1,
            },
        ),  # repeating group * 5
        "reserved1": U3,
    },
    # ********************************************************************
    # Navigation Results Messages: i.e. Position, Speed, Time, Acceleration, Heading, DOP, SVs used.
    # Messages in the NAV class are used to output navigation data such as position, altitude and velocity in a
    # number of formats. Additionally, status flags and accuracy figures are output. The messages are generated with
    # the configured navigation/measurement rate.
    "NAV-RESETODO": {},
    # ********************************************************************
    # Receiver Manager Messages: i.e. Satellite Status, RTC Status.
    # Messages in the RXM class are used to output status and result data from the Receiver Manager. The output
    # rate is not bound to the navigation/measurement rate and messages can also be generated on events.
    "RXM-PMREQ-S": {
        "duration": U4,
        "flags": X4,
    },  # this appears to be a deprecated version
    "RXM-PMREQ": {
        "version": U1,  # 0x00
        "reserved0": U3,
        "duration": U4,
        "flags": (
            X4,
            {
                "reserved1": U1,
                "backup": U1,
                "force": U1,
            },
        ),
        "wakeupSources": (
            X4,
            {
                "reserved2": U3,
                "uartrx": U1,
                "reserved3": U1,
                "extint0": U1,
                "extint1": U1,
                "spics": U1,
            },
        ),
    },
    # ********************************************************************
    # Timing Messages: i.e. Time Pulse Output, Time Mark Results.
    # Messages in the TIM class are used to output timing information from the receiver, like Time Pulse and Time
    # Mark measurements.
    "TIM-HOC": {
        "version": U1,
        "oscId": U1,
        "flags": U1,
        "reserved1": U1,
        "value": [I4, 2 ** -8],
    },
    "TIM-SMEAS": UBX_GET["TIM-SMEAS"],
    "TIM-VCOCAL-V0": {  # stop calibration
        "type": U1,  # 0x00
    },
    "TIM-VCOCAL": {
        "type": U1,  # 0x02
        "version": U1,  # 0x00
        "oscId": U1,
        "srcId": U1,
        "reserved1": U2,
        "raw0": U2,
        "raw1": U2,
        "maxStepSize": U2,
    },
    # ********************************************************************
    # Firmware Update Messages: i.e. Memory/Flash erase/write, Reboot, Flash identification, etc..
    # Messages in the UPD class are used to update the firmware and identify any attached flash device.
    "UPD-SOS": {"cmd": U1, "reserved1": U3},  # Create or clear backup in flash
}
