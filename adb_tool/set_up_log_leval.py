# # -*- coding: utf-8 -*-
import os
import re
import logging
from logging import handlers
import time
def check_device_type():
    # 获取当前所有连接的adb设备
    def check_current_adb():
        device_list = []
        device_re = r'(.*)	device'
        command = 'adb devices'
        r = os.popen(command)
        info = r.readlines()
        for line in info:
            line = line.strip('\r\n')
            search_result = re.match(device_re, line, re.M | re.I)
            if search_result:
                device_list.append(search_result.group(1))
        return device_list

    # 设备信息保存字典中
    device_type_dict = {'x_front_8155': '', 'x_rear_8155': '', 'phone': '', 'm01': ''}
    for i in range(0, len(check_current_adb())):
        # 如果设备名称以f或者r结尾，则为x01的前或后8155设备
        if 'f' == check_current_adb()[i][-1]:
            device_type_dict['x_front_8155'] = check_current_adb()[i]
        elif 'r' == check_current_adb()[i][-1]:
            device_type_dict['x_rear_8155'] = check_current_adb()[i]
        # 除此之外的设备，名称长度大于8的认为是手机设备，长度等于8的认为m01设备
        else:
            if len(check_current_adb()[i]) > 8:
                device_type_dict['phone'] = check_current_adb()[i]
            if len(check_current_adb()[i]) == 8:
                device_type_dict['m01'] = check_current_adb()[i]
    log.logger.info('flash_all_build: check_device_type: all device id is ' + str(device_type_dict))
    return device_type_dict
def runcmd(adb_command):
    os.system('adb -s ' + device_id + ' root')
    time.sleep(1)
    os.system('adb -s ' + device_id + ' shell')
    if device_id[-1] == "r":
        log.logger.info('flash_all_build: runcmd: ' + device_id +
                        ' shell ')
        os.system('adb -s ' + device_id + ' shell QFirehose -s /sys/bus/usb/devices/1-1 -f /data/modemfw')
    else:
        log.logger.info('flash_all_build: flash_5g: ' + device_id +
                        ' shell QFirehose -f /data/modemfw')
        os.system('adb -s ' + device_id + ' shell QFirehose -f /data/modemfw')


if __name__ == '__main__':
    try:
        device_info_dict = check_device_type()
        download_build_name_lst, flash_item_name_lst, car_type = download_need_build()
        if car_type == "X01" or car_type == "X02-Max" or car_type == "W01":
            if 'mcu' in flash_item_name_lst and device_info_dict['x_front_8155'] != '':
                log.logger.info('flash_all_build: main: start flash mcu')
                flash_udisk(device_info_dict['x_front_8155'], download_build_name_lst, "MCU")
            if '5G' in flash_item_name_lst and device_info_dict['x_rear_8155'] != '':
                log.logger.info('flash_all_build: main: start flash rear_8155')
                flash_5g(device_info_dict['x_rear_8155'], download_build_name_lst)
            if 'rear_8155' in flash_item_name_lst and device_info_dict['x_rear_8155'] != '':
                log.logger.info('flash_all_build: main: start flash rear_8155')
                flash_8155(device_info_dict['x_rear_8155'], download_build_name_lst, car_type)
            if 'front_8155' in flash_item_name_lst and device_info_dict['x_front_8155'] != '':
                log.logger.info('flash_all_build: main: start flash front_8155')
                flash_8155(device_info_dict['x_front_8155'], download_build_name_lst, car_type)
        elif car_type == "X02-Pro":
            if 'front_8155' in flash_item_name_lst and device_info_dict['x_front_8155'] != '':
                log.logger.info('flash_all_build: main: start flash front_8155')
                flash_8155(device_info_dict['x_front_8155'], download_build_name_lst, car_type)
            if '5G' in flash_item_name_lst and device_info_dict['x_front_8155'] != '':
                # log.logger.info('flash_all_build: main: start flash x_front_8155')
                # if os.path.exists(os.path.join(os.getcwd(), "no_code_change_and_last_version_path.txt")):
                #     flash_5g(device_info_dict['x_front_8155'], download_build_name_lst)
                #     time.sleep(180)
                # else:
                #     flash_udisk(device_info_dict['x_front_8155'], download_build_name_lst, "5G")
                #     time.sleep(600)
                # log.logger.info("ota 5G finished, waiting for starting up, then flashing mcu")
                log.logger.info('flash_all_build: main: start flash x_front_8155')
                flash_5g(device_info_dict['x_front_8155'], download_build_name_lst)
                log.logger.info("ota 5G finished, waiting for starting up, then flashing mcu")
                time.sleep(180)
            if 'mcu' in flash_item_name_lst and device_info_dict['x_front_8155'] != '':
                log.logger.info('flash_all_build: main: start flash mcu')
                flash_udisk(device_info_dict['x_front_8155'], download_build_name_lst, "MCU")
        os.system("taskkill /F /IM cmd.exe")
    except Exception as e:
        log.logger.error('flash_all_build: main: failed reason is %s' % e.args)